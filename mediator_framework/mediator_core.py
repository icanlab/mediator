from mediator_framework.tp_list import *
from mediator_framework.data_provider import *

def locate_translation_point(opdata):
    namespace = opdata["data"]["xmlns"]
    path = opdata["path"]
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None
    return path,PyTranslateReg[0]

def compute_configuration_by_operation(neid, json_data):
    path = json_data["path"]
    current_cc = get_controller_configuration(neid, path)
    cc = json_data["data"]
    oper = json_data["op"]
    expected_cc = None
    if oper == "merge":
        expected_cc = compute_merge(current_cc, cc)
    elif oper == "create" or oper == "replace":
        expected_cc  = cc
    else:
        expected_cc = compute_delete(current_cc,cc)
    return expected_cc

def translate_edit_congfig_content(data):
    expected_dc = None
    return expected_dc

def translate_get_config_content(data):
    expected_dc = None
    return expected_dc

def translate_rpcreply_data(rpcreply_data):
    return None

def compare_device_configuration(neid, expected_dc):
    path = expected_dc["path"]
    current_dc = get_device_configuration(neid,path)
    msg = compare(expected_dc,current_dc)
    return msg

### compute operation
def compute_merge(config, config1):
    return None

def compute_delete(config, config1):
    return None

### compare opeartion
def compare(config,config1):
    return None