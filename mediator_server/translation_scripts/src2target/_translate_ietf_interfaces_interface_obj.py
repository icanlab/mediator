import re

from lxml import etree

from mediator_server.yang_bindings.target_yang_bindings.huawei_ifm_binding import *

class XPATH(etree.XPath):
    def __init__(self, path, namespaces=None):
        super(XPATH, self).__init__(path, namespaces=namespaces)
        self.namespaces = namespaces

def parse_key_from_xpath(xpath):
    res = re.finditer(r'\[.*?\]', xpath)
    keys_map = {}
    for i in res:
        tmp = re.sub(r'[a-z]{1}:{1}', '', i.group()[1:-1])
        index = tmp.find('=')
        key = tmp[:index]
        value = tmp[index+2:-1]
        keys_map[key] = value
    return keys_map

def exchange_maskint(mask_int):
  bin_arr = ['0' for i in range(32)]
  for i in range(mask_int):
    bin_arr[i] = '1'
  tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
  tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
  return '.'.join(tmpmask)

def _translate__interfaces_interface_ipv4_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.type = "main"
    if input_yang_obj.prefix_length._changed():
        translated_yang_obj.mask = exchange_maskint(input_yang_obj.prefix_length)
        
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask

    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin

    return translated_yang_obj

def _translate__interfaces_interface_ipv4(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv4.enabled._changed():
        input_yang_obj.ipv4.enabled = input_yang_obj.ipv4.enabled

    if input_yang_obj.ipv4.forwarding._changed():
        input_yang_obj.ipv4.forwarding = input_yang_obj.ipv4.forwarding

    if input_yang_obj.ipv4.mtu._changed():
        input_yang_obj.ipv4.mtu = input_yang_obj.ipv4.mtu
        
    for k, listInst in input_yang_obj.ipv4.address.iteritems():
        ipv4_address_obj = translated_yang_obj.ipv4.addresses.address.add(ip=k)
        innerobj = _translate__interfaces_interface_ipv4_address(listInst, ipv4_address_obj)

        
    return translated_yang_obj

def _translate__interfaces_interface(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.link_up_down_trap_enable._changed():
        input_yang_obj.link_up_down_trap_enable = input_yang_obj.link_up_down_trap_enable
        
    if input_yang_obj.admin_status._changed():
        input_yang_obj.admin_status = input_yang_obj.admin_status
        
    if input_yang_obj.oper_status._changed():
        input_yang_obj.oper_status = input_yang_obj.oper_status
        
    if input_yang_obj.last_change._changed():
        input_yang_obj.last_change = input_yang_obj.last_change
        
    if input_yang_obj.if_index._changed():
        input_yang_obj.if_index = input_yang_obj.if_index
        
    if input_yang_obj.phys_address._changed():
        input_yang_obj.phys_address = input_yang_obj.phys_address
        
    if input_yang_obj.higher_layer_if._changed():
        input_yang_obj.higher_layer_if = input_yang_obj.higher_layer_if
        
    if input_yang_obj.lower_layer_if._changed():
        input_yang_obj.lower_layer_if = input_yang_obj.lower_layer_if
        
    if input_yang_obj.speed._changed():
        input_yang_obj.speed = input_yang_obj.speed

    innerobj = _translate__interfaces_interface_ipv4(input_yang_obj, translated_yang_obj)

    return translated_yang_obj

def _translate__interfaces(input_yang_obj, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("interface script")
    key_dic = parse_key_from_xpath(xpath)
    xpath = '/a:ifm/a:interfaces/a:interface[a:name="%s"]' % (key_dic['name'])
    ns_map = {'a': 'urn:huawei:yang:huawei-ifm'}
    target_xpath = XPATH(xpath, ns_map)
    # print(target_xpath)
    translated_yang_obj = yc_interfaces_huawei_ifm__ifm_interfaces()
    # translated_yang_obj = huawei_ifm()
    for k, listInst in input_yang_obj.interface.iteritems():
        interface_obj = translated_yang_obj.interface.add(name=k)
        inner_obj = _translate__interfaces_interface(listInst, interface_obj)
    return [[translated_yang_obj, target_xpath]]

