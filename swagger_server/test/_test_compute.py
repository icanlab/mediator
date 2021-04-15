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
        # print("compute res is :\n", compute_res)
        print("compute configuration is :\n",
              etree.tostring(compute_res[0][2], pretty_print=True).decode('utf-8'))
    # translate
    device_info = ('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2')
    translate_res = translate_src_configuration_list(compute_res, device_info)
    print(translate_res)
    compare_res = []
    for res in translate_res:
        root = res[0]
        xpath = res[1]
        ns_map = res[2]
        print("translated res is :\n",
              etree.tostring(root.getchildren()[0], pretty_print=True).decode('utf-8'))
        compare_configuration = root.getchildren()[0]
        compare_res.append(compare_target_configuration('router', compare_configuration, xpath, ns_map))
    return compare_res

def parse_key_from_xpath(xpath):
    res = re.finditer(r'\[.*?\]', xpath)
    keys_map = {}
    for i in res:
        tmp = re.sub(r'[a-z]{1}:{1}', '', i.group()[1:-1])
        index = tmp.find('=')
        key = tmp[:index]
        value = tmp[index+2:-1]
        keys_map[key] = value
    return keys_map

if __name__ == '__main__':
    # _test_compute_ietf_interfaces()
    # _test_compute_ietf_routing()
    # _test_compute_ietf_l3vpn_ntw()
    compare_res = _test_ietf_interfaces_non_top_level_translation()
    for item in compare_res:
        xpath = item[0]
        root = item[1]
        print("xpath is : ", xpath)