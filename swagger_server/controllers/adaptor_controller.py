import connexion
import six
import logging
import os

# from swagger_server import util
# from swagger_server.mediator_framework.parse import *
# from swagger_server.controllers.mediator_controller import *
from swagger_server.controllers.mediator_controller import translate_msg_from_adaptor
from swagger_server.controllers.util import make_response_json, make_response_xml
from swagger_server.mediator_framework.adaptor import *
from swagger_server.models.input_msg import InputMsg


def translate_msg(body=None):  # noqa: E501
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
    if connexion.request.is_json:
        body = InputMsg.from_dict(connexion.request.get_json())  # noqa: E501
        protocol = body.protocol
        neid = body.neid
        xml_msg = body.message
        if xml_msg != "" and not xml_msg.isspace():
            if protocol == "netconf":
                prepare = data_prepare(xml_msg)
                header = prepare[0]
                msg_config = prepare[1]
                if header:
                    data_to_core = unlock(msg_config)
                    protocol_operation = data_to_core[0]
                    data = data_to_core[1]
                    back = translate_msg_from_adaptor(neid, protocol_operation, data)
                    data_to_plugin = package(header, back)
                else:
                    data_to_plugin = xml_msg
        else:
            data_to_plugin = ""
    return make_response_xml(data_to_plugin)
