import re

from lxml import etree

from mediator_framework.tp_list import *
from mediator_framework.data_provider import *

def locate_translation_point(opdata):
    namespace = opdata["data"]["xmlns"]
    path = opdata["path"]
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None
    return path,PyTranslateReg[0]

def compute_configuration_by_operation(neid, json_data):
    path = json_data["path"]
    current_cc = get_controller_configuration(neid, path)
    cc = json_data["data"]
    oper = json_data["op"]
    expected_cc = None
    if oper == "merge":
        expected_cc = compute_merge(current_cc, cc)
    elif oper == "create" or oper == "replace":
        expected_cc  = cc
    else:
        expected_cc = compute_delete(current_cc,cc)
    return expected_cc

def translate_edit_congfig_content(data):
    expected_dc = None
    return expected_dc

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
                            if extract_tag_content(i.tag) == tag:
                                root = i
    elif isinstance(input_json, list):
        for input_json_array in input_json:
            parse_keyvalue_all(input_json_array,root)
    return root

def find_last_str(str):
    tag = str[str.rfind('/') + 1:]  # find the last content in path, for example:interfaces/interface/ipv4 --> ipv4
    return tag

def extract_tag_content(tag):
    if re.match(r'{.*',tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag


def compute_merge(config, config1):
    return None

def compute_delete(config, config1):
    return None

# compare operation
def compare(config, config1):
    return None