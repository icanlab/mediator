import connexion
import six
import logging
import os

# from swagger_server import util
# from swagger_server.mediator_framework.parse import *
from swagger_server.controllers.mediator_controller import *
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
        device_info = get_device_info_by_neid(neid)
        if xml_msg != "" and not xml_msg.isspace():
            if protocol == "netconf":
                classify_result = data_to_classify(xml_msg)
                rpc_model_type = classify_result[0]['rpc_model_type']
                data = classify_result[1]
                content = data['content_layer']
                if rpc_model_type == "rpc":
                    protocol_operation = classify_result[0]['protocol_operation']
                    if protocol_operation == "edit-config":
                        default_operation = data['default-operation']
                        data_to_core = rpc_edit_config_data_to_parse(content, default_operation)
                        return_data = edit_config_content_translation(neid, data_to_core, device_info)
                    elif protocol_operation == "get-config":
                        data_to_core = rpc_get_config_data_to_parse(content)
                        # return_data = function_2(neid, data_to_core)
                        return_data = ''
                elif rpc_model_type == "rpc-reply":
                    data_to_core = rpc_reply_data_to_parse(content)
                    # return_data = function_3(neid, data_to_core)
                    return_data = ''
                data_to_plugin = return_data_to_encapsulate(data, return_data)
        else:
            data_to_plugin = ""
    return make_response_xml(data_to_plugin)
