import transform
from copy import deepcopy
import re


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
    if "@xmlns" in content.keys():
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
        prefix_num = -1
        path_list = item['path'].split("/")
        path_new = ""
        for sub_path in path_list:
            if len(sub_path) > 1 and not sub_path[0].isdigit():
                key_list = ['[name', '[ip']
                for k in key_list:
                    if k in sub_path:
                        index = sub_path.index(k)
                        temp = list(sub_path)
                        temp.insert(index+1, 'a' + str(prefix_num) + ':')
                        sub_path = "".join(temp)
                if "@xmlns" in sub_path:
                    prefix_num = prefix_num + 1
                    l = re.split('\[|\]|=\"|\"', sub_path)
                    index = l.index("@xmlns")
                    label = 'a' + str(prefix_num)
                    item['ns_map'][label] = l[index + 1]
                    item['ns'] = l[index+1]
                    del l[index + 1]
                    del l[index]
                    sub_path = ""
                    for i in l:
                        sub_path = sub_path + i
                sub_path = 'a' + str(prefix_num) + ':' + sub_path
                path_new = path_new + '/' + sub_path
            elif len(sub_path) != 0:
                path_new = path_new + '/' + sub_path
        item['path'] = path_new
        if item['data'] == {}:
            item['data'] = ""
        else:
            label = item['path'].split("/a")[-1]
            if "[" in label:
                index = label.index("[")
                label = label[2:index]
            else:
                label = label[2:]
            item['data'] = {label: item['data']}
            item['data'] = transform.json_to_xml(transform.dict_to_json(item['data']))
            item['data'] = item['data'].replace("\n", "").replace("\t", "").replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
    return data


def parse(content):
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
