from lxml import etree

from mediator_server.translation_scripts.src2target._translate_ietf_ospf_obj import _translate__routing_control_plane_protocols_control_plane_protocol_ospf
from mediator_server.yang_bindings.src_yang_bindings.ietf_network_instance_schema_mount_binding import *
from mediator_server.yang_bindings.target_yang_bindings.huawei_network_instance_sm_binding import *

class XPATH(etree.XPath):
  def __init__(self, path, namespaces=None):
    super(XPATH, self).__init__(path, namespaces=namespaces)
    self.namespaces = namespaces

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

  innerobj = _translate__routing_control_plane_protocols_control_plane_protocol_ospf(input_yang_obj.ospf, translated_yang_obj)

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
    _translate__routing_control_plane_protocols(input_yang_obj.control_plane_protocols, site_obj)

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

    return [[translated_yang_obj.network_instance, target_xpath]]
