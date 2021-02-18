import json
import re

from lxml import etree, objectify

from pyangbind.lib.yangtypes import safe_name
from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder
from mediator_framework import tp_list
from mediator_framework.data_provider import *
from mediator_framework.yang2yang import add_to_dummy_xml


def add_children(parent_node, xml_doc_list):
    for xml_doc in xml_doc_list:
        parent_node.append(xml_doc)
    return

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
                    res['path'] = path  # add path to dict
                    res['script'] = tp_info.get(value)  # add the script info to dict
                    res['ns_map'] = ns_map  # add ns_map info to dict
                    res['ns'] = value  # add ns to dict

            if res and res not in trans_info_list:
                trans_info_list.append(res)
    else:
        print("Did not find device info!")
    return trans_info_list


def compute_configuration_by_operation(neid, input_data):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    cc_config = []
    trans_info_list = locate_translation_point(neid, input_data)
    if not trans_info_list:
        print("Can not find translation point!")
    else:
        for dic in trans_info_list:
            path = dic['path']
            ns_map = dic['ns_map']
            ns = dic['ns']
            root = compute_translation_point_configuration(neid, path, input_data, ns_map)  # compute every translation point configuration
            tmp = []
            tmp.append(ns)
            tmp.append(root)
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
    ns = eval(ns_map)  # convert str to dict
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
    print('Deal with merge operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    tag = find_tag_content(data.tag)  # find tag content : /10:interfaces --> interfaces
    # process path info
    if not data.nsmap:
        path = path + '/' + key + ':' + tag
        print('Do not have namespace!')
    else:
        key = key+str(1)
        for k, value in data.nsmap.items():
            ns_map[key] = value
        path = path + '/' + key + ':' + tag
    print(path, ns_map)
    for i in data:
        if i.text:
            xpath = path + '/' + key + ':' + i.tag
            res = root.xpath(xpath, namespaces=ns_map)[0]
            print(i.text, res.text)
            if i.text != res.text:
                res.text = i.text  # change the text in root config
        elif i.getchildren():
            compute_merge_operation(root, path, i, ns_map)


def compute_create_operation(root, path, data, ns_map):
    print('Deal with create operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    tag = find_tag_content(data.tag)  # find tag content : /10:interfaces --> interfaces
    # process path info
    xpath =None
    if not data.nsmap:
        xpath = path + '/' + key + ':' + tag
        print('Do not have namespace!')
    else:
        for k, value in data.nsmap.items():
            if None == k:
                key = key + str(1)
                ns_map[key] = value
        xpath = path + '/' + key + ':' + tag
    if root.xpath(xpath, namespaces=ns_map):
        print('Already has data!')
    else:
        res = root.xpath(path, namespaces=ns_map)[0]
        if not re.match(r'{.*', data.tag):
            _add_namespace(ns_map[key], data)  # if data do not have namespace , add it
        res.append(data)


def compute_replace_operation(root, path, data, ns_map):
    print('Deal with replace operation!')
    key = find_last_ns_key(path)  # find current ns key : /a0:interfaces --> a0
    tag = find_tag_content(data.tag)  # find tag content : /10:interfaces --> interfaces
    xpath = None
    # process path info
    if not data.nsmap:
        xpath = path + '/' + key + ':' + tag
        print('Do not have namespace!')
    else:
        key = key + str(1)
        for k, value in data.nsmap.items():
            ns_map[key] = value
        xpath = path + '/' + key + ':' + tag
    print(xpath, ns_map)
    if data.getchildren():  # if have data , delete first
        xpath = xpath + '[' + key + ':' + data.getchildren()[0].tag + '="' + data.getchildren()[0].text + '"]'
        print(xpath)
        res = root.xpath(xpath, namespaces=ns_map)[0]
        res.getparent().remove(res)
    if not re.match(r'{.*', data.tag):
        _add_namespace(ns_map[key], data)  # if data do not have namespace , add it
    root.xpath(path, namespaces=ns_map)[0].append(data)


def compute_remove_operation(root, path, data, ns_map):
    print('Deal with remove operation!')
    if root.xpath(path, namespaces=ns_map):
        child = root.xpath(path, namespaces=ns_map)[0]
        child.getparent().remove(child)  # delete the tag in root


def compute_delete_operation(root, path, data, ns_map):
    print('Deal with delete operation!')
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
    translated_node = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
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
        if module_yang_obj != None:
            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = translate_to_new_yang_xmldoc(module_yang_obj,translate_py)
            add_children(translated_node, module_xml_doc_list)
    return translated_node


def translate_to_new_yangobj(module_yang_obj, translate_py):

    # Use the APP's function to convert from Input Python YANG object to its own type.
    api_name  = "_translate__%s" % (safe_name(module_yang_obj._yang_name))

    # The translate API is part of the Yang module's top level object.
    translate_api = getattr(translate_py, api_name)

    translated_obj_list = translate_api(module_yang_obj)

    return translated_obj_list


def translate_to_new_yang_xmldoc(module_yang_obj,translate_py):

    # Get the list of obj, that we can get from the new yang obj.
    translated_obj_list = translate_to_new_yangobj(module_yang_obj, translate_py)

    module_xml_doc_list = []

    for translated_obj in translated_obj_list:

        # Convert this YANG object to its corresponding XML-doc
        module_xml_doc = pybindIETFXMLEncoder.encode(translated_obj)
        print(module_xml_doc)
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
    path = expected_dc["path"]
    current_dc = get_device_configuration(neid,path)
    root = {}
    path = ''
    res = compare_dc_configuration(expected_dc, current_dc, root, path)
    return json.dumps(res, indent=4)


def find_last_str(string):
    tag = string[string.rfind('/') + 1:]  # find the last content in path, for example:interfaces/interface/ipv4 --> ipv4
    return tag

def find_tag_content(tag):
    if re.match(r'{.*', tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag

def find_last_ns_key(path):
    tag = path[path.rfind('/') + 1: path.rfind(':')]  # find the last ns in path, for example:/a1:interfaces/a1:interface  --> a1
    return tag


# compare operation
def compare_dc_configuration(config0, config1, root, path_root):  # config0 and config1 are XML obj
    """
    :param config0: the expected device configuration
    :type config0: xml obj
    :param config1: the current device configuration
    :type config1: xml obj
    :param root: converted node
    :type root: python dict
    :param path_root: current path
    :type path_root: str
    """
    op = 'merge'
    path = path_root
    data = None
    if config0 is not None:
        data = etree.Element(config0.tag)
        path = path + '/' + config0.tag
        print(etree.tostring(data))
        root["op"] = op
        root["path"] = path
        if config0.getchildren()[0].text is not None:
            for i in config0.getchildren():
                if i.text is not None:
                    data.append(i)
                    root["data"] = str(etree.tostring(data), 'utf-8')
                else:
                    root["data"] = str(etree.tostring(data), 'utf-8')
                    root["subnode"] = {}
                    compare_dc_configuration(i, config1, root["subnode"], path)
        else:
            root["data"] = str(etree.tostring(data), 'utf-8')
            root["subnode"] = {}
            compare_dc_configuration(config0.getchildren()[0], config1, root["subnode"], path)

    return root