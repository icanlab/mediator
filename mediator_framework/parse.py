import json
import re
from copy import deepcopy

from lxml import etree
from lxml.etree import QName


class yang_namespace():
    a = 'urn:ietf:params:xml:ns:netconf:base:1.0'

def parse_config_content(root):
    res = root
    ns_map = {'xc': 'urn:ietf:params:xml:ns:netconf:base:1.0'}
    parent_path = '/'
    input_data = []
    if res.getchildren():
        parse_input_data(res.getchildren(), ns_map, parent_path, input_data)
    return input_data

def parse_input_data(root, ns_map, parent_path, input_data):
    for i in root:
        path = parent_path
        ns_tmp = deepcopy(ns_map)
        ns = get_namespace(i.tag)
        tag = find_tag_content(i.tag)
        if ns not in ns_tmp.values():  # if namespace not in ns_map
            if parent_path == '/':
                prefix = 'a'
                path = path + prefix + ':' + tag
            else:
                prefix = find_prefix(parent_path)
                prefix = chr(ord(prefix) + 1)
                path = path + '/' + prefix + ':' + tag
            ns_tmp[prefix] = ns
        else:
            prefix = find_prefix(parent_path)
            path = path + '/' + prefix + ':' + tag
        if i.getchildren() and i.getchildren()[0].text is not None:  # if node has child and child has text, add key value in path
            path = path + '[' + prefix + ':' + find_tag_content(i.getchildren()[0].tag) + '="' + i.getchildren()[
                0].text + '"]'
        if i.attrib:  # if node has operation
            op = i.attrib[QName(yang_namespace.a, 'operation')]
            data = deepcopy(i)
            if 'merge' == op:
                del data.attrib[QName(yang_namespace.a, 'operation')]
                process_operation(data)
            elif 'delete' == op:
                data = ""
            else:
                del data.attrib[QName(yang_namespace.a, 'operation')]
            if isinstance(data, etree._Element):
                data = etree.tostring(data).decode('utf-8')
            op_dict = {'op': op, 'path': path, 'ns_map': ns_tmp, 'ns': get_namespace(i.tag), 'data': data}
            input_data.append(op_dict)
        if i.getchildren():
            parse_input_data(i.getchildren(), ns_tmp, path, input_data)

    return input_data

def get_namespace(tag):
    res = re.match(r'{.*}', tag)
    if res:
        return res.group()[1:-1]

def get_keys(value, ns):
    return [k for k, v in ns.items() if v == value]

def find_prefix(path):
    tag = path[path.rfind('/') + 1: path.rfind(':')]  # find the last ns in path, for example:/a1:interfaces/a1:interface  --> a1
    if '' == tag:
        tag = path[path.rfind('[') + 1: path.rfind(':')]
    return tag

def find_tag_content(tag):
    if re.match(r'{.*', tag):
        tag = tag[tag.rfind('}') + 1:]  # deal with the situation like :{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4 , and extract the "ipv4"
    return tag

def process_operation(root):
    if root.getchildren():
        for i in root.getchildren():
            if i.attrib:
                root.remove(i)
            else:
                process_operation(i)


if __name__ == '__main__':
    lists = parse_config_content()
    print(json.dumps(lists, indent=4))