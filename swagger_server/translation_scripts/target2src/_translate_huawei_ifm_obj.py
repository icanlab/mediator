from swagger_server.yang_bindings.target_yang_bindings.huawei_ifm_binding import *
from swagger_server.yang_bindings.src_yang_bindings.ietf_interfaces_binding import *

def _translate__ifm_global(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/global

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.statistic_interval._changed():
        input_yang_obj.statistic_interval = input_yang_obj.statistic_interval
        
    if input_yang_obj.ipv4_ignore_primary_sub._changed():
        input_yang_obj.ipv4_ignore_primary_sub = input_yang_obj.ipv4_ignore_primary_sub
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_dynamic(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/dynamic

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.oper_status._changed():
        input_yang_obj.oper_status = input_yang_obj.oper_status
        
    if input_yang_obj.physical_status._changed():
        input_yang_obj.physical_status = input_yang_obj.physical_status
        
    if input_yang_obj.link_status._changed():
        input_yang_obj.link_status = input_yang_obj.link_status
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    if input_yang_obj.ipv4_status._changed():
        input_yang_obj.ipv4_status = input_yang_obj.ipv4_status
        
    if input_yang_obj.ipv6_status._changed():
        input_yang_obj.ipv6_status = input_yang_obj.ipv6_status
        
    if input_yang_obj.is_control_flap_damp._changed():
        input_yang_obj.is_control_flap_damp = input_yang_obj.is_control_flap_damp
        
    if input_yang_obj.mac_address._changed():
        input_yang_obj.mac_address = input_yang_obj.mac_address
        
    if input_yang_obj.line_protocol_up_time._changed():
        input_yang_obj.line_protocol_up_time = input_yang_obj.line_protocol_up_time
        
    if input_yang_obj.is_offline._changed():
        input_yang_obj.is_offline = input_yang_obj.is_offline
        
    if input_yang_obj.link_quality_grade._changed():
        input_yang_obj.link_quality_grade = input_yang_obj.link_quality_grade
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_mib_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/mib-statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.receive_byte._changed():
        input_yang_obj.receive_byte = input_yang_obj.receive_byte
        
    if input_yang_obj.send_byte._changed():
        input_yang_obj.send_byte = input_yang_obj.send_byte
        
    if input_yang_obj.receive_packet._changed():
        input_yang_obj.receive_packet = input_yang_obj.receive_packet
        
    if input_yang_obj.send_packet._changed():
        input_yang_obj.send_packet = input_yang_obj.send_packet
        
    if input_yang_obj.receive_unicast_packet._changed():
        input_yang_obj.receive_unicast_packet = input_yang_obj.receive_unicast_packet
        
    if input_yang_obj.receive_multicast_packet._changed():
        input_yang_obj.receive_multicast_packet = input_yang_obj.receive_multicast_packet
        
    if input_yang_obj.receive_broad_packet._changed():
        input_yang_obj.receive_broad_packet = input_yang_obj.receive_broad_packet
        
    if input_yang_obj.send_unicast_packet._changed():
        input_yang_obj.send_unicast_packet = input_yang_obj.send_unicast_packet
        
    if input_yang_obj.send_multicast_packet._changed():
        input_yang_obj.send_multicast_packet = input_yang_obj.send_multicast_packet
        
    if input_yang_obj.send_broad_packet._changed():
        input_yang_obj.send_broad_packet = input_yang_obj.send_broad_packet
        
    if input_yang_obj.receive_error_packet._changed():
        input_yang_obj.receive_error_packet = input_yang_obj.receive_error_packet
        
    if input_yang_obj.receive_drop_packet._changed():
        input_yang_obj.receive_drop_packet = input_yang_obj.receive_drop_packet
        
    if input_yang_obj.send_error_packet._changed():
        input_yang_obj.send_error_packet = input_yang_obj.send_error_packet
        
    if input_yang_obj.send_drop_packet._changed():
        input_yang_obj.send_drop_packet = input_yang_obj.send_drop_packet
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface_common_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ifm/interfaces/interface/common-statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.stati_interval._changed():
        input_yang_obj.stati_interval = input_yang_obj.stati_interval
        
    if input_yang_obj.in_byte_rate._changed():
        input_yang_obj.in_byte_rate = input_yang_obj.in_byte_rate
        
    if input_yang_obj.in_bit_rate._changed():
        input_yang_obj.in_bit_rate = input_yang_obj.in_bit_rate
        
    if input_yang_obj.in_packet_rate._changed():
        input_yang_obj.in_packet_rate = input_yang_obj.in_packet_rate
        
    if input_yang_obj.in_use_rate._changed():
        input_yang_obj.in_use_rate = input_yang_obj.in_use_rate
        
    if input_yang_obj.out_byte_rate._changed():
        input_yang_obj.out_byte_rate = input_yang_obj.out_byte_rate
        
    if input_yang_obj.out_bit_rate._changed():
        input_yang_obj.out_bit_rate = input_yang_obj.out_bit_rate
        
    if input_yang_obj.out_packet_rate._changed():
        input_yang_obj.out_packet_rate = input_yang_obj.out_packet_rate
        
    if input_yang_obj.out_use_rate._changed():
        input_yang_obj.out_use_rate = input_yang_obj.out_use_rate
        
    if input_yang_obj.receive_byte._changed():
        input_yang_obj.receive_byte = input_yang_obj.receive_byte
        
    if input_yang_obj.send_byte._changed():
        input_yang_obj.send_byte = input_yang_obj.send_byte
        
    if input_yang_obj.receive_packet._changed():
        input_yang_obj.receive_packet = input_yang_obj.receive_packet
        
    if input_yang_obj.send_packet._changed():
        input_yang_obj.send_packet = input_yang_obj.send_packet
        
    if input_yang_obj.receive_unicast_packet._changed():
        input_yang_obj.receive_unicast_packet = input_yang_obj.receive_unicast_packet
        
    if input_yang_obj.receive_multicast_packet._changed():
        input_yang_obj.receive_multicast_packet = input_yang_obj.receive_multicast_packet
        
    if input_yang_obj.receive_broad_packet._changed():
        input_yang_obj.receive_broad_packet = input_yang_obj.receive_broad_packet
        
    if input_yang_obj.send_unicast_packet._changed():
        input_yang_obj.send_unicast_packet = input_yang_obj.send_unicast_packet
        
    if input_yang_obj.send_multicast_packet._changed():
        input_yang_obj.send_multicast_packet = input_yang_obj.send_multicast_packet
        
    if input_yang_obj.send_broad_packet._changed():
        input_yang_obj.send_broad_packet = input_yang_obj.send_broad_packet
        
    if input_yang_obj.receive_error_packet._changed():
        input_yang_obj.receive_error_packet = input_yang_obj.receive_error_packet
        
    if input_yang_obj.receive_drop_packet._changed():
        input_yang_obj.receive_drop_packet = input_yang_obj.receive_drop_packet
        
    if input_yang_obj.send_error_packet._changed():
        input_yang_obj.send_error_packet = input_yang_obj.send_error_packet
        
    if input_yang_obj.send_drop_packet._changed():
        input_yang_obj.send_drop_packet = input_yang_obj.send_drop_packet
        
    if input_yang_obj.send_unicast_bit._changed():
        input_yang_obj.send_unicast_bit = input_yang_obj.send_unicast_bit
        
    if input_yang_obj.receive_unicast_bit._changed():
        input_yang_obj.receive_unicast_bit = input_yang_obj.receive_unicast_bit
        
    if input_yang_obj.send_multicast_bit._changed():
        input_yang_obj.send_multicast_bit = input_yang_obj.send_multicast_bit
        
    if input_yang_obj.receive_multicast_bit._changed():
        input_yang_obj.receive_multicast_bit = input_yang_obj.receive_multicast_bit
        
    if input_yang_obj.send_broad_bit._changed():
        input_yang_obj.send_broad_bit = input_yang_obj.send_broad_bit
        
    if input_yang_obj.receive_broad_bit._changed():
        input_yang_obj.receive_broad_bit = input_yang_obj.receive_broad_bit
        
    if input_yang_obj.send_unicast_bit_rate._changed():
        input_yang_obj.send_unicast_bit_rate = input_yang_obj.send_unicast_bit_rate
        
    if input_yang_obj.receive_unicast_bit_rate._changed():
        input_yang_obj.receive_unicast_bit_rate = input_yang_obj.receive_unicast_bit_rate
        
    if input_yang_obj.send_multicast_bit_rate._changed():
        input_yang_obj.send_multicast_bit_rate = input_yang_obj.send_multicast_bit_rate
        
    if input_yang_obj.receive_multicast_bit_rate._changed():
        input_yang_obj.receive_multicast_bit_rate = input_yang_obj.receive_multicast_bit_rate
        
    if input_yang_obj.send_broad_bit_rate._changed():
        input_yang_obj.send_broad_bit_rate = input_yang_obj.send_broad_bit_rate
        
    if input_yang_obj.receive_broad_bit_rate._changed():
        input_yang_obj.receive_broad_bit_rate = input_yang_obj.receive_broad_bit_rate
        
    if input_yang_obj.send_unicast_packet_rate._changed():
        input_yang_obj.send_unicast_packet_rate = input_yang_obj.send_unicast_packet_rate
        
    if input_yang_obj.receive_unicast_packet_rate._changed():
        input_yang_obj.receive_unicast_packet_rate = input_yang_obj.receive_unicast_packet_rate
        
    if input_yang_obj.send_multicast_packet_rate._changed():
        input_yang_obj.send_multicast_packet_rate = input_yang_obj.send_multicast_packet_rate
        
    if input_yang_obj.receive_multicast_packet_rate._changed():
        input_yang_obj.receive_multicast_packet_rate = input_yang_obj.receive_multicast_packet_rate
        
    if input_yang_obj.send_broadcast_packet_rate._changed():
        input_yang_obj.send_broadcast_packet_rate = input_yang_obj.send_broadcast_packet_rate
        
    if input_yang_obj.receive_broadcast_packet_rate._changed():
        input_yang_obj.receive_broadcast_packet_rate = input_yang_obj.receive_broadcast_packet_rate
        
    return translated_yang_obj

def _translate__ifm_interfaces_interface(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.index._changed():
        input_yang_obj.index = input_yang_obj.index
        
    if input_yang_obj.class_._changed():
        input_yang_obj.class_ = input_yang_obj.class_
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.position._changed():
        input_yang_obj.position = input_yang_obj.position
        
    if input_yang_obj.parent_name._changed():
        input_yang_obj.parent_name = input_yang_obj.parent_name
        
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.aggregation_name._changed():
        input_yang_obj.aggregation_name = input_yang_obj.aggregation_name
        
    if input_yang_obj.is_l2_switch._changed():
        input_yang_obj.is_l2_switch = input_yang_obj.is_l2_switch
        
    if input_yang_obj.admin_status._changed():
        input_yang_obj.admin_status = input_yang_obj.admin_status
        
    if input_yang_obj.link_protocol._changed():
        input_yang_obj.link_protocol = input_yang_obj.link_protocol
        
    if input_yang_obj.router_type._changed():
        input_yang_obj.router_type = input_yang_obj.router_type
        
    if input_yang_obj.clear_ip_df._changed():
        input_yang_obj.clear_ip_df = input_yang_obj.clear_ip_df
        
    if input_yang_obj.link_up_down_trap_enable._changed():
        input_yang_obj.link_up_down_trap_enable = input_yang_obj.link_up_down_trap_enable
        
    if input_yang_obj.statistic_enable._changed():
        input_yang_obj.statistic_enable = input_yang_obj.statistic_enable
        
    if input_yang_obj.statistic_mode._changed():
        input_yang_obj.statistic_mode = input_yang_obj.statistic_mode
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    if input_yang_obj.spread_mtu_flag._changed():
        input_yang_obj.spread_mtu_flag = input_yang_obj.spread_mtu_flag
        
    if input_yang_obj.statistic_interval._changed():
        input_yang_obj.statistic_interval = input_yang_obj.statistic_interval
        
    if input_yang_obj.vrf_name._changed():
        translated_yang_obj.bind_ni_name = input_yang_obj.vrf_name
        
    if input_yang_obj.l2_mode_enable._changed():
        input_yang_obj.l2_mode_enable = input_yang_obj.l2_mode_enable
        
    if input_yang_obj.down_delay_time._changed():
        input_yang_obj.down_delay_time = input_yang_obj.down_delay_time
        
    if input_yang_obj.mac_address._changed():
        input_yang_obj.mac_address = input_yang_obj.mac_address
        
    innerobj = _translate__ifm_interfaces_interface_dynamic(input_yang_obj.dynamic, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_mib_statistics(input_yang_obj.mib_statistics, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces_interface_common_statistics(input_yang_obj.common_statistics, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ifm_interfaces(input_yang_obj, translated_yang_obj=None):
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
        # innerobj = _translate__ifm_interfaces_interface(listInst, interface_obj)
        
    return translated_yang_obj

def _translate__ifm(input_yang_obj, translated_yang_obj=None):
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
    
 #   innerobj = _translate__ifm_global(input_yang_obj.global_, translated_yang_obj)
        
    innerobj = _translate__ifm_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ifm(input_yang_obj, translated_yang_obj=None):
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
    # print("translate start!")

    innerobj = _translate__ifm(input_yang_obj.ifm, translated_yang_obj)
        
    return [translated_yang_obj.interfaces]
