import json
from swagger_server.mediator_framework.mediator_core import *
from swagger_server.mediator_framework.parse import parse_config_content


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
    if msg_type == "edit_config":
        expected_cc = compute_configuration_by_operation(neid, opdata)
        for i in expected_cc:
            expected_dc = translate_expected_cc_by_translation_point(neid, i)
            for i in expected_dc:
                compared_res = compare_device_configuration(neid, i)
                op_list = parse_config_content(compared_res)
                converted_msg.append(op_list)
    elif msg_type == "get_config":
        converted_msg = translate_get_config_content(neid, opdata)
    return converted_msg
