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
        root = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})  # add the config element
        converted_msg = parse_keyvalue_all(opdata, root)
    return 'it work'
