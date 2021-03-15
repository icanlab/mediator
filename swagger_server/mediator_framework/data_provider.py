import json

import requests
from lxml import etree


def get_controller_configuration(neid, xpath, ns):
    """
    :param neid: device identifier
    :type neid: str
    :param xpath: the configuration request path
    :type xpath: str
    """
    # name = xpath[xpath.rfind(':')+1:]
    # root = None
    # if 'interfaces' == name:
    #     with open('swagger_server/test/controller_current_configuration/ietf_interfaces_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # elif 'routing' == name:
    #     with open('swagger_server/test/controller_current_configuration/ietf_routing_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # elif 'l3vpn-ntw' == name:
    #     with open('swagger_server/test/controller_current_configuration/ietf_l3vpn_ntw_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # controller_configuration = root.xpath(xpath, namespaces=ns)
    url = 'http://127.0.0.1:8089/v1/mediatorservice/get_controller_config'
    param = {'neid': neid, 'xpath': xpath, 'ns_map': json.dumps(ns)}
    root = requests.get(url, params=param).text.encode('utf-8')
    parse = etree.XMLParser(remove_blank_text=True)
    controller_configuration = etree.fromstring(root, parse)
    return controller_configuration

def get_device_configuration(neid, xpath, ns):
    """
        :param neid: device identifier
        :type neid: str
        :param xpath: the configuration request path
        :type xpath: str
        """
    # name = xpath[xpath.rfind(':') + 1:]
    # root = None
    # if 'ifm' == name:
    #     with open('swagger_server/test/device_current_configuration/huawei_ifm_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # elif 'bgp' == name:
    #     with open('swagger_server/test/device_current_configuration/huawei_bgp_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # elif 'network-instance' == name:
    #     with open('swagger_server/test/device_current_configuration/huawei_network_instance_cc.xml', 'r') as f:
    #         parse = etree.XMLParser(remove_blank_text=True)
    #         root = etree.parse(f, parse)
    # device_configuration = root.xpath(xpath, namespaces=ns)
    url = 'http://127.0.0.1:8089/v1/mediatorservice/get_device_config'
    param = {'neid': neid, 'xpath': xpath, 'ns_map': json.dumps(ns)}
    root = requests.get(url, params=param).text.encode('utf-8')
    parse = etree.XMLParser(remove_blank_text=True)
    device_configuration = etree.fromstring(root, parse)
    return device_configuration

def get_device_info_by_neid(neid):
    """
    :param neid: device identifier
    :type neid: str

    call plugin to get device info
    """
    # device_info = ('huawei', 'switch', 'S5700', '8.1.30')  # device info: [vendor,type,product,version]
    url = 'http://127.0.0.1:8089/v1/mediatorservice/get_device_info'
    param = {'neid': 'route'}
    res = requests.get(url, params=param)
    ans = eval(res.text)
    device_info = tuple(ans.values())
    return device_info

# controller config operation
def get_controller_configuration_from_cache(neid, path):
    config = None
    return config

def init_controller_cache_configuration(nied, config):
    return

def update_controller_cache_configuration(neid, config):
    return

# device config operation
def get_device_configuration_from_cache(neid, path):
    config = None
    return config

def init_changeSet(neid, config):
    return

def update_changeSet(neid, config):
    return