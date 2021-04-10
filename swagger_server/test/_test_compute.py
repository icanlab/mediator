import json

from lxml import etree

from swagger_server.mediator_framework.mediator_core import compute_configuration_by_operation
from swagger_server.mediator_framework.mediator_core import *
from swagger_server.mediator_framework.data_provider import *

def _test_compute_ietf_interfaces():
    with open('input_op_list/ietf_interfaces.json', 'r') as f:
        json_data = json.load(f)
        neid = 'router 0'
        device_info = get_device_info_by_neid(neid)
        res = compute_configuration_by_operation(neid, json_data, device_info)
        print(etree.tostring(res[0][1], pretty_print=True).decode('utf-8'))

def _test_compute_ietf_routing():
    with open('input_op_list/ietf_routing.json', 'r') as f:
        json_data = json.load(f)
        neid = 'route 1'
        res = compute_configuration_by_operation(neid, json_data)
        print(etree.tostring(res[0][1], pretty_print=True).decode('utf-8'))

def _test_compute_ietf_l3vpn_ntw():
    with open('input_op_list/ietf_l3vpn_ntw.json', 'r') as f:
        json_data = json.load(f)
        neid = 'route 2'
        res = compute_configuration_by_operation(neid, json_data)
        # print(res)
        print(etree.tostring(res[0][1], pretty_print=True).decode('utf-8'))

def _test_ietf_interfaces_non_top_level_translation():
    with open('input_op_list/test_interfaces.json', 'r') as f:
        input_data = json.load(f)
        # compute
        compute_res = compute_src_configuration('neid', input_data)
        print(compute_res)
    # translate
    device_info = ('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2')
    translate_res = translate_src_configuration_list(compute_res, device_info)
    print(translate_res)
    compare_res = []
    for root in translate_res:
        print(etree.tostring(root, pretty_print=True).decode('utf-8'))
        converted_msg = compare_device_configuration('neid', root)
        print(etree.tostring(converted_msg, pretty_print=True).decode('utf-8'))
        compare_res.append(converted_msg)
    return compare_res

if __name__ == '__main__':
    # _test_compute_ietf_interfaces()
    # _test_compute_ietf_routing()
    # _test_compute_ietf_l3vpn_ntw()
    _test_ietf_interfaces_non_top_level_translation()