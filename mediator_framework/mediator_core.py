from mediator_framework.tp_list import *

def locate_translation_point(opdata):
    namespace = opdata["data"]["xmlns"]
    path = opdata["path"]
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None
    return path,PyTranslateReg[0]

def compute_configuration_by_neid(current_cc,opdata):
    return None

def translate_edit_congfig_content(json_data):
    return None

def translate_get_config_content(json_data):
    return None

def translate_rpcreply_data(rpcreply_data):
    return None

def compare_device_configuration(current_dc,converted_json_data):
    return None