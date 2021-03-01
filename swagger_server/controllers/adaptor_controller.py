import connexion
import six

from swagger_server import util
from swagger_server.mediator_framework.parse import *
from swagger_server.controllers.mediator_controller import *

def translate_msg(protocol, neid, xml_msg):  # noqa: E501
    """translate msg

     # noqa: E501

    :param protocol: 
    :type protocol: str
    :param neid: 
    :type neid: str
    :param xml_msg: 
    :type xml_msg: str

    :rtype: str
    """
    converted_msg = []
    if 'netconf' == protocol:
        if isinstance(xml_msg, str):
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.fromstring(xml_msg, parser=parse)  # get config node
            op_data = parse_config_content(root)
            res = translate_msg_from_adaptor(neid, 'edit_config', op_data)
            converted_msg.append(res)
    return res
