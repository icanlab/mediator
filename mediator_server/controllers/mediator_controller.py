import json
from mediator_server.mediator_framework.mediator_core import *
from mediator_server.mediator_framework.parse import parse_config_content, parse_get_config_content


def translate_msg_from_adaptor(neid, msg_type, opdata):  # noqa: E501
    """translate msg from adaptor

     # noqa: E501

    :param neid: 
    :type neid: str
    :param msg_type: 
    :type msg_type: str
    :param opdata:

    :type opdata: str

    :rtype: str
    """
    converted_msg = []
    if isinstance(opdata, str):
        opdata = json.loads(opdata)
    device_info = get_device_info_by_neid(neid)
    if msg_type == "edit-config":
        expected_cc = compute_configuration_by_operation(neid, opdata, device_info)
        for i in expected_cc:
            expected_dc = translate_expected_cc_by_translation_point(neid, i, device_info)
            for i in expected_dc:
                compared_res = compare_device_configuration(neid, i)
                op_list = parse_config_content(compared_res)
                converted_msg.append(op_list)
    elif msg_type == "get-config":
        data = translate_get_config_content(neid, opdata, device_info)
        for i in data:
            converted_msg.append(parse_get_config_content(i))
    elif msg_type == "rpc-reply":
        data = translate_rpc_reply_data(neid, opdata, device_info)
        for i in data:
            converted_msg.append(parse_get_config_content(i))
    return converted_msg

def edit_config_content_translation(neid, input_data, device_info):
    compute_res = compute_src_configuration(neid, input_data, device_info)  # compute operation
    translate_res = translate_src_configuration_list(compute_res, device_info)  # translate operation
    compare_res = []
    for res in translate_res:
        root = res[0]
        xpath_obj = res[1]
        xpath = xpath_obj.path
        ns_map = xpath_obj.namespaces
        compare_configuration = root.getchildren()[0]
        compare_res.append(compare_target_configuration(neid, compare_configuration, xpath, ns_map))
    return compare_res

def get_config_content_translation(neid, input_data, device_info):
    res = []
    for item in input_data:
        schema_path = item['schema_path']
        xpath = item['path']
        config = item['data']
        translated_obj, target_xpath = translate_src_configuration(schema_path, xpath, config, device_info)
        res.append([target_xpath, translated_obj])
    return res

def rpc_reply_data_translation(neid, input_data, device_info):
    res = []
    for item in input_data:
        schema_path = item['schema_path']
        xpath = item['path']
        config = item['data']
        translated_obj, target_xpath = translate_src_configuration(schema_path, xpath, config, device_info)
        res.append([target_xpath, translated_obj])
    return res