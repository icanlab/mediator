import transform


# unlock
def get_header(flag, content):
    """
    :param flag: the end of the recursive
    :param content: complete data from plugin
    :type content: dict
    :return: msg_header: header information in the data
    """
    msg_header = dict()
    for sub_key, sub_value in content.items():
        if flag:
            if sub_key.startswith("@"):
                msg_header[sub_key] = sub_value
                return msg_header
        elif isinstance(sub_value, dict):
            if sub_key == "config":
                flag = 1
            sub_value = get_header(flag, sub_value)
        msg_header[sub_key] = sub_value
    return msg_header


def list_traversal(path, content):
    """
    :param path:  hierarchical path to the list
    :type path: str
    :param content: content of the list
    :type content: list
    :return: data: data after unpacking
    :return: flag: decide whether a sub_node need to be generated
    """
    data = list()
    flag = 0
    for item in content:
        if isinstance(item, dict):
            flag = 1
            result = dict_traversal(path, item)
            data.append(result)
        else:
            data.append(item)
    return data, flag


def dict_traversal(path, content):
    """
    :param path: hierarchical path to the dict
    :type path: str
    :param content: content of the dict
    :type content: dict
    :return: data: data in standard format after unpacking
    """
    data = dict()
    n = 0
    if "#text" in content.keys():
        return content
    elif "@xc:operation" in content.keys():
        data['op'] = content['@xc:operation']
        del content['@xc:operation']
    else:
        data['op'] = "merge"
    data['path'] = path
    data['data'] = dict()
    for sub_key, sub_value in content.items():
        path_str = path + "/" + sub_key
        if isinstance(sub_value, list):
            result = list_traversal(path_str, sub_value)
            if result[1]:
                for item in result[0]:
                    k = "sub_node_" + str(n)
                    data[k] = item
                    n = n + 1
            else:
                data['data'][sub_key] = sub_value
        elif isinstance(sub_value, dict):
            result = dict_traversal(path_str, sub_value)
            if "#text" in result.keys():
                data['data'][sub_key] = sub_value
            else:
                k = "sub_node_" + str(n)
                data[k] = result
                n = n + 1
        else:
            data['data'][sub_key] = sub_value
    data['data'] = {path.split("/")[-1]: data['data']}
    data['data'] = transform.json_to_xml(transform.dict_to_json(data['data']))
    data['data'] = data['data'].replace("\n", "").replace("\t", "").replace(
        "<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
    return data


def unlock(content):
    """
    :param content: data used to unpack
    :type content: dict
    :return: data_to_core: data prepared for Mediator core
    """
    data_to_core = list()
    for key, value in content.items():
        if not key.startswith("@"):
            result = dict_traversal(key, value)
            data_to_core.append(result)
    # print("data_to_core；")
    # print(data_to_core)
    return data_to_core


# package
def refactor(message):
    """
    :param message: data in standard format from Mediator core
    :type message: dict
    :return: data after packaging
    """
    key = message['path'].split("/")[-1]
    data = transform.json_to_dict(transform.xml_to_json(message['data']))
    if isinstance(data[key], dict):
        if not message['op'] == "merge":  # decide whether or not the default merge operation exists
            data[key]['@xc:operation'] = message['op']
    else:
        data[key] = dict()
        if not message['op'] == "merge":
            data[key]['@xc:operation'] = message['op']
    if "sub_node_0" in message.keys():
        for sub_key, sub_value in message.items():
            if sub_key.startswith("sub_node_"):
                inner_data = refactor(sub_value)
                k = list(inner_data.keys())[0]
                if k in data[key].keys():
                    if isinstance(data[key][k], list):
                        data[key][k].append(inner_data[k])
                    elif isinstance(data[key][k], dict):
                        temp = data[key][k]
                        data[key][k] = list()
                        data[key][k].append(temp)
                        data[key][k].append(inner_data[k])
                else:
                    data[key][k] = inner_data[k]
    return data


def package(header, message):
    """
    :param header: header information previously temporarily stored
    :type header: dict
    :param message: data from Mediator core
    :type message: list
    :return: data_to_plugin: data returned to plugin
    """
    data_to_plugin = ""
    for value in message:
        result = refactor(value)
        data_to_plugin = data_to_plugin + transform.dict_to_json(result)
    data_to_plugin = transform.json_to_dict(data_to_plugin)
    for k in data_to_plugin.keys():
        header['rpc']['edit-config']['config'][k] = data_to_plugin[k]
    data_to_plugin = transform.json_to_xml(transform.dict_to_json(header))
    # print("data_to_plugin:")
    # print(data_to_plugin)
    return data_to_plugin


# data preparation
def data_prepare(msg_xml):
    """
    :param msg_xml: xml data from plugin
    :type msg_xml: str
    :return: msg_header: temporarily store header information
    :return: msg_config: use to unpack
    """
    msg_json = transform.xml_to_json(msg_xml)
    msg_dict = transform.json_to_dict(msg_json)
    msg_config = dict()
    # action_type = "edit-config"
    if 'edit-config' in msg_dict['rpc'].keys():
        msg_config = msg_dict['rpc']['edit-config']['config']
    elif 'get-config' in msg_dict['rpc'].keys():
        # action_type = "get-config"
        msg_config = msg_dict['rpc']['get-config']['config']
    msg_header = get_header(0, msg_dict)
    return msg_header, msg_config
