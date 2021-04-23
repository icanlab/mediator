from lxml import etree

from mediator_server.mediator_framework.mediator_core import translate_expected_cc_by_translation_point
from mediator_server.mediator_framework.data_provider import *

def _test_translate_ietf_routing():
    neid = 'route 1'
    with open('controller_expected_configuration/ietf_routing_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    trans_list = ['urn:ietf:params:xml:ns:yang:ietf-routing', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

def _test_translate_ietf_l3vpn_ntw():
    neid = 'route 2'
    with open('controller_expected_configuration/ietf_l3vpn_ntw_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    trans_list = ['urn:ietf:params:xml:ns:yang:ietf-l3vpn-ntw', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

def _test_translate_ietf_interfaces():
    neid = 'router 0'
    with open('controller_expected_configuration/ietf_interfaces_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    # device_info = get_device_info_by_neid(neid)
    device_info = ('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2')
    trans_list = ['/interfaces', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list, device_info)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

def _test_translate_ietf_interfaces_interface():
    neid = 'router 0'
    with open('controller_expected_configuration/ietf_interfaces_interface_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    # device_info = get_device_info_by_neid(neid)
    device_info = ('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2')
    trans_list = ['/ietf-interfaces:interfaces/interface', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list, device_info)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

def _test_translate_ietf_interfaces_interface_ipv4():
    neid = 'router 0'
    with open('controller_expected_configuration/ietf_interfaces_interface_ipv4_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    # device_info = get_device_info_by_neid(neid)
    device_info = ('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2')
    trans_list = ['/ietf-interfaces:interfaces/interface/ietf-ip:ipv4', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list, device_info)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

if __name__ == "__main__":
    # _test_translate_ietf_routing()
    # _test_translate_ietf_l3vpn_ntw()
    # _test_translate_ietf_interfaces()
    # _test_translate_ietf_interfaces_interface()
    _test_translate_ietf_interfaces_interface_ipv4()