import json
from swagger_server.mediator_framework.mediator_core import *
from swagger_server.mediator_framework.parse import parse_config_content, parse_get_config_content


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
