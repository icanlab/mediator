import re

from lxml import etree, objectify
from lxml.etree import QName

from pyangbind.lib.yangtypes import safe_name
from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder
from swagger_server.mediator_framework import tp_list
from swagger_server.mediator_framework.data_provider import *
from swagger_server.mediator_framework.yang2yang import add_to_dummy_xml

class XMLNamespaces:
    xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'

def parse_xmlreq(xmlreq):
    # using a custom parser to strip comments (so we don't handle them later)
    parser = objectify.makeparser(remove_comments=True, remove_blank_text=True)
    xml_root = objectify.fromstring(xmlreq, parser=parser)
    return xml_root

# step1: compute
def locate_translation_point(neid, input_data):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    device_info = get_device_info_by_neid(neid)  # get device info : (vendor, product, type, version)
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    trans_info_list = []  # [{path, script, ns_map, ns}]
    if tp_info:
        # print(tp_info)
        for dic in input_data:
            res = {}
            path = ''
            ns_map = None
            for key, value in dic.items():
                if 'path' == key:
                    path = value
                elif 'ns_map' == key:
                    ns_map = value
                elif 'ns' == key and tp_info.get(value) is not None:
                    top_path = find_top_path(path)
                    if '/' == top_path[-1]:
                        top_path = top_path[:-1]
                    res['path'] = top_path  # add path to dict
                    res['script'] = tp_info.get(value)  # add the script info to dict
                    res['ns_map'] = ns_map  # add ns_map info to dict
                    res['ns'] = value  # add ns to dict
            if res and res not in trans_info_list:
                trans_info_list.append(res)
    else:
        print("Did not find device info!")
    return trans_info_list

def find_top_path(path):
    res = re.match(r'/[^/]+/', path)
    if res:
        return res.group()
    else:
        return path

def compute_configuration_by_operation(neid, input_data):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    cc_config = []
    trans_info_list = locate_translation_point(neid, input_data)
    # print(trans_info_list)
    if not trans_info_list:
        print("Can not find translation point!")
    else:
        for dic in trans_info_list:
            path = dic['path']
            ns_map = dic['ns_map']
            ns = dic['ns']
            root = compute_translation_point_configuration(neid, path, input_data, ns_map)  # compute every translation point configuration
            tmp = [ns, root]
            cc_config.append(tmp)
    return cc_config


def compute_translation_point_configuration(neid, path, input_data, ns_map):
    """
        :param neid: the device identifier
        :type neid: str
        :param path: the translation point path : /a0:interfaces
        :type path: str
        :param input_data: the complete msg
        :type input_data: list
        :param ns_map: namespace map of path : {'a0':'urn:ietf:params:xml:ns:yang:ietf-interfaces'}
        :type ns_map: str
    """
    if isinstance(ns_map, str):
        ns = eval(ns_map)  # convert str to dict
    else:
        ns = ns_map
    root = get_controller_configuration(neid, path, ns)[0]
    for ele in input_data:
        op = ele['op']
        path = ele['path']
        data = ele['data']
        ns_map = ele['ns_map']
        if isinstance(data, str) and data:
            data = etree.fromstring(data)  # convert str to lxml etree element
        if isinstance(ns_map, str):
            ns_map = eval(ns_map)  # convert str to dict
        if 'merge' == op:
            compute_merge_operation(root, path, data, ns_map)
        elif 'create' == op:
            compute_create_operation(root, path, data, ns_map)
        elif 'replace' == op:
            compute_replace_operation(root, path, data, ns_map)
        elif 'remove' == op:
            compute_remove_operation(root, path, data, ns_map)
        elif 'delete' == op:
            compute_delete_operation(root, path, data, ns_map)
        else:
            print("Unsolved operation!")
    return root


def compute_merge_operation(root, path, data, ns_map):
    # print('Deal with merge operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    for i in data:
        if None in i.nsmap.keys() and i.nsmap[None] not in ns_map.values():
            key = chr(ord(key) + 1)
            ns_map[key] = i.nsmap[None]
        if i.text:
            if ']' != path[-1]:
                path = path + '[' + key + ':' + find_tag_content(i.tag) + '="' + i.text + '"]'
            xpath = path + '/' + key + ':' + find_tag_content(i.tag)
            # print(xpath, ns_map)
            if root.xpath(xpath, namespaces=ns_map):
                res = root.xpath(xpath, namespaces=ns_map)[0]
                # print(i.text, res.text)
                if i.text != res.text:
                    res.text = i.text  # change the text in root config
            else:  # if not has data, create it in root node
                if path[-1] == ']':
                    query_path = path[:path.rfind('[')]
                else:
                    query_path = path
                # print(xpath, query_path, i.tag)
                temp = etree.SubElement(root.xpath(query_path, namespaces=ns_map)[0], i.tag)
                temp.text = i.text
        elif i.getchildren():
            xpath = path + '/' + key + ':' + find_tag_content(i.tag)
            if not root.xpath(xpath, namespaces=ns_map):
                print(path, i.tag)
                root.xpath(path, namespaces=ns_map)[0].append(i)
                return
            compute_merge_operation(root, xpath, i, ns_map)


def compute_create_operation(root, path, data, ns_map):
    # print('Deal with create operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    # print(path, key)
    if root.xpath(path, namespaces=ns_map):
        print('Already has data!')
    else:
        path = path[: path.rfind('/')]
        res = root.xpath(path, namespaces=ns_map)[0]
        if not re.match(r'{.*', data.tag):
            _add_namespace(ns_map[key], data)  # if data do not have namespace , add it
        res.append(data)


def compute_replace_operation(root, path, data, ns_map):
    # print('Deal with replace operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    # print(path, ns_map)
    if data.getchildren():  # if have data , delete first
        res = root.xpath(path, namespaces=ns_map)[0]
        res.getparent().remove(res)
    if not re.match(r'{.*', data.tag):
        _add_namespace(ns_map[key], data)  # if data do not have namespace , add it
    if path[-1] == ']':
        path = path[: path.rfind('[')]
    path = path[: path.rfind('/')]
    root.xpath(path, namespaces=ns_map)[0].append(data)


def compute_remove_operation(root, path, data, ns_map):
    # print('Deal with remove operation!')
    if root.xpath(path, namespaces=ns_map):
        child = root.xpath(path, namespaces=ns_map)[0]
        child.getparent().remove(child)  # delete the tag in root


def compute_delete_operation(root, path, data, ns_map):
    # print('Deal with delete operation!')
    if not root.xpath(path, namespaces=ns_map):
        print('Do not have data to delete!')
    else:
        child = root.xpath(path, namespaces=ns_map)[0]
        child.getparent().remove(child)  # delete the tag in root

#  add namespace in data
def _add_namespace(key, data):
    data.tag = etree.QName(key, data.tag)
    if data.getchildren():
        for i in data.getchildren():
            if not re.match(r'{.*', i.tag):
                _add_namespace(key, i)


# step2: translate
def translate_expected_cc_by_translation_point(neid, trans_list):
    device_info = get_device_info_by_neid(neid)  # get device info : (vendor, product, type, version)
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    ns = trans_list[0]
    xml = trans_list[1]
    xml = parse_xmlreq(etree.tostring(xml))
    if not tp_info.get(ns):
        print("Do not have translation script!")
    else:
        translate_py = tp_info.get(ns)[0]  # translation script name
        binding = tp_info.get(ns)[1]  # yang bindings
        module_name = tp_info.get(ns)[2]  # yang module name
        # use pyangbind to convert xml_obj to yang_obj
        dummy_root_node = add_to_dummy_xml(xml)
        module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
        if None != module_yang_obj:
            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj, translate_py)
    return module_xml_doc_list


def translate_to_new_yangobj(module_yang_obj, translate_py):

    # Use the APP's function to convert from Input Python YANG object to its own type.
    api_name  = "_translate__%s" % (safe_name(module_yang_obj._yang_name))

    # The translate API is part of the Yang module's top level object.
    translate_api = getattr(translate_py, api_name)

    translated_obj_list = translate_api(module_yang_obj)

    return translated_obj_list


def translate_to_new_yang_xmldoc(module_yang_obj, translate_py):

    # Get the list of obj, that we can get from the new yang obj.
    translated_obj_list = translate_to_new_yangobj(module_yang_obj, translate_py)

    module_xml_doc_list = []

    for translated_obj in translated_obj_list:

        # Convert this YANG object to its corresponding XML-doc
        module_xml_doc = pybindIETFXMLEncoder.encode(translated_obj)
        module_xml_doc_list.append(module_xml_doc)

    return module_xml_doc_list

# step3: compare
def compare_device_configuration(neid, expected_dc):
    """
    :param neid: device identifier
    :type neid: str
    :param expected_dc: expected device configuration
    :type expected_dc:
    """
    root = expected_dc
    if isinstance(root, etree._ElementTree):
        root = expected_dc.getroot()
    if 'config' == root.tag:
        root = root.getchildren()[0]
    tag = find_tag_content(root.tag)
    namespace = re.match(r'{.*}', root.tag).group()[1:-1]
    prefix = 'a'
    xpath = '/' + prefix + ':' + tag
    ns = {prefix: namespace}
    res = get_device_configuration(neid, xpath, ns)[0]  # get current device configuration
    converted_msg = etree.Element("config", nsmap={'xc': "urn:ietf:params:xml:ns:netconf:base:1.0"})
    if res is None:
        attributes = res.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'create'
        converted_msg.append(res)
    else:
        compare_expected_device_configuration(root, res, xpath, ns)
        compare_current_device_configuration(res, root, xpath, ns)
        trim_operation(root, False)
        converted_msg.append(root)
    return converted_msg

def compare_expected_device_configuration(config0, config1, path, ns):
    res = config1.xpath(path, namespaces=ns)
    if not res:
        attributes = config0.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'create'
        return config0
    else:
        attributes = config0.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'merge'
        if config0.getchildren():
            xpath = path
            for i in config0.getchildren():
                tag = find_tag_content(i.tag)
                namespace = re.match(r'{.*}', i.tag).group()[1:-1]
                prefix = find_last_ns_key(path)
                if namespace not in ns.values():
                    prefix = chr(ord(prefix)+1)
                    ns[prefix] = namespace
                    xpath = path + '/' + prefix + ':' + tag
                else:
                    prefix = get_keys(namespace, ns)[0]
                    xpath = path + '/' + prefix + ':' + tag
                if i.getchildren() and i.getchildren()[0].text is not None:
                    xpath = xpath + '[' + prefix + ':' + find_tag_content(i.getchildren()[0].tag) + '="' + i.getchildren()[0].text + '"]'
                compare_expected_device_configuration(i, config1, xpath, ns)

def compare_current_device_configuration(config0, config1, path, ns):
    res = config1.xpath(path, namespaces=ns)
    if not res:
        attributes = config0.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'delete'
        xpath = get_parent_path(path)
        res = config1.xpath(xpath, namespaces=ns)[0]
        res.append(config0)
        return config1
    else:
        if config0.getchildren():
            for i in config0.getchildren():
                xpath = path
                for i in config0.getchildren():
                    tag = find_tag_content(i.tag)
                    namespace = re.match(r'{.*}', i.tag).group()[1:-1]
                    prefix = find_last_ns_key(path)
                    if namespace not in ns.values():
                        prefix = chr(ord(prefix) + 1)
                        ns[prefix] = namespace
                        xpath = path + '/' + prefix + ':' + tag
                    else:
                        prefix = get_keys(namespace, ns)[0]
                        xpath = path + '/' + prefix + ':' + tag
                    if i.getchildren() and i.getchildren()[0].text is not None:
                        xpath = xpath + '[' + prefix + ':' + find_tag_content(i.getchildren()[0].tag) + '="' + i.getchildren()[0].text + '"]'
                    compare_current_device_configuration(i, config1, xpath, ns)
    return

def trim_operation(root, trim):
    op = root.get(QName(XMLNamespaces.xc, 'operation'))
    is_trim = trim
    if 'merge' == op:
        if is_trim:
            attributes = root.attrib
            del attributes[QName(XMLNamespaces.xc, 'operation')]
        if root.getchildren():
            is_trim = True
            for i in root.getchildren():
                trim_operation(i, is_trim)
        trim = True
    else:
        return

def get_keys(value, ns):
    return [k for k, v in ns.items() if v == value]

def get_parent_path(path):
    parent_path = None
    if '[' in path:
        path = path[: path.rfind('[')]
        parent_path = path[: path.rfind('/')]
    else:
        parent_path = path[: path.rfind('/')]
    return parent_path

# xml helper
def find_last_str(string):
    tag = string[string.rfind('/') + 1:]  # find the last content in path, for example:interfaces/interface/ipv4 --> ipv4
    return tag

def find_tag_content(tag):
    if re.match(r'{.*', tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag

def find_last_ns_key(path):
    if path[-1] != ']':
        tag = path[path.rfind('/') + 1: path.rfind(':')]  # find the last ns in path, for example:/a1:interfaces/a1:interface  --> a1
    else:
        tag = path[path.rfind('[') + 1: path.rfind(':')]
    return tag

# translate get config msg
def translate_get_config_content(neid, input_data):
    device_info = get_device_info_by_neid(neid)  # get device info : (vendor, product, type, version)
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    module_xml_doc_list = None
    msg = None
    ns = None
    for i in input_data:
        msg = i["data"]
        ns = i["ns"]
        if not tp_info.get(ns):
            print("Do not have translation script!")
        else:
            xml_msg = parse_xmlreq(msg)
            translate_py = tp_info.get(ns)[0]  # translation script name
            binding = tp_info.get(ns)[1]  # yang bindings
            module_name = tp_info.get(ns)[2]  # yang module name
            # use pyangbind to convert xml_obj to yang_obj
            dummy_root_node = add_to_dummy_xml(xml_msg)
            module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
            if None != module_yang_obj:
                # translate this yang-obj to the new yang-obj and get its xml-doc.
                module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj, translate_py)
        return module_xml_doc_list

# convert rpcreply_data to ietf
def translate_rpc_reply_data(neid, input_data):
    device_info = get_device_info_by_neid(neid)  # get device info : (vendor, product, type, version)
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    module_xml_doc_list = None
    msg = None
    ns = None
    for i in input_data:
        msg = i["data"]
        ns = i["ns"]
        if not tp_info.get(ns):
            print("Do not have translation script!")
        else:
            xml_msg = parse_xmlreq(msg)
            translate_py = tp_info.get(ns)[0]  # translation script name
            binding = tp_info.get(ns)[1]  # yang bindings
            module_name = tp_info.get(ns)[2]  # yang module name
            # use pyangbind to convert xml_obj to yang_obj
            dummy_root_node = add_to_dummy_xml(xml_msg)
            module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
            if None != module_yang_obj:
                # translate this yang-obj to the new yang-obj and get its xml-doc.
                module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj, translate_py)
        return module_xml_doc_list