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
    root = None
    trans_info_list = locate_translation_point(neid, input_data)
    if not trans_info_list:
        print("Can not find translation point!")
    else:
        for dic in trans_info_list:
            path = dic['path']
            ns_map = dic['ns_map']
            root = compute_translation_point_configuration(neid, path, input_data, ns_map)  # compute every translation point configuration
            # print(path, ns_map)
    return root


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
    return root

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

# compute operation
def parse_keyvalue_all(input_json, root, path, ns, n):
    """
    :param input_json: json data from adaptor
    :type input_json: str
    :param root: parse node
    :type root: xml obj
    """
    key_value = ''
    tag = None
    op = None
    if isinstance(input_json, dict):
        for key in input_json.keys():
            key_value = input_json.get(key)
            if "path" == key:  # get the path info
                # path = key_value
                tag = find_last_str(key_value)
            if "op" == key:  # get the operation info
                op = key_value
            if isinstance(key_value, dict):
                parse_keyvalue_all(key_value,root,path,ns,n)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    parse_keyvalue_all(json_array,root,path,ns,n)
            else:
                # print(str(key) + " = " + str(key_value))  # print all key and key_value
                if str(key) == "data":
                    # key_value = key_value.replace('\n', '').replace('\t', '')  # deal with \n and \t
                    node = etree.XML(key_value)
                    # print("node tag is:",node.tag)
                    v = find_xmlns(node.tag)
                    if v is not None:
                        n = n + 1
                        k = "a"+str(n)
                        ns[k] = v
                    else:
                        k = "a" + str(n)
                    path = path + '/' + k + ':' + tag
                    if node.getchildren():  # if node has children , find the key value
                        path = path + '[' + k + ':' + node.getchildren()[0].tag +  '="' + node.getchildren()[0].text + '"]'
                    print("path with namespace:", path)
                    node, changed = comupte_data_node(op, path, node, ns)  # compute the node configuration
                    root.append(node)
                    if None != root.getchildren():
                        for i in root.getchildren():
                            if extract_tag_content(i.tag) == tag:  # check the node level
                                root = i
    elif isinstance(input_json, list):
        for input_json_array in input_json:
            parse_keyvalue_all(input_json_array,root,path,ns,n)
    return root

def find_last_str(string):
    tag = string[string.rfind('/') + 1:]  # find the last content in path, for example:interfaces/interface/ipv4 --> ipv4
    return tag

def extract_tag_content(tag):
    if re.match(r'{.*', tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag

def find_xmlns(tag):
    ns = re.match(r'.*}', tag)
    if ns:
        return ns.group()[1:-1]
    return None

def find_last_ns(str):
    tag = str[str.rfind(':') -2: str.rfind(':')]  # find the last ns in path, for example:/a1:interfaces/a1:interface  --> a1
    return tag

def comupte_data_node(op, path, root, ns):
    """
    :param op: netconf edit-config operation: create merge delete remove replace
    :type op: str
    :param path: current path
    :type path: str
    :param root: compute node
    :type root: xml obj
    """
    changed = False
    res = root.xpath('//text()')
    if not res:  # check the xml if has the text
        # print("No text exist!")
        return root, changed
    else:
        parse = etree.XMLParser(remove_blank_text=True)
        cc = etree.parse("cc_configuration.xml", parse)
        if op == "merge":
            if root.getchildren():
                ns_key = find_last_ns(path)
                for i in root.getchildren():
                    tag = i.tag
                    text = i.text
                    tmp_path = path + '/' + ns_key + ':' + tag
                    # print("tmp_path is:", tmp_path)
                    text_cc = cc.xpath(tmp_path, namespaces=ns)
                    if text_cc:
                        print("converted_dc:", text, "current_dc:", text_cc[0].text)
                    else:
                        print("xpath does not work!")
                    # i.text = text_cc
        # elif op == "create":
        #     if cc.xpath(path):
        #         print("Already has data!")
        elif op == "replace":
            print()
        elif op == "delete":
            print()
        else:
            pass
        return root, changed

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