from lxml import etree

from mediator_framework.mediator_core import translate_expected_cc_by_translation_point

if __name__ == "__main__":
    neid = 'router 0'
    with open('../test/expected_cc.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    trans_list = ['urn:ietf:params:xml:ns:yang:ietf-interfaces', root]
    res = translate_expected_cc_by_translation_point(neid, trans_list)
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))