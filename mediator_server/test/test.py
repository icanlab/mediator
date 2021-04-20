import json

from lxml import etree

from mediator_server.mediator_framework import tp_list
from mediator_server.controllers.mediator_controller import *

def _test_tp_list():
    forth_tuple = ('huawei', 'switch', 'S5700', '8.1.30')
    path = "urn:ietf:params:xml:ns:yang:ietf-interfaces"
    print(tp_list.translate_yang_registry.get(forth_tuple).get(path)[2])

def _test_xpath_query():
    path = '/interfaces/interface'
    parse = etree.XMLParser(remove_blank_text=True)
    cc_xml = etree.parse("ietf_interfaces_cc.xml", parse)
    root = cc_xml.getroot()
    res = root.xpath('/i:interfaces', namespaces={'i':'urn:ietf:params:xml:ns:yang:ietf-interfaces'})
    print(res[0])
    for i in res[0].iter():
        print(i.tag)
    # print_tag_info(res)

def print_tag_info(res):
    if isinstance(res, list):
        for i in range(len(res)):
            for j in res[i]:
                print(j.tag)
                print_tag_info(j)
    else:
        for i in res:
            print(i.tag, i.text)
            print_tag_info(i)


def _test_locate_tp():
    with open('input_op_list/ietf_interfaces.json', 'r') as f:
        json_data = json.load(f)
        neid = 'switch 0'
        res = locate_translation_point(neid, json_data)
        return res

def _test_get_cc():
    neid = 'router'
    xpath = '/a:interfaces'
    ns = {'a': 'urn:ietf:params:xml:ns:yang:ietf-interfaces'}
    root = get_controller_configuration(neid, xpath, ns)[0]
    res = etree.ElementTree(root)
    for i, j in zip(root.iter(), res.iter()):
        # print(res.getelementpath(i))
        print(i.tag, j.tag)
        if i.text or j.text:
            print(i.text, j.text)

def _test_get_dc():
    neid = 'router 1'
    xpath = '/a:ifm'
    ns = {'a': 'urn:huawei:yang:huawei-ifm'}
    with open('device_expected_configuration/huawei_ifm_ec.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)  # get expected device configuration which translated by script
    res = get_device_configuration(neid, xpath, ns)[0]  # get current device configuration
    for i, j in zip(root.iter(), res.iter()):
        # print(res.getelementpath(i))
        print(i.tag, j.tag)
        if i.text:
            print(i.text, j.text)

if __name__ == '__main__':
    neid = 'route'
    msg_type = 'edit_config'
    with open('input_op_list/ietf_interfaces.json', 'r') as f:
        op_data = json.load(f)
    res = translate_msg_from_adaptor(neid, msg_type, op_data)
    print(res)