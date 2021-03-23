from swagger_server.mediator_framework.mediator_core import compare_device_configuration
from swagger_server.mediator_framework.parse import *

def _test_compare_ietf_interfaces():
    with open('device_expected_configuration/huawei_ifm_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'router 0'
    res = compare_device_configuration(neid, root)
    t = parse_config_content(res)
    print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

def _test_compare_ietf_routing_bgp():
    with open('device_expected_configuration/huawei_bgp_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'route 1'
    res = compare_device_configuration(neid, root)
    # t = parse_config_content(res)
    # print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

def _test_compare_ietf_routing_network_instance():
    with open('device_expected_configuration/huawei_network_instance_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'route 1'
    res = compare_device_configuration(neid, root)
    t = parse_config_content(res)
    print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

def _test_compare_ietf_l3vpn_ntw_bgp():
    with open('device_expected_configuration/huawei_l3vpn_bgp_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'route 2'
    res = compare_device_configuration(neid, root)
    # t = parse_config_content(res)
    # print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

def _test_compare_ietf_l3vpn_ntw_ifm():
    with open('device_expected_configuration/huawei_l3vpn_ifm_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'route 2'
    res = compare_device_configuration(neid, root)
    # t = parse_config_content(res)
    # print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

def _test_compare_ietf_l3vpn_ntw_network_instance():
    with open('device_expected_configuration/huawei_l3vpn_network_instance_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'route 2'
    res = compare_device_configuration(neid, root)
    # t = parse_config_content(res)
    # print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

if __name__ == '__main__':
    _test_compare_ietf_interfaces()
    # _test_compare_ietf_routing_bgp()
    # _test_compare_ietf_routing_network_instance()
    # _test_compare_ietf_l3vpn_ntw_bgp()
    # _test_compare_ietf_l3vpn_ntw_ifm()
    # _test_compare_ietf_l3vpn_ntw_network_instance()