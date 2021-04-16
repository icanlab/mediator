from swagger_server.yang_bindings.target_yang_bindings.huawei_ifm_binding import *
from swagger_server.yang_bindings.src_yang_bindings.ietf_interfaces_binding import *
from netaddr import IPAddress

def _translate__ifm_interfaces_interface_ipv4_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv4_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mask._changed():
        translated_yang_obj.prefix_length = IPAddress(input_yang_obj.mask).netmask_bits()
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv4_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        translated_yang_obj.ipv4.address.add(name=k)
        innerobj = _translate__ifm_interfaces_interface_ipv4_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_unnumbered_address(input_yang_obj: yc_unnumbered_address_huawei_ifm__ifm_interfaces_interface_ipv4_unnumbered_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/unnumbered-address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.unnumbered_if_name._changed():
        input_yang_obj.unnumbered_if_name = input_yang_obj.unnumbered_if_name
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_negotiation_address(input_yang_obj: yc_negotiation_address_huawei_ifm__ifm_interfaces_interface_ipv4_negotiation_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/negotiation-address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.negotiation_type._changed():
        input_yang_obj.negotiation_type = input_yang_obj.negotiation_type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv4_state_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mask._changed():
        input_yang_obj.mask = input_yang_obj.mask
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.is_block._changed():
        input_yang_obj.is_block = input_yang_obj.is_block
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv4_state_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv4_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_gateways_gateway(input_yang_obj: yc_gateway_huawei_ifm__ifm_interfaces_interface_ipv4_state_gateways_gateway, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/gateways/gateway

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__ifm_interfaces_interface_ipv4_state_gateways(input_yang_obj: yc_gateways_huawei_ifm__ifm_interfaces_interface_ipv4_state_gateways, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/gateways

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.gateway.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv4_state_gateways_gateway(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state(input_yang_obj: yc_state_huawei_ifm__ifm_interfaces_interface_ipv4_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces_interface_ipv4_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_state_gateways(input_yang_obj.gateways, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4(input_yang_obj: yc_ipv4_huawei_ifm__ifm_interfaces_interface_ipv4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces_interface_ipv4_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_unnumbered_address(input_yang_obj.unnumbered_address, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_negotiation_address(input_yang_obj.negotiation_address, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_state(input_yang_obj.state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv6_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.algorithm_type._changed():
        input_yang_obj.algorithm_type = input_yang_obj.algorithm_type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv6_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix(input_yang_obj: yc_nd_prefix_huawei_ifm__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/nd-prefixs/nd-prefix

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.valid_lifetime._changed():
        input_yang_obj.valid_lifetime = input_yang_obj.valid_lifetime
        
    if input_yang_obj.preferred_lifetime._changed():
        input_yang_obj.preferred_lifetime = input_yang_obj.preferred_lifetime
        
    if input_yang_obj.auto_flag._changed():
        input_yang_obj.auto_flag = input_yang_obj.auto_flag
        
    if input_yang_obj.on_link_flag._changed():
        input_yang_obj.on_link_flag = input_yang_obj.on_link_flag
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_nd_prefixs(input_yang_obj: yc_nd_prefixs_huawei_ifm__ifm_interfaces_interface_ipv6_nd_prefixs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/nd-prefixs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.nd_prefix.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv6_state_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.algorithm_type._changed():
        input_yang_obj.algorithm_type = input_yang_obj.algorithm_type
        
    if input_yang_obj.collision_count._changed():
        input_yang_obj.collision_count = input_yang_obj.collision_count
        
    if input_yang_obj.is_block._changed():
        input_yang_obj.is_block = input_yang_obj.is_block
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv6_state_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state(input_yang_obj: yc_state_huawei_ifm__ifm_interfaces_interface_ipv6_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mtu6._changed():
        input_yang_obj.mtu6 = input_yang_obj.mtu6
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6(input_yang_obj: yc_ipv6_huawei_ifm__ifm_interfaces_interface_ipv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mtu6._changed():
        input_yang_obj.mtu6 = input_yang_obj.mtu6
        
    if input_yang_obj.spread_mtu_flag._changed():
        input_yang_obj.spread_mtu_flag = input_yang_obj.spread_mtu_flag
        
    if input_yang_obj.auto_link_local._changed():
        input_yang_obj.auto_link_local = input_yang_obj.auto_link_local
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_nd_prefixs(input_yang_obj.nd_prefixs, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_state(input_yang_obj.state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface(input_yang_obj: yc_interface_huawei_ifm__ifm_interfaces_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vrf_name._changed():
        input_yang_obj.vrf_name = input_yang_obj.vrf_name
        
    innerobj = _translate__ifm_interfaces_interface_ipv4(input_yang_obj.ipv4, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv6(input_yang_obj.ipv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces(input_yang_obj: yc_interfaces_huawei_ifm__ifm_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__ifm_interfaces_interface(listInst, innerobj)
        
    return translated_yang_obj

def _translate__ifm(input_yang_obj: yc_ifm_huawei_ifm__ifm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ifm(input_yang_obj: huawei_ifm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ifm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm(input_yang_obj.ifm, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv4_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mask._changed():
        translated_yang_obj.prefix_length = 32
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv4_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        address_obj = translated_yang_obj.ipv4.address.add(ip=k)
        innerobj = _translate__ifm_interfaces_interface_ipv4_addresses_address(listInst, address_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_unnumbered_address(input_yang_obj: yc_unnumbered_address_huawei_ifm__ifm_interfaces_interface_ipv4_unnumbered_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/unnumbered-address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.unnumbered_if_name._changed():
        input_yang_obj.unnumbered_if_name = input_yang_obj.unnumbered_if_name
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_negotiation_address(input_yang_obj: yc_negotiation_address_huawei_ifm__ifm_interfaces_interface_ipv4_negotiation_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/negotiation-address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.negotiation_type._changed():
        input_yang_obj.negotiation_type = input_yang_obj.negotiation_type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv4_state_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mask._changed():
        input_yang_obj.mask = input_yang_obj.mask
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.is_block._changed():
        input_yang_obj.is_block = input_yang_obj.is_block
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv4_state_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv4_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state_gateways_gateway(input_yang_obj: yc_gateway_huawei_ifm__ifm_interfaces_interface_ipv4_state_gateways_gateway, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/gateways/gateway

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__ifm_interfaces_interface_ipv4_state_gateways(input_yang_obj: yc_gateways_huawei_ifm__ifm_interfaces_interface_ipv4_state_gateways, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state/gateways

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.gateway.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv4_state_gateways_gateway(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4_state(input_yang_obj: yc_state_huawei_ifm__ifm_interfaces_interface_ipv4_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces_interface_ipv4_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_state_gateways(input_yang_obj.gateways, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv4(input_yang_obj: yc_ipv4_huawei_ifm__ifm_interfaces_interface_ipv4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces_interface_ipv4_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_unnumbered_address(input_yang_obj.unnumbered_address, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_negotiation_address(input_yang_obj.negotiation_address, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv4_state(input_yang_obj.state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv6_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.algorithm_type._changed():
        input_yang_obj.algorithm_type = input_yang_obj.algorithm_type
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv6_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix(input_yang_obj: yc_nd_prefix_huawei_ifm__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/nd-prefixs/nd-prefix

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_len._changed():
        input_yang_obj.prefix_len = input_yang_obj.prefix_len
        
    if input_yang_obj.valid_lifetime._changed():
        input_yang_obj.valid_lifetime = input_yang_obj.valid_lifetime
        
    if input_yang_obj.preferred_lifetime._changed():
        input_yang_obj.preferred_lifetime = input_yang_obj.preferred_lifetime
        
    if input_yang_obj.auto_flag._changed():
        input_yang_obj.auto_flag = input_yang_obj.auto_flag
        
    if input_yang_obj.on_link_flag._changed():
        input_yang_obj.on_link_flag = input_yang_obj.on_link_flag
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_nd_prefixs(input_yang_obj: yc_nd_prefixs_huawei_ifm__ifm_interfaces_interface_ipv6_nd_prefixs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/nd-prefixs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.nd_prefix.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_nd_prefixs_nd_prefix(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state_addresses_address(input_yang_obj: yc_address_huawei_ifm__ifm_interfaces_interface_ipv6_state_addresses_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.algorithm_type._changed():
        input_yang_obj.algorithm_type = input_yang_obj.algorithm_type
        
    if input_yang_obj.collision_count._changed():
        input_yang_obj.collision_count = input_yang_obj.collision_count
        
    if input_yang_obj.is_block._changed():
        input_yang_obj.is_block = input_yang_obj.is_block
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state_addresses(input_yang_obj: yc_addresses_huawei_ifm__ifm_interfaces_interface_ipv6_state_addresses, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__ifm_interfaces_interface_ipv6_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6_state(input_yang_obj: yc_state_huawei_ifm__ifm_interfaces_interface_ipv6_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mtu6._changed():
        input_yang_obj.mtu6 = input_yang_obj.mtu6
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_ipv6(input_yang_obj: yc_ipv6_huawei_ifm__ifm_interfaces_interface_ipv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mtu6._changed():
        input_yang_obj.mtu6 = input_yang_obj.mtu6
        
    if input_yang_obj.spread_mtu_flag._changed():
        input_yang_obj.spread_mtu_flag = input_yang_obj.spread_mtu_flag
        
    if input_yang_obj.auto_link_local._changed():
        input_yang_obj.auto_link_local = input_yang_obj.auto_link_local
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_nd_prefixs(input_yang_obj.nd_prefixs, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_ipv6_state(input_yang_obj.state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface(input_yang_obj: yc_interface_huawei_ifm__ifm_interfaces_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vrf_name._changed():
        input_yang_obj.vrf_name = input_yang_obj.vrf_name
        
    innerobj = _translate__ifm_interfaces_interface_ipv4(input_yang_obj.ipv4, translated_yang_obj)
        
    # innerobj = _translate__ifm_interfaces_interface_ipv6(input_yang_obj.ipv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces(input_yang_obj: yc_interfaces_huawei_ifm__ifm_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        interface_obj = translated_yang_obj.interfaces.interface.add(name=k)
        innerobj = _translate__ifm_interfaces_interface(listInst, interface_obj)
        
    return translated_yang_obj

def _translate__ifm(input_yang_obj: yc_ifm_huawei_ifm__ifm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ifm_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ifm(input_yang_obj: huawei_ifm, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ifm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj = ietf_interfaces()
    target_xpath = '/a:interfaces'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-interfaces'}
    innerobj = _translate__ifm(input_yang_obj.ifm, translated_yang_obj)
        
    return translated_yang_obj.interfaces, target_xpath, ns_map
