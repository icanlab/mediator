from lxml import etree

from mediator_server.yang_bindings.src_yang_bindings.ietf_network_instance_schema_mount_binding import *
from mediator_server.yang_bindings.target_yang_bindings.huawei_network_instance_sm_binding import *

class XPATH(etree.XPath):
    def __init__(self, path, namespaces=None):
        super(XPATH, self).__init__(path, namespaces=namespaces)
        self.namespaces = namespaces

def _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces_interface(input_yang_obj: yc_interface_huawei_network_instance__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces_interface,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites/site/areas/area/interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    if input_yang_obj.network_type._changed():
        input_yang_obj.network_type = input_yang_obj.network_type

    if input_yang_obj.peer_ip_ignore._changed():
        input_yang_obj.peer_ip_ignore = input_yang_obj.peer_ip_ignore

    if input_yang_obj.transmit_delay._changed():
        input_yang_obj.transmit_delay = input_yang_obj.transmit_delay

    if input_yang_obj.mtu_enable._changed():
        input_yang_obj.mtu_enable = input_yang_obj.mtu_enable

    if input_yang_obj.dr_priority._changed():
        input_yang_obj.dr_priority = input_yang_obj.dr_priority

    if input_yang_obj.cost._changed():
        translated_yang_obj.cost = input_yang_obj.cost

    if input_yang_obj.smart_discover._changed():
        input_yang_obj.smart_discover = input_yang_obj.smart_discover

    if input_yang_obj.p2mp_mask_ignore._changed():
        input_yang_obj.p2mp_mask_ignore = input_yang_obj.p2mp_mask_ignore

    if input_yang_obj.ldp_sync_block._changed():
        input_yang_obj.ldp_sync_block = input_yang_obj.ldp_sync_block

    if input_yang_obj.ldp_sync_enable._changed():
        input_yang_obj.ldp_sync_enable = input_yang_obj.ldp_sync_enable

    if input_yang_obj.link_cost._changed():
        input_yang_obj.link_cost = input_yang_obj.link_cost

    if input_yang_obj.suppress_reachability._changed():
        input_yang_obj.suppress_reachability = input_yang_obj.suppress_reachability

    if input_yang_obj.mpls_ldp_auto_flag._changed():
        input_yang_obj.mpls_ldp_auto_flag = input_yang_obj.mpls_ldp_auto_flag

    if input_yang_obj.dcn_opq_blk_enable._changed():
        input_yang_obj.dcn_opq_blk_enable = input_yang_obj.dcn_opq_blk_enable

    if input_yang_obj.peer_hold_max_timer._changed():
        input_yang_obj.peer_hold_max_timer = input_yang_obj.peer_hold_max_timer

    if input_yang_obj.fallback_cost._changed():
        input_yang_obj.fallback_cost = input_yang_obj.fallback_cost

    if input_yang_obj.fallback_bw._changed():
        input_yang_obj.fallback_bw = input_yang_obj.fallback_bw

    if input_yang_obj.source_sub_ip_address._changed():
        input_yang_obj.source_sub_ip_address = input_yang_obj.source_sub_ip_address

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces(input_yang_obj: yc_interfaces_huawei_network_instance__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites/site/areas/area/interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        interface_obj = translated_yang_obj.interfaces.interface.add(k)
        innerobj = _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces_interface(listInst, interface_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area(input_yang_obj: yc_area_huawei_network_instance__network_instance_instances_instance_ospfv2_sites_site_areas_area,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites/site/areas/area

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    if input_yang_obj.area_type._changed():
        input_yang_obj.area_type = input_yang_obj.area_type

    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description

    innerobj = _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area_interfaces(input_yang_obj.interfaces, translated_yang_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2_sites_site_areas(input_yang_obj: yc_areas_huawei_network_instance__network_instance_instances_instance_ospfv2_sites_site_areas,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites/site/areas

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    for k, listInst in input_yang_obj.area.iteritems():
        area_obj = translated_yang_obj.ospf.areas.area.add(k)
        translated_yang_obj.ospf.address_family = "ipv4"
        innerobj = _translate__network_instance_instances_instance_ospfv2_sites_site_areas_area(listInst, area_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2_sites_site(input_yang_obj: yc_site_huawei_network_instance__network_instance_instances_instance_ospfv2_sites_site, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites/site

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

    control_plane_protocol_obj = None

    if hasattr(translated_yang_obj, "vrf_root"):
        translated_yang_obj.vrf_root.routing.router_id = input_yang_obj.router_id
        control_plane_protocol_obj = translated_yang_obj.vrf_root.routing.control_plane_protocols.control_plane_protocol.add(name="1", type="ospf")
    else:
        translated_yang_obj.routing.router_id = input_yang_obj.router_id
        control_plane_protocol_obj = translated_yang_obj.routing.control_plane_protocols.control_plane_protocol.add(name="1", type="ospf")

    innerobj = _translate__network_instance_instances_instance_ospfv2_sites_site_areas(input_yang_obj.areas, control_plane_protocol_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2_sites(input_yang_obj: yc_sites_huawei_network_instance__network_instance_instances_instance_ospfv2_sites,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2/sites

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    for k, listInst in input_yang_obj.site.iteritems():
        innerobj = _translate__network_instance_instances_instance_ospfv2_sites_site(listInst, translated_yang_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance_ospfv2(input_yang_obj: yc_ospfv2_huawei_network_instance__network_instance_instances_instance_ospfv2,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    innerobj = _translate__network_instance_instances_instance_ospfv2_sites(input_yang_obj.sites, translated_yang_obj)

    return translated_yang_obj

def _translate__network_instance_instances_instance(input_yang_obj: yc_instance_huawei_network_instance__network_instance_instances_instance,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

    if input_yang_obj.sys_router_id._changed():
        input_yang_obj.sys_router_id = input_yang_obj.sys_router_id

    if input_yang_obj.vrf_id._changed():
        input_yang_obj.vrf_id = input_yang_obj.vrf_id

    if input_yang_obj.traffic_statistic_enable._changed():
        input_yang_obj.traffic_statistic_enable = input_yang_obj.traffic_statistic_enable

    innerobj = _translate__network_instance_instances_instance_ospfv2(input_yang_obj.ospfv2, translated_yang_obj)

    return translated_yang_obj

def _translate__network_instance_instances(input_yang_obj: yc_instances_huawei_network_instance__network_instance_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        print("the k is :", k)
        if k == '_public_':
            print("translate to ietf_routing!")
            translated_yang_obj = ietf_routing()
            xpath = '/a:routing'
            ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
            innerobj = _translate__network_instance_instances_instance(listInst, translated_yang_obj)
        else:
            print("translate to ietf_network_instance!")
            translated_yang_obj = ietf_network_instance()
            network_instance_obj = translated_yang_obj.network_instances.network_instance.add(k)
            xpath = '/a:network-instances'
            ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-network-instance'}
            innerobj = _translate__network_instance_instances_instance(listInst, network_instance_obj)
        target_xpath = XPATH(xpath, ns_map)
        for item in translated_yang_obj:
            if hasattr(translated_yang_obj, "routing"):
                translated_yang_obj = translated_yang_obj.routing
            elif hasattr(translated_yang_obj, "network_instances"):
                translated_yang_obj = translated_yang_obj.network_instances

    return [[translated_yang_obj, target_xpath]]

def _translate__network_instance(input_yang_obj: yc_network_instance_huawei_network_instance__network_instance,translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    res = _translate__network_instance_instances(input_yang_obj.instances, translated_yang_obj)

    return res

def _translate__huawei_network_instance(input_yang_obj: huawei_network_instance, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-network-instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("enter huawei network instance translation script!")
    res = _translate__network_instance(input_yang_obj.network_instance, translated_yang_obj)
    return res
