import swagger_server.mediator_framework.transform
from copy import deepcopy
import re

prefix = ""
config_xmlns = ""
op_property = "@xc:operation"


def get_header(content_str):
    """
    :param content_str: complete data from plugin
    :type content_str: dict
    :return: msg_header: the header information of the data
    """
    msg_header = deepcopy(content_str)
    if "edit-config" in msg_header['rpc'].keys():
        del msg_header['rpc']['edit-config']['config']
    return msg_header


def data_prepare(msg_xml):
    """
    prepare data in standard format for unlocking
    :param msg_xml: xml data from plugin
    :type msg_xml: str
    :return: header: temporarily store header information
    :return: msg_config: use to unpack
    """
    msg_json = transform.xml_to_json(msg_xml)
    msg_dict = transform.json_to_dict(msg_json)
    msg_config = msg_dict['rpc']['edit-config']['config']
    header = get_header(msg_dict)
    global prefix
    global config_xmlns
    global op_property
    for item in msg_config.keys():
        if item.startswith("@xmlns"):
            prefix = item.split(":")[-1]
            config_xmlns = msg_config[item]
            op_property = '@' + prefix + ':operation'
            break
    if "default-operation" in msg_dict['rpc']['edit-config'].keys():
        if msg_dict['rpc']['edit-config']['default-operation'] != "None":
            default_op = msg_dict['rpc']['edit-config']['default-operation']
            for item in msg_config.keys():
                if not item.startswith("@"):
                    if op_property in msg_config[item].keys():
                        msg_config[item][op_property] = default_op
                    else:
                        msg_config[item][op_property] = default_op
    else:
        for item in msg_config.keys():
            if not item.startswith("@"):
                msg_config[item][op_property] = "merge"
    return header, msg_config


# unlock part
def get_child(path, content_str):
    """
    get child node
    :param path: the path of the child node
    :type path: str
    :param content_str: the content of the child node
    :type content_str: dict
    :return: data: new child node
    """
    data = dict()
    content = deepcopy(content_str)
    data['op'] = content[op_property]
    del content[op_property]
    data['path'] = '/' + path
    path_list = path.split("/")
    if ("@xmlns" in content.keys()) and ("@xmlns" not in path_list[-1]):
        data['path'] = data['path'] + '[@xmlns="' + content['@xmlns'] + '"]'
    data['ns_map'] = {prefix: config_xmlns}
    data['ns'] = ""
    data['data'] = dict()
    for key, value in content.items():
        data['data'][key] = value
    if data['op'] == "delete" or data['op'] == "remove":
        data['data'] = {}
    return data


def get_path_key(path, content):
    """
    add key to the path and find the namespace from the path
    :param path: the existing path
    :type path: str
    :param content: data that may contain a key
    :return: path: the path added key or namespace
    """
    key_list = ['name', 'ip', '@xmlns']
    for key_item in key_list:
        if key_item in content.keys():
            path = path + '[' + key_item + '="' + content[key_item] + '"]'
    return path


def data_traversal(path, content_str):
    """
    traversal the op_node['data']
    :param path: op_node['path']
    :type path: str
    :param content_str: op_node['data']
    :type content_str: dict
    :return: op_list: the list of op_node from op_node['data']
    """
    op_list = list()
    content = deepcopy(content_str)
    for key, value in content.items():
        path_str = path + "/" + key
        if isinstance(value, dict):
            back_list = dict_traversal(path_str, content_str[key])
            if back_list[0]:
                del content_str[key]
            if len(back_list[1]):
                for item in back_list[1]:
                    op_list.append(item)
        elif isinstance(value, list):
            back_list = list_traversal(path_str, content_str[key])
            for item in back_list:
                op_list.append(item)
    return op_list


def dict_traversal(path, content_src):
    """
    traverse the dict
    :param path: hierarchical path to the dict
    :type path: str
    :param content_src: content of the dict
    :type content_src: dict
    :return: op_list: the list of op_node from dict
    """
    flag = 0
    op_list = list()
    content = deepcopy(content_src)
    path = get_path_key(path, content)
    if op_property in content.keys():
        flag = 1
        result = get_child(path, content)
        op_list.append(result)
        back_list = data_traversal(result['path'], result['data'])
        for item in back_list:
            op_list.append(item)
    else:
        back_list = data_traversal(path, content_src)
        for item in back_list:
            op_list.append(item)
    return flag, op_list


def list_traversal(path, content_src):
    """
    traverse the list
    :param path: hierarchical path to the list
    :type path: str
    :param content_src: content of the list
    :type content_src: list
    :return: op_list: the list of op_node from list
    """
    op_list = list()
    content = deepcopy(content_src)
    del_index_list = []
    for index, dict_item in enumerate(content):
        back_list = dict_traversal(path, content_src[index])
        if back_list[0]:
            del_index_list.append(index)
        if len(back_list[1]):
            for item in back_list[1]:
                op_list.append(item)
    del_index_list.reverse()
    for i in del_index_list:
        del content_src[i]
    return op_list


def add_ns(data):
    """
    normalize op_node['path'] and op_node['data'] and get op_node['ns_map'] and op_node['ns']
    :param data: the data prepared for Mediator core
    :type data: list
    :return: the data can send to Mediator core
    """
    for item in data:
        prefix_label = chr(ord('a') - 1)
        path_list = item['path'].split("/")
        path_new = ""
        for sub_path in path_list:
            if len(sub_path) > 1 and not sub_path[0].isdigit():
                key_list = ['[name', '[ip']
                for k in key_list:
                    if k in sub_path:
                        index = sub_path.index(k)
                        temp = list(sub_path)
                        temp.insert(index + 1, prefix_label + ':')
                        sub_path = "".join(temp)
                if "@xmlns" in sub_path:
                    prefix_label = chr(ord(prefix_label) + 1)
                    l = re.split('\[|\]|=\"|\"', sub_path)
                    index = l.index("@xmlns")
                    item['ns_map'][prefix_label] = l[index + 1]
                    item['ns'] = l[index + 1]
                    del l[index + 1]
                    del l[index]
                    sub_path = ""
                    for i in l:
                        sub_path = sub_path + i
                sub_path = prefix_label + ':' + sub_path
                path_new = path_new + '/' + sub_path
            elif len(sub_path) != 0:
                path_new = path_new + '/' + sub_path
        item['path'] = path_new
        if item['data'] == {}:
            item['data'] = ""
        else:
            label = re.split('/[a-z]:', item['path'])[-1]
            if "[" in label:
                index = label.index("[")
                label = label[:index]
            item['data'] = {label: item['data']}
            item['data'] = transform.json_to_xml(transform.dict_to_json(item['data']))
            item['data'] = item['data'].replace("\n", "").replace("\t", "").replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
    return data


def unlock(content):
    """
    parse the data from Plugin and standardize the data formats
    :param content: data that has been preprocessed
    :type content: dict
    :return: data_to_core: the list of the op_node
    """
    data_to_core = list()
    for key, value in content.items():
        if not key.startswith("@"):
            dt = get_child(key, value)
            data_to_core.append(dt)
            back_list = data_traversal(dt['path'], dt['data'])
            for item in back_list:
                data_to_core.append(item)
    data_to_core = add_ns(data_to_core)
    return data_to_core


# package part
def refactor(node_info, prefix_l):
    """
    populate the data to complete it
    :param node_info: node information
    :type node_info: dict
    :param prefix_l: op_property
    :type prefix_l: str
    :return:  node_info: node information after populating
    """
    prefix_label = re.sub("@", "", prefix_l)
    if node_info['op'] == "delete" or node_info['op'] == "remove":
        k = re.split('/[a-z]:', node_info['path'])[-1]
        path = deepcopy(node_info['path'])
        key_value = []
        while "[" in path:
            l_index = path.index("[")
            r_index = path.index("]")
            key_value = re.split('=\"|\"', path[l_index + 1:r_index].split(":")[-1])  # eg: ['name', 'GigabitEthernet 3/0/1', '']
            path = path.replace(path[l_index:r_index + 1], "", 1)
        path = path.split("/")[-1]  # eg: "b:address"
        path_list = path.split(":")  # eg: ['b', 'address']
        root = path_list[-1]  # eg: "address"
        node_info['data'] = {root: ""}
        ns = "/" + path_list[0] + ":"  # eg: "/b:"
        if node_info['path'].count(ns) == 1:
            node_info['data'][root] = dict()
            node_info['data'][root]['@xmlns'] = node_info['ns']
        if "[" in k:
            if isinstance(node_info['data'][root], str):
                node_info['data'][root] = dict()
            node_info['data'][root][key_value[0]] = key_value[1]
    else:
        node_info['data'] = transform.json_to_dict(transform.xml_to_json(node_info['data']))
    key = list(node_info['data'].keys())[0]
    op_label = "@" + prefix_label
    node_info['data'][key][op_label] = node_info['op']
    return node_info


def child_judge(parent, child):
    """
    judge the parent-child relationship between nodes
    :param parent: previous node
    :type parent: dict
    :param child: later node
    :type child: dict
    :return: flag: sign the relationship between parameters
    :return parent: previous node adjusted according to the parent-child relationship
    """
    flag = 1
    if parent['path'] in child['path']:
        f = 0
        label_list = list(parent.keys())
        if len(label_list) > 5:
            for sub_node in label_list[5:]:
                result = child_judge(parent[sub_node], child)
                f = result[0]
                if f:
                    parent[sub_node] = result[1]
                    break
        if f == 0:
            key = "sub_node_" + str(len(label_list) - 5)
            parent[key] = child
    else:
        flag = 0
    return flag, parent


def encapsulate_nested(total):
    """
    incorporate child_node
    :param total: top_node information
    :type total: dict
    :return: total: top_node information after incorporating child_node data
    """
    label_list = list(total.keys())
    root = list(total['data'].keys())[0]
    if len(label_list) > 5:
        for sub_node in label_list[5:]:
            child = encapsulate_nested(total[sub_node])
            path_list = re.split('/[a-z]:|\[[a-z]:|\]', child['path'])
            while '' in path_list:
                path_list.remove('')
            if "=" in path_list[-1]:
                del path_list[-1]
            child_key = deepcopy(path_list[-1])
            del path_list[-1]
            root_index = path_list.index(root)
            path_length = len(path_list[root_index:]) - 1
            data = total['data']
            for index, path in enumerate(path_list[root_index:]):
                if "=" in path:
                    k_v = re.split('=\"|\"', path)
                    if isinstance(data, dict):
                        if (k_v[0] in data.keys()) and (data[k_v[0]] == k_v[1]):
                            if index == path_length:
                                if child_key in data.keys():
                                    if isinstance(data[child_key], dict):
                                        temp = data[child_key]
                                        data[child_key] = list()
                                        data[child_key].append(temp)
                                        data[child_key].append(child['data'][child_key])
                                    elif isinstance(data[child_key], list):
                                        data[child_key].append(child['data'][child_key])
                                else:
                                    data[child_key] = child['data'][child_key]
                        else:
                            temp = data
                            data = list()
                            data.append(temp)
                            data.append(child['data'][child_key])
                    elif isinstance(data, list):
                        for i, branch in enumerate(data):
                            if (k_v[0] in branch.keys()) and (branch[k_v[0]] == k_v[1]):
                                if index == path_length:
                                    if child_key in branch.keys():
                                        if isinstance(branch[child_key], dict):
                                            temp = branch[child_key]
                                            branch[child_key] = list()
                                            branch[child_key].append(temp)
                                            branch[child_key].append(child['data'][child_key])
                                        elif isinstance(branch[child_key], list):
                                            branch[child_key].append(child['data'][child_key])
                                    else:
                                        branch[child_key] = child['data'][child_key]
                                else:
                                    data = data[i]
                                break
                elif path in data.keys():
                    if index == path_length:
                        if isinstance(data[path], dict):
                            if child_key in data[path].keys():
                                if isinstance(data[path][child_key], dict):
                                    temp = data[path][child_key]
                                    data[path][child_key] = list()
                                    data[path][child_key].append(temp)
                                    data[path][child_key].append(child['data'][child_key])
                                elif isinstance(data[path][child_key], list):
                                    data[path][child_key].append(child['data'][child_key])
                            else:
                                data[path][child_key] = child['data'][child_key]
                        else:
                            data[path] = dict()
                            data[path][child_key] = child['data'][child_key]
                    else:
                        data = data[path]
    return total


def package(header, message):
    """
    package the data from Mediator core
    :param header: header information previously temporarily stored
    :type header: dict
    :param message: data from Mediator core
    :type message: list
    :return: data can be passed to plugin after packaging
    """
    data_to_plugin = ""
    xmlns_label = "@xmlns:" + prefix
    header['rpc']['edit-config']['config'] = {xmlns_label: config_xmlns}
    temp = list()
    if isinstance(message[0], list):
        message = [x for item in message for x in item]
    for child in message:
        result = refactor(child, op_property)
        if data_to_plugin == "":
            data_to_plugin = result
        else:
            back = child_judge(data_to_plugin, result)
            if back[0]:
                data_to_plugin = back[1]
            else:
                temp.append(data_to_plugin)
                data_to_plugin = ""
    if data_to_plugin:
        temp.append(data_to_plugin)
    for top in temp:
        top_node = encapsulate_nested(top)
        top_root = list(top_node['data'].keys())[0]
        header['rpc'][
            'edit-config']['config'][top_root] = top_node['data'][top_root]
        data_to_plugin = transform.json_to_xml(transform.dict_to_json(header))
    return data_to_plugin
