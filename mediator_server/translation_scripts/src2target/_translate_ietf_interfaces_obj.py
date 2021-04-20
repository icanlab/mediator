from mediator_server.yang_bindings.target_yang_bindings.huawei_ifm_binding import *

def exchange_maskint(mask_int):
  bin_arr = ['0' for i in range(32)]
  for i in range(mask_int):
    bin_arr[i] = '1'
  tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
  tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
  return '.'.join(tmpmask)

def _translate__interfaces_interface_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.discontinuity_time._changed():
        input_yang_obj.discontinuity_time = input_yang_obj.discontinuity_time
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    if input_yang_obj.in_unicast_pkts._changed():
        input_yang_obj.in_unicast_pkts = input_yang_obj.in_unicast_pkts
        
    if input_yang_obj.in_broadcast_pkts._changed():
        input_yang_obj.in_broadcast_pkts = input_yang_obj.in_broadcast_pkts
        
    if input_yang_obj.in_multicast_pkts._changed():
        input_yang_obj.in_multicast_pkts = input_yang_obj.in_multicast_pkts
        
    if input_yang_obj.in_discards._changed():
        input_yang_obj.in_discards = input_yang_obj.in_discards
        
    if input_yang_obj.in_errors._changed():
        input_yang_obj.in_errors = input_yang_obj.in_errors
        
    if input_yang_obj.in_unknown_protos._changed():
        input_yang_obj.in_unknown_protos = input_yang_obj.in_unknown_protos
        
    if input_yang_obj.out_octets._changed():
        input_yang_obj.out_octets = input_yang_obj.out_octets
        
    if input_yang_obj.out_unicast_pkts._changed():
        input_yang_obj.out_unicast_pkts = input_yang_obj.out_unicast_pkts
        
    if input_yang_obj.out_broadcast_pkts._changed():
        input_yang_obj.out_broadcast_pkts = input_yang_obj.out_broadcast_pkts
        
    if input_yang_obj.out_multicast_pkts._changed():
        input_yang_obj.out_multicast_pkts = input_yang_obj.out_multicast_pkts
        
    if input_yang_obj.out_discards._changed():
        input_yang_obj.out_discards = input_yang_obj.out_discards
        
    if input_yang_obj.out_errors._changed():
        input_yang_obj.out_errors = input_yang_obj.out_errors
        
    return translated_yang_obj

def _translate__interfaces_interface_carrier_delay(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/carrier-delay

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.down._changed():
        input_yang_obj.down = input_yang_obj.down
        
    if input_yang_obj.up._changed():
        input_yang_obj.up = input_yang_obj.up
        
    if input_yang_obj.carrier_transitions._changed():
        input_yang_obj.carrier_transitions = input_yang_obj.carrier_transitions
        
    if input_yang_obj.timer_running._changed():
        input_yang_obj.timer_running = input_yang_obj.timer_running
        
    return translated_yang_obj

def _translate__interfaces_interface_dampening(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/dampening

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.half_life._changed():
        input_yang_obj.half_life = input_yang_obj.half_life
        
    if input_yang_obj.reuse._changed():
        input_yang_obj.reuse = input_yang_obj.reuse
        
    if input_yang_obj.suppress._changed():
        input_yang_obj.suppress = input_yang_obj.suppress
        
    if input_yang_obj.max_suppress_time._changed():
        input_yang_obj.max_suppress_time = input_yang_obj.max_suppress_time
        
    if input_yang_obj.penalty._changed():
        input_yang_obj.penalty = input_yang_obj.penalty
        
    if input_yang_obj.suppressed._changed():
        input_yang_obj.suppressed = input_yang_obj.suppressed
        
    if input_yang_obj.time_remaining._changed():
        input_yang_obj.time_remaining = input_yang_obj.time_remaining
        
    return translated_yang_obj

def _translate__interfaces_interface_encapsulation_dot1q_vlan_outer_tag(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/encapsulation/dot1q-vlan/outer-tag

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.tag_type._changed():
        input_yang_obj.tag_type = input_yang_obj.tag_type
        
    if input_yang_obj.vlan_id._changed():
        input_yang_obj.vlan_id = input_yang_obj.vlan_id
        
    return translated_yang_obj

def _translate__interfaces_interface_encapsulation_dot1q_vlan_second_tag(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/encapsulation/dot1q-vlan/second-tag

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.tag_type._changed():
        input_yang_obj.tag_type = input_yang_obj.tag_type
        
    if input_yang_obj.vlan_id._changed():
        input_yang_obj.vlan_id = input_yang_obj.vlan_id
        
    return translated_yang_obj

def _translate__interfaces_interface_encapsulation_dot1q_vlan(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/encapsulation/dot1q-vlan

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__interfaces_interface_encapsulation_dot1q_vlan_outer_tag(input_yang_obj.outer_tag, translated_yang_obj)
        
    innerobj = _translate__interfaces_interface_encapsulation_dot1q_vlan_second_tag(input_yang_obj.second_tag, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_interface_encapsulation(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/encapsulation

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__interfaces_interface_encapsulation_dot1q_vlan(input_yang_obj.dot1q_vlan, translated_yang_obj)
        
    return translated_yang_obj

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

def _translate__interfaces_interface_ipv4_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
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

def _translate__interfaces_interface_ipv6_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.type = "global"
    translated_yang_obj.algorithm_type = "none"
    if input_yang_obj.prefix_length._changed():
        translated_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.is_router._changed():
        input_yang_obj.is_router = input_yang_obj.is_router
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6_autoconf(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/autoconf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.create_global_addresses._changed():
        input_yang_obj.create_global_addresses = input_yang_obj.create_global_addresses
        
    if input_yang_obj.create_temporary_addresses._changed():
        input_yang_obj.create_temporary_addresses = input_yang_obj.create_temporary_addresses
        
    if input_yang_obj.temporary_valid_lifetime._changed():
        input_yang_obj.temporary_valid_lifetime = input_yang_obj.temporary_valid_lifetime
        
    if input_yang_obj.temporary_preferred_lifetime._changed():
        input_yang_obj.temporary_preferred_lifetime = input_yang_obj.temporary_preferred_lifetime
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv6.enabled._changed():
        input_yang_obj.ipv6.enabled = input_yang_obj.ipv6.enabled
        
    if input_yang_obj.ipv6.forwarding._changed():
        input_yang_obj.ipv6.forwarding = input_yang_obj.ipv6.forwarding
        
    if input_yang_obj.ipv6.mtu._changed():
        input_yang_obj.ipv6.mtu = input_yang_obj.ipv6.mtu
        
    for k, listInst in input_yang_obj.ipv6.address.iteritems():
        ipv6_obj = translated_yang_obj.ipv6_ifs.ipv6_if.add(name=input_yang_obj.name)
        ipv6_address_obj = ipv6_obj.addresses.address.add(ip=listInst.ip)
        innerobj = _translate__interfaces_interface_ipv6_address(listInst, ipv6_address_obj)
        
    for k, listInst in input_yang_obj.ipv6.neighbor.iteritems():
        innerobj = _translate__interfaces_interface_ipv6_neighbor(listInst, translated_yang_obj)
        
    if input_yang_obj.ipv6.dup_addr_detect_transmits._changed():
        input_yang_obj.ipv6.dup_addr_detect_transmits = input_yang_obj.ipv6.dup_addr_detect_transmits
        
    innerobj = _translate__interfaces_interface_ipv6_autoconf(input_yang_obj.ipv6.autoconf, translated_yang_obj)

        
    return translated_yang_obj

def _translate__interfaces_interface_mpls_label_security(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/mpls-label-security

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.rpf._changed():
        input_yang_obj.rpf = input_yang_obj.rpf
        
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
        
    innerobj = _translate__interfaces_interface_ipv6(input_yang_obj, translated_yang_obj)

    return translated_yang_obj

def _translate__interfaces(input_yang_obj, translated_yang_obj=None):
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
    list_obj = []

    for k, listInst in input_yang_obj.interface.iteritems():
        interface_obj = translated_yang_obj.ifm.interfaces.interface.add(name=k)
        inner_obj = _translate__interfaces_interface(listInst, interface_obj)
        # ipv4 = _translate__interfaces_interface_ipv4(listInst,interface_obj)
    list_obj.append(translated_yang_obj)

    return list_obj, translated_yang_obj

def _translate__interfaces_state_interface_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.discontinuity_time._changed():
        input_yang_obj.discontinuity_time = input_yang_obj.discontinuity_time
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    if input_yang_obj.in_unicast_pkts._changed():
        input_yang_obj.in_unicast_pkts = input_yang_obj.in_unicast_pkts
        
    if input_yang_obj.in_broadcast_pkts._changed():
        input_yang_obj.in_broadcast_pkts = input_yang_obj.in_broadcast_pkts
        
    if input_yang_obj.in_multicast_pkts._changed():
        input_yang_obj.in_multicast_pkts = input_yang_obj.in_multicast_pkts
        
    if input_yang_obj.in_discards._changed():
        input_yang_obj.in_discards = input_yang_obj.in_discards
        
    if input_yang_obj.in_errors._changed():
        input_yang_obj.in_errors = input_yang_obj.in_errors
        
    if input_yang_obj.in_unknown_protos._changed():
        input_yang_obj.in_unknown_protos = input_yang_obj.in_unknown_protos
        
    if input_yang_obj.out_octets._changed():
        input_yang_obj.out_octets = input_yang_obj.out_octets
        
    if input_yang_obj.out_unicast_pkts._changed():
        input_yang_obj.out_unicast_pkts = input_yang_obj.out_unicast_pkts
        
    if input_yang_obj.out_broadcast_pkts._changed():
        input_yang_obj.out_broadcast_pkts = input_yang_obj.out_broadcast_pkts
        
    if input_yang_obj.out_multicast_pkts._changed():
        input_yang_obj.out_multicast_pkts = input_yang_obj.out_multicast_pkts
        
    if input_yang_obj.out_discards._changed():
        input_yang_obj.out_discards = input_yang_obj.out_discards
        
    if input_yang_obj.out_errors._changed():
        input_yang_obj.out_errors = input_yang_obj.out_errors
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv4_address(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv4_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.is_router._changed():
        input_yang_obj.is_router = input_yang_obj.is_router
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv6_address(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv6_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state_interface(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    innerobj = _translate__interfaces_state_interface_statistics(input_yang_obj.statistics, translated_yang_obj)
        
    innerobj = _translate__interfaces_state_interface_ipv4(input_yang_obj.ipv4, translated_yang_obj)
        
    innerobj = _translate__interfaces_state_interface_ipv6(input_yang_obj.ipv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__interfaces_state_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ietf_interfaces(input_yang_obj, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    trans_yang_list = []

    translated_yang_obj = huawei_ifm()

    list, innerobj = _translate__interfaces(input_yang_obj.interfaces, translated_yang_obj)

    target_xpath = "/a:ifm/a:interfaces"
    ns_map = {'a': 'urn:huawei:yang:huawei-ifm'}

    for listInst in list:
        if hasattr(listInst, "ifm"):
            trans_yang_list.append(listInst.ifm)
        elif hasattr(listInst, "network_instance"):
            trans_yang_list.append(listInst.network_instance)

    return translated_yang_obj.ifm, target_xpath, ns_map