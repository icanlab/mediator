import copy
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
def locate_translation_point(neid, input_data, device_info):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    trans_info_list = []  # [{path, script, ns_map, ns}]
    if tp_info:
        for dic in input_data:
            res = {}
            path = None
            schema_path = None
            ns_map = None
            for key, value in dic.items():
                if 'path' == key:
                    path = value
                    schema_path = re.sub(r'[a-z]{1}:{1}', '', value)
                elif 'ns_map' == key:
                    ns_map = value
                elif 'ns' == key and tp_info.get(schema_path) is not None:
                    res['path'] = path  # add path to dict
                    res['schema_path'] = schema_path  # add schema_path to dict
                    res['script'] = tp_info.get(value)  # add the script info to dict
                    res['ns_map'] = ns_map  # add ns_map info to dict
                    res['ns'] = value  # add ns to dict
            if res and res not in trans_info_list:
                trans_info_list.append(res)
    else:
        print("Did not find device info!")
    return trans_info_list

def compute_configuration_by_operation(neid, input_data, device_info):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    cc_config = []
    trans_info_list = locate_translation_point(neid, input_data, device_info)
    if not trans_info_list:
        print("Can not find translation point!")
    else:
        for dic in trans_info_list:
            path = dic['path']
            ns_map = dic['ns_map']
            schema_path = dic['schema_path']
            root = compute_translation_point_configuration(neid, path, input_data, ns_map)  # compute every translation point configuration
            tmp = [schema_path, root]
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
    root = get_controller_configuration(neid, path, ns)
    if root is None:
        print('Do not have controller configuration!')
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
    if not root.xpath(path, namespaces=ns_map):
        parent_path = get_parent_path(path)
        if root.xpath(parent_path, namespaces=ns_map):
            parent_root = root.xpath(parent_path, namespaces=ns_map)[0]
            if not re.match(r'{.*', data.tag):
                _add_namespace(ns_map[key], data)  # if data do not have namespace , add it
            parent_root.append(data)
            return

    for i in data:
        if None in i.nsmap.keys() and i.nsmap[None] not in ns_map.values():
            key = chr(ord(key) + 1)
            ns_map[key] = i.nsmap[None]
        if i.text:
            if ']' != path[-1]:
                path = path + '[' + key + ':' + find_tag_content(i.tag) + '="' + i.text + '"]'
            xpath = path + '/' + key + ':' + find_tag_content(i.tag)
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
                temp = etree.SubElement(root.xpath(query_path, namespaces=ns_map)[0], i.tag)
                temp.text = i.text
        elif i.getchildren():
            xpath = path + '/' + key + ':' + find_tag_content(i.tag)  # get current level path
            if i.getchildren()[0].text:  # check if has leaf child
                xpath = xpath + '[' + key + ':' + find_tag_content(i.getchildren()[0].tag) + '="' + i.getchildren()[0].text + '"]'
            if not root.xpath(xpath, namespaces=ns_map):
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
        if root.xpath(path, namespaces=ns_map):
            res = root.xpath(path, namespaces=ns_map)[0]
        else:
            parent_path = get_parent_path(path)
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
def translate_expected_cc_by_translation_point(neid, trans_list, device_info):
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    path = trans_list[0]  # translation point path : /ietf:interfaces
    xml = trans_list[1]  # data need to translate
    xml = parse_xmlreq(etree.tostring(xml))
    if not tp_info.get(path):
        print("Do not have translation script!")
    else:
        translate_py = tp_info.get(path)[0]  # translation script name
        binding = tp_info.get(path)[1]  # yang bindings
        module_name = tp_info.get(path)[2]  # yang module name
        # use pyangbind to convert xml_obj to yang_obj
        dummy_root_node = add_to_dummy_xml(xml)
        module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
        if module_yang_obj is not None:
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
    res = get_device_configuration(neid, xpath, ns)  # get current device configuration
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

def compare_expected_device_configuration(source, target, path, ns):
    res = target.xpath(path, namespaces=ns)
    if not res:
        attributes = source.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'create'
        return source
    else:
        attributes = source.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'merge'
        if source.getchildren():
            xpath = path
            for i in source.getchildren():
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
                compare_expected_device_configuration(i, target, xpath, ns)

def compare_current_device_configuration(targrt, source, path, ns):
    res = source.xpath(path, namespaces=ns)
    if not res:
        attributes = targrt.attrib
        attributes[QName(XMLNamespaces.xc, 'operation')] = 'delete'
        xpath = get_parent_path(path)
        res = source.xpath(xpath, namespaces=ns)[0]
        res.append(targrt)
        return source
    else:
        if targrt.getchildren():
            for i in targrt.getchildren():
                xpath = path
                for i in targrt.getchildren():
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
                    compare_current_device_configuration(i, source, xpath, ns)
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
    if '[' in path and path[-1] == ']':
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
        if ':' in tag:
            tag = tag[:tag.find(':')]
    return tag

# translate get config msg
def translate_get_config_content(neid, input_data, device_info):
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    module_xml_doc_list = None
    for i in input_data:
        msg = i["data"]
        path = i["path"]
        if not tp_info.get(path):
            print("Do not have translation script!")
        else:
            xml_msg = parse_xmlreq(msg)
            translate_py = tp_info.get(path)[0]  # translation script name
            binding = tp_info.get(path)[1]  # yang bindings
            module_name = tp_info.get(path)[2]  # yang module name
            # use pyangbind to convert xml_obj to yang_obj
            dummy_root_node = add_to_dummy_xml(xml_msg)
            module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
            if None != module_yang_obj:
                # translate this yang-obj to the new yang-obj and get its xml-doc.
                module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj, translate_py)
        return module_xml_doc_list

# convert rpcreply_data to ietf
def translate_rpc_reply_data(neid, input_data, device_info):
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    module_xml_doc_list = None
    for i in input_data:
        msg = i["data"]
        path = i["path"]
        if not tp_info.get(path):
            print("Do not have translation script!")
        else:
            xml_msg = parse_xmlreq(msg)
            translate_py = tp_info.get(path)[0]  # translation script name
            binding = tp_info.get(path)[1]  # yang bindings
            module_name = tp_info.get(path)[2]  # yang module name
            # use pyangbind to convert xml_obj to yang_obj
            dummy_root_node = add_to_dummy_xml(xml_msg)
            module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)
            if None != module_yang_obj:
                # translate this yang-obj to the new yang-obj and get its xml-doc.
                module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj, translate_py)
        return module_xml_doc_list


'''
    non top-level translation point design for mediator : edit-config
    step 1 : compute
    step 2 : translate
    step 3 : compare
'''

# step1: compute
def compute_src_configuration(neid, input_data):
    compute_res = []
    for item in input_data:
        res = compute_src_configuration_by_operation(neid, item)  # compute operation one by one
        # print(etree.tostring(res, pretty_print=True).decode('utf-8'))
        compute_res.append([item['schema_path'], item['path'], res])
    return compute_res  # return all compute res

def compute_src_configuration_by_operation(neid, op_data):
    xpath = op_data['path']
    ns_map = op_data['ns_map']
    data = op_data['data']
    if isinstance(data, str) and data:
        data = etree.fromstring(data)  # convert str to lxml etree element

    # step1: get controller config by xpath
    current_configuration = get_controller_configuration(neid, xpath, ns_map)
    xpath = '/a:' + find_tag_content(data.tag)
    left = data.tag.find('{')
    right = data.tag.find('}')
    ns = data.tag[left + 1:right]
    ns_map = {'a': ns}
    # print('current src configuration is :\n', etree.tostring(current_configuration, pretty_print=True).decode('utf-8'))
    # check op to decide which function to call
    op = op_data['op']
    if 'merge' == op:
        compute_merge_operation(current_configuration, xpath, data, ns_map)
    elif 'create' == op:
        if current_configuration is None:
            current_configuration = data
        else:
            raise Exception("Data already exists!")
    elif 'replace' == op:
        current_configuration = data
    elif 'delete' == op:
        if current_configuration is not None:
            current_configuration = data
        else:
            raise Exception("Data did not exists!")
    elif 'remove' == op:
        current_configuration = data
    else:
        raise Exception("unsolved operation!")
    return current_configuration

# step 2: translate
def translate_src_configuration_list(compute_res, device_info):
    translate_res = []
    for schema_path, xpath,  item in compute_res:
        translated_obj, target_xpath, ns_map = translate_src_configuration(schema_path, xpath, item, device_info)
        translate_res.append([translated_obj, target_xpath, ns_map])
    return translate_res


def translate_src_configuration(schema_path, xpath, src_configuration, device_info):
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    trans_info = locate_translation_point_path(schema_path, tp_info, src_configuration)
    if trans_info is None:
        raise Exception("did not find translation script")
    else:
        translate_py = trans_info[0]  # translation script name
        binding = trans_info[1]  # yang bindings
        yang_base = trans_info[2]  # yang_base

        # use pyangbind to convert xml_obj to yang_obj
        dummy_root_node = add_to_dummy_xml(src_configuration)
        module_yang_obj = pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=yang_base)

        # Use the APP's function to convert from Input Python YANG object to its own type.
        api_name = "_translate__%s" % (safe_name(module_yang_obj._yang_name))
        # print(api_name)

        # The translate API is part of the Yang module's top level object.
        translate_api = getattr(translate_py, api_name)

        translated_obj, target_xpath, ns_map = translate_api(module_yang_obj, None, xpath)  # input_obj, translated_obj, xpath

        xml = pybindIETFXMLEncoder.serialise(translated_obj)  # xml

        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.fromstring(xml, parser)  # lxml obj
    return root, target_xpath, ns_map

#  locate translation point , find translation info
def locate_translation_point_path(path, tp_info, src_configuration):
    if tp_info.get(path) is not None:  # Check if the current level matches
        return tp_info.get(path)
    else:
        trans_info = None
        trans_info = locate_translation_point_path_up(path, tp_info, trans_info)  # go up for trans_info
        if trans_info is not None:
            return trans_info
        else:
            tmp_path = path[:path.find(':')]
            parent_module_name = tmp_path[tmp_path.find('/')+1:]
            trans_info = locate_translation_point_path_down(path, tp_info, src_configuration, parent_module_name, trans_info)  # look down for trans_info
            return trans_info

def locate_translation_point_path_up(path, tp_info, trans_info):
    parent_path = path[:path.rfind('/')]
    if parent_path is '':
        return None
    if tp_info.get(parent_path) is not None:
        return tp_info.get(parent_path)
    else:
        trans_info = locate_translation_point_path_up(parent_path, tp_info, trans_info)
    return trans_info


def locate_translation_point_path_down(path, tp_info, root, parent_module_name, trans_info):
    left = root.tag.rfind(':')
    right = root.tag.find('}')
    cur_module_name = root.tag[left+1:right]
    if cur_module_name != parent_module_name or path == '':
        child_path = path + '/' + cur_module_name + ':' + find_tag_content(root.tag)
        parent_module_name = cur_module_name
    else:
        child_path = path + '/' + find_tag_content(root.tag)
    if tp_info.get(child_path) is not None:
        return tp_info.get(child_path)
    else:
        if root.getchildren():
            for i in root.getchildren():
                trans_info = locate_translation_point_path_down(child_path, tp_info, i, parent_module_name, trans_info)
    return trans_info

# step 3:compare
def compare_target_configuration(neid, expected_target_config, xpath, ns_map):
    # print(xpath,ns_map)
    current_target_config = get_device_configuration(neid, xpath, ns_map)
    if current_target_config is None:  # if target configuration is None, we need not to compare
        expected_target_config.attrib[QName(XMLNamespaces.xc, 'operation')] = 'create'
        return [xpath, ns_map, expected_target_config]
    else:
        root = etree.Element("root")
        if len(expected_target_config.getchildren())==1 and expected_target_config.getchildren()[0].text is not None:
            expected_target_config.attrib[QName(XMLNamespaces.xc, 'operation')] = 'delete'
            root.append(expected_target_config)
        else:
            compare_expected_target_config(expected_target_config, current_target_config, None, {}, root, None)
            # print(etree.tostring(expected_target_config, pretty_print=True).decode('utf-8'))
            compare_current_target_config(current_target_config, expected_target_config, None, {}, root, None)
            # print(etree.tostring(root, pretty_print=True).decode('utf-8'))
    return [xpath, ns_map, root.getchildren()[0]]

def compare_expected_target_config(source, target, xpath, ns_map, root, key):
    tag = find_tag_content(source.tag)
    ns = re.match(r'{.*}', source.tag).group()[1:-1]
    # build current level xpath
    if xpath is None:
        xpath = '/a:' + tag
        prefix = 'a'
        ns_map[prefix] = ns
    else:
        prefix = find_last_ns_key(xpath)
        if ns not in ns_map.values():
            prefix = chr(ord(prefix) + 1)
            ns_map[prefix] = ns
            xpath = xpath + '/' + prefix + ':' + tag
        else:  # add key in root element
            prefix = get_keys(ns, ns_map)[0]
            xpath = xpath + '/' + prefix + ':' + tag
    if source.getchildren() and source.getchildren()[0].text is not None:
        xpath = xpath + '[' + prefix + ':' + find_tag_content(source.getchildren()[0].tag) + '="' + source.getchildren()[0].text + '"]'
    ans = target.xpath(xpath, namespaces=ns_map)
    # print(xpath, source)
    if ans:
        NSMAP = {None: ns}
        ch = etree.Element(source.tag, nsmap=NSMAP)

        # leaf node
        if source.text is not None:
            if source.text != ans[0].text:
                ch.text = source.text
                ch.attrib[QName(XMLNamespaces.xc, 'operation')] = 'merge'
                root.append(ch)
            else:
                if key == tag:
                    ch.text = source.text
                    root.append(ch)
        elif source.getchildren():
            root.append(ch)
        # non leaf node
        if source.getchildren():
            if source.getchildren()[0].text is not None:  # add key in xpath
                key = find_tag_content(source.getchildren()[0].tag)
            for child in source.getchildren():
                compare_expected_target_config(child, target, xpath, ns_map, ch, key)
    else:
        tmp = copy.deepcopy(source)
        tmp.attrib[QName(XMLNamespaces.xc, 'operation')] = 'create'
        root.append(tmp)

def compare_current_target_config(source, target, xpath, ns_map, root, key):
    tag = find_tag_content(source.tag)
    ns = re.match(r'{.*}', source.tag).group()[1:-1]
    # build current level xpath
    if xpath is None:
        xpath = '/a:' + tag
        prefix = 'a'
        ns_map[prefix] = ns
    else:
        prefix = find_last_ns_key(xpath)
        if ns not in ns_map.values():
            prefix = chr(ord(prefix) + 1)
            ns_map[prefix] = ns
            xpath = xpath + '/' + prefix + ':' + tag
        else:  # add key in root element
            prefix = get_keys(ns, ns_map)[0]
            xpath = xpath + '/' + prefix + ':' + tag
    if source.getchildren() and source.getchildren()[0].text is not None:
        xpath = xpath + '[' + prefix + ':' + find_tag_content(source.getchildren()[0].tag) + '="' + source.getchildren()[0].text + '"]'
    ans = source.xpath(xpath, namespaces=ns_map)
    if ans:
        if source.getchildren():
            if source.getchildren()[0].text is not None:  # add key in xpath
                key = find_tag_content(source.getchildren()[0].tag)
            for child in source.getchildren():
                compare_current_target_config(child, target, xpath, ns_map, root, key)
    else:
        tmp = copy.deepcopy(source)
        res = root.xpath(xpath, namespaces=ns_map)[0]
        tmp.attrib[QName(XMLNamespaces.xc, 'operation')] = 'delete'
        res.append(tmp)