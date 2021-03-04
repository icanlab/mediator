import connexion
import six

# from swagger_server import util
# from swagger_server.mediator_framework.parse import *
# from swagger_server.controllers.mediator_controller import *
from swagger_server.controllers.mediator_controller import translate_msg_from_adaptor
from swagger_server.mediator_framework.adaptor  import *
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
        if protocol == "netconf":
            prepare = data_prepare(xml_msg)
            header = prepare[0]
            msg_config = prepare[1]
            data_to_core = unlock(msg_config)
            back = translate_msg_from_adaptor(neid, "edit_config", data_to_core)
            data_to_plugin = package(header, back)
            # data_to_plugin = data_to_plugin.replace("\n", "").replace("\t", "")
    return data_to_plugin
