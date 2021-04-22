from copy import deepcopy
from lxml import etree
from lxml.etree import QName
import re
import json


class XPATH(etree.XPath):
    def __init__(self, path, namespaces=None):
        super(XPATH, self).__init__(path, namespaces=namespaces)
        self.namespaces = namespaces


def get_xpath(path, ns_map):
    xpath = XPATH(path, ns_map)
    return xpath


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
    message = etree.fromstring(xml_msg.encode('utf-8'), parser=parse)
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
                node['xpath'] = path + node['xpath']
                node_list.append(node)
    for item in trim_list:
        parent_node_data.remove(item)
    return node_list


def get_child(content, attrib_op, ns_map):
    node_list = []
    node = dict()
    node['op'] = content.get(attrib_op)
    del content.attrib[attrib_op]
    node['xpath'] = ''
    node['ns_map'] = deepcopy(ns_map)
    if content.nsmap[None] not in node['ns_map'].values():
        prefix_label = chr(ord('a')+len(node['ns_map'])-1)
        node['ns_map'][prefix_label] = content.nsmap[None]
    ns_list = dict(zip(node['ns_map'].values(), node['ns_map'].keys()))
    node['xpath'] = '/' + ns_list[get_ns(content)] + ':' + get_tag(content)
    if content[0].text is not None:     # add the namespace for path
        node['xpath'] = node['xpath'] + '[' + ns_list[get_ns(content[0])] + ':' + get_tag(content[0]) \
                       + '="' + content[0].text + '"]'
    node_list.append(node)
    if node['op'] == "delete" or node['op'] == "remove":
        node['data'] = content
        for index in range(len(content)):
            if index != 0:
                node['data'].remove(node['data'][1])
    else:
        node['data'] = content
        nodes_from_data = get_node_from_data(node['data'], attrib_op, node['ns_map'])
        for item in nodes_from_data:
            item['xpath'] = node['xpath'] + item['xpath']
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
        if len(item['data']) == 0:
            del_list.append(index)
        else:
            item['xpath'] = get_xpath(item['xpath'], item['ns_map'])
            del item['ns_map']
    del_list.reverse()
    for i in del_list:
        del data[i]
    return data


def rpc_get_config_data_to_parse(content):
    data = []
    for i in range(len(content)):
        data.append({})
        data[i]['path'] = '/' + get_tag(content[i])
        data[i]['schema_path'] = '/' + get_model_name(content[i].nsmap[None]) + ':' + get_tag(content[i])
        data[i]['ns'] = content[i].nsmap[None]
        data[i]['data'] = content[i]
        # data[i]['data'] = etree.tostring(content[i])
    return data


def rpc_reply_data_to_parse(content):
    data = []
    for i in range(len(content)):
        data.append({})
        data[i]['path'] = '/' + get_tag(content[i])
        data[i]['schema_path'] = '/' + get_model_name(content[i].nsmap[None]) + ':' + get_tag(content[i])
        data[i]['ns'] = content[i].nsmap[None]
        data[i]['data'] = content[i]
        # data[i]['data'] = etree.tostring(content[i])
    return data


def return_data_to_encapsulate(data, back):
    data_to_plugin = data['messages_layer']
    rpc_model_type = get_tag(data['messages_layer'])
    if rpc_model_type == 'rpc':
        data_to_plugin.append(data['operations_layer'])
        protocol_operation = get_tag(data['operations_layer'])
        if protocol_operation == 'edit-config':
            op_layer = data_to_plugin.xpath('//x:edit-config',
                                            namespaces={'x': 'urn:ietf:params:xml:ns:netconf:base:1.0'})[0]
            for i in range(len(data['content_layer'])):
                data['content_layer'].remove(data['content_layer'][0])
            nns_0 = data['content_layer'].nsmap
            del nns_0[None]
            root = etree.Element(get_tag(data['content_layer']), nsmap=nns_0)
            position = -1
            for item in back:
                nns = nns_0
                inner_layer = root
                path_list = [x for x in item[0].path.split('/') if x != '']
                flags = []
                for i, s in enumerate(path_list):   # to deal with the key
                    if len(s) == 1:
                        flags.append(i)
                flags.reverse()
                for flag in flags:
                    path_list[flag-1] = path_list[flag-1]+'/'+path_list[flag]+'/'+path_list[flag+1]
                    del path_list[flag]
                    del path_list[flag]
                mark = 0
                for i, p in enumerate(path_list):
                    nns[p.split(':')[0]] = item[0].namespaces[p.split(':')[0]]
                    if i == len(path_list) - 1:
                        f = inner_layer.xpath(p, namespaces=nns)
                        if len(f) != 0:
                            inner_layer.remove(f[0])
                        inner_layer.append(item[1])
                    else:
                        if mark == 0:
                            temp = inner_layer.xpath(p.split('[')[0].split(':')[-1], namespaces={})
                        else:
                            temp = inner_layer.xpath(p, namespaces=nns)
                        if len(temp) == 0:
                            tag = p.split('[')[0].split(':')[-1]
                            inner_layer = etree.SubElement(inner_layer, tag,
                                                           nsmap={None: nns[p.split(':')[0]]})
                            if nns[p.split(':')[0]] is not None:
                                mark = 1
                                position = i
                        else:
                            inner_layer = temp[0]
                            if i == position:
                                mark = 1

            op_layer.append(root)
        elif protocol_operation == 'get-config':
            op_layer = data_to_plugin.xpath('//x:get-config',
                                            namespaces={'x': 'urn:ietf:params:xml:ns:netconf:base:1.0'})[0]
            for i in range(len(data['content_layer'])):
                data['content_layer'].remove(data['content_layer'][0])
            ns_get = data['content_layer'].nsmap
            op_layer.append(data['content_layer'])
            root = data_to_plugin.xpath('//x:filter', namespaces={'x': ns_get[None]})[0]
            for child in back:
                root.append(child[1])
    elif rpc_model_type == 'rpc-reply':
        for i in range(len(data['content_layer'])):
            data['content_layer'].remove(data['content_layer'][0])
        data_to_plugin.append(data['content_layer'])
        for child in back:
            data_to_plugin[0].append(child[1])
    return data_to_plugin
