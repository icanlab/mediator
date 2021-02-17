import json

from lxml import etree


def get_controller_configuration(neid, xpath, ns):
    """
    :param neid: device identifier
    :type neid: str
    :param xpath: the configuration request path
    :type xpath: str
    """
    with open('../test/cc_configuration.xml', 'r') as f:
        parse = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(f, parse)
    res = root.xpath(xpath, namespaces=ns)
    return res

def get_device_configuration(neid, toppath):
    """
        :param neid: device identifier
        :type neid: str
        :param xpath: the configuration request path
        :type xpath: str
        """
    current_dc = get_device_configuration_from_cache(neid, toppath)
    if None == current_dc:
        current_dc = get_target_config(neid, toppath)  # call plugin interface
        init_changeSet(neid, current_dc) # init changeSet
    else:
        update_changeSet(neid, current_dc) # upate changeSet
    return current_dc

def get_device_info_by_neid(neid):
    """
    :param neid: device identifier
    :type neid: str

    call plugin to get device info
    """
    device_info = ('huawei', 'switch', 'S5700', '8.1.30') # device info: [vendor,type,product,version]
    return device_info

# controller config operation
def get_controller_configuration_from_cache(neid,path):
    config = None
    return config

def init_controller_cache_configuration(nied, config):
    return

def update_controller_cache_configuration(neid,config):
    return

# device config operation
def get_device_configuration_from_cache(neid,path):
    config = None
    return config

def init_changeSet(neid,config):
    return

def update_changeSet(neid,config):
    return