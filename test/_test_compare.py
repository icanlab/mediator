from lxml import etree

from mediator_framework.mediator_core import compare_device_configuration

if __name__ == '__main__':
    with open('../test/expected_dc.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'router 0'
    res = compare_device_configuration(neid, root)
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))