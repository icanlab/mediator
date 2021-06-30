from lxml import etree

from mediator_server.yang_bindings.src_yang_bindings.ietf_network_instance_schema_mount_binding import *
from mediator_server.yang_bindings.target_yang_bindings.huawei_network_instance_sm_binding import *


class XPATH(etree.XPath):
  def __init__(self, path, namespaces=None):
    super(XPATH, self).__init__(path, namespaces=namespaces)
    self.namespaces = namespaces

def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces_interface(
  input_yang_obj: yc_interface_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces_interface,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
  For ex:
      To add a srv6 locator instance:
          loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

      To iterate over list instances:
          for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
              -- Use this for APP business logic.

  We need to add translation logic only for non-key leaves.
  Keys are already added as part of yang list instance creation
  """

  if input_yang_obj.interface_type._changed():
    input_yang_obj.interface_type = input_yang_obj.interface_type

  if input_yang_obj.passive._changed():
    input_yang_obj.passive = input_yang_obj.passive

  if input_yang_obj.demand_circuit._changed():
    input_yang_obj.demand_circuit = input_yang_obj.demand_circuit

  if input_yang_obj.priority._changed():
    input_yang_obj.priority = input_yang_obj.priority


  if input_yang_obj.node_flag._changed():
    input_yang_obj.node_flag = input_yang_obj.node_flag

  if input_yang_obj.hello_interval._changed():
    input_yang_obj.hello_interval = input_yang_obj.hello_interval

  if input_yang_obj.dead_interval._changed():
    input_yang_obj.dead_interval = input_yang_obj.dead_interval

  if input_yang_obj.retransmit_interval._changed():
    input_yang_obj.retransmit_interval = input_yang_obj.retransmit_interval

  if input_yang_obj.transmit_delay._changed():
    input_yang_obj.transmit_delay = input_yang_obj.transmit_delay

  if input_yang_obj.lls._changed():
    input_yang_obj.lls = input_yang_obj.lls

  if input_yang_obj.enable._changed():
    input_yang_obj.enable = input_yang_obj.enable

  if input_yang_obj.cost._changed():
    translated_yang_obj.cost = input_yang_obj.cost

  if input_yang_obj.mtu_ignore._changed():
    input_yang_obj.mtu_ignore = input_yang_obj.mtu_ignore

  if input_yang_obj.prefix_suppression._changed():
    input_yang_obj.prefix_suppression = input_yang_obj.prefix_suppression

  if input_yang_obj.state._changed():
    input_yang_obj.state = input_yang_obj.state

  if input_yang_obj.hello_timer._changed():
    input_yang_obj.hello_timer = input_yang_obj.hello_timer

  if input_yang_obj.wait_timer._changed():
    input_yang_obj.wait_timer = input_yang_obj.wait_timer

  if input_yang_obj.dr_router_id._changed():
    input_yang_obj.dr_router_id = input_yang_obj.dr_router_id

  if input_yang_obj.dr_ip_addr._changed():
    input_yang_obj.dr_ip_addr = input_yang_obj.dr_ip_addr

  if input_yang_obj.bdr_router_id._changed():
    input_yang_obj.bdr_router_id = input_yang_obj.bdr_router_id

  if input_yang_obj.bdr_ip_addr._changed():
    input_yang_obj.bdr_ip_addr = input_yang_obj.bdr_ip_addr

  if input_yang_obj.instance_id._changed():
    input_yang_obj.instance_id = input_yang_obj.instance_id

  if input_yang_obj.interface_id._changed():
    input_yang_obj.interface_id = input_yang_obj.interface_id

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces(
  input_yang_obj: yc_interfaces_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
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
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces_interface(listInst, interface_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges_range(
  input_yang_obj: yc_range_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges_range,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/topologies/topology/ranges/range

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
  For ex:
      To add a srv6 locator instance:
          loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

      To iterate over list instances:
          for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
              -- Use this for APP business logic.

  We need to add translation logic only for non-key leaves.
  Keys are already added as part of yang list instance creation
  """

  if input_yang_obj.advertise._changed():
    input_yang_obj.advertise = input_yang_obj.advertise

  if input_yang_obj.cost._changed():
    input_yang_obj.cost = input_yang_obj.cost

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges(
  input_yang_obj: yc_ranges_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/topologies/topology/ranges

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
  For ex:
      To add a srv6 locator instance:
          loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

      To iterate over list instances:
          for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
              -- Use this for APP business logic.

  We need to add translation logic only for non-key leaves.
  Keys are already added as part of yang list instance creation
  """

  for k, listInst in input_yang_obj.range.iteritems():
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges_range(
      listInst, translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology(
  input_yang_obj: yc_topology_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/topologies/topology

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
  For ex:
      To add a srv6 locator instance:
          loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

      To iterate over list instances:
          for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
              -- Use this for APP business logic.

  We need to add translation logic only for non-key leaves.
  Keys are already added as part of yang list instance creation
  """

  if input_yang_obj.summary._changed():
    input_yang_obj.summary = input_yang_obj.summary

  if input_yang_obj.default_cost._changed():
    input_yang_obj.default_cost = input_yang_obj.default_cost

  innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology_ranges(
    input_yang_obj.ranges, translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies(
  input_yang_obj: yc_topologies_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/topologies

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
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
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_topologies_topology(
      listInst, translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area(
  input_yang_obj: yc_area_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas/area

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
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

  if input_yang_obj.summary._changed():
    input_yang_obj.summary = input_yang_obj.summary

  if input_yang_obj.default_cost._changed():
    input_yang_obj.default_cost = input_yang_obj.default_cost

  innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area_interfaces(
    input_yang_obj.interfaces, translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas(
  input_yang_obj: yc_areas_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf_areas,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf/areas

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
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
    area_obj = translated_yang_obj.areas.area.add(k)
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas_area(listInst,
                                                                                                  area_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol_ospf(
  input_yang_obj: yc_ospf_ietf_routing__routing_control_plane_protocols_control_plane_protocol_ospf,
  translated_yang_obj=None):
  """
  Translate method. This can only be called after object pointing to "self" is instantiated.
  This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol/ospf

  Most of the times, for each yang list instance in the source, we may need to create
  a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
  instance.
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

  if input_yang_obj.enable._changed():
    input_yang_obj.enable = input_yang_obj.enable

  if input_yang_obj.explicit_router_id._changed():
    input_yang_obj.explicit_router_id = input_yang_obj.explicit_router_id

  if input_yang_obj.router_id._changed():
    input_yang_obj.router_id = input_yang_obj.router_id

  innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf_areas(input_yang_obj.areas,
                                                                                           translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols_control_plane_protocol(
  input_yang_obj: yc_control_plane_protocol_ietf_routing__routing_control_plane_protocols_control_plane_protocol,
  translated_yang_obj=None):
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

  innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf(input_yang_obj.ospf,
                                                                                     translated_yang_obj)

  return translated_yang_obj


def _translate__routing_control_plane_protocols(
  input_yang_obj: yc_control_plane_protocols_ietf_routing__routing_control_plane_protocols, translated_yang_obj=None):
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
    innerobj = _translate__routing_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)

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

  site_obj = translated_yang_obj.ospfv2.sites.site.add("1")

  if input_yang_obj.router_id._changed():
    site_obj.router_id = input_yang_obj.router_id
  else:
    innerobj = _translate__routing_control_plane_protocols(input_yang_obj.control_plane_protocols, site_obj)

  return translated_yang_obj


def _translate__network_instances_network_instance_vrf_root(input_yang_obj: yc_vrf_root_ietf_network_instance__network_instances_network_instance_vrf_root, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances/network-instance/vrf-root

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    innerobj = _translate__routing(input_yang_obj.routing, translated_yang_obj)

    return translated_yang_obj


def _translate__network_instances_network_instance(input_yang_obj: yc_network_instance_ietf_network_instance__network_instances_network_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances/network-instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description

    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.vrf_root, translated_yang_obj)


    return translated_yang_obj

def _translate__network_instances(input_yang_obj: yc_network_instances_ietf_network_instance__network_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    for k, listInst in input_yang_obj.network_instance.iteritems():
        instance_obj = translated_yang_obj.network_instance.instances.instance.add(k)
        innerobj = _translate__network_instances_network_instance(listInst, instance_obj)

    return translated_yang_obj

def _translate__ietf_network_instance(input_yang_obj: ietf_network_instance, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-network-instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("ni schema mount script")
    xpath = "/a:network-instance"
    ns_map = {"a": "urn:huawei:yang:huawei-network-instance"}
    target_xpath = XPATH(xpath, ns_map)
    translated_yang_obj = huawei_network_instance()
    innerobj = _translate__network_instances(input_yang_obj.network_instances, translated_yang_obj)

    return [[translated_yang_obj, target_xpath]]
