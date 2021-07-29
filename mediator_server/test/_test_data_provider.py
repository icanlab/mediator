from mediator_server.mediator_framework.data_provider import *


def test_get_device_info():
    neid = 'ce'
    res = get_device_info_by_neid(neid)
    print(res)

def test_get_controller_config():
    neid = 'ce'
    xpath = '/a:routing'
    ns = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
    res = get_controller_configuration(neid, xpath, ns)
    print(etree.tostring(res, pretty_print=True).decode())

def test_get_device_config():
    neid = 'ce'
    xpath = '/a:ifm'
    ns = {'a': 'urn:huawei:yang:huawei-ifm'}
    res = get_device_configuration(neid, xpath, ns)
    print(etree.tostring(res, pretty_print=True).decode())

if __name__ == '__main__':
    # test_get_device_info()
    # test_get_controller_config()
    test_get_device_config()