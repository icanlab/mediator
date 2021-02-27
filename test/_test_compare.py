from lxml import etree

from mediator_framework.mediator_core import compare_device_configuration
from mediator_framework.parse import *


def _test_compare_ietf_interfaces():
    with open('device_expected_configuration/huawei_ifm_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    neid = 'router 0'
    res = compare_device_configuration(neid, root)
    t = parse_config_content(res)
    print(json.dumps(t, indent=4))
    print(etree.tostring(res, pretty_print=True).decode('utf-8'))

if __name__ == '__main__':
    _test_compare_ietf_interfaces()