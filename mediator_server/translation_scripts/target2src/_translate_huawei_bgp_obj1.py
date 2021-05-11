from mediator_server.mediator_framework.adaptor import XPATH
from mediator_server.yang_bindings.src_yang_bindings.ietf_l3vpn_ntw_binding import ietf_l3vpn_ntw
from mediator_server.yang_bindings.src_yang_bindings.ietf_routing_binding import *

def _translate__bgp_global(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/global

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.yang_enable._changed():
        input_yang_obj.yang_enable = input_yang_obj.yang_enable
        
    return translated_yang_obj

def _translate__bgp_base_process_confederation(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/base-process/confederation

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.id._changed():
        input_yang_obj.id = input_yang_obj.id
        
    if input_yang_obj.nonstanded._changed():
        input_yang_obj.nonstanded = input_yang_obj.nonstanded
        
    if input_yang_obj.as_._changed():
        input_yang_obj.as_ = input_yang_obj.as_
        
    return translated_yang_obj

def _translate__bgp_base_process_graceful_restart(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/base-process/graceful-restart

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.time_wait_for_rib._changed():
        input_yang_obj.time_wait_for_rib = input_yang_obj.time_wait_for_rib
        
    if input_yang_obj.restart_time._changed():
        input_yang_obj.restart_time = input_yang_obj.restart_time
        
    if input_yang_obj.peer_reset._changed():
        input_yang_obj.peer_reset = input_yang_obj.peer_reset
        
    return translated_yang_obj

def _translate__bgp_base_process_reference_period(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/base-process/reference-period

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.suppress_interval._changed():
        input_yang_obj.suppress_interval = input_yang_obj.suppress_interval
        
    if input_yang_obj.hold_interval._changed():
        input_yang_obj.hold_interval = input_yang_obj.hold_interval
        
    if input_yang_obj.clear_interval._changed():
        input_yang_obj.clear_interval = input_yang_obj.clear_interval
        
    return translated_yang_obj

def _translate__bgp_base_process_timer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/base-process/timer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.connect_retry_time._changed():
        input_yang_obj.connect_retry_time = input_yang_obj.connect_retry_time
        
    if input_yang_obj.keep_alive_time._changed():
        input_yang_obj.keep_alive_time = input_yang_obj.keep_alive_time
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.min_hold_time._changed():
        input_yang_obj.min_hold_time = input_yang_obj.min_hold_time
        
    return translated_yang_obj

def _translate__bgp_base_process(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/base-process

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.as_._changed():
        vpn_service_obj = translated_yang_obj.l3vpn_ntw.vpn_services.vpn_service.add("4G")
        vpn_service_obj.customer_name = "mycustomer"
        vpn_node_obj = vpn_service_obj.vpn_nodes.vpn_node.add("44")
        vpn_node_obj.local_autonomous_system = input_yang_obj.as_
        
    # if input_yang_obj.keep_all_routes._changed():
    #     input_yang_obj.keep_all_routes = input_yang_obj.keep_all_routes
    #
    # if input_yang_obj.check_first_as._changed():
    #     input_yang_obj.check_first_as = input_yang_obj.check_first_as
    #
    # if input_yang_obj.router_id_auto_select._changed():
    #     input_yang_obj.router_id_auto_select = input_yang_obj.router_id_auto_select
    #
    # if input_yang_obj.shutdown._changed():
    #     input_yang_obj.shutdown = input_yang_obj.shutdown
    #
    # if input_yang_obj.local_ifnet_mtu._changed():
    #     input_yang_obj.local_ifnet_mtu = input_yang_obj.local_ifnet_mtu
    #
    # if input_yang_obj.private_4byte_as._changed():
    #     input_yang_obj.private_4byte_as = input_yang_obj.private_4byte_as
    #
    # if input_yang_obj.local_cross_no_med._changed():
    #     input_yang_obj.local_cross_no_med = input_yang_obj.local_cross_no_med
    #
    # if input_yang_obj.as_path_limit._changed():
    #     input_yang_obj.as_path_limit = input_yang_obj.as_path_limit
    #
    # innerobj = _translate__bgp_base_process_confederation(input_yang_obj.confederation, translated_yang_obj)
    #
    # innerobj = _translate__bgp_base_process_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
    #
    # innerobj = _translate__bgp_base_process_reference_period(input_yang_obj.reference_period, translated_yang_obj)
    #
    # innerobj = _translate__bgp_base_process_timer(input_yang_obj.timer, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__bgp_global(input_yang_obj.global_, translated_yang_obj)
        
    innerobj = _translate__bgp_base_process(input_yang_obj.base_process, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_bgp(input_yang_obj, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-bgp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("13vpn-ntw bgp script")
    translated_yang_obj = ietf_l3vpn_ntw()
    xpath = '/a:l3vpn-ntw'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-l3vpn-ntw'}
    target_xpath = XPATH(xpath, ns_map)

    innerobj = _translate__bgp(input_yang_obj.bgp, translated_yang_obj)
        
    return [[translated_yang_obj.l3vpn_ntw, target_xpath]]
