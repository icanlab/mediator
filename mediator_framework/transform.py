"""
    The module for converting between xml, json and dict
"""

import json
import xmltodict


def xml_to_json(xml_str):
    xmlparse = xmltodict.parse(xml_str)
    json_str = json.dumps(xmlparse, indent=1)
    # json_str = json.dumps(xmlparse)
    return json_str


def json_to_xml(json_str):
    # json_dict = json_str if type(json_str) == dict else json.loads(json_str)
    json_dict = json.loads(json_str)
    xml_str = xmltodict.unparse(json_dict, pretty=1)
    return xml_str


# def xml_to_dict(xml_str):
#     dict_str = xmltodict.parse(xml_str, process_namespaces=True)
#     return dict

def json_to_dict(json_str):
    dict_str = json.loads(json_str)
    return dict_str


def dict_to_json(dict_str):
    json_str = json.dumps(dict_str)
    return json_str


# if __name__ == '__main__':
