import json
from swagger_server.mediator_framework.mediator_core import *
def translate_msg_from_adaptor(neid, msg_type, opdata):  # noqa: E501
    """translte msg from adaptor

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
            expected_dc = translate_expected_cc_by_translation_point(neid, i)[0]
            compared_res = compare_device_configuration(neid, expected_dc)
            converted_msg.append(etree.tostring(compared_res, pretty_print=True).decode('utf-8'))
    return converted_msg[0]
