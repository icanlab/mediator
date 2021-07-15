import re
from copy import deepcopy

from lxml import etree

from mediator_server.yang_bindings.src_yang_bindings.ietf_105_binding import *
from mediator_server.yang_bindings.target_yang_bindings.huawei_bgp_binding_105 import huawei_bgp
from mediator_server.yang_bindings.target_yang_bindings.huawei_isiscomm_binding import huawei_isiscomm
from mediator_server.yang_bindings.target_yang_bindings.huawei_segripv6_binding import huawei_segripv6

#将ipv6中段中的0压缩，如005e 压缩为5e
def subZero(ipseg):
    index=0
    for i in range(len(ipseg)):
        if ipseg[i]=='0':
            index+=1
        else:
            break
    if index>=2:
        return ipseg[index:] if ipseg[index:] else '0'
    else:
        return ipseg
#将十进制数转换为ipv6
def dec2ipv6(dec):
    if checkdec(dec) and int(dec)<=340282366920938463463374607431768211455:
        hexstr=(hex(int(dec)))[2:]
        hexstrlen = len(hexstr)
        while hexstrlen<32:
            hexstr='0'+hexstr
            hexstrlen+=1
        result=subZero(hexstr[0:4])+":"+subZero(hexstr[4:8])+":"+subZero(hexstr[8:12])+":"+subZero(hexstr[12:16])+":"+subZero(hexstr[16:20])+":"+subZero(hexstr[20:24])+":"+subZero(hexstr[24:28])+":"+subZero(hexstr[28:])
        # print("result:"+result)
        return result
    else:
        return ""
#校验十进制数字
def checkdec(dec):
    matchobj = re.match(r'(0[dD])?[0-9]+$',dec)
    if matchobj:
        return True
    else:
        return False

class XPATH(etree.XPath):
    def __init__(self, path, namespaces=None):
        super(XPATH, self).__init__(path, namespaces=namespaces)
        self.namespaces = namespaces

def _translate__routing_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/interfaces

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/graceful-restart

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.restart_interval._changed():
        input_yang_obj.restart_interval = input_yang_obj.restart_interval
        
    if input_yang_obj.helper_enable._changed():
        input_yang_obj.helper_enable = input_yang_obj.helper_enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_nsr(input_yang_obj: yc_nsr_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_nsr, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/nsr

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_node_tags_node_tag(input_yang_obj: yc_node_tag_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_node_tags_node_tag, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/node-tags/node-tag

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_node_tags(input_yang_obj: yc_node_tags_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_node_tags, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/node-tags

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
    
    for k, listInst in input_yang_obj.node_tag.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_node_tags_node_tag(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/metric-type/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/metric-type/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_metric_type(input_yang_obj: yc_metric_type_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_metric_type, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/metric-type

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_metric_type_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/default-metric/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/default-metric/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_default_metric(input_yang_obj: yc_default_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_default_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/default-metric

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_default_metric_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_auto_cost(input_yang_obj: yc_auto_cost_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_auto_cost, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/auto-cost

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.reference_bandwidth._changed():
        input_yang_obj.reference_bandwidth = input_yang_obj.reference_bandwidth
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/authentication/level-1

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/authentication/level-2

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_authentication(input_yang_obj: yc_authentication_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_authentication, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/authentication

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_authentication_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_address_families_address_family_list(input_yang_obj: yc_address_family_list_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_address_families_address_family_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/address-families/address-family-list

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_address_families(input_yang_obj: yc_address_families_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_address_families, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/address-families

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
    
    for k, listInst in input_yang_obj.address_family_list.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_address_families_address_family_list(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_mpls_te_rid(input_yang_obj: yc_te_rid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_mpls_te_rid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/mpls/te-rid

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
    
    if input_yang_obj.ipv4_router_id._changed():
        input_yang_obj.ipv4_router_id = input_yang_obj.ipv4_router_id
        
    if input_yang_obj.ipv6_router_id._changed():
        input_yang_obj.ipv6_router_id = input_yang_obj.ipv6_router_id
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_mpls(input_yang_obj: yc_mpls_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_mpls, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/mpls

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_mpls_te_rid(input_yang_obj.te_rid, translated_yang_obj)

    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_control_ietf_spf_delay(input_yang_obj: yc_ietf_spf_delay_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_spf_control_ietf_spf_delay, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/spf-control/ietf-spf-delay

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
    
    if input_yang_obj.initial_delay._changed():
        input_yang_obj.initial_delay = input_yang_obj.initial_delay
        
    if input_yang_obj.short_delay._changed():
        input_yang_obj.short_delay = input_yang_obj.short_delay
        
    if input_yang_obj.long_delay._changed():
        input_yang_obj.long_delay = input_yang_obj.long_delay
        
    if input_yang_obj.hold_down._changed():
        input_yang_obj.hold_down = input_yang_obj.hold_down
        
    if input_yang_obj.time_to_learn._changed():
        input_yang_obj.time_to_learn = input_yang_obj.time_to_learn
        
    if input_yang_obj.current_state._changed():
        input_yang_obj.current_state = input_yang_obj.current_state
        
    if input_yang_obj.remaining_time_to_learn._changed():
        input_yang_obj.remaining_time_to_learn = input_yang_obj.remaining_time_to_learn
        
    if input_yang_obj.remaining_hold_down._changed():
        input_yang_obj.remaining_hold_down = input_yang_obj.remaining_hold_down
        
    if input_yang_obj.last_event_received._changed():
        input_yang_obj.last_event_received = input_yang_obj.last_event_received
        
    if input_yang_obj.next_spf_time._changed():
        input_yang_obj.next_spf_time = input_yang_obj.next_spf_time
        
    if input_yang_obj.last_spf_time._changed():
        input_yang_obj.last_spf_time = input_yang_obj.last_spf_time
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_control(input_yang_obj: yc_spf_control_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_spf_control, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/spf-control

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
    
    if input_yang_obj.paths._changed():
        input_yang_obj.paths = input_yang_obj.paths
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_control_ietf_spf_delay(input_yang_obj.ietf_spf_delay, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_preference(input_yang_obj: yc_preference_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_preference, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/preference

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
    
    if input_yang_obj.internal._changed():
        input_yang_obj.internal = input_yang_obj.internal
        
    if input_yang_obj.external._changed():
        input_yang_obj.external = input_yang_obj.external
        
    if input_yang_obj.default_._changed():
        input_yang_obj.default_ = input_yang_obj.default_
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_overload(input_yang_obj: yc_overload_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_overload, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/overload

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
    
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_overload_max_metric(input_yang_obj: yc_overload_max_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_overload_max_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/overload-max-metric

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
    
    if input_yang_obj.timeout._changed():
        input_yang_obj.timeout = input_yang_obj.timeout
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event_trigger_lsp(input_yang_obj: yc_trigger_lsp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event_trigger_lsp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/spf-log/event/trigger-lsp

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
    
    if input_yang_obj.sequence._changed():
        input_yang_obj.sequence = input_yang_obj.sequence
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event(input_yang_obj: yc_event_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/spf-log/event

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
    
    if input_yang_obj.spf_type._changed():
        input_yang_obj.spf_type = input_yang_obj.spf_type
        
    if input_yang_obj.level._changed():
        input_yang_obj.level = input_yang_obj.level
        
    if input_yang_obj.schedule_timestamp._changed():
        input_yang_obj.schedule_timestamp = input_yang_obj.schedule_timestamp
        
    if input_yang_obj.start_timestamp._changed():
        input_yang_obj.start_timestamp = input_yang_obj.start_timestamp
        
    if input_yang_obj.end_timestamp._changed():
        input_yang_obj.end_timestamp = input_yang_obj.end_timestamp
        
    for k, listInst in input_yang_obj.trigger_lsp.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event_trigger_lsp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_log(input_yang_obj: yc_spf_log_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_spf_log, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/spf-log

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
    
    for k, listInst in input_yang_obj.event.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_spf_log_event(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event_lsp(input_yang_obj: yc_lsp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event_lsp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/lsp-log/event/lsp

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
    
    if input_yang_obj.lsp._changed():
        input_yang_obj.lsp = input_yang_obj.lsp
        
    if input_yang_obj.sequence._changed():
        input_yang_obj.sequence = input_yang_obj.sequence
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event(input_yang_obj: yc_event_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/lsp-log/event

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
    
    if input_yang_obj.level._changed():
        input_yang_obj.level = input_yang_obj.level
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event_lsp(input_yang_obj.lsp, translated_yang_obj)
        
    if input_yang_obj.received_timestamp._changed():
        input_yang_obj.received_timestamp = input_yang_obj.received_timestamp
        
    if input_yang_obj.reason._changed():
        input_yang_obj.reason = input_yang_obj.reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log(input_yang_obj: yc_lsp_log_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/lsp-log

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
    
    for k, listInst in input_yang_obj.event.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_lsp_log_event(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_hostnames_hostname(input_yang_obj: yc_hostname_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_hostnames_hostname, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/hostnames/hostname

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
    
    if input_yang_obj.hostname._changed():
        input_yang_obj.hostname = input_yang_obj.hostname
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_hostnames(input_yang_obj: yc_hostnames_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_hostnames, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/hostnames

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
    
    for k, listInst in input_yang_obj.hostname.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_hostnames_hostname(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_authentication(input_yang_obj: yc_authentication_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_authentication, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/authentication

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
    
    if input_yang_obj.authentication_type._changed():
        input_yang_obj.authentication_type = input_yang_obj.authentication_type
        
    if input_yang_obj.authentication_key._changed():
        input_yang_obj.authentication_key = input_yang_obj.authentication_key
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries_topology(input_yang_obj: yc_topology_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries_topology, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-entries/topology

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
    
    if input_yang_obj.mt_id._changed():
        input_yang_obj.mt_id = input_yang_obj.mt_id
        
    if input_yang_obj.attributes._changed():
        input_yang_obj.attributes = input_yang_obj.attributes
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries(input_yang_obj: yc_mt_entries_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-entries

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
    
    for k, listInst in input_yang_obj.topology.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags_node_tag(input_yang_obj: yc_node_tag_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags_node_tag, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/router-capability/node-tags/node-tag

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
    
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags(input_yang_obj: yc_node_tags_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/router-capability/node-tags

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
    
    for k, listInst in input_yang_obj.node_tag.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags_node_tag(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/router-capability/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/router-capability/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability(input_yang_obj: yc_router_capability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/router-capability

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_node_tags(input_yang_obj.node_tags, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    if input_yang_obj.binary._changed():
        input_yang_obj.binary = input_yang_obj.binary
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_capability(input_yang_obj: yc_v6_capability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_capability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/v6-capability

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_msd(input_yang_obj: yc_v6_msd_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_msd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities/v6-msd

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
    
    if input_yang_obj.max_segments_left._changed():
        input_yang_obj.max_segments_left = input_yang_obj.max_segments_left
        
    if input_yang_obj.max_end_pop._changed():
        input_yang_obj.max_end_pop = input_yang_obj.max_end_pop
        
    if input_yang_obj.max_t_insert._changed():
        input_yang_obj.max_t_insert = input_yang_obj.max_t_insert
        
    if input_yang_obj.max_t_encap._changed():
        input_yang_obj.max_t_encap = input_yang_obj.max_t_encap
        
    if input_yang_obj.max_end_d._changed():
        input_yang_obj.max_end_d = input_yang_obj.max_end_d
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities(input_yang_obj: yc_router_capabilities_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/router-capabilities

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
    
    for k, listInst in input_yang_obj.router_capability.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_router_capability(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_capability(input_yang_obj.v6_capability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities_v6_msd(input_yang_obj.v6_msd, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links_srlgs(input_yang_obj: yc_srlgs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links_srlgs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/links-srlgs/links/srlgs

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
    
    if input_yang_obj.srlg._changed():
        input_yang_obj.srlg = input_yang_obj.srlg
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links(input_yang_obj: yc_links_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/links-srlgs/links

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
    
    if input_yang_obj.neighbor_id._changed():
        input_yang_obj.neighbor_id = input_yang_obj.neighbor_id
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.link_local_id._changed():
        input_yang_obj.link_local_id = input_yang_obj.link_local_id
        
    if input_yang_obj.link_remote_id._changed():
        input_yang_obj.link_remote_id = input_yang_obj.link_remote_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links_srlgs(input_yang_obj.srlgs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs(input_yang_obj: yc_links_srlgs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/links-srlgs

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
    
    for k, listInst in input_yang_obj.links.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs_links(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_default_metric(input_yang_obj: yc_default_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_default_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances/instance/default-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_delay_metric(input_yang_obj: yc_delay_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_delay_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances/instance/delay-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_expense_metric(input_yang_obj: yc_expense_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_expense_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances/instance/expense-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_error_metric(input_yang_obj: yc_error_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_error_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances/instance/error-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance(input_yang_obj: yc_instance_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances/instance

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
    
    if input_yang_obj.i_e._changed():
        input_yang_obj.i_e = input_yang_obj.i_e
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_default_metric(input_yang_obj.default_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_delay_metric(input_yang_obj.delay_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_expense_metric(input_yang_obj.expense_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance_error_metric(input_yang_obj.error_metric, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances(input_yang_obj: yc_instances_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor/instances

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
    
    for k, listInst in input_yang_obj.instance.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor(input_yang_obj: yc_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor/neighbor

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor_instances(input_yang_obj.instances, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor(input_yang_obj: yc_is_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/is-neighbor

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
    
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth(input_yang_obj: yc_max_lsp_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/interface-switching-capability/max-lsp-bandwidths/max-lsp-bandwidth

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
    
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths(input_yang_obj: yc_max_lsp_bandwidths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/interface-switching-capability/max-lsp-bandwidths

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
    
    for k, listInst in input_yang_obj.max_lsp_bandwidth.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific(input_yang_obj: yc_tdm_specific_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/interface-switching-capability/tdm-specific

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
    
    if input_yang_obj.minimum_lsp_bandwidth._changed():
        input_yang_obj.minimum_lsp_bandwidth = input_yang_obj.minimum_lsp_bandwidth
        
    if input_yang_obj.indication._changed():
        input_yang_obj.indication = input_yang_obj.indication
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific(input_yang_obj: yc_psc_specific_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/interface-switching-capability/psc-specific

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
    
    if input_yang_obj.minimum_lsp_bandwidth._changed():
        input_yang_obj.minimum_lsp_bandwidth = input_yang_obj.minimum_lsp_bandwidth
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability(input_yang_obj: yc_interface_switching_capability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/interface-switching-capability

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
    
    if input_yang_obj.switching_capability._changed():
        input_yang_obj.switching_capability = input_yang_obj.switching_capability
        
    if input_yang_obj.encoding._changed():
        input_yang_obj.encoding = input_yang_obj.encoding
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths(input_yang_obj.max_lsp_bandwidths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific(input_yang_obj.tdm_specific, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific(input_yang_obj.psc_specific, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs(input_yang_obj: yc_local_if_ipv4_addrs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/local-if-ipv4-addrs

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
    
    if input_yang_obj.local_if_ipv4_addr._changed():
        input_yang_obj.local_if_ipv4_addr = input_yang_obj.local_if_ipv4_addr
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs(input_yang_obj: yc_remote_if_ipv4_addrs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/remote-if-ipv4-addrs

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
    
    if input_yang_obj.remote_if_ipv4_addr._changed():
        input_yang_obj.remote_if_ipv4_addr = input_yang_obj.remote_if_ipv4_addr
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth(input_yang_obj: yc_unreserved_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unreserved-bandwidths/unreserved-bandwidth

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
    
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.unreserved_bandwidth._changed():
        input_yang_obj.unreserved_bandwidth = input_yang_obj.unreserved_bandwidth
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths(input_yang_obj: yc_unreserved_bandwidths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unreserved-bandwidths

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
    
    for k, listInst in input_yang_obj.unreserved_bandwidth.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay(input_yang_obj: yc_unidirectional_link_delay_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-delay

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay(input_yang_obj: yc_min_max_unidirectional_link_delay_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/min-max-unidirectional-link-delay

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.min_value._changed():
        input_yang_obj.min_value = input_yang_obj.min_value
        
    if input_yang_obj.max_value._changed():
        input_yang_obj.max_value = input_yang_obj.max_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation(input_yang_obj: yc_unidirectional_link_delay_variation_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-delay-variation

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_loss(input_yang_obj: yc_unidirectional_link_loss_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_loss, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-loss

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth(input_yang_obj: yc_unidirectional_link_residual_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-residual-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth(input_yang_obj: yc_unidirectional_link_available_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-available-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth(input_yang_obj: yc_unidirectional_link_utilized_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unidirectional-link-utilized-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance(input_yang_obj: yc_instance_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances/instance

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.link_local_id._changed():
        input_yang_obj.link_local_id = input_yang_obj.link_local_id
        
    if input_yang_obj.remote_local_id._changed():
        input_yang_obj.remote_local_id = input_yang_obj.remote_local_id
        
    if input_yang_obj.protection_capability._changed():
        input_yang_obj.protection_capability = input_yang_obj.protection_capability
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_interface_switching_capability(input_yang_obj.interface_switching_capability, translated_yang_obj)
        
    if input_yang_obj.admin_group._changed():
        input_yang_obj.admin_group = input_yang_obj.admin_group
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs(input_yang_obj.local_if_ipv4_addrs, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs(input_yang_obj.remote_if_ipv4_addrs, translated_yang_obj)
        
    if input_yang_obj.te_metric._changed():
        input_yang_obj.te_metric = input_yang_obj.te_metric
        
    if input_yang_obj.max_bandwidth._changed():
        input_yang_obj.max_bandwidth = input_yang_obj.max_bandwidth
        
    if input_yang_obj.max_reservable_bandwidth._changed():
        input_yang_obj.max_reservable_bandwidth = input_yang_obj.max_reservable_bandwidth
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unreserved_bandwidths(input_yang_obj.unreserved_bandwidths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay(input_yang_obj.unidirectional_link_delay, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay(input_yang_obj.min_max_unidirectional_link_delay, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation(input_yang_obj.unidirectional_link_delay_variation, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_loss(input_yang_obj.unidirectional_link_loss, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth(input_yang_obj.unidirectional_link_residual_bandwidth, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth(input_yang_obj.unidirectional_link_available_bandwidth, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth(input_yang_obj.unidirectional_link_utilized_bandwidth, translated_yang_obj)
        
    if input_yang_obj.link_attributes_flags._changed():
        input_yang_obj.link_attributes_flags = input_yang_obj.link_attributes_flags
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances(input_yang_obj: yc_instances_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/instances

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
    
    for k, listInst in input_yang_obj.instance.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func(input_yang_obj: yc_endpoint_func_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/srv6-end-x-sids/end-x-sid/endpoint-func

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.endpoint_func._changed():
        input_yang_obj.endpoint_func = input_yang_obj.endpoint_func
        
    if input_yang_obj.undefined_endpoint_func._changed():
        input_yang_obj.undefined_endpoint_func = input_yang_obj.undefined_endpoint_func
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid(input_yang_obj: yc_end_x_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/srv6-end-x-sids/end-x-sid

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
    
    if input_yang_obj.func_flags._changed():
        input_yang_obj.func_flags = input_yang_obj.func_flags
        
    if input_yang_obj.algorithm._changed():
        input_yang_obj.algorithm = input_yang_obj.algorithm
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func(input_yang_obj.endpoint_func, translated_yang_obj)
        
    if input_yang_obj.neighbor_id._changed():
        input_yang_obj.neighbor_id = input_yang_obj.neighbor_id
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids(input_yang_obj: yc_srv6_end_x_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor/srv6-end-x-sids

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
    
    for k, listInst in input_yang_obj.end_x_sid.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor(input_yang_obj: yc_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor/neighbor

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_instances(input_yang_obj.instances, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor_srv6_end_x_sids(input_yang_obj.srv6_end_x_sids, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor(input_yang_obj: yc_extended_is_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-is-neighbor

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
    
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_default_metric(input_yang_obj: yc_default_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_default_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability/prefixes/default-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_delay_metric(input_yang_obj: yc_delay_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_delay_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability/prefixes/delay-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_expense_metric(input_yang_obj: yc_expense_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_expense_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability/prefixes/expense-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_error_metric(input_yang_obj: yc_error_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_error_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability/prefixes/error-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability/prefixes

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
    
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.i_e._changed():
        input_yang_obj.i_e = input_yang_obj.i_e
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_default_metric(input_yang_obj.default_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_delay_metric(input_yang_obj.delay_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_expense_metric(input_yang_obj.expense_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes_error_metric(input_yang_obj.error_metric, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability(input_yang_obj: yc_ipv4_internal_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-internal-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_default_metric(input_yang_obj: yc_default_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_default_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability/prefixes/default-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_delay_metric(input_yang_obj: yc_delay_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_delay_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability/prefixes/delay-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_expense_metric(input_yang_obj: yc_expense_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_expense_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability/prefixes/expense-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_error_metric(input_yang_obj: yc_error_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_error_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability/prefixes/error-metric

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability/prefixes

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
    
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.i_e._changed():
        input_yang_obj.i_e = input_yang_obj.i_e
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_default_metric(input_yang_obj.default_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_delay_metric(input_yang_obj.delay_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_expense_metric(input_yang_obj.expense_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes_error_metric(input_yang_obj.error_metric, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability(input_yang_obj: yc_ipv4_external_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv4-external-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-ipv4-reachability/prefixes/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-ipv4-reachability/prefixes/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-ipv4-reachability/prefixes

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
    
    if input_yang_obj.up_down._changed():
        input_yang_obj.up_down = input_yang_obj.up_down
        
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.tag64._changed():
        input_yang_obj.tag64 = input_yang_obj.tag64
        
    if input_yang_obj.external_prefix_flag._changed():
        input_yang_obj.external_prefix_flag = input_yang_obj.external_prefix_flag
        
    if input_yang_obj.readvertisement_flag._changed():
        input_yang_obj.readvertisement_flag = input_yang_obj.readvertisement_flag
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    if input_yang_obj.ipv4_source_router_id._changed():
        input_yang_obj.ipv4_source_router_id = input_yang_obj.ipv4_source_router_id
        
    if input_yang_obj.ipv6_source_router_id._changed():
        input_yang_obj.ipv6_source_router_id = input_yang_obj.ipv6_source_router_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability(input_yang_obj: yc_extended_ipv4_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/extended-ipv4-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth(input_yang_obj: yc_max_lsp_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/interface-switching-capability/max-lsp-bandwidths/max-lsp-bandwidth

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
    
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths(input_yang_obj: yc_max_lsp_bandwidths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/interface-switching-capability/max-lsp-bandwidths

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
    
    for k, listInst in input_yang_obj.max_lsp_bandwidth.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths_max_lsp_bandwidth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific(input_yang_obj: yc_tdm_specific_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/interface-switching-capability/tdm-specific

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
    
    if input_yang_obj.minimum_lsp_bandwidth._changed():
        input_yang_obj.minimum_lsp_bandwidth = input_yang_obj.minimum_lsp_bandwidth
        
    if input_yang_obj.indication._changed():
        input_yang_obj.indication = input_yang_obj.indication
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific(input_yang_obj: yc_psc_specific_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/interface-switching-capability/psc-specific

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
    
    if input_yang_obj.minimum_lsp_bandwidth._changed():
        input_yang_obj.minimum_lsp_bandwidth = input_yang_obj.minimum_lsp_bandwidth
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability(input_yang_obj: yc_interface_switching_capability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/interface-switching-capability

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
    
    if input_yang_obj.switching_capability._changed():
        input_yang_obj.switching_capability = input_yang_obj.switching_capability
        
    if input_yang_obj.encoding._changed():
        input_yang_obj.encoding = input_yang_obj.encoding
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_max_lsp_bandwidths(input_yang_obj.max_lsp_bandwidths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_tdm_specific(input_yang_obj.tdm_specific, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability_psc_specific(input_yang_obj.psc_specific, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs(input_yang_obj: yc_local_if_ipv4_addrs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/local-if-ipv4-addrs

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
    
    if input_yang_obj.local_if_ipv4_addr._changed():
        input_yang_obj.local_if_ipv4_addr = input_yang_obj.local_if_ipv4_addr
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs(input_yang_obj: yc_remote_if_ipv4_addrs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/remote-if-ipv4-addrs

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
    
    if input_yang_obj.remote_if_ipv4_addr._changed():
        input_yang_obj.remote_if_ipv4_addr = input_yang_obj.remote_if_ipv4_addr
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth(input_yang_obj: yc_unreserved_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unreserved-bandwidths/unreserved-bandwidth

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
    
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.unreserved_bandwidth._changed():
        input_yang_obj.unreserved_bandwidth = input_yang_obj.unreserved_bandwidth
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths(input_yang_obj: yc_unreserved_bandwidths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unreserved-bandwidths

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
    
    for k, listInst in input_yang_obj.unreserved_bandwidth.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths_unreserved_bandwidth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay(input_yang_obj: yc_unidirectional_link_delay_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-delay

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay(input_yang_obj: yc_min_max_unidirectional_link_delay_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/min-max-unidirectional-link-delay

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.min_value._changed():
        input_yang_obj.min_value = input_yang_obj.min_value
        
    if input_yang_obj.max_value._changed():
        input_yang_obj.max_value = input_yang_obj.max_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation(input_yang_obj: yc_unidirectional_link_delay_variation_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-delay-variation

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_loss(input_yang_obj: yc_unidirectional_link_loss_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_loss, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-loss

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth(input_yang_obj: yc_unidirectional_link_residual_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-residual-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth(input_yang_obj: yc_unidirectional_link_available_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-available-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth(input_yang_obj: yc_unidirectional_link_utilized_bandwidth_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unidirectional-link-utilized-bandwidth

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance(input_yang_obj: yc_instance_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances/instance

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
    
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.link_local_id._changed():
        input_yang_obj.link_local_id = input_yang_obj.link_local_id
        
    if input_yang_obj.remote_local_id._changed():
        input_yang_obj.remote_local_id = input_yang_obj.remote_local_id
        
    if input_yang_obj.protection_capability._changed():
        input_yang_obj.protection_capability = input_yang_obj.protection_capability
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_interface_switching_capability(input_yang_obj.interface_switching_capability, translated_yang_obj)
        
    if input_yang_obj.admin_group._changed():
        input_yang_obj.admin_group = input_yang_obj.admin_group
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_local_if_ipv4_addrs(input_yang_obj.local_if_ipv4_addrs, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_remote_if_ipv4_addrs(input_yang_obj.remote_if_ipv4_addrs, translated_yang_obj)
        
    if input_yang_obj.te_metric._changed():
        input_yang_obj.te_metric = input_yang_obj.te_metric
        
    if input_yang_obj.max_bandwidth._changed():
        input_yang_obj.max_bandwidth = input_yang_obj.max_bandwidth
        
    if input_yang_obj.max_reservable_bandwidth._changed():
        input_yang_obj.max_reservable_bandwidth = input_yang_obj.max_reservable_bandwidth
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unreserved_bandwidths(input_yang_obj.unreserved_bandwidths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay(input_yang_obj.unidirectional_link_delay, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_min_max_unidirectional_link_delay(input_yang_obj.min_max_unidirectional_link_delay, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_delay_variation(input_yang_obj.unidirectional_link_delay_variation, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_loss(input_yang_obj.unidirectional_link_loss, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_residual_bandwidth(input_yang_obj.unidirectional_link_residual_bandwidth, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_available_bandwidth(input_yang_obj.unidirectional_link_available_bandwidth, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unidirectional_link_utilized_bandwidth(input_yang_obj.unidirectional_link_utilized_bandwidth, translated_yang_obj)
        
    if input_yang_obj.link_attributes_flags._changed():
        input_yang_obj.link_attributes_flags = input_yang_obj.link_attributes_flags
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances(input_yang_obj: yc_instances_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/instances

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
    
    for k, listInst in input_yang_obj.instance.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func(input_yang_obj: yc_endpoint_func_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/srv6-end-x-sids/end-x-sid/endpoint-func

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.endpoint_func._changed():
        input_yang_obj.endpoint_func = input_yang_obj.endpoint_func
        
    if input_yang_obj.undefined_endpoint_func._changed():
        input_yang_obj.undefined_endpoint_func = input_yang_obj.undefined_endpoint_func
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid(input_yang_obj: yc_end_x_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/srv6-end-x-sids/end-x-sid

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
    
    if input_yang_obj.func_flags._changed():
        input_yang_obj.func_flags = input_yang_obj.func_flags
        
    if input_yang_obj.algorithm._changed():
        input_yang_obj.algorithm = input_yang_obj.algorithm
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid_endpoint_func(input_yang_obj.endpoint_func, translated_yang_obj)
        
    if input_yang_obj.neighbor_id._changed():
        input_yang_obj.neighbor_id = input_yang_obj.neighbor_id
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids(input_yang_obj: yc_srv6_end_x_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor/srv6-end-x-sids

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
    
    for k, listInst in input_yang_obj.end_x_sid.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids_end_x_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor(input_yang_obj: yc_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor/neighbor

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
    
    if input_yang_obj.mt_id._changed():
        input_yang_obj.mt_id = input_yang_obj.mt_id
        
    if input_yang_obj.neighbor_id._changed():
        input_yang_obj.neighbor_id = input_yang_obj.neighbor_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_instances(input_yang_obj.instances, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor_srv6_end_x_sids(input_yang_obj.srv6_end_x_sids, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor(input_yang_obj: yc_mt_is_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-is-neighbor

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
    
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-extended-ipv4-reachability/prefixes/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-extended-ipv4-reachability/prefixes/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-extended-ipv4-reachability/prefixes

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
    
    if input_yang_obj.mt_id._changed():
        input_yang_obj.mt_id = input_yang_obj.mt_id
        
    if input_yang_obj.up_down._changed():
        input_yang_obj.up_down = input_yang_obj.up_down
        
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.tag64._changed():
        input_yang_obj.tag64 = input_yang_obj.tag64
        
    if input_yang_obj.external_prefix_flag._changed():
        input_yang_obj.external_prefix_flag = input_yang_obj.external_prefix_flag
        
    if input_yang_obj.readvertisement_flag._changed():
        input_yang_obj.readvertisement_flag = input_yang_obj.readvertisement_flag
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    if input_yang_obj.ipv4_source_router_id._changed():
        input_yang_obj.ipv4_source_router_id = input_yang_obj.ipv4_source_router_id
        
    if input_yang_obj.ipv6_source_router_id._changed():
        input_yang_obj.ipv6_source_router_id = input_yang_obj.ipv6_source_router_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability(input_yang_obj: yc_mt_extended_ipv4_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-extended-ipv4-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-ipv6-reachability/prefixes/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-ipv6-reachability/prefixes/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-ipv6-reachability/prefixes

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
    
    if input_yang_obj.MT_ID._changed():
        input_yang_obj.MT_ID = input_yang_obj.MT_ID
        
    if input_yang_obj.up_down._changed():
        input_yang_obj.up_down = input_yang_obj.up_down
        
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.tag64._changed():
        input_yang_obj.tag64 = input_yang_obj.tag64
        
    if input_yang_obj.external_prefix_flag._changed():
        input_yang_obj.external_prefix_flag = input_yang_obj.external_prefix_flag
        
    if input_yang_obj.readvertisement_flag._changed():
        input_yang_obj.readvertisement_flag = input_yang_obj.readvertisement_flag
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    if input_yang_obj.ipv4_source_router_id._changed():
        input_yang_obj.ipv4_source_router_id = input_yang_obj.ipv4_source_router_id
        
    if input_yang_obj.ipv6_source_router_id._changed():
        input_yang_obj.ipv6_source_router_id = input_yang_obj.ipv6_source_router_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability(input_yang_obj: yc_mt_ipv6_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/mt-ipv6-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv(input_yang_obj: yc_unknown_tlv_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv6-reachability/prefixes/unknown-tlvs/unknown-tlv

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
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.length._changed():
        input_yang_obj.length = input_yang_obj.length
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs(input_yang_obj: yc_unknown_tlvs_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv6-reachability/prefixes/unknown-tlvs

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
    
    for k, listInst in input_yang_obj.unknown_tlv.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs_unknown_tlv(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv6-reachability/prefixes

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
    
    if input_yang_obj.up_down._changed():
        input_yang_obj.up_down = input_yang_obj.up_down
        
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.tag64._changed():
        input_yang_obj.tag64 = input_yang_obj.tag64
        
    if input_yang_obj.external_prefix_flag._changed():
        input_yang_obj.external_prefix_flag = input_yang_obj.external_prefix_flag
        
    if input_yang_obj.readvertisement_flag._changed():
        input_yang_obj.readvertisement_flag = input_yang_obj.readvertisement_flag
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    if input_yang_obj.ipv4_source_router_id._changed():
        input_yang_obj.ipv4_source_router_id = input_yang_obj.ipv4_source_router_id
        
    if input_yang_obj.ipv6_source_router_id._changed():
        input_yang_obj.ipv6_source_router_id = input_yang_obj.ipv6_source_router_id
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability(input_yang_obj: yc_ipv6_reachability_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/ipv6-reachability

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
    
    for k, listInst in input_yang_obj.prefixes.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability_prefixes(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid_endpoint_func(input_yang_obj: yc_endpoint_func_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid_endpoint_func, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/srv6-locators/locator/srv6-end-sids/end-sid/endpoint-func

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.endpoint_func._changed():
        input_yang_obj.endpoint_func = input_yang_obj.endpoint_func
        
    if input_yang_obj.undefined_endpoint_func._changed():
        input_yang_obj.undefined_endpoint_func = input_yang_obj.undefined_endpoint_func
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid(input_yang_obj: yc_end_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/srv6-locators/locator/srv6-end-sids/end-sid

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid_endpoint_func(input_yang_obj.endpoint_func, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids(input_yang_obj: yc_srv6_end_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/srv6-locators/locator/srv6-end-sids

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
    
    for k, listInst in input_yang_obj.end_sid.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids_end_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator(input_yang_obj: yc_locator_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/srv6-locators/locator

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
    
    if input_yang_obj.mt_id._changed():
        input_yang_obj.mt_id = input_yang_obj.mt_id
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.algorithm._changed():
        input_yang_obj.algorithm = input_yang_obj.algorithm
        
    if input_yang_obj.loc_size._changed():
        input_yang_obj.loc_size = input_yang_obj.loc_size
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator_srv6_end_sids(input_yang_obj.srv6_end_sids, translated_yang_obj)
        
    if input_yang_obj.external_prefix_flag._changed():
        input_yang_obj.external_prefix_flag = input_yang_obj.external_prefix_flag
        
    if input_yang_obj.readvertisement_flag._changed():
        input_yang_obj.readvertisement_flag = input_yang_obj.readvertisement_flag
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    if input_yang_obj.ipv4_source_router_id._changed():
        input_yang_obj.ipv4_source_router_id = input_yang_obj.ipv4_source_router_id
        
    if input_yang_obj.ipv6_source_router_id._changed():
        input_yang_obj.ipv6_source_router_id = input_yang_obj.ipv6_source_router_id
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators(input_yang_obj: yc_srv6_locators_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp/srv6-locators

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
    
    for k, listInst in input_yang_obj.locator.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators_locator(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp(input_yang_obj: yc_lsp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels/lsp

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
    
    if input_yang_obj.decoded_completed._changed():
        input_yang_obj.decoded_completed = input_yang_obj.decoded_completed
        
    if input_yang_obj.raw_data._changed():
        input_yang_obj.raw_data = input_yang_obj.raw_data
        
    if input_yang_obj.checksum._changed():
        input_yang_obj.checksum = input_yang_obj.checksum
        
    if input_yang_obj.remaining_lifetime._changed():
        input_yang_obj.remaining_lifetime = input_yang_obj.remaining_lifetime
        
    if input_yang_obj.sequence._changed():
        input_yang_obj.sequence = input_yang_obj.sequence
        
    if input_yang_obj.attributes._changed():
        input_yang_obj.attributes = input_yang_obj.attributes
        
    if input_yang_obj.ipv4_addresses._changed():
        input_yang_obj.ipv4_addresses = input_yang_obj.ipv4_addresses
        
    if input_yang_obj.ipv6_addresses._changed():
        input_yang_obj.ipv6_addresses = input_yang_obj.ipv6_addresses
        
    if input_yang_obj.ipv4_te_routerid._changed():
        input_yang_obj.ipv4_te_routerid = input_yang_obj.ipv4_te_routerid
        
    if input_yang_obj.ipv6_te_routerid._changed():
        input_yang_obj.ipv6_te_routerid = input_yang_obj.ipv6_te_routerid
        
    if input_yang_obj.protocol_supported._changed():
        input_yang_obj.protocol_supported = input_yang_obj.protocol_supported
        
    if input_yang_obj.dynamic_hostname._changed():
        input_yang_obj.dynamic_hostname = input_yang_obj.dynamic_hostname
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_authentication(input_yang_obj.authentication, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_entries(input_yang_obj.mt_entries, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_router_capabilities(input_yang_obj.router_capabilities, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_links_srlgs(input_yang_obj.links_srlgs, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_unknown_tlvs(input_yang_obj.unknown_tlvs, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_is_neighbor(input_yang_obj.is_neighbor, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_is_neighbor(input_yang_obj.extended_is_neighbor, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_internal_reachability(input_yang_obj.ipv4_internal_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv4_external_reachability(input_yang_obj.ipv4_external_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_extended_ipv4_reachability(input_yang_obj.extended_ipv4_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_is_neighbor(input_yang_obj.mt_is_neighbor, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_extended_ipv4_reachability(input_yang_obj.mt_extended_ipv4_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_mt_ipv6_reachability(input_yang_obj.mt_ipv6_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_ipv6_reachability(input_yang_obj.ipv6_reachability, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp_srv6_locators(input_yang_obj.srv6_locators, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels(input_yang_obj: yc_levels_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database_levels, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database/levels

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
    
    for k, listInst in input_yang_obj.lsp.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels_lsp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_database(input_yang_obj: yc_database_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_database, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/database

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
    
    for k, listInst in input_yang_obj.levels.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_database_levels(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/local-rib/route/next-hops/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops(input_yang_obj: yc_next_hops_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/local-rib/route/next-hops

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/local-rib/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route_next_hops(input_yang_obj.next_hops, translated_yang_obj)
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.level._changed():
        input_yang_obj.level = input_yang_obj.level
        
    if input_yang_obj.route_tag._changed():
        input_yang_obj.route_tag = input_yang_obj.route_tag
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib(input_yang_obj: yc_local_rib_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_local_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/local-rib

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_local_rib_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_system_counters_level(input_yang_obj: yc_level_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_system_counters_level, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/system-counters/level

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
    
    if input_yang_obj.corrupted_lsps._changed():
        input_yang_obj.corrupted_lsps = input_yang_obj.corrupted_lsps
        
    if input_yang_obj.authentication_type_fails._changed():
        input_yang_obj.authentication_type_fails = input_yang_obj.authentication_type_fails
        
    if input_yang_obj.authentication_fails._changed():
        input_yang_obj.authentication_fails = input_yang_obj.authentication_fails
        
    if input_yang_obj.database_overload._changed():
        input_yang_obj.database_overload = input_yang_obj.database_overload
        
    if input_yang_obj.own_lsp_purge._changed():
        input_yang_obj.own_lsp_purge = input_yang_obj.own_lsp_purge
        
    if input_yang_obj.manual_address_drop_from_area._changed():
        input_yang_obj.manual_address_drop_from_area = input_yang_obj.manual_address_drop_from_area
        
    if input_yang_obj.max_sequence._changed():
        input_yang_obj.max_sequence = input_yang_obj.max_sequence
        
    if input_yang_obj.sequence_number_skipped._changed():
        input_yang_obj.sequence_number_skipped = input_yang_obj.sequence_number_skipped
        
    if input_yang_obj.id_len_mismatch._changed():
        input_yang_obj.id_len_mismatch = input_yang_obj.id_len_mismatch
        
    if input_yang_obj.partition_changes._changed():
        input_yang_obj.partition_changes = input_yang_obj.partition_changes
        
    if input_yang_obj.lsp_errors._changed():
        input_yang_obj.lsp_errors = input_yang_obj.lsp_errors
        
    if input_yang_obj.spf_runs._changed():
        input_yang_obj.spf_runs = input_yang_obj.spf_runs
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_system_counters(input_yang_obj: yc_system_counters_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_system_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/system-counters

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
    
    for k, listInst in input_yang_obj.level.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_system_counters_level(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_protected_routes_address_family_stats(input_yang_obj: yc_address_family_stats_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_protected_routes_address_family_stats, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/protected-routes/address-family-stats

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
    
    if input_yang_obj.alternate_type._changed():
        input_yang_obj.alternate_type = input_yang_obj.alternate_type
        
    if input_yang_obj.best._changed():
        input_yang_obj.best = input_yang_obj.best
        
    if input_yang_obj.non_best_reason._changed():
        input_yang_obj.non_best_reason = input_yang_obj.non_best_reason
        
    if input_yang_obj.protection_available._changed():
        input_yang_obj.protection_available = input_yang_obj.protection_available
        
    if input_yang_obj.alternate_metric1._changed():
        input_yang_obj.alternate_metric1 = input_yang_obj.alternate_metric1
        
    if input_yang_obj.alternate_metric2._changed():
        input_yang_obj.alternate_metric2 = input_yang_obj.alternate_metric2
        
    if input_yang_obj.alternate_metric3._changed():
        input_yang_obj.alternate_metric3 = input_yang_obj.alternate_metric3
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_protected_routes(input_yang_obj: yc_protected_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_protected_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/protected-routes

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
    
    for k, listInst in input_yang_obj.address_family_stats.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_protected_routes_address_family_stats(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_unprotected_routes_address_family_stats(input_yang_obj: yc_address_family_stats_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_unprotected_routes_address_family_stats, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/unprotected-routes/address-family-stats

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_unprotected_routes(input_yang_obj: yc_unprotected_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_unprotected_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/unprotected-routes

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
    
    for k, listInst in input_yang_obj.address_family_stats.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_unprotected_routes_address_family_stats(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_protection_statistics_address_family_stats(input_yang_obj: yc_address_family_stats_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_protection_statistics_address_family_stats, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/protection-statistics/address-family-stats

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
    
    if input_yang_obj.total_routes._changed():
        input_yang_obj.total_routes = input_yang_obj.total_routes
        
    if input_yang_obj.unprotected_routes._changed():
        input_yang_obj.unprotected_routes = input_yang_obj.unprotected_routes
        
    if input_yang_obj.protected_routes._changed():
        input_yang_obj.protected_routes = input_yang_obj.protected_routes
        
    if input_yang_obj.linkprotected_routes._changed():
        input_yang_obj.linkprotected_routes = input_yang_obj.linkprotected_routes
        
    if input_yang_obj.nodeprotected_routes._changed():
        input_yang_obj.nodeprotected_routes = input_yang_obj.nodeprotected_routes
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_protection_statistics(input_yang_obj: yc_protection_statistics_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_protection_statistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/protection-statistics

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
    
    for k, listInst in input_yang_obj.address_family_stats.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_protection_statistics_address_family_stats(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology/default-metric/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology/default-metric/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric(input_yang_obj: yc_default_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology/default-metric

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags_node_tag(input_yang_obj: yc_node_tag_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags_node_tag, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology/node-tags/node-tag

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags(input_yang_obj: yc_node_tags_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology/node-tags

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
    
    for k, listInst in input_yang_obj.node_tag.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags_node_tag(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology(input_yang_obj: yc_topology_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies/topology

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_default_metric(input_yang_obj.default_metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology_node_tags(input_yang_obj.node_tags, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies(input_yang_obj: yc_topologies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_topologies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/topologies

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
    
    for k, listInst in input_yang_obj.topology.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_topologies_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_padding(input_yang_obj: yc_hello_padding_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_padding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-padding

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-authentication/level-1

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-authentication/level-2

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication(input_yang_obj: yc_hello_authentication_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-authentication

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
    
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.key._changed():
        input_yang_obj.key = input_yang_obj.key
        
    if input_yang_obj.crypto_algorithm._changed():
        input_yang_obj.crypto_algorithm = input_yang_obj.crypto_algorithm
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-interval/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-interval/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval(input_yang_obj: yc_hello_interval_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-interval

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-multiplier/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-multiplier/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier(input_yang_obj: yc_hello_multiplier_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/hello-multiplier

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/priority/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/priority/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority(input_yang_obj: yc_priority_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/priority

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/metric/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/metric/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric(input_yang_obj: yc_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/metric

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_bfd(input_yang_obj: yc_bfd_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_bfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/bfd

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.local_multiplier._changed():
        input_yang_obj.local_multiplier = input_yang_obj.local_multiplier
        
    if input_yang_obj.desired_min_tx_interval._changed():
        input_yang_obj.desired_min_tx_interval = input_yang_obj.desired_min_tx_interval
        
    if input_yang_obj.required_min_rx_interval._changed():
        input_yang_obj.required_min_rx_interval = input_yang_obj.required_min_rx_interval
        
    if input_yang_obj.min_interval._changed():
        input_yang_obj.min_interval = input_yang_obj.min_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families_address_family_list(input_yang_obj: yc_address_family_list_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families_address_family_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/address-families/address-family-list

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families(input_yang_obj: yc_address_families_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/address-families

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
    
    for k, listInst in input_yang_obj.address_family_list.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families_address_family_list(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls_ldp(input_yang_obj: yc_ldp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls_ldp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/mpls/ldp

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
    
    if input_yang_obj.igp_sync._changed():
        input_yang_obj.igp_sync = input_yang_obj.igp_sync
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls(input_yang_obj: yc_mpls_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/mpls

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls_ldp(input_yang_obj.ldp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_remote_lfa(input_yang_obj: yc_remote_lfa_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_remote_lfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa/remote-lfa

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1_remote_lfa(input_yang_obj: yc_remote_lfa_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1_remote_lfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa/level-1/remote-lfa

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa/level-1

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
    
    if input_yang_obj.candidate_enable._changed():
        input_yang_obj.candidate_enable = input_yang_obj.candidate_enable
        
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1_remote_lfa(input_yang_obj.remote_lfa, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2_remote_lfa(input_yang_obj: yc_remote_lfa_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2_remote_lfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa/level-2/remote-lfa

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa/level-2

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
    
    if input_yang_obj.candidate_enable._changed():
        input_yang_obj.candidate_enable = input_yang_obj.candidate_enable
        
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2_remote_lfa(input_yang_obj.remote_lfa, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa(input_yang_obj: yc_lfa_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/lfa

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
    
    if input_yang_obj.candidate_enable._changed():
        input_yang_obj.candidate_enable = input_yang_obj.candidate_enable
        
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_remote_lfa(input_yang_obj.remote_lfa, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_srv6_ti_lfa(input_yang_obj: yc_srv6_ti_lfa_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_srv6_ti_lfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute/srv6-ti-lfa

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute(input_yang_obj: yc_fast_reroute_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/fast-reroute

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_lfa(input_yang_obj.lfa, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute_srv6_ti_lfa(input_yang_obj.srv6_ti_lfa, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid_endpoint_func(input_yang_obj: yc_endpoint_func_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid_endpoint_func, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/adjacencies/adjacency/end-x-sid/endpoint-func

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
    
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.endpoint_func._changed():
        input_yang_obj.endpoint_func = input_yang_obj.endpoint_func
        
    if input_yang_obj.undefined_endpoint_func._changed():
        input_yang_obj.undefined_endpoint_func = input_yang_obj.undefined_endpoint_func
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid(input_yang_obj: yc_end_x_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/adjacencies/adjacency/end-x-sid

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
    
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.protection_requested._changed():
        input_yang_obj.protection_requested = input_yang_obj.protection_requested
        
    if input_yang_obj.persistent._changed():
        input_yang_obj.persistent = input_yang_obj.persistent
        
    if input_yang_obj.algorithm._changed():
        input_yang_obj.algorithm = input_yang_obj.algorithm
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid_endpoint_func(input_yang_obj.endpoint_func, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency(input_yang_obj: yc_adjacency_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/adjacencies/adjacency

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
    
    if input_yang_obj.neighbor_sys_type._changed():
        input_yang_obj.neighbor_sys_type = input_yang_obj.neighbor_sys_type
        
    if input_yang_obj.neighbor_sysid._changed():
        input_yang_obj.neighbor_sysid = input_yang_obj.neighbor_sysid
        
    if input_yang_obj.neighbor_extended_circuit_id._changed():
        input_yang_obj.neighbor_extended_circuit_id = input_yang_obj.neighbor_extended_circuit_id
        
    if input_yang_obj.neighbor_snpa._changed():
        input_yang_obj.neighbor_snpa = input_yang_obj.neighbor_snpa
        
    if input_yang_obj.usage._changed():
        input_yang_obj.usage = input_yang_obj.usage
        
    if input_yang_obj.hold_timer._changed():
        input_yang_obj.hold_timer = input_yang_obj.hold_timer
        
    if input_yang_obj.neighbor_priority._changed():
        input_yang_obj.neighbor_priority = input_yang_obj.neighbor_priority
        
    if input_yang_obj.lastuptime._changed():
        input_yang_obj.lastuptime = input_yang_obj.lastuptime
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    for k, listInst in input_yang_obj.end_x_sid.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency_end_x_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies(input_yang_obj: yc_adjacencies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/adjacencies

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
    
    for k, listInst in input_yang_obj.adjacency.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies_adjacency(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_event_counters(input_yang_obj: yc_event_counters_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_event_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/event-counters

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
    
    if input_yang_obj.adjacency_changes._changed():
        input_yang_obj.adjacency_changes = input_yang_obj.adjacency_changes
        
    if input_yang_obj.adjacency_number._changed():
        input_yang_obj.adjacency_number = input_yang_obj.adjacency_number
        
    if input_yang_obj.init_fails._changed():
        input_yang_obj.init_fails = input_yang_obj.init_fails
        
    if input_yang_obj.adjacency_rejects._changed():
        input_yang_obj.adjacency_rejects = input_yang_obj.adjacency_rejects
        
    if input_yang_obj.id_len_mismatch._changed():
        input_yang_obj.id_len_mismatch = input_yang_obj.id_len_mismatch
        
    if input_yang_obj.max_area_addresses_mismatch._changed():
        input_yang_obj.max_area_addresses_mismatch = input_yang_obj.max_area_addresses_mismatch
        
    if input_yang_obj.authentication_type_fails._changed():
        input_yang_obj.authentication_type_fails = input_yang_obj.authentication_type_fails
        
    if input_yang_obj.authentication_fails._changed():
        input_yang_obj.authentication_fails = input_yang_obj.authentication_fails
        
    if input_yang_obj.lan_dis_changes._changed():
        input_yang_obj.lan_dis_changes = input_yang_obj.lan_dis_changes
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_iih(input_yang_obj: yc_iih_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_iih, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/iih

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_ish(input_yang_obj: yc_ish_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_ish, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/ish

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_esh(input_yang_obj: yc_esh_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_esh, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/esh

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_lsp(input_yang_obj: yc_lsp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_lsp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/lsp

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_psnp(input_yang_obj: yc_psnp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_psnp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/psnp

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_csnp(input_yang_obj: yc_csnp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_csnp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/csnp

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_unknown(input_yang_obj: yc_unknown_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_unknown, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level/unknown

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
    
    if input_yang_obj.in_._changed():
        input_yang_obj.in_ = input_yang_obj.in_
        
    if input_yang_obj.out._changed():
        input_yang_obj.out = input_yang_obj.out
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level(input_yang_obj: yc_level_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters/level

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_iih(input_yang_obj.iih, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_ish(input_yang_obj.ish, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_esh(input_yang_obj.esh, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_lsp(input_yang_obj.lsp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_psnp(input_yang_obj.psnp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_csnp(input_yang_obj.csnp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level_unknown(input_yang_obj.unknown, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters(input_yang_obj: yc_packet_counters_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/packet-counters

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
    
    for k, listInst in input_yang_obj.level.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters_level(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_1(input_yang_obj: yc_level_1_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/topologies/topology/metric/level-1

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_2(input_yang_obj: yc_level_2_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/topologies/topology/metric/level-2

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric(input_yang_obj: yc_metric_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/topologies/topology/metric

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
    
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_1(input_yang_obj.level_1, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric_level_2(input_yang_obj.level_2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology(input_yang_obj: yc_topology_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/topologies/topology

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology_metric(input_yang_obj.metric, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies(input_yang_obj: yc_topologies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface/topologies

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
    
    for k, listInst in input_yang_obj.topology.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface(input_yang_obj: yc_interface_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces/interface

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
    
    if input_yang_obj.level_type._changed():
        input_yang_obj.level_type = input_yang_obj.level_type
        
    if input_yang_obj.lsp_pacing_interval._changed():
        input_yang_obj.lsp_pacing_interval = input_yang_obj.lsp_pacing_interval
        
    if input_yang_obj.lsp_retransmit_interval._changed():
        input_yang_obj.lsp_retransmit_interval = input_yang_obj.lsp_retransmit_interval
        
    if input_yang_obj.passive._changed():
        input_yang_obj.passive = input_yang_obj.passive
        
    if input_yang_obj.csnp_interval._changed():
        input_yang_obj.csnp_interval = input_yang_obj.csnp_interval
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_padding(input_yang_obj.hello_padding, translated_yang_obj)
        
    if input_yang_obj.mesh_group_enable._changed():
        input_yang_obj.mesh_group_enable = input_yang_obj.mesh_group_enable
        
    if input_yang_obj.mesh_group._changed():
        input_yang_obj.mesh_group = input_yang_obj.mesh_group
        
    if input_yang_obj.interface_type._changed():
        input_yang_obj.interface_type = input_yang_obj.interface_type
        
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.tag64._changed():
        input_yang_obj.tag64 = input_yang_obj.tag64
        
    if input_yang_obj.node_flag._changed():
        input_yang_obj.node_flag = input_yang_obj.node_flag
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_authentication(input_yang_obj.hello_authentication, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_interval(input_yang_obj.hello_interval, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_hello_multiplier(input_yang_obj.hello_multiplier, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_priority(input_yang_obj.priority, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_metric(input_yang_obj.metric, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_bfd(input_yang_obj.bfd, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_address_families(input_yang_obj.address_families, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_mpls(input_yang_obj.mpls, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_fast_reroute(input_yang_obj.fast_reroute, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_adjacencies(input_yang_obj.adjacencies, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_event_counters(input_yang_obj.event_counters, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_packet_counters(input_yang_obj.packet_counters, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface_topologies(input_yang_obj.topologies, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/interfaces

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
    
    for k, listInst in input_yang_obj.interface.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_interfaces_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis_srv6_cfg(input_yang_obj: yc_srv6_cfg_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis_srv6_cfg, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis/srv6-cfg

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.default_locator._changed():
        translated_yang_obj.isSrv6Cfg.defaultLocator = input_yang_obj.default_locator
        
    if input_yang_obj.locator_name._changed():
        translated_yang_obj.isSrv6Cfg.locatorName = input_yang_obj.locator_name
        
    if input_yang_obj.persistent_end_x_sid._changed():
        translated_yang_obj.isSrv6Cfg.autoSid = input_yang_obj.persistent_end_x_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_isis(input_yang_obj: yc_isis_ietf_routing__routing_control_plane_protocols_control_plane_protocol_isis, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/isis

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
    isSite_obj = translated_yang_obj.isiscomm.isSites.isSite.add("1")

    isSite_obj.baseTopoType = "ipv6"

    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.level_type._changed():
        isSite_obj.isLevel = input_yang_obj.level_type
        
    if input_yang_obj.system_id._changed() and input_yang_obj.area_address._changed():
        netEntity = str(input_yang_obj.area_address[0]) + str(input_yang_obj.system_id).replace(".", "") + "00"
        # print(netEntity)
        isSite_obj.isNetEntitys.isNetEntity.add(netEntity)
        
    if input_yang_obj.maximum_area_addresses._changed():
        input_yang_obj.maximum_area_addresses = input_yang_obj.maximum_area_addresses

    if input_yang_obj.lsp_mtu._changed():
        input_yang_obj.lsp_mtu = input_yang_obj.lsp_mtu
        
    if input_yang_obj.lsp_lifetime._changed():
        input_yang_obj.lsp_lifetime = input_yang_obj.lsp_lifetime
        
    if input_yang_obj.lsp_refresh._changed():
        input_yang_obj.lsp_refresh = input_yang_obj.lsp_refresh
        
    if input_yang_obj.poi_tlv._changed():
        input_yang_obj.poi_tlv = input_yang_obj.poi_tlv

    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis_srv6_cfg(input_yang_obj.srv6_cfg, isSite_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_default_route_distance(input_yang_obj: yc_default_route_distance_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_default_route_distance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/default-route-distance

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
    
    if input_yang_obj.external_route_distance._changed():
        input_yang_obj.external_route_distance = input_yang_obj.external_route_distance
        
    if input_yang_obj.internal_route_distance._changed():
        input_yang_obj.internal_route_distance = input_yang_obj.internal_route_distance
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_confederation(input_yang_obj: yc_confederation_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_confederation, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/confederation

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    if input_yang_obj.member_as._changed():
        input_yang_obj.member_as = input_yang_obj.member_as
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.restart_time._changed():
        input_yang_obj.restart_time = input_yang_obj.restart_time
        
    if input_yang_obj.stale_routes_time._changed():
        input_yang_obj.stale_routes_time = input_yang_obj.stale_routes_time
        
    if input_yang_obj.helper_only._changed():
        input_yang_obj.helper_only = input_yang_obj.helper_only
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ibgp(input_yang_obj: yc_ibgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ibgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/use-multiple-paths/ibgp

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
    
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ibgp(input_yang_obj.ibgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_route_selection_options(input_yang_obj: yc_route_selection_options_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_route_selection_options, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/route-selection-options

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
    
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_route_selection_options(input_yang_obj: yc_route_selection_options_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_route_selection_options, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/route-selection-options

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
    
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj: yc_ibgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ibgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/use-multiple-paths/ibgp

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
    
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj.ibgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_received_sids(input_yang_obj: yc_received_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_received_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes/route/srv6/received-sids

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes/route/srv6/local-sids

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
    
    if input_yang_obj.locator._changed():
        input_yang_obj.locator = input_yang_obj.locator
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes/route/srv6

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
    
    for k, listInst in input_yang_obj.received_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_received_sids(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6_local_sids(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/segment-routing/srv6

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

    bgpVrfAF_obj = translated_yang_obj.bgpVrfAFs.bgpVrfAF.add("ipv4uni")
    
    if input_yang_obj.sid_alloc_mode._changed():
        locatorName = input_yang_obj.sid_alloc_mode
        locator_obj = bgpVrfAF_obj.locators.locator.add(locatorName)
        locator_obj.autoSid = "true"
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing(input_yang_obj: yc_segment_routing_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/segment-routing

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast(input_yang_obj: yc_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_segment_routing(input_yang_obj.segment_routing, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_received_sids(input_yang_obj: yc_received_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_received_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes/route/srv6/received-sids

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes/route/srv6/local-sids

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
    
    if input_yang_obj.locator._changed():
        input_yang_obj.locator = input_yang_obj.locator
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes/route/srv6

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
    
    for k, listInst in input_yang_obj.received_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_received_sids(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6_local_sids(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/segment-routing/srv6

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
    
    if input_yang_obj.sid_alloc_mode._changed():
        input_yang_obj.sid_alloc_mode = input_yang_obj.sid_alloc_mode
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing(input_yang_obj: yc_segment_routing_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast/segment-routing

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast(input_yang_obj: yc_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_segment_routing(input_yang_obj.segment_routing, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges(input_yang_obj: yc_srgb_ranges_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes/route/prefix-sid/originator-srgb/srgb-ranges

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb(input_yang_obj: yc_originator_srgb_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes/route/prefix-sid/originator-srgb

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
    
    for k, listInst in input_yang_obj.srgb_ranges.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid(input_yang_obj: yc_prefix_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes/route/prefix-sid

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
    
    if input_yang_obj.label_index._changed():
        input_yang_obj.label_index = input_yang_obj.label_index
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid_originator_srgb(input_yang_obj.originator_srgb, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_prefix_sid(input_yang_obj.prefix_sid, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj: yc_ipv4_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges(input_yang_obj: yc_srgb_ranges_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes/route/prefix-sid/originator-srgb/srgb-ranges

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb(input_yang_obj: yc_originator_srgb_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes/route/prefix-sid/originator-srgb

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
    
    for k, listInst in input_yang_obj.srgb_ranges.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb_srgb_ranges(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid(input_yang_obj: yc_prefix_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes/route/prefix-sid

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
    
    if input_yang_obj.label_index._changed():
        input_yang_obj.label_index = input_yang_obj.label_index
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid_originator_srgb(input_yang_obj.originator_srgb, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_prefix_sid(input_yang_obj.prefix_sid, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj: yc_ipv6_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_received_sids(input_yang_obj: yc_received_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_received_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes/route/srv6/received-sids

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes/route/srv6/local-sids

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
    
    if input_yang_obj.locator._changed():
        input_yang_obj.locator = input_yang_obj.locator
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes/route/srv6

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
    
    for k, listInst in input_yang_obj.received_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_received_sids(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6_local_sids(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj: yc_l3vpn_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_received_sids(input_yang_obj: yc_received_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_received_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes/route/srv6/received-sids

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes/route/srv6/local-sids

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
    
    if input_yang_obj.locator._changed():
        input_yang_obj.locator = input_yang_obj.locator
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes/route/srv6

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
    
    for k, listInst in input_yang_obj.received_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_received_sids(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6_local_sids(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj: yc_l3vpn_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj: yc_l3vpn_ipv4_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv4-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj: yc_l3vpn_ipv6_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l3vpn-ipv6-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-vpls/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj: yc_l2vpn_vpls_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-vpls

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_automatic_steering(input_yang_obj: yc_automatic_steering_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_automatic_steering, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes/route/automatic-steering

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
    
    if input_yang_obj.color._changed():
        input_yang_obj.color = input_yang_obj.color
        
    if input_yang_obj.end_point._changed():
        input_yang_obj.end_point = input_yang_obj.end_point
        
    if input_yang_obj.co_flag._changed():
        input_yang_obj.co_flag = input_yang_obj.co_flag
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_received_sids(input_yang_obj: yc_received_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_received_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes/route/srv6/received-sids

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes/route/srv6/local-sids

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
    
    if input_yang_obj.locator._changed():
        input_yang_obj.locator = input_yang_obj.locator
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes/route/srv6

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
    
    for k, listInst in input_yang_obj.received_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_received_sids(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sids.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6_local_sids(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route(input_yang_obj: yc_route_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes/route

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_automatic_steering(input_yang_obj.automatic_steering, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes(input_yang_obj: yc_routes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj: yc_l2vpn_evpn_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/l2vpn-evpn

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy_explicit_binding_sid(input_yang_obj: yc_explicit_binding_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy_explicit_binding_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-srpolicy/explicit-policies/sr-policy/explicit-binding-sid

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
    
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    if input_yang_obj.strict._changed():
        input_yang_obj.strict = input_yang_obj.strict
        
    if input_yang_obj.drop_on_invalid._changed():
        input_yang_obj.drop_on_invalid = input_yang_obj.drop_on_invalid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy(input_yang_obj: yc_sr_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-srpolicy/explicit-policies/sr-policy

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
    
    if input_yang_obj.preference._changed():
        input_yang_obj.preference = input_yang_obj.preference
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy_explicit_binding_sid(input_yang_obj.explicit_binding_sid, translated_yang_obj)
        
    if input_yang_obj.usable._changed():
        input_yang_obj.usable = input_yang_obj.usable
        
    if input_yang_obj.registered._changed():
        input_yang_obj.registered = input_yang_obj.registered
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies(input_yang_obj: yc_explicit_policies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-srpolicy/explicit-policies

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
    
    for k, listInst in input_yang_obj.sr_policy.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies_sr_policy(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy(input_yang_obj: yc_ipv4_srpolicy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv4-srpolicy

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy_explicit_policies(input_yang_obj.explicit_policies, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy_explicit_binding_sid(input_yang_obj: yc_explicit_binding_sid_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy_explicit_binding_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-srpolicy/explicit-policies/sr-policy/explicit-binding-sid

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
    
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    if input_yang_obj.strict._changed():
        input_yang_obj.strict = input_yang_obj.strict
        
    if input_yang_obj.drop_on_invalid._changed():
        input_yang_obj.drop_on_invalid = input_yang_obj.drop_on_invalid
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy(input_yang_obj: yc_sr_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-srpolicy/explicit-policies/sr-policy

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
    
    if input_yang_obj.preference._changed():
        input_yang_obj.preference = input_yang_obj.preference
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy_explicit_binding_sid(input_yang_obj.explicit_binding_sid, translated_yang_obj)
        
    if input_yang_obj.usable._changed():
        input_yang_obj.usable = input_yang_obj.usable
        
    if input_yang_obj.registered._changed():
        input_yang_obj.registered = input_yang_obj.registered
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies(input_yang_obj: yc_explicit_policies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-srpolicy/explicit-policies

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
    
    for k, listInst in input_yang_obj.sr_policy.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies_sr_policy(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy(input_yang_obj: yc_ipv6_srpolicy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi/ipv6-srpolicy

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy_explicit_policies(input_yang_obj.explicit_policies, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi(input_yang_obj: yc_afi_safi_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis/afi-safi

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.total_paths._changed():
        input_yang_obj.total_paths = input_yang_obj.total_paths
        
    if input_yang_obj.total_prefixes._changed():
        input_yang_obj.total_prefixes = input_yang_obj.total_prefixes
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_route_selection_options(input_yang_obj.route_selection_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj.ipv4_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj.ipv6_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj.l3vpn_ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj.l3vpn_ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj.l3vpn_ipv4_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj.l3vpn_ipv6_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj.l2vpn_vpls, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj.l2vpn_evpn, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_srpolicy(input_yang_obj.ipv4_srpolicy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_srpolicy(input_yang_obj.ipv6_srpolicy, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis(input_yang_obj: yc_afi_safis_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/afi-safis

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

    bgpVrf_obj = translated_yang_obj.bgpVrfs.bgpVrf.add("test")

    for k, listInst in input_yang_obj.afi_safi.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi(listInst, bgpVrf_obj)
        pass
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors_colors(input_yang_obj: yc_colors_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors_colors, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/on-demand-policies/authorized-colors/colors

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors(input_yang_obj: yc_authorized_colors_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/on-demand-policies/authorized-colors

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
    
    for k, listInst in input_yang_obj.colors.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors_colors(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies_sr_policy(input_yang_obj: yc_sr_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies_sr_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/on-demand-policies/installed-policies/sr-policy

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies(input_yang_obj: yc_installed_policies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/on-demand-policies/installed-policies

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
    
    for k, listInst in input_yang_obj.sr_policy.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies_sr_policy(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies(input_yang_obj: yc_on_demand_policies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/on-demand-policies

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_authorized_colors(input_yang_obj.authorized_colors, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies_installed_policies(input_yang_obj.installed_policies, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state_sr_policy(input_yang_obj: yc_sr_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state_sr_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/policy-state/sr-policy

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
    
    if input_yang_obj.policy_state._changed():
        input_yang_obj.policy_state = input_yang_obj.policy_state
        
    if input_yang_obj.binding_sid._changed():
        input_yang_obj.binding_sid = input_yang_obj.binding_sid
        
    if input_yang_obj.steering_disabled._changed():
        input_yang_obj.steering_disabled = input_yang_obj.steering_disabled
        
    if input_yang_obj.ref_count._changed():
        input_yang_obj.ref_count = input_yang_obj.ref_count
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state(input_yang_obj: yc_policy_state_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing/policy-state

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
    
    for k, listInst in input_yang_obj.sr_policy.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state_sr_policy(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing(input_yang_obj: yc_segment_routing_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/segment-routing

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_on_demand_policies(input_yang_obj.on_demand_policies, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing_policy_state(input_yang_obj.policy_state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global(input_yang_obj: yc_global__ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_global, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global

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
    bgpcomm_obj = translated_yang_obj.bgp.bgpcomm
    # bgpcomm_obj.bgpSite.bgpVersion = 1

    if input_yang_obj.as_._changed():
        print(input_yang_obj.as_)
        translated_yang_obj.bgp.bgpcomm.bgpSite.bgpEnable = "true"
        translated_yang_obj.bgp.bgpcomm.bgpSite.asNumber = str(input_yang_obj.as_)
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_default_route_distance(input_yang_obj.default_route_distance, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_confederation(input_yang_obj.confederation, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_route_selection_options(input_yang_obj.route_selection_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis(input_yang_obj.afi_safis, bgpcomm_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_segment_routing(input_yang_obj.segment_routing, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_timers(input_yang_obj: yc_timers_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_timers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/timers

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
    
    if input_yang_obj.connect_retry_interval._changed():
        input_yang_obj.connect_retry_interval = input_yang_obj.connect_retry_interval
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.keepalive_interval._changed():
        input_yang_obj.keepalive_interval = input_yang_obj.keepalive_interval
        
    if input_yang_obj.hold_time_configured._changed():
        input_yang_obj.hold_time_configured = input_yang_obj.hold_time_configured
        
    if input_yang_obj.keep_alive_configured._changed():
        input_yang_obj.keep_alive_configured = input_yang_obj.keep_alive_configured
        
    if input_yang_obj.min_as_origination_interval._changed():
        input_yang_obj.min_as_origination_interval = input_yang_obj.min_as_origination_interval
        
    if input_yang_obj.min_route_advertisement_interval._changed():
        input_yang_obj.min_route_advertisement_interval = input_yang_obj.min_route_advertisement_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_transport(input_yang_obj: yc_transport_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_transport, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/transport

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
    
    if input_yang_obj.tcp_mss._changed():
        input_yang_obj.tcp_mss = input_yang_obj.tcp_mss
        
    if input_yang_obj.mtu_discovery._changed():
        input_yang_obj.mtu_discovery = input_yang_obj.mtu_discovery
        
    if input_yang_obj.passive_mode._changed():
        input_yang_obj.passive_mode = input_yang_obj.passive_mode
        
    if input_yang_obj.local_address._changed():
        input_yang_obj.local_address = input_yang_obj.local_address
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.restart_time._changed():
        input_yang_obj.restart_time = input_yang_obj.restart_time
        
    if input_yang_obj.stale_routes_time._changed():
        input_yang_obj.stale_routes_time = input_yang_obj.stale_routes_time
        
    if input_yang_obj.helper_only._changed():
        input_yang_obj.helper_only = input_yang_obj.helper_only
        
    if input_yang_obj.peer_restart_time._changed():
        input_yang_obj.peer_restart_time = input_yang_obj.peer_restart_time
        
    if input_yang_obj.peer_restarting._changed():
        input_yang_obj.peer_restarting = input_yang_obj.peer_restarting
        
    if input_yang_obj.local_restarting._changed():
        input_yang_obj.local_restarting = input_yang_obj.local_restarting
        
    if input_yang_obj.mode._changed():
        input_yang_obj.mode = input_yang_obj.mode
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_ebgp_multihop(input_yang_obj: yc_ebgp_multihop_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_ebgp_multihop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/ebgp-multihop

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.multihop_ttl._changed():
        input_yang_obj.multihop_ttl = input_yang_obj.multihop_ttl
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_reflector(input_yang_obj: yc_route_reflector_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_reflector, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/route-reflector

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
    
    if input_yang_obj.route_reflector_cluster_id._changed():
        input_yang_obj.route_reflector_cluster_id = input_yang_obj.route_reflector_cluster_id
        
    if input_yang_obj.route_reflector_client._changed():
        input_yang_obj.route_reflector_client = input_yang_obj.route_reflector_client
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_as_path_options(input_yang_obj: yc_as_path_options_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_as_path_options, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/as-path-options

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
    
    if input_yang_obj.allow_own_as._changed():
        input_yang_obj.allow_own_as = input_yang_obj.allow_own_as
        
    if input_yang_obj.replace_peer_as._changed():
        input_yang_obj.replace_peer_as = input_yang_obj.replace_peer_as
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_add_paths(input_yang_obj: yc_add_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_add_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/add-paths

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
    
    if input_yang_obj.receive._changed():
        input_yang_obj.receive = input_yang_obj.receive
        
    if input_yang_obj.send_max._changed():
        input_yang_obj.send_max = input_yang_obj.send_max
        
    if input_yang_obj.eligible_prefix_policy._changed():
        input_yang_obj.eligible_prefix_policy = input_yang_obj.eligible_prefix_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_prefixes(input_yang_obj: yc_prefixes_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_prefixes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/prefixes

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
    
    if input_yang_obj.received._changed():
        input_yang_obj.received = input_yang_obj.received
        
    if input_yang_obj.sent._changed():
        input_yang_obj.sent = input_yang_obj.sent
        
    if input_yang_obj.installed._changed():
        input_yang_obj.installed = input_yang_obj.installed
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.received._changed():
        input_yang_obj.received = input_yang_obj.received
        
    if input_yang_obj.advertised._changed():
        input_yang_obj.advertised = input_yang_obj.advertised
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast(input_yang_obj: yc_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast(input_yang_obj: yc_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj: yc_ipv4_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv6-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj: yc_ipv6_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv6-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj: yc_l3vpn_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj: yc_l3vpn_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv4-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj: yc_l3vpn_ipv4_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv4-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj: yc_l3vpn_ipv6_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l2vpn-vpls/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj: yc_l2vpn_vpls_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l2vpn-vpls

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l2vpn-evpn/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj: yc_l2vpn_evpn_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l2vpn-evpn

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi(input_yang_obj: yc_afi_safi_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis/afi-safi

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_prefixes(input_yang_obj.prefixes, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj.ipv4_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj.ipv6_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj.l3vpn_ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj.l3vpn_ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj.l3vpn_ipv4_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj.l3vpn_ipv6_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj.l2vpn_vpls, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj.l2vpn_evpn, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis(input_yang_obj: yc_afi_safis_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/afi-safis

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
    
    for k, listInst in input_yang_obj.afi_safi.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_sent(input_yang_obj: yc_sent_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_sent, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/messages/sent

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
    
    if input_yang_obj.updates_received._changed():
        input_yang_obj.updates_received = input_yang_obj.updates_received
        
    if input_yang_obj.updates_sent._changed():
        input_yang_obj.updates_sent = input_yang_obj.updates_sent
        
    if input_yang_obj.messages_received._changed():
        input_yang_obj.messages_received = input_yang_obj.messages_received
        
    if input_yang_obj.messages_sent._changed():
        input_yang_obj.messages_sent = input_yang_obj.messages_sent
        
    if input_yang_obj.notification._changed():
        input_yang_obj.notification = input_yang_obj.notification
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_received(input_yang_obj: yc_received_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_received, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/messages/received

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
    
    if input_yang_obj.updates_received._changed():
        input_yang_obj.updates_received = input_yang_obj.updates_received
        
    if input_yang_obj.updates_sent._changed():
        input_yang_obj.updates_sent = input_yang_obj.updates_sent
        
    if input_yang_obj.messages_received._changed():
        input_yang_obj.messages_received = input_yang_obj.messages_received
        
    if input_yang_obj.messages_sent._changed():
        input_yang_obj.messages_sent = input_yang_obj.messages_sent
        
    if input_yang_obj.notification._changed():
        input_yang_obj.notification = input_yang_obj.notification
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages(input_yang_obj: yc_messages_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/messages

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
    
    if input_yang_obj.in_total_messages._changed():
        input_yang_obj.in_total_messages = input_yang_obj.in_total_messages
        
    if input_yang_obj.out_total_messages._changed():
        input_yang_obj.out_total_messages = input_yang_obj.out_total_messages
        
    if input_yang_obj.in_update_elapsed_time._changed():
        input_yang_obj.in_update_elapsed_time = input_yang_obj.in_update_elapsed_time
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_sent(input_yang_obj.sent, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_received(input_yang_obj.received, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_queues(input_yang_obj: yc_queues_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_queues, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/queues

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
    
    if input_yang_obj.input._changed():
        input_yang_obj.input = input_yang_obj.input
        
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear_input(input_yang_obj: yc_input_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear_input, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear-statistics/clear/input

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
    
    if input_yang_obj.clear_at._changed():
        input_yang_obj.clear_at = input_yang_obj.clear_at
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear_output(input_yang_obj: yc_output_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear-statistics/clear/output

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
    
    if input_yang_obj.clear_finished_at._changed():
        input_yang_obj.clear_finished_at = input_yang_obj.clear_finished_at
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear(input_yang_obj: yc_clear_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics_clear, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear-statistics/clear

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
    
    if input_yang_obj.input._changed():
        input_yang_obj.input = input_yang_obj.input
        
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics(input_yang_obj: yc_clear_statistics_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear-statistics

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
    
    if input_yang_obj.clear._changed():
        input_yang_obj.clear = input_yang_obj.clear
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics(input_yang_obj: yc_statistics_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics

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
    
    if input_yang_obj.established_transitions._changed():
        input_yang_obj.established_transitions = input_yang_obj.established_transitions
        
    if input_yang_obj.fsm_established_transitions._changed():
        input_yang_obj.fsm_established_transitions = input_yang_obj.fsm_established_transitions
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages(input_yang_obj.messages, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_queues(input_yang_obj.queues, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_statistics(input_yang_obj.clear_statistics, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor(input_yang_obj: yc_neighbor_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor

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
    
    if input_yang_obj.local_address._changed():
        input_yang_obj.local_address = input_yang_obj.local_address
        
    if input_yang_obj.local_port._changed():
        input_yang_obj.local_port = input_yang_obj.local_port
        
    if input_yang_obj.peer_group._changed():
        input_yang_obj.peer_group = input_yang_obj.peer_group
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    if input_yang_obj.remote_port._changed():
        input_yang_obj.remote_port = input_yang_obj.remote_port
        
    if input_yang_obj.remote_as._changed():
        input_yang_obj.remote_as = input_yang_obj.remote_as
        
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.peer_as._changed():
        input_yang_obj.peer_as = input_yang_obj.peer_as
        
    if input_yang_obj.local_as._changed():
        input_yang_obj.local_as = input_yang_obj.local_as
        
    if input_yang_obj.peer_type._changed():
        input_yang_obj.peer_type = input_yang_obj.peer_type
        
    if input_yang_obj.auth_password._changed():
        input_yang_obj.auth_password = input_yang_obj.auth_password
        
    if input_yang_obj.remove_private_as._changed():
        input_yang_obj.remove_private_as = input_yang_obj.remove_private_as
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.session_state._changed():
        input_yang_obj.session_state = input_yang_obj.session_state
        
    if input_yang_obj.last_established._changed():
        input_yang_obj.last_established = input_yang_obj.last_established
        
    if input_yang_obj.supported_capabilities._changed():
        input_yang_obj.supported_capabilities = input_yang_obj.supported_capabilities
        
    if input_yang_obj.negotiated_hold_time._changed():
        input_yang_obj.negotiated_hold_time = input_yang_obj.negotiated_hold_time
        
    if input_yang_obj.last_error._changed():
        input_yang_obj.last_error = input_yang_obj.last_error
        
    if input_yang_obj.fsm_established_time._changed():
        input_yang_obj.fsm_established_time = input_yang_obj.fsm_established_time
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_timers(input_yang_obj.timers, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_transport(input_yang_obj.transport, translated_yang_obj)
        
    if input_yang_obj.erroneous_update_messages._changed():
        input_yang_obj.erroneous_update_messages = input_yang_obj.erroneous_update_messages
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_ebgp_multihop(input_yang_obj.ebgp_multihop, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_reflector(input_yang_obj.route_reflector, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_as_path_options(input_yang_obj.as_path_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_add_paths(input_yang_obj.add_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis(input_yang_obj.afi_safis, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics(input_yang_obj.statistics, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_established(input_yang_obj: yc_established_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_established, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/established

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
    
    if input_yang_obj.remote_address._changed():
        input_yang_obj.remote_address = input_yang_obj.remote_address
        
    if input_yang_obj.last_error._changed():
        input_yang_obj.last_error = input_yang_obj.last_error
        
    if input_yang_obj.session_state._changed():
        input_yang_obj.session_state = input_yang_obj.session_state
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_backward_transition(input_yang_obj: yc_backward_transition_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_backward_transition, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/backward-transition

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
    
    if input_yang_obj.remote_addr._changed():
        input_yang_obj.remote_addr = input_yang_obj.remote_addr
        
    if input_yang_obj.last_error._changed():
        input_yang_obj.last_error = input_yang_obj.last_error
        
    if input_yang_obj.session_state._changed():
        input_yang_obj.session_state = input_yang_obj.session_state
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear_input(input_yang_obj: yc_input_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear_input, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear-neighbors/clear/input

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
    
    if input_yang_obj.clear_at._changed():
        input_yang_obj.clear_at = input_yang_obj.clear_at
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear_output(input_yang_obj: yc_output_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear-neighbors/clear/output

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
    
    if input_yang_obj.clear_finished_at._changed():
        input_yang_obj.clear_finished_at = input_yang_obj.clear_finished_at
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear(input_yang_obj: yc_clear_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors_clear, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear-neighbors/clear

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
    
    if input_yang_obj.input._changed():
        input_yang_obj.input = input_yang_obj.input
        
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors(input_yang_obj: yc_clear_neighbors_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear-neighbors

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
    
    if input_yang_obj.clear._changed():
        input_yang_obj.clear = input_yang_obj.clear
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors(input_yang_obj: yc_neighbors_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors

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
    
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor(listInst, translated_yang_obj)
        
    if input_yang_obj.established._changed():
        input_yang_obj.established = input_yang_obj.established
        
    if input_yang_obj.backward_transition._changed():
        input_yang_obj.backward_transition = input_yang_obj.backward_transition
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_neighbors(input_yang_obj.clear_neighbors, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_timers(input_yang_obj: yc_timers_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_timers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/timers

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
    
    if input_yang_obj.connect_retry_interval._changed():
        input_yang_obj.connect_retry_interval = input_yang_obj.connect_retry_interval
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.keepalive_interval._changed():
        input_yang_obj.keepalive_interval = input_yang_obj.keepalive_interval
        
    if input_yang_obj.hold_time_configured._changed():
        input_yang_obj.hold_time_configured = input_yang_obj.hold_time_configured
        
    if input_yang_obj.keep_alive_configured._changed():
        input_yang_obj.keep_alive_configured = input_yang_obj.keep_alive_configured
        
    if input_yang_obj.min_as_origination_interval._changed():
        input_yang_obj.min_as_origination_interval = input_yang_obj.min_as_origination_interval
        
    if input_yang_obj.min_route_advertisement_interval._changed():
        input_yang_obj.min_route_advertisement_interval = input_yang_obj.min_route_advertisement_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_transport(input_yang_obj: yc_transport_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_transport, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/transport

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
    
    if input_yang_obj.tcp_mss._changed():
        input_yang_obj.tcp_mss = input_yang_obj.tcp_mss
        
    if input_yang_obj.mtu_discovery._changed():
        input_yang_obj.mtu_discovery = input_yang_obj.mtu_discovery
        
    if input_yang_obj.passive_mode._changed():
        input_yang_obj.passive_mode = input_yang_obj.passive_mode
        
    if input_yang_obj.local_address._changed():
        input_yang_obj.local_address = input_yang_obj.local_address
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.restart_time._changed():
        input_yang_obj.restart_time = input_yang_obj.restart_time
        
    if input_yang_obj.stale_routes_time._changed():
        input_yang_obj.stale_routes_time = input_yang_obj.stale_routes_time
        
    if input_yang_obj.helper_only._changed():
        input_yang_obj.helper_only = input_yang_obj.helper_only
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_ebgp_multihop(input_yang_obj: yc_ebgp_multihop_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_ebgp_multihop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/ebgp-multihop

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.multihop_ttl._changed():
        input_yang_obj.multihop_ttl = input_yang_obj.multihop_ttl
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_reflector(input_yang_obj: yc_route_reflector_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_reflector, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/route-reflector

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
    
    if input_yang_obj.route_reflector_cluster_id._changed():
        input_yang_obj.route_reflector_cluster_id = input_yang_obj.route_reflector_cluster_id
        
    if input_yang_obj.route_reflector_client._changed():
        input_yang_obj.route_reflector_client = input_yang_obj.route_reflector_client
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_as_path_options(input_yang_obj: yc_as_path_options_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_as_path_options, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/as-path-options

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
    
    if input_yang_obj.allow_own_as._changed():
        input_yang_obj.allow_own_as = input_yang_obj.allow_own_as
        
    if input_yang_obj.replace_peer_as._changed():
        input_yang_obj.replace_peer_as = input_yang_obj.replace_peer_as
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_add_paths(input_yang_obj: yc_add_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_add_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/add-paths

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
    
    if input_yang_obj.receive._changed():
        input_yang_obj.receive = input_yang_obj.receive
        
    if input_yang_obj.send_max._changed():
        input_yang_obj.send_max = input_yang_obj.send_max
        
    if input_yang_obj.eligible_prefix_policy._changed():
        input_yang_obj.eligible_prefix_policy = input_yang_obj.eligible_prefix_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ibgp(input_yang_obj: yc_ibgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ibgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/use-multiple-paths/ibgp

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
    
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ibgp(input_yang_obj.ibgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_graceful_restart(input_yang_obj: yc_graceful_restart_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_graceful_restart, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/graceful-restart

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_route_selection_options(input_yang_obj: yc_route_selection_options_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_route_selection_options, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/route-selection-options

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
    
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj: yc_ebgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ebgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/use-multiple-paths/ebgp

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
    
    if input_yang_obj.allow_multiple_as._changed():
        input_yang_obj.allow_multiple_as = input_yang_obj.allow_multiple_as
        
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj: yc_ibgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ibgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/use-multiple-paths/ibgp

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
    
    if input_yang_obj.maximum_paths._changed():
        input_yang_obj.maximum_paths = input_yang_obj.maximum_paths
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths(input_yang_obj: yc_use_multiple_paths_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/use-multiple-paths

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj.ebgp, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj.ibgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_apply_policy(input_yang_obj: yc_apply_policy_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_apply_policy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/apply-policy

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
    
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.default_import_policy._changed():
        input_yang_obj.default_import_policy = input_yang_obj.default_import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.default_export_policy._changed():
        input_yang_obj.default_export_policy = input_yang_obj.default_export_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast(input_yang_obj: yc_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast(input_yang_obj: yc_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    if input_yang_obj.send_default_route._changed():
        input_yang_obj.send_default_route = input_yang_obj.send_default_route
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv4-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj: yc_ipv4_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv4-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv6-labeled-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj: yc_ipv6_labeled_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/ipv6-labeled-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv4-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj: yc_l3vpn_ipv4_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv4-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv6-unicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj: yc_l3vpn_ipv6_unicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv6-unicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv4-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj: yc_l3vpn_ipv4_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv4-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv6-multicast/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj: yc_l3vpn_ipv6_multicast_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l3vpn-ipv6-multicast

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l2vpn-vpls/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj: yc_l2vpn_vpls_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l2vpn-vpls

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj: yc_prefix_limit_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn_prefix_limit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l2vpn-evpn/prefix-limit

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
    
    if input_yang_obj.max_prefixes._changed():
        input_yang_obj.max_prefixes = input_yang_obj.max_prefixes
        
    if input_yang_obj.shutdown_threshold_pct._changed():
        input_yang_obj.shutdown_threshold_pct = input_yang_obj.shutdown_threshold_pct
        
    if input_yang_obj.restart_timer._changed():
        input_yang_obj.restart_timer = input_yang_obj.restart_timer
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj: yc_l2vpn_evpn_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi/l2vpn-evpn

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj.prefix_limit, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi(input_yang_obj: yc_afi_safi_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis/afi-safi

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
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_route_selection_options(input_yang_obj.route_selection_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj.ipv4_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj.ipv6_labeled_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj.l3vpn_ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj.l3vpn_ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj.l3vpn_ipv4_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj.l3vpn_ipv6_multicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj.l2vpn_vpls, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj.l2vpn_evpn, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis(input_yang_obj: yc_afi_safis_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/afi-safis

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
    
    for k, listInst in input_yang_obj.afi_safi.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group(input_yang_obj: yc_peer_group_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group

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
    
    if input_yang_obj.peer_as._changed():
        input_yang_obj.peer_as = input_yang_obj.peer_as
        
    if input_yang_obj.local_as._changed():
        input_yang_obj.local_as = input_yang_obj.local_as
        
    if input_yang_obj.peer_type._changed():
        input_yang_obj.peer_type = input_yang_obj.peer_type
        
    if input_yang_obj.auth_password._changed():
        input_yang_obj.auth_password = input_yang_obj.auth_password
        
    if input_yang_obj.remove_private_as._changed():
        input_yang_obj.remove_private_as = input_yang_obj.remove_private_as
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.total_paths._changed():
        input_yang_obj.total_paths = input_yang_obj.total_paths
        
    if input_yang_obj.total_prefixes._changed():
        input_yang_obj.total_prefixes = input_yang_obj.total_prefixes
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_timers(input_yang_obj.timers, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_transport(input_yang_obj.transport, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_ebgp_multihop(input_yang_obj.ebgp_multihop, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_reflector(input_yang_obj.route_reflector, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_as_path_options(input_yang_obj.as_path_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_add_paths(input_yang_obj.add_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis(input_yang_obj.afi_safis, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups(input_yang_obj: yc_peer_groups_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups

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
    
    for k, listInst in input_yang_obj.peer_group.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface_bfd(input_yang_obj: yc_bfd_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface_bfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/interfaces/interface/bfd

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.local_multiplier._changed():
        input_yang_obj.local_multiplier = input_yang_obj.local_multiplier
        
    if input_yang_obj.desired_min_tx_interval._changed():
        input_yang_obj.desired_min_tx_interval = input_yang_obj.desired_min_tx_interval
        
    if input_yang_obj.required_min_rx_interval._changed():
        input_yang_obj.required_min_rx_interval = input_yang_obj.required_min_rx_interval
        
    if input_yang_obj.min_interval._changed():
        input_yang_obj.min_interval = input_yang_obj.min_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface(input_yang_obj: yc_interface_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/interfaces/interface

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface_bfd(input_yang_obj.bfd, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/interfaces

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
    
    for k, listInst in input_yang_obj.interface.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_aggregator(input_yang_obj: yc_aggregator_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_aggregator, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/aggregator

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
    
    if input_yang_obj.as_._changed():
        input_yang_obj.as_ = input_yang_obj.as_
        
    if input_yang_obj.as4._changed():
        input_yang_obj.as4 = input_yang_obj.as4
        
    if input_yang_obj.address._changed():
        input_yang_obj.address = input_yang_obj.address
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set(input_yang_obj: yc_attr_set_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set

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
    
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.atomic_aggregate._changed():
        input_yang_obj.atomic_aggregate = input_yang_obj.atomic_aggregate
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.med._changed():
        input_yang_obj.med = input_yang_obj.med
        
    if input_yang_obj.local_pref._changed():
        input_yang_obj.local_pref = input_yang_obj.local_pref
        
    if input_yang_obj.originator_id._changed():
        input_yang_obj.originator_id = input_yang_obj.originator_id
        
    if input_yang_obj.cluster_list._changed():
        input_yang_obj.cluster_list = input_yang_obj.cluster_list
        
    if input_yang_obj.aigp_metric._changed():
        input_yang_obj.aigp_metric = input_yang_obj.aigp_metric
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_aggregator(input_yang_obj.aggregator, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets(input_yang_obj: yc_attr_sets_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets

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
    
    for k, listInst in input_yang_obj.attr_set.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities_community(input_yang_obj: yc_community_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities_community, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/communities/community

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities(input_yang_obj: yc_communities_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/communities

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
    
    for k, listInst in input_yang_obj.community.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities_community(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities_ext_community(input_yang_obj: yc_ext_community_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities_ext_community, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/ext-communities/ext-community

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
    
    if input_yang_obj.ext_community._changed():
        input_yang_obj.ext_community = input_yang_obj.ext_community
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities(input_yang_obj: yc_ext_communities_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/ext-communities

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
    
    for k, listInst in input_yang_obj.ext_community.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities_ext_community(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi(input_yang_obj: yc_afi_safi_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi

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
    
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis(input_yang_obj: yc_afi_safis_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis

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
    
    for k, listInst in input_yang_obj.afi_safi.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib(input_yang_obj: yc_rib_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets(input_yang_obj.attr_sets, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities(input_yang_obj.communities, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities(input_yang_obj.ext_communities, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis(input_yang_obj.afi_safis, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp(input_yang_obj: yc_bgp_ietf_routing__routing_control_plane_protocols_control_plane_protocol_bgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp

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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global(input_yang_obj.global_, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors(input_yang_obj.neighbors, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups(input_yang_obj.peer_groups, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib(input_yang_obj.rib, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol(input_yang_obj: yc_control_plane_protocol_ietf_routing__routing_control_plane_protocols_control_plane_protocol, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol

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

    if hasattr(translated_yang_obj, "isiscomm"):
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_isis(input_yang_obj.isis, translated_yang_obj)
    elif hasattr(translated_yang_obj, "bgp"):
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp(input_yang_obj.bgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols(input_yang_obj: yc_control_plane_protocols_ietf_routing__routing_control_plane_protocols, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols

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
    global ISIS, BGP
    for k, listInst in input_yang_obj.control_plane_protocol.iteritems():
        type = k.split(" ")[0]
        if type == "isis" and hasattr(translated_yang_obj, "isiscomm"):
            ISIS = "true"
            innerobj = _translate__routing_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)
        elif type == "bgp" and hasattr(translated_yang_obj, "bgp"):
            BGP = "true"
            innerobj = _translate__routing_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)

    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_ribs_rib_routes_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_routes_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route(input_yang_obj: yc_route_ietf_routing__routing_ribs_rib_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route

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
    
    if input_yang_obj.route_preference._changed():
        input_yang_obj.route_preference = input_yang_obj.route_preference
        
    innerobj = _translate__routing_ribs_rib_routes_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    if input_yang_obj.metric._changed():
        input_yang_obj.metric = input_yang_obj.metric
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.route_type._changed():
        input_yang_obj.route_type = input_yang_obj.route_type
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes(input_yang_obj: yc_routes_ietf_routing__routing_ribs_rib_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_ribs_rib_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route(input_yang_obj: yc_route_ietf_routing__routing_ribs_rib_active_route_output_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route

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
    
    innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output(input_yang_obj: yc_output_ietf_routing__routing_ribs_rib_active_route_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output

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
    
    innerobj = _translate__routing_ribs_rib_active_route_output_route(input_yang_obj.route, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route(input_yang_obj: yc_active_route_ietf_routing__routing_ribs_rib_active_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route

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
    
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_ribs_rib(input_yang_obj: yc_rib_ietf_routing__routing_ribs_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib

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
    
    if input_yang_obj.address_family._changed():
        input_yang_obj.address_family = input_yang_obj.address_family
        
    if input_yang_obj.default_rib._changed():
        input_yang_obj.default_rib = input_yang_obj.default_rib
        
    innerobj = _translate__routing_ribs_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    if input_yang_obj.active_route._changed():
        input_yang_obj.active_route = input_yang_obj.active_route
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    return translated_yang_obj

def _translate__routing_ribs(input_yang_obj: yc_ribs_ietf_routing__routing_ribs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs

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
    
    for k, listInst in input_yang_obj.rib.iteritems():
        innerobj = _translate__routing_ribs_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_encapsulation(input_yang_obj: yc_encapsulation_ietf_routing__routing_srv6_encapsulation, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/encapsulation

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
    
    if input_yang_obj.source_address._changed():
        translated_yang_obj.segripv6.srv6Site.encapSource.encapSrcAddr = input_yang_obj.source_address
        
    if input_yang_obj.ip_ttl_propagation._changed():
        translated_yang_obj.segripv6.srv6Site.encapSource.encapSrcAddrTTL = input_yang_obj.ip_ttl_propagation
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_prefix(input_yang_obj: yc_prefix_ietf_routing__routing_srv6_locators_locator_prefix, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/prefix

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
    
    if input_yang_obj.address._changed():
        translated_yang_obj.ipv6Prefix = input_yang_obj.address
        
    if input_yang_obj.length._changed():
        translated_yang_obj.maskLength = input_yang_obj.length
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_t(input_yang_obj: yc_end_t_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_t, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-t

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
    
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_t_psp(input_yang_obj: yc_end_t_psp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_t_psp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-t_psp

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
    
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_t_usp(input_yang_obj: yc_end_t_usp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_t_usp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-t_usp

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
    
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_t_psp_usp(input_yang_obj: yc_end_t_psp_usp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_t_psp_usp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-t_psp_usp

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
    
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x(input_yang_obj: yc_end_x_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x

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
    
    if input_yang_obj.protected._changed():
        input_yang_obj.protected = input_yang_obj.protected
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp(input_yang_obj: yc_end_x_psp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp

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
    
    if input_yang_obj.protected._changed():
        input_yang_obj.protected = input_yang_obj.protected
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_usp/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_usp/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_usp/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_usp/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp(input_yang_obj: yc_end_x_usp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_usp

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
    
    if input_yang_obj.protected._changed():
        input_yang_obj.protected = input_yang_obj.protected
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_usp_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp_usp/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp_usp/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp_usp/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp_usp/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp(input_yang_obj: yc_end_x_psp_usp_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-x_psp_usp

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
    
    if input_yang_obj.protected._changed():
        input_yang_obj.protected = input_yang_obj.protected
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_x_psp_usp_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6(input_yang_obj: yc_end_b6_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6

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
    
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6-encaps/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6-encaps/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6-encaps/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6-encaps/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps(input_yang_obj: yc_end_b6_encaps_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-b6-encaps

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
    
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    if input_yang_obj.source_address._changed():
        input_yang_obj.source_address = input_yang_obj.source_address
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_b6_encaps_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap_out_label(input_yang_obj: yc_out_label_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap_out_label, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-bm/paths/path/encap/out-label

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-bm/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_label.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap_out_label(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-bm/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-bm/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm(input_yang_obj: yc_end_bm_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_bm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-bm

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
    
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_bm_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx6/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx6/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx6/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx6/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6(input_yang_obj: yc_end_dx6_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx6

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
    
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx6_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx4/paths/path/encap/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap(input_yang_obj: yc_encap_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx4/paths/path/encap

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
    
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap_out_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx4/paths/path

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path_encap(input_yang_obj.encap, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx4/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4(input_yang_obj: yc_end_dx4_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx4

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
    
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx4_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dt6(input_yang_obj: yc_end_dt6_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dt6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dt6

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
    
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dt4(input_yang_obj: yc_end_dt4_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dt4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dt4

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
    
    if input_yang_obj.lookup_table_ipv4._changed():
        translated_yang_obj.vpnName = input_yang_obj.lookup_table_ipv4
        translated_yang_obj.protocolType = "End.DT4"
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dt46(input_yang_obj: yc_end_dt46_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dt46, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dt46

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
    
    if input_yang_obj.lookup_table_ipv4._changed():
        input_yang_obj.lookup_table_ipv4 = input_yang_obj.lookup_table_ipv4
        
    if input_yang_obj.lookup_table_ipv6._changed():
        input_yang_obj.lookup_table_ipv6 = input_yang_obj.lookup_table_ipv6
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx2_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx2_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx2/paths

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx2(input_yang_obj: yc_end_dx2_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid_end_dx2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid/end-dx2

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
    
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dx2_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids_sid(input_yang_obj: yc_sid_ietf_routing__routing_srv6_locators_locator_static_local_sids_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids/sid

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
    
    if input_yang_obj.end_behavior_type._changed():
        input_yang_obj.end_behavior_type = input_yang_obj.end_behavior_type

    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dt6(input_yang_obj.end_dt6, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid_end_dt4(input_yang_obj.end_dt4, translated_yang_obj)


    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_srv6_locators_locator_static_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static/local-sids

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
    
    for k, listInst in input_yang_obj.sid.iteritems():
        k = dec2ipv6(k)
        if listInst.end_behavior_type._changed() and listInst.end_behavior_type == "End":
            endOpcode_obj = translated_yang_obj.srv6Opcodes.endOpcodes.endOpcode.add(k)
            endOpcode_obj.flavor = "true"
        else:
            endDt4Opcodes_obj = translated_yang_obj.srv6Opcodes.endDt4Opcodes.endDt4Opcode.add(k)
            innerobj = _translate__routing_srv6_locators_locator_static_local_sids_sid(listInst, endDt4Opcodes_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator_static(input_yang_obj: yc_static_ietf_routing__routing_srv6_locators_locator_static, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator/static

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
    
    innerobj = _translate__routing_srv6_locators_locator_static_local_sids(input_yang_obj.local_sids, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators_locator(input_yang_obj: yc_locator_ietf_routing__routing_srv6_locators_locator, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators/locator

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
    
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.is_default._changed():
        translated_yang_obj.defaultFlag = input_yang_obj.is_default
        
    innerobj = _translate__routing_srv6_locators_locator_prefix(input_yang_obj.prefix, translated_yang_obj)
        
    if input_yang_obj.operational_status._changed():
        input_yang_obj.operational_status = input_yang_obj.operational_status
        
    if input_yang_obj.is_in_address_conflict._changed():
        input_yang_obj.is_in_address_conflict = input_yang_obj.is_in_address_conflict
        
    innerobj = _translate__routing_srv6_locators_locator_static(input_yang_obj.static, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_locators(input_yang_obj: yc_locators_ietf_routing__routing_srv6_locators, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/locators

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
    global SEGRIPV6
    for k, listInst in input_yang_obj.locator.iteritems():
        SEGRIPV6 = "true"
        srv6Locator_obj = translated_yang_obj.segripv6.srv6Locators.srv6Locator.add(k)
        innerobj = _translate__routing_srv6_locators_locator(listInst, srv6Locator_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities_end_behavior(input_yang_obj: yc_end_behavior_ietf_routing__routing_srv6_node_capabilities_end_behavior, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities/end-behavior

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
    
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities_transit_behavior(input_yang_obj: yc_transit_behavior_ietf_routing__routing_srv6_node_capabilities_transit_behavior, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities/transit-behavior

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
    
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities_signaled_parameters(input_yang_obj: yc_signaled_parameters_ietf_routing__routing_srv6_node_capabilities_signaled_parameters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities/signaled-parameters

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
    
    if input_yang_obj.max_sl._changed():
        input_yang_obj.max_sl = input_yang_obj.max_sl
        
    if input_yang_obj.max_end_pop_srh._changed():
        input_yang_obj.max_end_pop_srh = input_yang_obj.max_end_pop_srh
        
    if input_yang_obj.max_t_insert._changed():
        input_yang_obj.max_t_insert = input_yang_obj.max_t_insert
        
    if input_yang_obj.max_t_encap._changed():
        input_yang_obj.max_t_encap = input_yang_obj.max_t_encap
        
    if input_yang_obj.max_end_d._changed():
        input_yang_obj.max_end_d = input_yang_obj.max_end_d
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities_security_rule(input_yang_obj: yc_security_rule_ietf_routing__routing_srv6_node_capabilities_security_rule, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities/security-rule

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
    
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities_counters(input_yang_obj: yc_counters_ietf_routing__routing_srv6_node_capabilities_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities/counters

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
    
    if input_yang_obj.supported._changed():
        input_yang_obj.supported = input_yang_obj.supported
        
    return translated_yang_obj

def _translate__routing_srv6_node_capabilities(input_yang_obj: yc_node_capabilities_ietf_routing__routing_srv6_node_capabilities, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/node-capabilities

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
    
    for k, listInst in input_yang_obj.end_behavior.iteritems():
        innerobj = _translate__routing_srv6_node_capabilities_end_behavior(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.transit_behavior.iteritems():
        innerobj = _translate__routing_srv6_node_capabilities_transit_behavior(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_node_capabilities_signaled_parameters(input_yang_obj.signaled_parameters, translated_yang_obj)
        
    for k, listInst in input_yang_obj.security_rule.iteritems():
        innerobj = _translate__routing_srv6_node_capabilities_security_rule(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.counters.iteritems():
        innerobj = _translate__routing_srv6_node_capabilities_counters(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_counters_cnt3(input_yang_obj: yc_cnt3_ietf_routing__routing_srv6_local_sids_counters_cnt3, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/counters/cnt3

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
    
    if input_yang_obj.in_pkts._changed():
        input_yang_obj.in_pkts = input_yang_obj.in_pkts
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_counters(input_yang_obj: yc_counters_ietf_routing__routing_srv6_local_sids_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/counters

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
    
    innerobj = _translate__routing_srv6_local_sids_counters_cnt3(input_yang_obj.cnt3, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_owner(input_yang_obj: yc_owner_ietf_routing__routing_srv6_local_sids_local_sid_owner, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/owner

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
    
    if input_yang_obj.is_winner._changed():
        input_yang_obj.is_winner = input_yang_obj.is_winner
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_l2(input_yang_obj: yc_l2_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths_path_l2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths/path/l2

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_l3(input_yang_obj: yc_l3_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths_path_l3, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths/path/l3

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    if input_yang_obj.next_hop._changed():
        input_yang_obj.next_hop = input_yang_obj.next_hop
        
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.backup_path_index._changed():
        input_yang_obj.backup_path_index = input_yang_obj.backup_path_index
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_sid(input_yang_obj: yc_out_sid_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths/path/out-sid

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
    
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_label(input_yang_obj: yc_out_label_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_label, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths/path/out-label

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
    
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path(input_yang_obj: yc_path_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths_path, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths/path

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
    
    innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_l2(input_yang_obj.l2, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_l3(input_yang_obj.l3, translated_yang_obj)
        
    for k, listInst in input_yang_obj.out_sid.iteritems():
        innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_sid(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.out_label.iteritems():
        innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path_out_label(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding_paths(input_yang_obj: yc_paths_ietf_routing__routing_srv6_local_sids_local_sid_forwarding_paths, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding/paths

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
    
    for k, listInst in input_yang_obj.path.iteritems():
        innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths_path(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_forwarding(input_yang_obj: yc_forwarding_ietf_routing__routing_srv6_local_sids_local_sid_forwarding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/forwarding

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
    
    if input_yang_obj.is_installed._changed():
        input_yang_obj.is_installed = input_yang_obj.is_installed
        
    if input_yang_obj.next_hop_type._changed():
        input_yang_obj.next_hop_type = input_yang_obj.next_hop_type
        
    innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding_paths(input_yang_obj.paths, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_counters_cnt1(input_yang_obj: yc_cnt1_ietf_routing__routing_srv6_local_sids_local_sid_counters_cnt1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/counters/cnt1

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
    
    if input_yang_obj.in_pkts._changed():
        input_yang_obj.in_pkts = input_yang_obj.in_pkts
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid_counters(input_yang_obj: yc_counters_ietf_routing__routing_srv6_local_sids_local_sid_counters, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid/counters

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
    
    innerobj = _translate__routing_srv6_local_sids_local_sid_counters_cnt1(input_yang_obj.cnt1, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids_local_sid(input_yang_obj: yc_local_sid_ietf_routing__routing_srv6_local_sids_local_sid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids/local-sid

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
    
    if input_yang_obj.locator_ref._changed():
        input_yang_obj.locator_ref = input_yang_obj.locator_ref
        
    if input_yang_obj.is_reserved._changed():
        input_yang_obj.is_reserved = input_yang_obj.is_reserved
        
    if input_yang_obj.end_behavior_type._changed():
        input_yang_obj.end_behavior_type = input_yang_obj.end_behavior_type
        
    if input_yang_obj.alloc_type._changed():
        input_yang_obj.alloc_type = input_yang_obj.alloc_type
        
    for k, listInst in input_yang_obj.owner.iteritems():
        innerobj = _translate__routing_srv6_local_sids_local_sid_owner(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_local_sids_local_sid_forwarding(input_yang_obj.forwarding, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_local_sids_local_sid_counters(input_yang_obj.counters, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6_local_sids(input_yang_obj: yc_local_sids_ietf_routing__routing_srv6_local_sids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6/local-sids

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
    
    innerobj = _translate__routing_srv6_local_sids_counters(input_yang_obj.counters, translated_yang_obj)
        
    for k, listInst in input_yang_obj.local_sid.iteritems():
        innerobj = _translate__routing_srv6_local_sids_local_sid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_srv6(input_yang_obj: yc_srv6_ietf_routing__routing_srv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/srv6

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
    global SEGRIPV6
    if input_yang_obj.enable._changed():
        SEGRIPV6 = "true"
        translated_yang_obj.segripv6.srv6Site.srv6Enable = input_yang_obj.enable
        
    innerobj = _translate__routing_srv6_encapsulation(input_yang_obj.encapsulation, translated_yang_obj)
        
    innerobj = _translate__routing_srv6_locators(input_yang_obj.locators, translated_yang_obj)

    return translated_yang_obj

def _translate__routing(input_yang_obj: yc_routing_ietf_routing__routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing

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
    
    if input_yang_obj.router_id._changed():
        input_yang_obj.router_id = input_yang_obj.router_id

    if hasattr(translated_yang_obj, "segripv6"):
        innerobj = _translate__routing_srv6(input_yang_obj.srv6, translated_yang_obj)
    else:
        innerobj = _translate__routing_control_plane_protocols(input_yang_obj.control_plane_protocols, translated_yang_obj)

    return translated_yang_obj

def _translate__routing_state_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_state_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/interfaces

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_state_control_plane_protocols_control_plane_protocol(input_yang_obj: yc_control_plane_protocol_ietf_routing__routing_state_control_plane_protocols_control_plane_protocol, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/control-plane-protocols/control-plane-protocol

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
    
    return translated_yang_obj

def _translate__routing_state_control_plane_protocols(input_yang_obj: yc_control_plane_protocols_ietf_routing__routing_state_control_plane_protocols, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/control-plane-protocols

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
    
    for k, listInst in input_yang_obj.control_plane_protocol.iteritems():
        innerobj = _translate__routing_state_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_state_ribs_rib_routes_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_routes_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route(input_yang_obj: yc_route_ietf_routing__routing_state_ribs_rib_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route

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
    
    if input_yang_obj.route_preference._changed():
        input_yang_obj.route_preference = input_yang_obj.route_preference
        
    innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes(input_yang_obj: yc_routes_ietf_routing__routing_state_ribs_rib_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_state_ribs_rib_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route(input_yang_obj: yc_route_ietf_routing__routing_state_ribs_rib_active_route_output_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route

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
    
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output(input_yang_obj: yc_output_ietf_routing__routing_state_ribs_rib_active_route_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output

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
    
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route(input_yang_obj.route, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route(input_yang_obj: yc_active_route_ietf_routing__routing_state_ribs_rib_active_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route

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
    
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib(input_yang_obj: yc_rib_ietf_routing__routing_state_ribs_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib

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
    
    if input_yang_obj.address_family._changed():
        input_yang_obj.address_family = input_yang_obj.address_family
        
    if input_yang_obj.default_rib._changed():
        input_yang_obj.default_rib = input_yang_obj.default_rib
        
    innerobj = _translate__routing_state_ribs_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    if input_yang_obj.active_route._changed():
        input_yang_obj.active_route = input_yang_obj.active_route
        
    return translated_yang_obj

def _translate__routing_state_ribs(input_yang_obj: yc_ribs_ietf_routing__routing_state_ribs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs

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
    
    for k, listInst in input_yang_obj.rib.iteritems():
        innerobj = _translate__routing_state_ribs_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state(input_yang_obj: yc_routing_state_ietf_routing__routing_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state

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
    
    if input_yang_obj.router_id._changed():
        input_yang_obj.router_id = input_yang_obj.router_id
        
    innerobj = _translate__routing_state_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__routing_state_control_plane_protocols(input_yang_obj.control_plane_protocols, translated_yang_obj)
        
    innerobj = _translate__routing_state_ribs(input_yang_obj.ribs, translated_yang_obj)
        
    return translated_yang_obj

ISIS = None
BGP = None
SEGRIPV6 = None
def _translate__ietf_routing(input_yang_obj: ietf_routing, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-routing

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
    print("ietf 105 routing translation script!")

    trans_yang_list = []
    global ISIS, BGP, SEGRIPV6

    # huawei_isiscomm
    print("enter huawei isiscomm script")
    translated_yang_obj_isiscomm = huawei_isiscomm()
    _translate__routing(input_yang_obj.routing, translated_yang_obj_isiscomm)
    xpath = "/a:isiscomm"
    ns_map = {"a": "http://www.huawei.com/netconf/vrp/huawei-isiscomm"}
    target_xpath = XPATH(xpath, ns_map)
    if ISIS == "true":
        ISIS = "false"
        trans_yang_list.append([translated_yang_obj_isiscomm.isiscomm, target_xpath])

    # huawei_bgp
    print("enter huawei bgp script")
    translated_yang_obj_bgp = huawei_bgp()
    _translate__routing(input_yang_obj.routing, translated_yang_obj_bgp)
    xpath = "/a:bgp"
    ns_map = {"a": "http://www.huawei.com/netconf/vrp/huawei-bgp"}
    target_xpath = XPATH(xpath, ns_map)
    if BGP == "true":
        BGP = "false"
        trans_yang_list.append([translated_yang_obj_bgp.bgp, target_xpath])

    # huawei-segripv6
    print("enter huawei segripv6 script")
    translated_yang_obj_segripv6 = huawei_segripv6()
    _translate__routing(input_yang_obj.routing, translated_yang_obj_segripv6)
    xpath = "/a:segripv6"
    ns_map = {"a": "http://www.huawei.com/netconf/vrp/huawei-segripv6"}
    target_xpath = XPATH(xpath, ns_map)
    if SEGRIPV6 == "true":
        SEGRIPV6 = "false"
        trans_yang_list.append([translated_yang_obj_segripv6.segripv6, target_xpath])

    return trans_yang_list
