import json
import re

from lxml import etree, objectify

from mediator_framework import yang2yang
from mediator_framework import tp_list
from mediator_framework.data_provider import *

def add_children(parent_node, xml_doc_list):
    for xml_doc in xml_doc_list:
        parent_node.append(xml_doc)
    return

def parse_xmlreq(xmlreq):
    # using a custom parser to strip comments (so we don't handle them later)
    parser = objectify.makeparser(remove_comments=True, remove_blank_text=True)
    xml_root = objectify.fromstring(xmlreq, parser=parser)
    return xml_root

def locate_translation_point(neid, input_data):
    """
        :param neid: the device identifier
        :type neid: str
        :param input_data: the complete msg
        :type input_data: list
    """
    device_info = get_device_info_by_neid(neid)  # get device info : (vendor, product, type, version)
    tp_info = tp_list.translate_yang_registry.get(device_info)  # get tp_info in tp_list
    trans_info_list = []  # [{path, script, ns_map}]
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
            root = compute_translation_point_configuration(neid, path, input_data, ns_map)  # compute every translation point configuration
            cc_config.append(root)
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




def translate_edit_congfig_content(input_json):
    neid = "Router0"
    msg = compute_configuration_by_operation(neid,input_json)
    configNode = parse_xmlreq(msg)
    translated, translated_node = translate_edit_confignode_content(configNode)
    if translated == True:
        return etree.tostring(translated_node, pretty_print=True).decode("utf8")
    else:
        return msg

def translate_edit_confignode_content(configNode):
    need_translate = False
    translated_node = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})

    for appnode in configNode.getchildren():
        # Use the namespace of the nodes and get the Python Yang Object for this XML node.
        module_yang_obj = yang2yang.get_yang_obj_from_xmldoc(appnode)
        if None != module_yang_obj:
            need_translate = True
            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = yang2yang.translate_to_new_yang_xmldoc(module_yang_obj)
            add_children(translated_node, module_xml_doc_list)
    # Return translated, if we have translated anything.
    if need_translate is True:
        return True, translated_node
    else:
        return False, configNode

def translate_get_config_content(data):
    expected_dc = None
    return expected_dc

def translate_rpcreply_data(rpcreply_data):
    return None

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