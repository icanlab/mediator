import json

from lxml import etree

from mediator_framework import tp_list
from mediator_framework.mediator_core import *
from mediator_framework.data_provider import *

def _test_tp_list():
    forth_tuple = ('huawei', 'switch', 'S5700', '8.1.30')
    path = "urn:ietf:params:xml:ns:yang:ietf-interfaces"
    print(tp_list.translate_yang_registry.get(forth_tuple).get(path)[2])

def _test_xpath_query():
    path = '/interfaces/interface'
    parse = etree.XMLParser(remove_blank_text=True)
    cc_xml = etree.parse("cc_configuration.xml", parse)
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
    with open('ietf_interface.json','r') as f:
        json_data = json.load(f)
        neid = 'switch 0'
        res = locate_translation_point(neid,json_data)
        return res

def _test_get_cc():
    neid = 'router'
    xpath = '/a:interfaces'
    ns = {'a': 'urn:ietf:params:xml:ns:yang:ietf-interfaces'}
    root = get_controller_configuration(neid, xpath, ns)[0]
    res = etree.ElementTree(root)
    for i in root.iter():
        print(res.getelementpath(i))



if __name__ == '__main__':
    _test_get_cc()