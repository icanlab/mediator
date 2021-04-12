from copy import deepcopy
from lxml import etree
from lxml.etree import QName
import re
import json


def get_tag(el):
    tag = QName(el.tag).localname
    return tag


def get_ns(el):
    ns = QName(el.tag).namespace
    return ns


def get_model_name(ns):
    model_name = ns.split(':')[-1]
    return model_name


def data_to_classify(xml_msg):
    model = {}
    data = {}
    parse = etree.XMLParser(remove_blank_text=True)
    message = etree.fromstring(xml_msg, parser=parse)
    # data['original_message'] = deepcopy(message)
    ns_map = message.nsmap
    # netconf_ns = ns_map[None]
    model['rpc_model_type'] = get_tag(message)   # messages layer
    data_to_parse = deepcopy(message[0])
    message.remove(message[0])
    data['messages_layer'] = message
    if model['rpc_model_type'] == "rpc":
        model['protocol_operation'] = get_tag(data_to_parse)    # operations layer
        data['operations_layer'] = data_to_parse
        data['content_layer'] = deepcopy(data_to_parse[-1])
        data_to_parse.remove(data_to_parse[-1])
        if model['protocol_operation'] == "edit-config":
            if data['operations_layer'].find('default-operation', ns_map) is not None:
                data['default-operation'] = data['operations_layer'].find('default-operation', ns_map).text
            else:
                data['default-operation'] = ''
    elif model['rpc_model_type'] == "rpc-reply":
        data['content_layer'] = data_to_parse
    return model, data


def edit_config_pretreat(content, default_op, attrib_op):
    if default_op == "merge" or default_op == "replace":
        for i in range(len(content)):
            content[i].set(attrib_op, 'merge')
    elif default_op == '':
        for i in range(len(content)):
            if content[i].get(attrib_op) is None:
                content[i].set(attrib_op, 'merge')
    return content


def get_node_from_data(parent_node_data, attrib_op, ns_map):
    node_list = []
    trim_list = []
    for child in parent_node_data:
        if child.get(attrib_op):
            trim_list.append(child)
            child_content = deepcopy(child)
            nodes = get_child(child_content, attrib_op, ns_map)
            node_list = node_list + nodes
        elif len(child):
            nodes = get_node_from_data(child, attrib_op, ns_map)
            for node in nodes:
                ns_list = dict(zip(node['ns_map'].values(), node['ns_map'].keys()))
                path = '/' + ns_list[get_ns(child)] + ':' + get_tag(child)
                node['path'] = path + node['path']
                node_list.append(node)
    for item in trim_list:
        parent_node_data.remove(item)
    return node_list


def get_child(content, attrib_op, ns_map):
    node_list = []
    node = dict()
    node['op'] = content.get(attrib_op)
    del content.attrib[attrib_op]
    node['path'] = ''
    node['schema_path'] = ''
    node['ns_map'] = deepcopy(ns_map)
    node['ns'] = content.nsmap[None]
    if node['ns'] not in node['ns_map'].values():
        prefix_label = chr(ord('a')+len(node['ns_map'])-1)
        node['ns_map'][prefix_label] = node['ns']
    ns_list = dict(zip(node['ns_map'].values(), node['ns_map'].keys()))
    node['path'] = '/' + ns_list[get_ns(content)] + ':' + get_tag(content)
    if content[0].text is not None:     # add the namespace for path
        node['path'] = node['path'] + '[' + ns_list[get_ns(content[0])] + ':' + get_tag(content[0]) \
                       + '="' + content[0].text + '"]'
    node_list.append(node)
    if node['op'] != "delete" and node['op'] != "remove":
        node['data'] = content
        nodes_from_data = get_node_from_data(node['data'], attrib_op, node['ns_map'])
        for item in nodes_from_data:
            item['path'] = node['path'] + item['path']
            node_list.append(item)
#         node['data'] = etree.tostring(node['data'])
#         node['data'] = str(node['data'], encoding='ascii')
    return node_list


def rpc_edit_config_data_to_parse(content, default_op):
    data = []
    ns_map = content.nsmap
    del ns_map[None]
    prefix = list(ns_map.keys())[0]
    attrib_op = QName(ns_map[prefix], 'operation')
    content = edit_config_pretreat(content, default_op, attrib_op)
    for i in range(len(content)):
        node_list = get_child(content[i], attrib_op, ns_map)
        # print("node_list:\n", node_list)
        data = data + node_list
    del_list = []
    for index, item in enumerate(data):
        # item['schema_path'] = ''
        if 'data' in item.keys() and len(item['data']) == 0:
            del_list.append(index)
        else:
            split_list = re.split('\[|\]', deepcopy(item['path']))
            for x in split_list:
                if "=" not in x:
                    item['schema_path'] = item['schema_path'] + x
            for k in item['ns_map'].keys():
                if '/'+k+':' in item['schema_path']:
                    model_name = get_model_name(item['ns_map'][k])
                    item['schema_path'] = item['schema_path'].replace('/'+k+':', '/'+model_name+':', 1)
                    item['schema_path'] = item['schema_path'].replace('/'+k+':', '/')
    del_list.reverse()
    for i in del_list:
        del data[i]
    return data


def rpc_get_config_data_to_parse(content):
    data = []
    for i in range(len(content)):
        data.append({})
        data[i]['ns'] = content[i].nsmap[None]
        data[i]['path'] = '/' + get_tag(content[i])
        data[i]['data'] = content[i]
        # data[i]['data'] = etree.tostring(content[i])
    return data


def rpc_reply_data_to_parse(content):
    data = []
    for i in range(len(content)):
        data.append({})
        data[i]['ns'] = content[i].nsmap[None]
        data[i]['path'] = '/' + get_tag(content[i])
        data[i]['data'] = content[i]
        # data[i]['data'] = etree.tostring(content[i])
    return data


def return_data_to_encapsulate(data, back):
    return data
