from ..yang_bindings.huawei_ifm_binding import *
from ..yang_bindings.huawei_bgp_binding import *
def _translate__routing_interfaces(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_distance(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/global/distance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.external._changed():
        input_yang_obj.external = input_yang_obj.external
        
    if input_yang_obj.internal._changed():
        input_yang_obj.internal = input_yang_obj.internal
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_confederation(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths_ibgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_route_selection_options(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.ignore_as_path_length._changed():
        input_yang_obj.ignore_as_path_length = input_yang_obj.ignore_as_path_length
        
    if input_yang_obj.external_compare_router_id._changed():
        input_yang_obj.external_compare_router_id = input_yang_obj.external_compare_router_id
        
    if input_yang_obj.advertise_inactive_routes._changed():
        input_yang_obj.advertise_inactive_routes = input_yang_obj.advertise_inactive_routes
        
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    if input_yang_obj.ignore_next_hop_igp_metric._changed():
        input_yang_obj.ignore_next_hop_igp_metric = input_yang_obj.ignore_next_hop_igp_metric
        
    if input_yang_obj.enable_med._changed():
        input_yang_obj.enable_med = input_yang_obj.enable_med
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_route_selection_options(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.ignore_as_path_length._changed():
        input_yang_obj.ignore_as_path_length = input_yang_obj.ignore_as_path_length
        
    if input_yang_obj.external_compare_router_id._changed():
        input_yang_obj.external_compare_router_id = input_yang_obj.external_compare_router_id
        
    if input_yang_obj.advertise_inactive_routes._changed():
        input_yang_obj.advertise_inactive_routes = input_yang_obj.advertise_inactive_routes
        
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    if input_yang_obj.ignore_next_hop_igp_metric._changed():
        input_yang_obj.ignore_next_hop_igp_metric = input_yang_obj.ignore_next_hop_igp_metric
        
    if input_yang_obj.enable_med._changed():
        input_yang_obj.enable_med = input_yang_obj.enable_med
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis_afi_safi(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis(input_yang_obj, translated_yang_obj=None):
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
    
    for k, listInst in input_yang_obj.afi_safi.iteritems():
        af_obj = translated_yang_obj.bgp.base_process.afs.af.add(type="ipv4uni")
        af_obj.ipv4_unicast.import_routes.import_route.add(protocol="static",process_id="0")

    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.as_._changed():
        input_yang_obj.as_ = input_yang_obj.as_
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_distance(input_yang_obj.distance, translated_yang_obj)
    #
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_confederation(input_yang_obj.confederation, translated_yang_obj)
    #
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
    #
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
    #
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_route_selection_options(input_yang_obj.route_selection_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_afi_safis(input_yang_obj.afi_safis, translated_yang_obj)
        
    # innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    # if input_yang_obj.total_paths._changed():
    #     input_yang_obj.total_paths = input_yang_obj.total_paths
    #
    # if input_yang_obj.total_prefixes._changed():
    #     input_yang_obj.total_prefixes = input_yang_obj.total_prefixes
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_secure_session(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/secure-session

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_ao._changed():
        input_yang_obj.enable_ao = input_yang_obj.enable_ao
        
    if input_yang_obj.send_id._changed():
        input_yang_obj.send_id = input_yang_obj.send_id
        
    if input_yang_obj.recv_id._changed():
        input_yang_obj.recv_id = input_yang_obj.recv_id
        
    if input_yang_obj.include_tcp_options._changed():
        input_yang_obj.include_tcp_options = input_yang_obj.include_tcp_options
        
    if input_yang_obj.accept_ao_mismatch._changed():
        input_yang_obj.accept_ao_mismatch = input_yang_obj.accept_ao_mismatch
        
    if input_yang_obj.ao_keychain._changed():
        input_yang_obj.ao_keychain = input_yang_obj.ao_keychain
        
    if input_yang_obj.enable_md5._changed():
        input_yang_obj.enable_md5 = input_yang_obj.enable_md5
        
    if input_yang_obj.md5_keychain._changed():
        input_yang_obj.md5_keychain = input_yang_obj.md5_keychain
        
    if input_yang_obj.sa._changed():
        input_yang_obj.sa = input_yang_obj.sa
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_flap_damping(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/route-flap-damping

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.suppress_above._changed():
        input_yang_obj.suppress_above = input_yang_obj.suppress_above
        
    if input_yang_obj.reuse_above._changed():
        input_yang_obj.reuse_above = input_yang_obj.reuse_above
        
    if input_yang_obj.max_flap._changed():
        input_yang_obj.max_flap = input_yang_obj.max_flap
        
    if input_yang_obj.reach_decay._changed():
        input_yang_obj.reach_decay = input_yang_obj.reach_decay
        
    if input_yang_obj.unreach_decay._changed():
        input_yang_obj.unreach_decay = input_yang_obj.unreach_decay
        
    if input_yang_obj.keep_history._changed():
        input_yang_obj.keep_history = input_yang_obj.keep_history
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_selection_options(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/route-selection-options

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.ignore_as_path_length._changed():
        input_yang_obj.ignore_as_path_length = input_yang_obj.ignore_as_path_length
        
    if input_yang_obj.external_compare_router_id._changed():
        input_yang_obj.external_compare_router_id = input_yang_obj.external_compare_router_id
        
    if input_yang_obj.advertise_inactive_routes._changed():
        input_yang_obj.advertise_inactive_routes = input_yang_obj.advertise_inactive_routes
        
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    if input_yang_obj.ignore_next_hop_igp_metric._changed():
        input_yang_obj.ignore_next_hop_igp_metric = input_yang_obj.ignore_next_hop_igp_metric
        
    if input_yang_obj.enable_med._changed():
        input_yang_obj.enable_med = input_yang_obj.enable_med
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_timers(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.keepalive._changed():
        input_yang_obj.keepalive = input_yang_obj.keepalive
        
    if input_yang_obj.min_as_origination_interval._changed():
        input_yang_obj.min_as_origination_interval = input_yang_obj.min_as_origination_interval
        
    if input_yang_obj.min_route_advertisement_interval._changed():
        input_yang_obj.min_route_advertisement_interval = input_yang_obj.min_route_advertisement_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_transport(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.auth_password._changed():
        input_yang_obj.auth_password = input_yang_obj.auth_password
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_logging_options(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/logging-options

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.log_neighbor_state_changes._changed():
        input_yang_obj.log_neighbor_state_changes = input_yang_obj.log_neighbor_state_changes
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_ebgp_multihop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_reflector(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.no_client_reflect._changed():
        input_yang_obj.no_client_reflect = input_yang_obj.no_client_reflect
        
    if input_yang_obj.route_reflector_client._changed():
        input_yang_obj.route_reflector_client = input_yang_obj.route_reflector_client
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_as_path_options(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_add_paths(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.max_._changed():
        input_yang_obj.max_ = input_yang_obj.max_
        
    if input_yang_obj.all._changed():
        input_yang_obj.all = input_yang_obj.all
        
    if input_yang_obj.eligible_prefix_policy._changed():
        input_yang_obj.eligible_prefix_policy = input_yang_obj.eligible_prefix_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_prefixes(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis_afi_safi(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_sent(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages_received(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_messages(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_queues(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/neighbor/statistics/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.clear._changed():
        input_yang_obj.clear = input_yang_obj.clear
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.peer_type._changed():
        input_yang_obj.peer_type = input_yang_obj.peer_type
        
    if input_yang_obj.peer_group._changed():
        input_yang_obj.peer_group = input_yang_obj.peer_group
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    if input_yang_obj.remote_port._changed():
        input_yang_obj.remote_port = input_yang_obj.remote_port
        
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.secure_session_enable._changed():
        input_yang_obj.secure_session_enable = input_yang_obj.secure_session_enable
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_secure_session(input_yang_obj.secure_session, translated_yang_obj)
        
    if input_yang_obj.ttl_security._changed():
        input_yang_obj.ttl_security = input_yang_obj.ttl_security
        
    if input_yang_obj.remote_as._changed():
        input_yang_obj.remote_as = input_yang_obj.remote_as
        
    if input_yang_obj.peer_as._changed():
        input_yang_obj.peer_as = input_yang_obj.peer_as
        
    if input_yang_obj.local_as._changed():
        input_yang_obj.local_as = input_yang_obj.local_as
        
    if input_yang_obj.remove_private_as._changed():
        input_yang_obj.remove_private_as = input_yang_obj.remove_private_as
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_flap_damping(input_yang_obj.route_flap_damping, translated_yang_obj)
        
    if input_yang_obj.send_community._changed():
        input_yang_obj.send_community = input_yang_obj.send_community
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_selection_options(input_yang_obj.route_selection_options, translated_yang_obj)
        
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
        
    if input_yang_obj.treat_as_withdraw._changed():
        input_yang_obj.treat_as_withdraw = input_yang_obj.treat_as_withdraw
        
    if input_yang_obj.erroneous_update_messages._changed():
        input_yang_obj.erroneous_update_messages = input_yang_obj.erroneous_update_messages
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_graceful_restart(input_yang_obj.graceful_restart, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_logging_options(input_yang_obj.logging_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_ebgp_multihop(input_yang_obj.ebgp_multihop, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_route_reflector(input_yang_obj.route_reflector, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_as_path_options(input_yang_obj.as_path_options, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_add_paths(input_yang_obj.add_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_use_multiple_paths(input_yang_obj.use_multiple_paths, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_apply_policy(input_yang_obj.apply_policy, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_afi_safis(input_yang_obj.afi_safis, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_neighbor_statistics(input_yang_obj.statistics, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_established(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_backward_transition(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/neighbors/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors(input_yang_obj, translated_yang_obj=None):
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
        peer_obj = translated_yang_obj.bgp.base_process.peers.peer.add(address=k)
        peer_obj.remote_as = str(listInst.remote_as)
        peer_obj.afs.af.add(type="ipv4uni")

    if input_yang_obj.established._changed():
        input_yang_obj.established = input_yang_obj.established
        
    if input_yang_obj.backward_transition._changed():
        input_yang_obj.backward_transition = input_yang_obj.backward_transition
        
    if input_yang_obj.clear._changed():
        input_yang_obj.clear = input_yang_obj.clear
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_flap_damping(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/peer-groups/peer-group/route-flap-damping

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.suppress_above._changed():
        input_yang_obj.suppress_above = input_yang_obj.suppress_above
        
    if input_yang_obj.reuse_above._changed():
        input_yang_obj.reuse_above = input_yang_obj.reuse_above
        
    if input_yang_obj.max_flap._changed():
        input_yang_obj.max_flap = input_yang_obj.max_flap
        
    if input_yang_obj.reach_decay._changed():
        input_yang_obj.reach_decay = input_yang_obj.reach_decay
        
    if input_yang_obj.unreach_decay._changed():
        input_yang_obj.unreach_decay = input_yang_obj.unreach_decay
        
    if input_yang_obj.keep_history._changed():
        input_yang_obj.keep_history = input_yang_obj.keep_history
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_timers(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.keepalive._changed():
        input_yang_obj.keepalive = input_yang_obj.keepalive
        
    if input_yang_obj.min_as_origination_interval._changed():
        input_yang_obj.min_as_origination_interval = input_yang_obj.min_as_origination_interval
        
    if input_yang_obj.min_route_advertisement_interval._changed():
        input_yang_obj.min_route_advertisement_interval = input_yang_obj.min_route_advertisement_interval
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_transport(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.auth_password._changed():
        input_yang_obj.auth_password = input_yang_obj.auth_password
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_ebgp_multihop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_reflector(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.no_client_reflect._changed():
        input_yang_obj.no_client_reflect = input_yang_obj.no_client_reflect
        
    if input_yang_obj.route_reflector_client._changed():
        input_yang_obj.route_reflector_client = input_yang_obj.route_reflector_client
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_as_path_options(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_add_paths(input_yang_obj, translated_yang_obj=None):
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
        
    if input_yang_obj.max_._changed():
        input_yang_obj.max_ = input_yang_obj.max_
        
    if input_yang_obj.all._changed():
        input_yang_obj.all = input_yang_obj.all
        
    if input_yang_obj.eligible_prefix_policy._changed():
        input_yang_obj.eligible_prefix_policy = input_yang_obj.eligible_prefix_policy
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths_ibgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_graceful_restart(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_route_selection_options(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.ignore_as_path_length._changed():
        input_yang_obj.ignore_as_path_length = input_yang_obj.ignore_as_path_length
        
    if input_yang_obj.external_compare_router_id._changed():
        input_yang_obj.external_compare_router_id = input_yang_obj.external_compare_router_id
        
    if input_yang_obj.advertise_inactive_routes._changed():
        input_yang_obj.advertise_inactive_routes = input_yang_obj.advertise_inactive_routes
        
    if input_yang_obj.enable_aigp._changed():
        input_yang_obj.enable_aigp = input_yang_obj.enable_aigp
        
    if input_yang_obj.ignore_next_hop_igp_metric._changed():
        input_yang_obj.ignore_next_hop_igp_metric = input_yang_obj.ignore_next_hop_igp_metric
        
    if input_yang_obj.enable_med._changed():
        input_yang_obj.enable_med = input_yang_obj.enable_med
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ebgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths_ibgp(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_use_multiple_paths(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_apply_policy(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv4_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_ipv6_labeled_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l3vpn_ipv6_multicast(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_vpls(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn_prefix_limit(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi_l2vpn_evpn(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis_afi_safi(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_afi_safis(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.remote_as._changed():
        input_yang_obj.remote_as = input_yang_obj.remote_as
        
    if input_yang_obj.peer_as._changed():
        input_yang_obj.peer_as = input_yang_obj.peer_as
        
    if input_yang_obj.local_as._changed():
        input_yang_obj.local_as = input_yang_obj.local_as
        
    if input_yang_obj.remove_private_as._changed():
        input_yang_obj.remove_private_as = input_yang_obj.remove_private_as
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups_peer_group_route_flap_damping(input_yang_obj.route_flap_damping, translated_yang_obj)
        
    if input_yang_obj.send_community._changed():
        input_yang_obj.send_community = input_yang_obj.send_community
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_peer_groups(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface_bfd(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces_interface(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_interfaces(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_aggregator(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes/aggregator

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as_path_segment(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes/as-path/segment

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.member._changed():
        input_yang_obj.member = input_yang_obj.member
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as_path(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes/as-path

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.segment.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as_path_segment(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as4_path_segment(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes/as4-path/segment

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.member._changed():
        input_yang_obj.member = input_yang_obj.member
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as4_path(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes/as4-path

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.segment.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as4_path_segment(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/attr-sets/attr-set/attr-set-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_aggregator(input_yang_obj.aggregator, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as_path(input_yang_obj.as_path, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes_as4_path(input_yang_obj.as4_path, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set(input_yang_obj, translated_yang_obj=None):
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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets_attr_set_attr_set_attributes(input_yang_obj.attr_set_attributes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_attr_sets(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities_community(input_yang_obj, translated_yang_obj=None):
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
    
    if input_yang_obj.community._changed():
        input_yang_obj.community = input_yang_obj.community
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_communities(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities_ext_community(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_ext_communities(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    if input_yang_obj.best_path._changed():
        input_yang_obj.best_path = input_yang_obj.best_path
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-pre

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_pre(input_yang_obj.adj_rib_in_pre, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_in_post(input_yang_obj.adj_rib_in_post, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_pre(input_yang_obj.adj_rib_out_pre, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor_adj_rib_out_post(input_yang_obj.adj_rib_out_post, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_loc_rib(input_yang_obj.loc_rib, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast_neighbors(input_yang_obj.neighbors, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    if input_yang_obj.best_path._changed():
        input_yang_obj.best_path = input_yang_obj.best_path
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-pre

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes_unknown_attribute(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/route/unknown-attributes/unknown-attribute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.optional._changed():
        input_yang_obj.optional = input_yang_obj.optional
        
    if input_yang_obj.transitive._changed():
        input_yang_obj.transitive = input_yang_obj.transitive
        
    if input_yang_obj.partial._changed():
        input_yang_obj.partial = input_yang_obj.partial
        
    if input_yang_obj.extended._changed():
        input_yang_obj.extended = input_yang_obj.extended
        
    if input_yang_obj.attr_len._changed():
        input_yang_obj.attr_len = input_yang_obj.attr_len
        
    if input_yang_obj.attr_value._changed():
        input_yang_obj.attr_value = input_yang_obj.attr_value
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/route/unknown-attributes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unknown_attribute.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes_unknown_attribute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.attr_index._changed():
        input_yang_obj.attr_index = input_yang_obj.attr_index
        
    if input_yang_obj.community_index._changed():
        input_yang_obj.community_index = input_yang_obj.community_index
        
    if input_yang_obj.ext_community_index._changed():
        input_yang_obj.ext_community_index = input_yang_obj.ext_community_index
        
    if input_yang_obj.last_modified._changed():
        input_yang_obj.last_modified = input_yang_obj.last_modified
        
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.invalid_reason._changed():
        input_yang_obj.invalid_reason = input_yang_obj.invalid_reason
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route_unknown_attributes(input_yang_obj.unknown_attributes, translated_yang_obj)
        
    if input_yang_obj.reject_reason._changed():
        input_yang_obj.reject_reason = input_yang_obj.reject_reason
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear_input(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear/input

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear_output(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear/output

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes_clear(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes/clear

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/clear-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_route(listInst, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes_clear_routes(input_yang_obj.clear_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_pre(input_yang_obj.adj_rib_in_pre, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_in_post(input_yang_obj.adj_rib_in_post, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_pre(input_yang_obj.adj_rib_out_pre, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor_adj_rib_out_post(input_yang_obj.adj_rib_out_post, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_loc_rib(input_yang_obj.loc_rib, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast_neighbors(input_yang_obj.neighbors, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi(input_yang_obj, translated_yang_obj=None):
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
    
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis_afi_safi_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib_afi_safis(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp_rib(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_control_plane_protocols_control_plane_protocol_bgp(input_yang_obj, translated_yang_obj=None):
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
    if hasattr(translated_yang_obj,"bgp"):
        translated_yang_obj.bgp.global_.yang_enable = "true"
        translated_yang_obj.bgp.base_process.enable = "true"
        translated_yang_obj.bgp.base_process.as_ = str(input_yang_obj.global_.as_)
    else:
        interface_obj = translated_yang_obj.network_instance.instances.instance.add(name="_pubilc_")
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_global(input_yang_obj.global_, interface_obj)
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp_neighbors(input_yang_obj.neighbors, interface_obj)

    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol(input_yang_obj, translated_yang_obj=None):
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
    
    # if input_yang_obj.description._changed():
    #     input_yang_obj.description = input_yang_obj.description
        
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_bgp(input_yang_obj.bgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols(input_yang_obj, translated_yang_obj=None):
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
    
    for k, listInst in input_yang_obj.control_plane_protocol.iteritems():
        if listInst.type == "bgp:bgp":
            innerobj = _translate__routing_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)

    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_routes_route_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_routes_route(input_yang_obj, translated_yang_obj=None):
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
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route_output_route_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route_output_route(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route_output(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib_active_route(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs_rib(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_ribs(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing(input_yang_obj, translated_yang_obj=None):
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

    innerobj = _translate__routing_control_plane_protocols(input_yang_obj.control_plane_protocols, translated_yang_obj)

    return translated_yang_obj

def _translate__routing_state_interfaces(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_control_plane_protocols_control_plane_protocol(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_control_plane_protocols(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_routes_route_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_routes_route(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_routes(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route_output_route(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route_output(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib_active_route(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs_rib(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state_ribs(input_yang_obj, translated_yang_obj=None):
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

def _translate__routing_state(input_yang_obj, translated_yang_obj=None):
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

def _translate__ietf_routing(input_yang_obj, translated_yang_obj=None):
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
    
    trans_yang_list=[]

    # huwei_bgp
    translated_yang_obj = huawei_bgp()
    _translate__routing(input_yang_obj.routing, translated_yang_obj)
    trans_yang_list.append(translated_yang_obj.bgp)

    huawei_network_instance
    translated_yang_obj1 = huawei_network_instance()
    _translate__routing(input_yang_obj.routing,translated_yang_obj1)
    trans_yang_list.append(translated_yang_obj1.network_instance)


    return trans_yang_list
