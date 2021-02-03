import re

from lxml import etree, objectify

from mediator_framework import yang2yang
from mediator_framework.tp_list import *
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

def locate_translation_point(input_json):
    """
        :param input_json: the complete msg
        :type input_json: dict
    """
    xml_data = etree.XML(input_json["data"])  # convert the XML str
    path = input_json["path"]
    qn = etree.QName(xml_data)  # use the QName helper class to build tag names
    print(qn.namespace)
    PyTranslateReg = translate_yang_registry.get(qn.namespace)  # get the key_value with namespace in tp_list
    if None == PyTranslateReg:
        return None
    return path, PyTranslateReg[0]

def compute_configuration_by_operation(neid, input_json):
    # path = input_json["path"]
    # current_cc = get_controller_configuration(neid, path)
    root = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})  # add the config element
    parse_keyvalue_all(input_json,root)
    # expected_cc = compute_configuration_between_current_cc_and_cc(current_cc, cc)
    return etree.tostring(root)

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
    path = expected_dc["path"]
    current_dc = get_device_configuration(neid,path)
    msg = compare(expected_dc, current_dc)
    return msg

# compute operation
"""
    parse json data: dict and list
    get the data which scripts need
"""
def parse_keyvalue_all(input_json,root):
    key_value = ''
    tag = None
    if isinstance(input_json, dict):
        for key in input_json.keys():
            key_value = input_json.get(key)
            if "path" == key:
                tag = find_last_str(key_value)
            if isinstance(key_value, dict):
                parse_keyvalue_all(key_value,root)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    parse_keyvalue_all(json_array,root)
            else:
                print(str(key) + " = " + str(key_value))  # print all key and key_value
                if str(key) == "data":
                    node = etree.XML(key_value)
                    print("node tag is:",node.tag)
                    root.append(node)
                    if None != root.getchildren():
                        for i in root.getchildren():
                            if extract_tag_content(i.tag) == tag:  # check the node level
                                root = i
    elif isinstance(input_json, list):
        for input_json_array in input_json:
            parse_keyvalue_all(input_json_array,root)
    return root

def find_last_str(str):
    tag = str[str.rfind('/') + 1:]  # find the last content in path, for example:interfaces/interface/ipv4 --> ipv4
    return tag

def extract_tag_content(tag):
    if re.match(r'{.*', tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag

def compute_configuration_between_current_cc_and_cc(current_cc, cc):
    expected_cc = None
    return expected_cc

def compute_merge(config, config1):
    return None

def compute_create(config, config1):
    return None

# compare operation
def compare(config, config1):
    return None