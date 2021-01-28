import connexion
import six

from swagger_server import util
from mediator_framework.mediator_core import *


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
    converted_msg = None
    if msg_type == "edit_config":
        expected_cc = compute_configuration_by_operation(neid,opdata)
        expected_dc = translate_edit_congfig_content(expected_cc)
        converted_msg = compare_device_configuration(neid,expected_dc)
    elif msg_type == "get_config":
        converted_msg = translate_get_config_content(opdata)
    return converted_msg
