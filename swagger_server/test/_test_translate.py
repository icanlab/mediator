from lxml import etree

from swagger_server.mediator_framework.mediator_core import translate_expected_cc_by_translation_point

def _test_translate_ietf_interfaces():
    neid = 'router 0'
    with open('controller_expected_configuration/ietf_interfaces_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    trans_list = ['urn:ietf:params:xml:ns:yang:ietf-interfaces', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list)
    for i in res:
        print(etree.tostring(i, pretty_print=True).decode('utf-8'))

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

if __name__ == "__main__":
    # _test_translate_ietf_interfaces()
    # _test_translate_ietf_routing()
    _test_translate_ietf_l3vpn_ntw()