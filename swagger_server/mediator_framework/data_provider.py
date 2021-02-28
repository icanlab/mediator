import json

from lxml import etree


def get_controller_configuration(neid, xpath, ns):
    """
    :param neid: device identifier
    :type neid: str
    :param xpath: the configuration request path
    :type xpath: str
    """
    name = xpath[xpath.rfind(':')+1:]
    root = None
    if 'interfaces' == name:
        with open('swagger_server/test/controller_current_configuration/ietf_interfaces_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    elif 'routing' == name:
        with open('swagger_server/test/controller_current_configuration/ietf_routing_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    elif 'l3vpn-ntw' == name:
        with open('swagger_server/test/controller_current_configuration/ietf_l3vpn_ntw_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    controller_configuration = root.xpath(xpath, namespaces=ns)
    return controller_configuration

def get_device_configuration(neid, xpath, ns):
    """
        :param neid: device identifier
        :type neid: str
        :param xpath: the configuration request path
        :type xpath: str
        """
    name = xpath[xpath.rfind(':') + 1:]
    root = None
    if 'ifm' == name:
        with open('swagger_server/test/device_current_configuration/huawei_ifm_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    elif 'bgp' == name:
        with open('swagger_server/test/device_current_configuration/huawei_bgp_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    elif 'network-instance' == name:
        with open('swagger_server/test/device_current_configuration/huawei_network_instance_cc.xml', 'r') as f:
            parse = etree.XMLParser(remove_blank_text=True)
            root = etree.parse(f, parse)
    print(root)
    device_configuration = root.xpath(xpath, namespaces=ns)
    return device_configuration

def get_device_info_by_neid(neid):
    """
    :param neid: device identifier
    :type neid: str

    call plugin to get device info
    """
    device_info = ('huawei', 'switch', 'S5700', '8.1.30') # device info: [vendor,type,product,version]
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