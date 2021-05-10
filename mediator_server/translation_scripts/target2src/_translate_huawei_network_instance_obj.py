from mediator_server.mediator_framework.adaptor import XPATH
from mediator_server.yang_bindings.src_yang_bindings.ietf_routing_binding import *
from mediator_server.yang_bindings.target_yang_bindings.huawei_bgp_binding import *
import re

def ipv62dec(ipv6):
    if checkipv6(ipv6):
        compressIndex = ipv6.find('::')
        #print("compressIndex:"+str(compressIndex))
        ipv4Index = ipv6.find('.')
        #print("ipv4Index:"+str(ipv4Index))
        if compressIndex==-1 and ipv4Index==-1:
            return noCompressipv62dec(ipv6)
        elif compressIndex!=-1 and ipv4Index==-1:
            return compressipv62dec(ipv6)
        elif compressIndex==-1 and ipv4Index!=-1:
            ipv4,ipv6=ipv4v6Split(ipv6)
            if ipv4 and ipv6:
                return str(int(ipv42dec(ipv4))+int(noCompressipv62dec(ipv6)))
            else:
                return ""
        elif compressIndex != -1 and ipv4Index != -1:
            ipv4, ipv6 = ipv4v6Split(ipv6)
            if ipv4 and ipv6:
                return str(int(ipv42dec(ipv4))+int(compressipv62dec(ipv6)))
            else:
                return ""
        else:
            return ""
    else:
        return ""


def ipv42dec(ip):
    dec_value = 0
    v_list = ip.split('.')
    v_list.reverse()
    t = 1
    for v in v_list:
        dec_value += int(v) * t
        t = t * (2 ** 8)
    return dec_value


def ipseg2str(ipseglist):
    ipstr=''
    for ipseg in ipseglist:
        if len(ipseg) == 1:
            ipseg = '000' + ipseg
        elif len(ipseg) == 2:
            ipseg = '00' + ipseg
        elif len(ipseg) == 3:
            ipseg = '0' + ipseg
        elif len(ipseg) == 4:
            ipseg = ipseg
        else:
            return ""
        ipstr += ipseg
    return ipstr


def noCompressipv62dec(ipv6):
    iplist = ipv6.split(":")
    if iplist:
        ipstr = ipseg2str(iplist)
        #print(ipstr)
        return int(ipstr, 16)
    else:
        return ""


def compressipv62dec(ipv6):
    compressList = ipv6.split("::")
    #print("compressList:" + str(compressList))
    ipstr = ""
    part1 = []
    part2 = []
    if len(compressList) == 2:
        part1 = compressList[0].split(":") if compressList[0] else []
        part2 = compressList[1].split(":") if compressList[1] else []
    if part1 or part2:
        ipstr += ipseg2str(part1)
        for i in range(8 - len(part1) - len(part2)):
            ipstr += '0000'
        ipstr += ipseg2str(part2)
        #print("ipstr:" + ipstr)
        return int(ipstr, 16)
    else:
        return ""


def ipv4v6Split(ipv6):
    ipv4str = ''
    ipv6str = ''
    if checkipv6(ipv6):
        list = ipv6.split(":")
        if list:
            ipv4str = list[len(list) - 1]
            list.pop()
            ipv6str = ":".join(list) + ":0000:0000"
            #print("ipv4:" + ipv4str)
            #print("ipv6:" + ipv6str)
    return ipv4str,ipv6str


def checkipv6(ipv6):
    matchobj = re.match(r'^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$',ipv6)
    if matchobj:
        return True
    else:
        return False

def _translate__network_instance_global(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/global

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.cfg_router_id._changed():
        input_yang_obj.cfg_router_id = input_yang_obj.cfg_router_id
        
    if input_yang_obj.as_notation_plain._changed():
        input_yang_obj.as_notation_plain = input_yang_obj.as_notation_plain
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_vpn_targets_vpn_target(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/vpn-targets/vpn-target

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_afs_af_vpn_targets(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/vpn-targets

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.vpn_target.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af_vpn_targets_vpn_target(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.create_time._changed():
        input_yang_obj.create_time = input_yang_obj.create_time
        
    if input_yang_obj.up_time._changed():
        input_yang_obj.up_time = input_yang_obj.up_time
        
    if input_yang_obj.label._changed():
        input_yang_obj.label = input_yang_obj.label
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_option(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/option

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.frr_enable._changed():
        input_yang_obj.frr_enable = input_yang_obj.frr_enable
        
    if input_yang_obj.prefix_limit_number._changed():
        input_yang_obj.prefix_limit_number = input_yang_obj.prefix_limit_number
        
    if input_yang_obj.prefix_alert_percent._changed():
        input_yang_obj.prefix_alert_percent = input_yang_obj.prefix_alert_percent
        
    if input_yang_obj.route_unchanged._changed():
        input_yang_obj.route_unchanged = input_yang_obj.route_unchanged
        
    if input_yang_obj.prefix_simply_alert._changed():
        input_yang_obj.prefix_simply_alert = input_yang_obj.prefix_simply_alert
        
    if input_yang_obj.route_limit_number._changed():
        input_yang_obj.route_limit_number = input_yang_obj.route_limit_number
        
    if input_yang_obj.route_alert_percent._changed():
        input_yang_obj.route_alert_percent = input_yang_obj.route_alert_percent
        
    if input_yang_obj.route_simply_alert._changed():
        input_yang_obj.route_simply_alert = input_yang_obj.route_simply_alert
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes_ipv4_unicast_routes_ipv4_unicast_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/topologys/topology/routes/ipv4-unicast-routes/ipv4-unicast-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.nexthop._changed():
        input_yang_obj.nexthop = input_yang_obj.nexthop
        
    if input_yang_obj.frr_type._changed():
        input_yang_obj.frr_type = input_yang_obj.frr_type
        
    if input_yang_obj.preference._changed():
        input_yang_obj.preference = input_yang_obj.preference
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.flag._changed():
        input_yang_obj.flag = input_yang_obj.flag
        
    if input_yang_obj.qos_id._changed():
        input_yang_obj.qos_id = input_yang_obj.qos_id
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.label._changed():
        input_yang_obj.label = input_yang_obj.label
        
    if input_yang_obj.indirect_id._changed():
        input_yang_obj.indirect_id = input_yang_obj.indirect_id
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    if input_yang_obj.neighbour._changed():
        input_yang_obj.neighbour = input_yang_obj.neighbour
        
    if input_yang_obj.age._changed():
        input_yang_obj.age = input_yang_obj.age
        
    if input_yang_obj.sub_protocol_type._changed():
        input_yang_obj.sub_protocol_type = input_yang_obj.sub_protocol_type
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes_ipv4_unicast_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/topologys/topology/routes/ipv4-unicast-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_unicast_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes_ipv4_unicast_routes_ipv4_unicast_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/topologys/topology/routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes_ipv4_unicast_routes(input_yang_obj.ipv4_unicast_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/topologys/topology

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology_routes(input_yang_obj.routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage/topologys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_routing_manage(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/routing-manage

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_option(input_yang_obj.option, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage_topologys(input_yang_obj.topologys, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_direct_routing_import_ribs_import_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/direct-routing/import-ribs/import-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.filter_name._changed():
        input_yang_obj.filter_name = input_yang_obj.filter_name
        
    if input_yang_obj.filter_parameter._changed():
        input_yang_obj.filter_parameter = input_yang_obj.filter_parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_direct_routing_import_ribs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/direct-routing/import-ribs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_rib.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af_routing_direct_routing_import_ribs_import_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_direct_routing(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/direct-routing

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_direct_routing_import_ribs(input_yang_obj.import_ribs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing_import_ribs_import_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing/import-ribs/import-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    if input_yang_obj.filter_name._changed():
        input_yang_obj.filter_name = input_yang_obj.filter_name
        
    if input_yang_obj.filter_parameter._changed():
        input_yang_obj.filter_parameter = input_yang_obj.filter_parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing_import_ribs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing/import-ribs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_rib.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing_import_ribs_import_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing_unicast_routes_unicast_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing/unicast-routes/unicast-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.inherit_cost._changed():
        input_yang_obj.inherit_cost = input_yang_obj.inherit_cost
        
    if input_yang_obj.permanent._changed():
        input_yang_obj.permanent = input_yang_obj.permanent
        
    if input_yang_obj.no_advertise._changed():
        input_yang_obj.no_advertise = input_yang_obj.no_advertise
        
    if input_yang_obj.no_install._changed():
        input_yang_obj.no_install = input_yang_obj.no_install
        
    if input_yang_obj.relay_host_route._changed():
        input_yang_obj.relay_host_route = input_yang_obj.relay_host_route
        
    if input_yang_obj.dhcp_enable._changed():
        input_yang_obj.dhcp_enable = input_yang_obj.dhcp_enable
        
    if input_yang_obj.ldp_sync._changed():
        input_yang_obj.ldp_sync = input_yang_obj.ldp_sync
        
    if input_yang_obj.inter_protocol_ecmp._changed():
        input_yang_obj.inter_protocol_ecmp = input_yang_obj.inter_protocol_ecmp
        
    if input_yang_obj.session_name._changed():
        input_yang_obj.session_name = input_yang_obj.session_name
        
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing_unicast_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing/unicast-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.unicast_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing_unicast_routes_unicast_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing_route_frr_set(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing/route-frr-set

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.unicast_route_frr_enable._changed():
        input_yang_obj.unicast_route_frr_enable = input_yang_obj.unicast_route_frr_enable
        
    if input_yang_obj.multicast_route_frr_enable._changed():
        input_yang_obj.multicast_route_frr_enable = input_yang_obj.multicast_route_frr_enable
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing_static_routing(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing/static-routing

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing_import_ribs(input_yang_obj.import_ribs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing_unicast_routes(input_yang_obj.unicast_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing_route_frr_set(input_yang_obj.route_frr_set, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af_routing(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af/routing

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_routing_manage(input_yang_obj.routing_manage, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_direct_routing(input_yang_obj.direct_routing, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing_static_routing(input_yang_obj.static_routing, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.route_distinguisher._changed():
        input_yang_obj.route_distinguisher = input_yang_obj.route_distinguisher
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.export_policy_add_ert_first._changed():
        input_yang_obj.export_policy_add_ert_first = input_yang_obj.export_policy_add_ert_first
        
    if input_yang_obj.label_mode._changed():
        input_yang_obj.label_mode = input_yang_obj.label_mode
        
    if input_yang_obj.vpn_frr._changed():
        input_yang_obj.vpn_frr = input_yang_obj.vpn_frr
        
    if input_yang_obj.tunnel_policy._changed():
        input_yang_obj.tunnel_policy = input_yang_obj.tunnel_policy
        
    if input_yang_obj.transit_vpn._changed():
        input_yang_obj.transit_vpn = input_yang_obj.transit_vpn
        
    if input_yang_obj.lsp_operation._changed():
        input_yang_obj.lsp_operation = input_yang_obj.lsp_operation
        
    innerobj = _translate__network_instance_instances_instance_afs_af_vpn_targets(input_yang_obj.vpn_targets, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_state(input_yang_obj.state, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_afs_af_routing(input_yang_obj.routing, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.af.iteritems():
        innerobj = _translate__network_instance_instances_instance_afs_af(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_common_mpls_interfaces_mpls_interface(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/common/mpls-interfaces/mpls-interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mtu_value._changed():
        input_yang_obj.mtu_value = input_yang_obj.mtu_value
        
    if input_yang_obj.ldp_enable._changed():
        input_yang_obj.ldp_enable = input_yang_obj.ldp_enable
        
    if input_yang_obj.te_enable._changed():
        input_yang_obj.te_enable = input_yang_obj.te_enable
        
    if input_yang_obj.rsvp_te_enable._changed():
        input_yang_obj.rsvp_te_enable = input_yang_obj.rsvp_te_enable
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_common_mpls_interfaces(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/common/mpls-interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.mpls_interface.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_common_mpls_interfaces_mpls_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_common(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/common

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_mpls_common_mpls_interfaces(input_yang_obj.mpls_interfaces, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_authentication(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/authentication

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auth_mode._changed():
        input_yang_obj.auth_mode = input_yang_obj.auth_mode
        
    if input_yang_obj.md5_type._changed():
        input_yang_obj.md5_type = input_yang_obj.md5_type
        
    if input_yang_obj.md5_password._changed():
        input_yang_obj.md5_password = input_yang_obj.md5_password
        
    if input_yang_obj.keychain_name._changed():
        input_yang_obj.keychain_name = input_yang_obj.keychain_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces_interface_status(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/interfaces/interface/status

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.if_state._changed():
        input_yang_obj.if_state = input_yang_obj.if_state
        
    if input_yang_obj.label_distribution_mode._changed():
        input_yang_obj.label_distribution_mode = input_yang_obj.label_distribution_mode
        
    if input_yang_obj.negotiated_hello_hold_time._changed():
        input_yang_obj.negotiated_hello_hold_time = input_yang_obj.negotiated_hello_hold_time
        
    if input_yang_obj.effective_mtu._changed():
        input_yang_obj.effective_mtu = input_yang_obj.effective_mtu
        
    if input_yang_obj.auto_trigger_type._changed():
        input_yang_obj.auto_trigger_type = input_yang_obj.auto_trigger_type
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces_interface(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.hello_send_time._changed():
        input_yang_obj.hello_send_time = input_yang_obj.hello_send_time
        
    if input_yang_obj.hello_hold_time._changed():
        input_yang_obj.hello_hold_time = input_yang_obj.hello_hold_time
        
    if input_yang_obj.keep_alive_send_time._changed():
        input_yang_obj.keep_alive_send_time = input_yang_obj.keep_alive_send_time
        
    if input_yang_obj.keep_alive_hold_time._changed():
        input_yang_obj.keep_alive_hold_time = input_yang_obj.keep_alive_hold_time
        
    if input_yang_obj.igp_sync_delay_time._changed():
        input_yang_obj.igp_sync_delay_time = input_yang_obj.igp_sync_delay_time
        
    if input_yang_obj.mldp_p2mp_disable._changed():
        input_yang_obj.mldp_p2mp_disable = input_yang_obj.mldp_p2mp_disable
        
    if input_yang_obj.transport_address._changed():
        input_yang_obj.transport_address = input_yang_obj.transport_address
        
    if input_yang_obj.local_lsr_id_address._changed():
        input_yang_obj.local_lsr_id_address = input_yang_obj.local_lsr_id_address
        
    if input_yang_obj.label_advertise_mode._changed():
        input_yang_obj.label_advertise_mode = input_yang_obj.label_advertise_mode
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces_interface_status(input_yang_obj.status, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer_status_auto_create_type(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/remote-peers/remote-peer/status/auto-create-type

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.l2vpn._changed():
        input_yang_obj.l2vpn = input_yang_obj.l2vpn
        
    if input_yang_obj.session_protection._changed():
        input_yang_obj.session_protection = input_yang_obj.session_protection
        
    if input_yang_obj.rlfa._changed():
        input_yang_obj.rlfa = input_yang_obj.rlfa
        
    if input_yang_obj.auto_accept_function._changed():
        input_yang_obj.auto_accept_function = input_yang_obj.auto_accept_function
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer_status(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/remote-peers/remote-peer/status

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.remote_neighbor_state._changed():
        input_yang_obj.remote_neighbor_state = input_yang_obj.remote_neighbor_state
        
    if input_yang_obj.negotiated_hello_hold_time._changed():
        input_yang_obj.negotiated_hello_hold_time = input_yang_obj.negotiated_hello_hold_time
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer_status_auto_create_type(input_yang_obj.auto_create_type, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/remote-peers/remote-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.remote_ip._changed():
        input_yang_obj.remote_ip = input_yang_obj.remote_ip
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.no_mapping._changed():
        input_yang_obj.no_mapping = input_yang_obj.no_mapping
        
    if input_yang_obj.auto_dod_request_mode._changed():
        input_yang_obj.auto_dod_request_mode = input_yang_obj.auto_dod_request_mode
        
    if input_yang_obj.hello_send_time._changed():
        input_yang_obj.hello_send_time = input_yang_obj.hello_send_time
        
    if input_yang_obj.hello_hold_time._changed():
        input_yang_obj.hello_hold_time = input_yang_obj.hello_hold_time
        
    if input_yang_obj.keep_alive_send_time._changed():
        input_yang_obj.keep_alive_send_time = input_yang_obj.keep_alive_send_time
        
    if input_yang_obj.keep_alive_hold_time._changed():
        input_yang_obj.keep_alive_hold_time = input_yang_obj.keep_alive_hold_time
        
    if input_yang_obj.igp_sync_delay_time._changed():
        input_yang_obj.igp_sync_delay_time = input_yang_obj.igp_sync_delay_time
        
    if input_yang_obj.local_lsr_id_address._changed():
        input_yang_obj.local_lsr_id_address = input_yang_obj.local_lsr_id_address
        
    if input_yang_obj.label_advertise_mode._changed():
        input_yang_obj.label_advertise_mode = input_yang_obj.label_advertise_mode
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer_status(input_yang_obj.status, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/remote-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.remote_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers_remote_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_auth_peers_auth_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/auth-peers/auth-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.authen_enable._changed():
        input_yang_obj.authen_enable = input_yang_obj.authen_enable
        
    if input_yang_obj.authen_mode._changed():
        input_yang_obj.authen_mode = input_yang_obj.authen_mode
        
    if input_yang_obj.md5_type._changed():
        input_yang_obj.md5_type = input_yang_obj.md5_type
        
    if input_yang_obj.md5_password._changed():
        input_yang_obj.md5_password = input_yang_obj.md5_password
        
    if input_yang_obj.keychain_name._changed():
        input_yang_obj.keychain_name = input_yang_obj.keychain_name
        
    if input_yang_obj.out_bound._changed():
        input_yang_obj.out_bound = input_yang_obj.out_bound
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_auth_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/auth-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.auth_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_auth_peers_auth_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_session_protection(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/session-protection

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mode._changed():
        input_yang_obj.mode = input_yang_obj.mode
        
    if input_yang_obj.ip_prefix_name._changed():
        input_yang_obj.ip_prefix_name = input_yang_obj.ip_prefix_name
        
    if input_yang_obj.duration_type._changed():
        input_yang_obj.duration_type = input_yang_obj.duration_type
        
    if input_yang_obj.duration._changed():
        input_yang_obj.duration = input_yang_obj.duration
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_accept_target_hello(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/accept-target-hello

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.mode._changed():
        input_yang_obj.mode = input_yang_obj.mode
        
    if input_yang_obj.ip_prefix_name._changed():
        input_yang_obj.ip_prefix_name = input_yang_obj.ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_all(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/fec-peer-all

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_all(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/bgp-peer-all

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.bgp_policy_mode._changed():
        input_yang_obj.bgp_policy_mode = input_yang_obj.bgp_policy_mode
        
    if input_yang_obj.bgp_ip_prefix_name._changed():
        input_yang_obj.bgp_ip_prefix_name = input_yang_obj.bgp_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_groups_fec_peer_group(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/fec-peer-groups/fec-peer-group

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_groups(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/fec-peer-groups

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.fec_peer_group.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_groups_fec_peer_group(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_groups_bgp_peer_group(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/bgp-peer-groups/bgp-peer-group

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.bgp_policy_mode._changed():
        input_yang_obj.bgp_policy_mode = input_yang_obj.bgp_policy_mode
        
    if input_yang_obj.bgp_ip_prefix_name._changed():
        input_yang_obj.bgp_ip_prefix_name = input_yang_obj.bgp_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_groups(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/bgp-peer-groups

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.bgp_peer_group.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_groups_bgp_peer_group(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peers_fec_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/fec-peers/fec-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/fec-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.fec_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peers_fec_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peers_bgp_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/bgp-peers/bgp-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.bgp_policy_mode._changed():
        input_yang_obj.bgp_policy_mode = input_yang_obj.bgp_policy_mode
        
    if input_yang_obj.bgp_ip_prefix_name._changed():
        input_yang_obj.bgp_ip_prefix_name = input_yang_obj.bgp_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound/bgp-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.bgp_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peers_bgp_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/outbound

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_all(input_yang_obj.fec_peer_all, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_all(input_yang_obj.bgp_peer_all, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peer_groups(input_yang_obj.fec_peer_groups, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peer_groups(input_yang_obj.bgp_peer_groups, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_fec_peers(input_yang_obj.fec_peers, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound_bgp_peers(input_yang_obj.bgp_peers, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_all(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound/fec-peer-all

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_groups_fec_peer_group(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound/fec-peer-groups/fec-peer-group

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_groups(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound/fec-peer-groups

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.fec_peer_group.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_groups_fec_peer_group(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peers_fec_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound/fec-peers/fec-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fec_policy_mode._changed():
        input_yang_obj.fec_policy_mode = input_yang_obj.fec_policy_mode
        
    if input_yang_obj.fec_ip_prefix_name._changed():
        input_yang_obj.fec_ip_prefix_name = input_yang_obj.fec_ip_prefix_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound/fec-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.fec_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peers_fec_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance/inbound

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_all(input_yang_obj.fec_peer_all, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peer_groups(input_yang_obj.fec_peer_groups, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound_fec_peers(input_yang_obj.fec_peers, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances/topology-instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.topology_name._changed():
        input_yang_obj.topology_name = input_yang_obj.topology_name
        
    if input_yang_obj.lsp_transit_policy_name._changed():
        input_yang_obj.lsp_transit_policy_name = input_yang_obj.lsp_transit_policy_name
        
    if input_yang_obj.auto_frr_lsp_trigger_mode._changed():
        input_yang_obj.auto_frr_lsp_trigger_mode = input_yang_obj.auto_frr_lsp_trigger_mode
        
    if input_yang_obj.auto_frr_lsp_ip_prefix_name._changed():
        input_yang_obj.auto_frr_lsp_ip_prefix_name = input_yang_obj.auto_frr_lsp_ip_prefix_name
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_outbound(input_yang_obj.outbound, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance_inbound(input_yang_obj.inbound, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/topology-instances

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.topology_instance.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances_topology_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_adjacencys_adjacency(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/adjacencys/adjacency

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.create_date._changed():
        input_yang_obj.create_date = input_yang_obj.create_date
        
    if input_yang_obj.create_time._changed():
        input_yang_obj.create_time = input_yang_obj.create_time
        
    if input_yang_obj.age_time._changed():
        input_yang_obj.age_time = input_yang_obj.age_time
        
    if input_yang_obj.discovery_source_name._changed():
        input_yang_obj.discovery_source_name = input_yang_obj.discovery_source_name
        
    if input_yang_obj.udp_socket_id._changed():
        input_yang_obj.udp_socket_id = input_yang_obj.udp_socket_id
        
    if input_yang_obj.cfg_hello_hold_time._changed():
        input_yang_obj.cfg_hello_hold_time = input_yang_obj.cfg_hello_hold_time
        
    if input_yang_obj.sequence_no._changed():
        input_yang_obj.sequence_no = input_yang_obj.sequence_no
        
    if input_yang_obj.received_hello._changed():
        input_yang_obj.received_hello = input_yang_obj.received_hello
        
    if input_yang_obj.crc_error_rate._changed():
        input_yang_obj.crc_error_rate = input_yang_obj.crc_error_rate
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_adjacencys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/adjacencys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_adjacencys_adjacency(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_peer_infos_peer_info(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/peer-infos/peer-info

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.max_pdu_len._changed():
        input_yang_obj.max_pdu_len = input_yang_obj.max_pdu_len
        
    if input_yang_obj.loop_detect._changed():
        input_yang_obj.loop_detect = input_yang_obj.loop_detect
        
    if input_yang_obj.support_ft_flag._changed():
        input_yang_obj.support_ft_flag = input_yang_obj.support_ft_flag
        
    if input_yang_obj.transport_address._changed():
        input_yang_obj.transport_address = input_yang_obj.transport_address
        
    if input_yang_obj.path_vector_limit._changed():
        input_yang_obj.path_vector_limit = input_yang_obj.path_vector_limit
        
    if input_yang_obj.keep_alive_send_time._changed():
        input_yang_obj.keep_alive_send_time = input_yang_obj.keep_alive_send_time
        
    if input_yang_obj.recovery_timer._changed():
        input_yang_obj.recovery_timer = input_yang_obj.recovery_timer
        
    if input_yang_obj.reconnect_timer._changed():
        input_yang_obj.reconnect_timer = input_yang_obj.reconnect_timer
        
    if input_yang_obj.announcement_capability._changed():
        input_yang_obj.announcement_capability = input_yang_obj.announcement_capability
        
    if input_yang_obj.mldp_p2mp_capability._changed():
        input_yang_obj.mldp_p2mp_capability = input_yang_obj.mldp_p2mp_capability
        
    if input_yang_obj.mldp_mbb_capability._changed():
        input_yang_obj.mldp_mbb_capability = input_yang_obj.mldp_mbb_capability
        
    if input_yang_obj.discovery_source._changed():
        input_yang_obj.discovery_source = input_yang_obj.discovery_source
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_peer_infos(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/peer-infos

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.peer_info.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_peer_infos_peer_info(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_sessions_session(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/sessions/session

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.local_lsr_id._changed():
        input_yang_obj.local_lsr_id = input_yang_obj.local_lsr_id
        
    if input_yang_obj.tcp_source_address._changed():
        input_yang_obj.tcp_source_address = input_yang_obj.tcp_source_address
        
    if input_yang_obj.tcp_dest_address._changed():
        input_yang_obj.tcp_dest_address = input_yang_obj.tcp_dest_address
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.negotiate_keep_alive_hold_time._changed():
        input_yang_obj.negotiate_keep_alive_hold_time = input_yang_obj.negotiate_keep_alive_hold_time
        
    if input_yang_obj.keep_alive_sent._changed():
        input_yang_obj.keep_alive_sent = input_yang_obj.keep_alive_sent
        
    if input_yang_obj.keep_alive_received._changed():
        input_yang_obj.keep_alive_received = input_yang_obj.keep_alive_received
        
    if input_yang_obj.distribute_mode._changed():
        input_yang_obj.distribute_mode = input_yang_obj.distribute_mode
        
    if input_yang_obj.peer_label_state._changed():
        input_yang_obj.peer_label_state = input_yang_obj.peer_label_state
        
    if input_yang_obj.ft_flag._changed():
        input_yang_obj.ft_flag = input_yang_obj.ft_flag
        
    if input_yang_obj.md5_flag._changed():
        input_yang_obj.md5_flag = input_yang_obj.md5_flag
        
    if input_yang_obj.reconnet_time._changed():
        input_yang_obj.reconnet_time = input_yang_obj.reconnet_time
        
    if input_yang_obj.recovery_time._changed():
        input_yang_obj.recovery_time = input_yang_obj.recovery_time
        
    if input_yang_obj.age._changed():
        input_yang_obj.age = input_yang_obj.age
        
    if input_yang_obj.announcement_capability._changed():
        input_yang_obj.announcement_capability = input_yang_obj.announcement_capability
        
    if input_yang_obj.mldp_p2mp_capability._changed():
        input_yang_obj.mldp_p2mp_capability = input_yang_obj.mldp_p2mp_capability
        
    if input_yang_obj.mldp_mbb_capability._changed():
        input_yang_obj.mldp_mbb_capability = input_yang_obj.mldp_mbb_capability
        
    if input_yang_obj.msg_count_in_last_period._changed():
        input_yang_obj.msg_count_in_last_period = input_yang_obj.msg_count_in_last_period
        
    if input_yang_obj.over_run_period_count._changed():
        input_yang_obj.over_run_period_count = input_yang_obj.over_run_period_count
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_sessions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/sessions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.session.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_sessions_session(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_lsps_lsp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/lsps/lsp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.is_frr_lsp._changed():
        input_yang_obj.is_frr_lsp = input_yang_obj.is_frr_lsp
        
    if input_yang_obj.is_rlfa_lsp._changed():
        input_yang_obj.is_rlfa_lsp = input_yang_obj.is_rlfa_lsp
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    if input_yang_obj.time_stamp._changed():
        input_yang_obj.time_stamp = input_yang_obj.time_stamp
        
    if input_yang_obj.in_label._changed():
        input_yang_obj.in_label = input_yang_obj.in_label
        
    if input_yang_obj.out_label._changed():
        input_yang_obj.out_label = input_yang_obj.out_label
        
    if input_yang_obj.entropy_label_capability._changed():
        input_yang_obj.entropy_label_capability = input_yang_obj.entropy_label_capability
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_lsps(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/lsps

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_lsps_lsp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_fecs_fec(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/fecs/fec

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    if input_yang_obj.lsp._changed():
        input_yang_obj.lsp = input_yang_obj.lsp
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_fecs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/fecs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.fec.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_fecs_fec(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers_auto_config_remote_peer_auto_config_type(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/auto-config-remote-peers/auto-config-remote-peer/auto-config-type

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.l2vpn._changed():
        input_yang_obj.l2vpn = input_yang_obj.l2vpn
        
    if input_yang_obj.session_protection._changed():
        input_yang_obj.session_protection = input_yang_obj.session_protection
        
    if input_yang_obj.rlfa._changed():
        input_yang_obj.rlfa = input_yang_obj.rlfa
        
    if input_yang_obj.auto_accept_function._changed():
        input_yang_obj.auto_accept_function = input_yang_obj.auto_accept_function
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers_auto_config_remote_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/auto-config-remote-peers/auto-config-remote-peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.remote_peer_name._changed():
        input_yang_obj.remote_peer_name = input_yang_obj.remote_peer_name
        
    if input_yang_obj.peer_state._changed():
        input_yang_obj.peer_state = input_yang_obj.peer_state
        
    if input_yang_obj.negotiated_hello_hold_time._changed():
        input_yang_obj.negotiated_hello_hold_time = input_yang_obj.negotiated_hello_hold_time
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers_auto_config_remote_peer_auto_config_type(input_yang_obj.auto_config_type, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/auto-config-remote-peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.auto_config_remote_peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers_auto_config_remote_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance_instance_status(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance/instance-status

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.label_dist_mode._changed():
        input_yang_obj.label_dist_mode = input_yang_obj.label_dist_mode
        
    if input_yang_obj.label_retention_mode._changed():
        input_yang_obj.label_retention_mode = input_yang_obj.label_retention_mode
        
    if input_yang_obj.lsp_number._changed():
        input_yang_obj.lsp_number = input_yang_obj.lsp_number
        
    if input_yang_obj.session_number._changed():
        input_yang_obj.session_number = input_yang_obj.session_number
        
    if input_yang_obj.adjacency_number._changed():
        input_yang_obj.adjacency_number = input_yang_obj.adjacency_number
        
    if input_yang_obj.interface_number._changed():
        input_yang_obj.interface_number = input_yang_obj.interface_number
        
    if input_yang_obj.fec_number._changed():
        input_yang_obj.fec_number = input_yang_obj.fec_number
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp_instance(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp/instance

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.lsr_id._changed():
        input_yang_obj.lsr_id = input_yang_obj.lsr_id
        
    if input_yang_obj.igp_sync_delay_time._changed():
        input_yang_obj.igp_sync_delay_time = input_yang_obj.igp_sync_delay_time
        
    if input_yang_obj.graceful_delete_enable._changed():
        input_yang_obj.graceful_delete_enable = input_yang_obj.graceful_delete_enable
        
    if input_yang_obj.graceful_delete_time._changed():
        input_yang_obj.graceful_delete_time = input_yang_obj.graceful_delete_time
        
    if input_yang_obj.no_mapping_enable._changed():
        input_yang_obj.no_mapping_enable = input_yang_obj.no_mapping_enable
        
    if input_yang_obj.auto_dod_request_enable._changed():
        input_yang_obj.auto_dod_request_enable = input_yang_obj.auto_dod_request_enable
        
    if input_yang_obj.split_horizon._changed():
        input_yang_obj.split_horizon = input_yang_obj.split_horizon
        
    if input_yang_obj.send_all_loopback._changed():
        input_yang_obj.send_all_loopback = input_yang_obj.send_all_loopback
        
    if input_yang_obj.longest_match._changed():
        input_yang_obj.longest_match = input_yang_obj.longest_match
        
    if input_yang_obj.loop_detect._changed():
        input_yang_obj.loop_detect = input_yang_obj.loop_detect
        
    if input_yang_obj.label_ctrl_mode._changed():
        input_yang_obj.label_ctrl_mode = input_yang_obj.label_ctrl_mode
        
    if input_yang_obj.auto_remote_keep_alive_hold._changed():
        input_yang_obj.auto_remote_keep_alive_hold = input_yang_obj.auto_remote_keep_alive_hold
        
    if input_yang_obj.traffic_statistic_mode._changed():
        input_yang_obj.traffic_statistic_mode = input_yang_obj.traffic_statistic_mode
        
    if input_yang_obj.traffic_statistic_ip_prefix_name._changed():
        input_yang_obj.traffic_statistic_ip_prefix_name = input_yang_obj.traffic_statistic_ip_prefix_name
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_authentication(input_yang_obj.authentication, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_remote_peers(input_yang_obj.remote_peers, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_auth_peers(input_yang_obj.auth_peers, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_session_protection(input_yang_obj.session_protection, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_accept_target_hello(input_yang_obj.accept_target_hello, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_topology_instances(input_yang_obj.topology_instances, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_adjacencys(input_yang_obj.adjacencys, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_peer_infos(input_yang_obj.peer_infos, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_sessions(input_yang_obj.sessions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_lsps(input_yang_obj.lsps, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_fecs(input_yang_obj.fecs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_auto_config_remote_peers(input_yang_obj.auto_config_remote_peers, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance_instance_status(input_yang_obj.instance_status, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls_ldp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls/ldp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_mpls_ldp_instance(input_yang_obj.instance, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_mpls(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/mpls

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_mpls_common(input_yang_obj.common, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_mpls_ldp(input_yang_obj.ldp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsp_fragments_extend(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsp-fragments-extend

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_level1._changed():
        input_yang_obj.enable_level1 = input_yang_obj.enable_level1
        
    if input_yang_obj.enable_level2._changed():
        input_yang_obj.enable_level2 = input_yang_obj.enable_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_poi_tlv(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/poi-tlv

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.always._changed():
        input_yang_obj.always = input_yang_obj.always
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsdb_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsdb-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.max_number._changed():
        input_yang_obj.max_number = input_yang_obj.max_number
        
    if input_yang_obj.threshold_upper._changed():
        input_yang_obj.threshold_upper = input_yang_obj.threshold_upper
        
    if input_yang_obj.threshold_lower._changed():
        input_yang_obj.threshold_lower = input_yang_obj.threshold_lower
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_suppress_flapping_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/suppress-flapping/peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_suppress_flapping(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/suppress-flapping

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_suppress_flapping_peer(input_yang_obj.peer, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_timer_spf(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/timer/spf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.max_._changed():
        input_yang_obj.max_ = input_yang_obj.max_
        
    if input_yang_obj.init._changed():
        input_yang_obj.init = input_yang_obj.init
        
    if input_yang_obj.incr._changed():
        input_yang_obj.incr = input_yang_obj.incr
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_timer_lsp_generation(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/timer/lsp-generation

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.max_level1._changed():
        input_yang_obj.max_level1 = input_yang_obj.max_level1
        
    if input_yang_obj.max_level2._changed():
        input_yang_obj.max_level2 = input_yang_obj.max_level2
        
    if input_yang_obj.init_level1._changed():
        input_yang_obj.init_level1 = input_yang_obj.init_level1
        
    if input_yang_obj.init_level2._changed():
        input_yang_obj.init_level2 = input_yang_obj.init_level2
        
    if input_yang_obj.incr_level1._changed():
        input_yang_obj.incr_level1 = input_yang_obj.incr_level1
        
    if input_yang_obj.incr_level2._changed():
        input_yang_obj.incr_level2 = input_yang_obj.incr_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_timer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/timer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.lsp_max._changed():
        input_yang_obj.lsp_max = input_yang_obj.lsp_max
        
    if input_yang_obj.lsp_refresh._changed():
        input_yang_obj.lsp_refresh = input_yang_obj.lsp_refresh
        
    if input_yang_obj.purge_lsp_delay._changed():
        input_yang_obj.purge_lsp_delay = input_yang_obj.purge_lsp_delay
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_timer_spf(input_yang_obj.spf, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_timer_lsp_generation(input_yang_obj.lsp_generation, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsp_length(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsp-length

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.originate_level1._changed():
        input_yang_obj.originate_level1 = input_yang_obj.originate_level1
        
    if input_yang_obj.originate_level2._changed():
        input_yang_obj.originate_level2 = input_yang_obj.originate_level2
        
    if input_yang_obj.receive._changed():
        input_yang_obj.receive = input_yang_obj.receive
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_flash_flood(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/flash-flood

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_level1._changed():
        input_yang_obj.enable_level1 = input_yang_obj.enable_level1
        
    if input_yang_obj.enable_level2._changed():
        input_yang_obj.enable_level2 = input_yang_obj.enable_level2
        
    if input_yang_obj.lsp_num_level1._changed():
        input_yang_obj.lsp_num_level1 = input_yang_obj.lsp_num_level1
        
    if input_yang_obj.lsp_num_level2._changed():
        input_yang_obj.lsp_num_level2 = input_yang_obj.lsp_num_level2
        
    if input_yang_obj.max_timer_level1._changed():
        input_yang_obj.max_timer_level1 = input_yang_obj.max_timer_level1
        
    if input_yang_obj.max_timer_level2._changed():
        input_yang_obj.max_timer_level2 = input_yang_obj.max_timer_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_set_overload(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/set-overload

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.wait_type._changed():
        input_yang_obj.wait_type = input_yang_obj.wait_type
        
    if input_yang_obj.nbr_system_id._changed():
        input_yang_obj.nbr_system_id = input_yang_obj.nbr_system_id
        
    if input_yang_obj.timeout1._changed():
        input_yang_obj.timeout1 = input_yang_obj.timeout1
        
    if input_yang_obj.timeout2._changed():
        input_yang_obj.timeout2 = input_yang_obj.timeout2
        
    if input_yang_obj.inter_level._changed():
        input_yang_obj.inter_level = input_yang_obj.inter_level
        
    if input_yang_obj.external._changed():
        input_yang_obj.external = input_yang_obj.external
        
    if input_yang_obj.send_sa_bit._changed():
        input_yang_obj.send_sa_bit = input_yang_obj.send_sa_bit
        
    if input_yang_obj.sa_bit_time._changed():
        input_yang_obj.sa_bit_time = input_yang_obj.sa_bit_time
        
    if input_yang_obj.rt_delay_time._changed():
        input_yang_obj.rt_delay_time = input_yang_obj.rt_delay_time
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsp_lifetime(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsp-lifetime

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.max_age._changed():
        input_yang_obj.max_age = input_yang_obj.max_age
        
    if input_yang_obj.value._changed():
        input_yang_obj.value = input_yang_obj.value
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_bgp_ls(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/bgp-ls

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_level1._changed():
        input_yang_obj.enable_level1 = input_yang_obj.enable_level1
        
    if input_yang_obj.enable_level2._changed():
        input_yang_obj.enable_level2 = input_yang_obj.enable_level2
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_extern_ability(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/extern-ability

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.adj_strict_check._changed():
        input_yang_obj.adj_strict_check = input_yang_obj.adj_strict_check
        
    if input_yang_obj.ecmp_prefer._changed():
        input_yang_obj.ecmp_prefer = input_yang_obj.ecmp_prefer
        
    if input_yang_obj.opt_checksum._changed():
        input_yang_obj.opt_checksum = input_yang_obj.opt_checksum
        
    if input_yang_obj.virtual_cluster._changed():
        input_yang_obj.virtual_cluster = input_yang_obj.virtual_cluster
        
    if input_yang_obj.virtual_access._changed():
        input_yang_obj.virtual_access = input_yang_obj.virtual_access
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_srgbs_srgb(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/srgbs/srgb

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_srgbs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/srgbs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srgb.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_srgbs_srgb(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_net_entitys_net_entity(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/net-entitys/net-entity

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.isis.system_id = input_yang_obj.value[3:17]
    translated_yang_obj.isis.maximum_area_addresses = 3
    translated_yang_obj.isis.area_address = input_yang_obj.value[0:2]

    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_net_entitys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/net-entitys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.net_entity.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_net_entitys_net_entity(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsp_auths_lsp_auth(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsp-auths/lsp-auth

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.pw_type._changed():
        input_yang_obj.pw_type = input_yang_obj.pw_type
        
    if input_yang_obj.simple._changed():
        input_yang_obj.simple = input_yang_obj.simple
        
    if input_yang_obj.md5._changed():
        input_yang_obj.md5 = input_yang_obj.md5
        
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.service._changed():
        input_yang_obj.service = input_yang_obj.service
        
    if input_yang_obj.usage._changed():
        input_yang_obj.usage = input_yang_obj.usage
        
    if input_yang_obj.key_id._changed():
        input_yang_obj.key_id = input_yang_obj.key_id
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsp_auths(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsp-auths

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.lsp_auth.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsp_auths_lsp_auth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_srlgs_srlg(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/srlgs/srlg

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_srlgs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/srlgs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srlg.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_srlgs_srlg(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_mesh_group(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/mesh-group

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_suppress_flapping_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/suppress-flapping/peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.detect_interval._changed():
        input_yang_obj.detect_interval = input_yang_obj.detect_interval
        
    if input_yang_obj.threshold._changed():
        input_yang_obj.threshold = input_yang_obj.threshold
        
    if input_yang_obj.resume_interval._changed():
        input_yang_obj.resume_interval = input_yang_obj.resume_interval
        
    if input_yang_obj.hold_down._changed():
        input_yang_obj.hold_down = input_yang_obj.hold_down
        
    if input_yang_obj.hold_max_cost._changed():
        input_yang_obj.hold_max_cost = input_yang_obj.hold_max_cost
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_suppress_flapping(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/suppress-flapping

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_suppress_flapping_peer(input_yang_obj.peer, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_timer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/timer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.csnp_interval_level1._changed():
        input_yang_obj.csnp_interval_level1 = input_yang_obj.csnp_interval_level1
        
    if input_yang_obj.csnp_interval_level2._changed():
        input_yang_obj.csnp_interval_level2 = input_yang_obj.csnp_interval_level2
        
    if input_yang_obj.throttle_interval._changed():
        input_yang_obj.throttle_interval = input_yang_obj.throttle_interval
        
    if input_yang_obj.throttle_count._changed():
        input_yang_obj.throttle_count = input_yang_obj.throttle_count
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_broadcast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/broadcast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.dis_priority_level1._changed():
        input_yang_obj.dis_priority_level1 = input_yang_obj.dis_priority_level1
        
    if input_yang_obj.dis_priority_level2._changed():
        input_yang_obj.dis_priority_level2 = input_yang_obj.dis_priority_level2
        
    if input_yang_obj.hello_timer_level1._changed():
        input_yang_obj.hello_timer_level1 = input_yang_obj.hello_timer_level1
        
    if input_yang_obj.hello_timer_level2._changed():
        input_yang_obj.hello_timer_level2 = input_yang_obj.hello_timer_level2
        
    if input_yang_obj.hold_multiplier_level1._changed():
        input_yang_obj.hold_multiplier_level1 = input_yang_obj.hold_multiplier_level1
        
    if input_yang_obj.hold_multiplier_level2._changed():
        input_yang_obj.hold_multiplier_level2 = input_yang_obj.hold_multiplier_level2
        
    if input_yang_obj.conser_level1._changed():
        input_yang_obj.conser_level1 = input_yang_obj.conser_level1
        
    if input_yang_obj.conser_level2._changed():
        input_yang_obj.conser_level2 = input_yang_obj.conser_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_p2p(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/p2p

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.snpa_check._changed():
        input_yang_obj.snpa_check = input_yang_obj.snpa_check
        
    if input_yang_obj.peer_ip_ignore._changed():
        input_yang_obj.peer_ip_ignore = input_yang_obj.peer_ip_ignore
        
    if input_yang_obj.ppp_negotiation._changed():
        input_yang_obj.ppp_negotiation = input_yang_obj.ppp_negotiation
        
    if input_yang_obj.hello_timer._changed():
        input_yang_obj.hello_timer = input_yang_obj.hello_timer
        
    if input_yang_obj.hold_multiplier._changed():
        input_yang_obj.hold_multiplier = input_yang_obj.hold_multiplier
        
    if input_yang_obj.lsp_retransmit_interval._changed():
        input_yang_obj.lsp_retransmit_interval = input_yang_obj.lsp_retransmit_interval
        
    if input_yang_obj.ppp_osicp_check._changed():
        input_yang_obj.ppp_osicp_check = input_yang_obj.ppp_osicp_check
        
    if input_yang_obj.conser._changed():
        input_yang_obj.conser = input_yang_obj.conser
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_hello_auths_hello_auth(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/hello-auths/hello-auth

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.pw_type._changed():
        input_yang_obj.pw_type = input_yang_obj.pw_type
        
    if input_yang_obj.simple._changed():
        input_yang_obj.simple = input_yang_obj.simple
        
    if input_yang_obj.key_chain._changed():
        input_yang_obj.key_chain = input_yang_obj.key_chain
        
    if input_yang_obj.md5._changed():
        input_yang_obj.md5 = input_yang_obj.md5
        
    if input_yang_obj.service._changed():
        input_yang_obj.service = input_yang_obj.service
        
    if input_yang_obj.send_only._changed():
        input_yang_obj.send_only = input_yang_obj.send_only
        
    if input_yang_obj.key_id._changed():
        input_yang_obj.key_id = input_yang_obj.key_id
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_hello_auths(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/hello-auths

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.hello_auth.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_hello_auths_hello_auth(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_mpls_ldp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/mpls-ldp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auto_flag_block._changed():
        input_yang_obj.auto_flag_block = input_yang_obj.auto_flag_block
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_frr(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/frr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.lfa_block_level1._changed():
        input_yang_obj.lfa_block_level1 = input_yang_obj.lfa_block_level1
        
    if input_yang_obj.lfa_block_level2._changed():
        input_yang_obj.lfa_block_level2 = input_yang_obj.lfa_block_level2
        
    if input_yang_obj.rlfa_disable_level1._changed():
        input_yang_obj.rlfa_disable_level1 = input_yang_obj.rlfa_disable_level1
        
    if input_yang_obj.rlfa_disable_level2._changed():
        input_yang_obj.rlfa_disable_level2 = input_yang_obj.rlfa_disable_level2
        
    if input_yang_obj.tilfa_disable_level1._changed():
        input_yang_obj.tilfa_disable_level1 = input_yang_obj.tilfa_disable_level1
        
    if input_yang_obj.tilfa_disable_level2._changed():
        input_yang_obj.tilfa_disable_level2 = input_yang_obj.tilfa_disable_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_bfd(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/bfd

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.static._changed():
        input_yang_obj.static = input_yang_obj.static
        
    if input_yang_obj.block._changed():
        input_yang_obj.block = input_yang_obj.block
        
    if input_yang_obj.min_rx._changed():
        input_yang_obj.min_rx = input_yang_obj.min_rx
        
    if input_yang_obj.min_tx._changed():
        input_yang_obj.min_tx = input_yang_obj.min_tx
        
    if input_yang_obj.detect_multiplier._changed():
        input_yang_obj.detect_multiplier = input_yang_obj.detect_multiplier
        
    if input_yang_obj.frr_binding._changed():
        input_yang_obj.frr_binding = input_yang_obj.frr_binding
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_ldp_sync(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/ldp-sync

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.hold_down_timer._changed():
        input_yang_obj.hold_down_timer = input_yang_obj.hold_down_timer
        
    if input_yang_obj.timer._changed():
        input_yang_obj.timer = input_yang_obj.timer
        
    if input_yang_obj.infinite._changed():
        input_yang_obj.infinite = input_yang_obj.infinite
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_topologys_topology(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/topologys/topology

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.incr_cost._changed():
        input_yang_obj.incr_cost = input_yang_obj.incr_cost
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_topologys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af/topologys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_topologys_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.cost_level1._changed():
        input_yang_obj.cost_level1 = input_yang_obj.cost_level1
        
    if input_yang_obj.cost_level2._changed():
        input_yang_obj.cost_level2 = input_yang_obj.cost_level2
        
    if input_yang_obj.tag_level1._changed():
        input_yang_obj.tag_level1 = input_yang_obj.tag_level1
        
    if input_yang_obj.tag_level2._changed():
        input_yang_obj.tag_level2 = input_yang_obj.tag_level2
        
    if input_yang_obj.suppress_reach._changed():
        input_yang_obj.suppress_reach = input_yang_obj.suppress_reach
        
    if input_yang_obj.incr_cost._changed():
        input_yang_obj.incr_cost = input_yang_obj.incr_cost
        
    if input_yang_obj.bfd_bit_error._changed():
        input_yang_obj.bfd_bit_error = input_yang_obj.bfd_bit_error
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_mpls_ldp(input_yang_obj.mpls_ldp, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_frr(input_yang_obj.frr, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_bfd(input_yang_obj.bfd, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_ldp_sync(input_yang_obj.ldp_sync, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af_topologys(input_yang_obj.topologys, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    for k, listInst in input_yang_obj.af.iteritems():
        address_family_type = ""
        if (k == "ipv6-unicast"):
            address_family_type = "ipv6"
        elif (k == "ipv4-unicast"):
            address_family_type = "ipv4"
        address_family_obj = translated_yang_obj.address_families.address_family_list.add(address_family=address_family_type)
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs_af(listInst, address_family_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_disp_data(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit/disp-data

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    if input_yang_obj.dis_level1._changed():
        input_yang_obj.dis_level1 = input_yang_obj.dis_level1
        
    if input_yang_obj.dis_level2._changed():
        input_yang_obj.dis_level2 = input_yang_obj.dis_level2
        
    if input_yang_obj.v4_status._changed():
        input_yang_obj.v4_status = input_yang_obj.v4_status
        
    if input_yang_obj.mtu_state._changed():
        input_yang_obj.mtu_state = input_yang_obj.mtu_state
        
    if input_yang_obj.link_state._changed():
        input_yang_obj.link_state = input_yang_obj.link_state
        
    if input_yang_obj.ip_state._changed():
        input_yang_obj.ip_state = input_yang_obj.ip_state
        
    if input_yang_obj.v6_status._changed():
        input_yang_obj.v6_status = input_yang_obj.v6_status
        
    if input_yang_obj.mtu_v6_state._changed():
        input_yang_obj.mtu_v6_state = input_yang_obj.mtu_v6_state
        
    if input_yang_obj.link_v6_state._changed():
        input_yang_obj.link_v6_state = input_yang_obj.link_v6_state
        
    if input_yang_obj.ip_v6_state._changed():
        input_yang_obj.ip_v6_state = input_yang_obj.ip_v6_state
        
    if input_yang_obj.vc_state._changed():
        input_yang_obj.vc_state = input_yang_obj.vc_state
        
    if input_yang_obj.peer_flap_status._changed():
        input_yang_obj.peer_flap_status = input_yang_obj.peer_flap_status
        
    if input_yang_obj.peer_flap_count._changed():
        input_yang_obj.peer_flap_count = input_yang_obj.peer_flap_count
        
    if input_yang_obj.peer_flap_threshold._changed():
        input_yang_obj.peer_flap_threshold = input_yang_obj.peer_flap_threshold
        
    if input_yang_obj.peer_flap_timer._changed():
        input_yang_obj.peer_flap_timer = input_yang_obj.peer_flap_timer
        
    if input_yang_obj.peer_flap_remain_timer._changed():
        input_yang_obj.peer_flap_remain_timer = input_yang_obj.peer_flap_remain_timer
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits/circuit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.p2p_enable._changed():
        input_yang_obj.p2p_enable = input_yang_obj.p2p_enable
        
    if input_yang_obj.hello_mode._changed():
        input_yang_obj.hello_mode = input_yang_obj.hello_mode
        
    if input_yang_obj.peer_hold_max._changed():
        input_yang_obj.peer_hold_max = input_yang_obj.peer_hold_max
        
    if input_yang_obj.silent_enable._changed():
        input_yang_obj.silent_enable = input_yang_obj.silent_enable
        
    if input_yang_obj.purge_source_trace_block._changed():
        input_yang_obj.purge_source_trace_block = input_yang_obj.purge_source_trace_block
        
    if input_yang_obj.silent_cost._changed():
        input_yang_obj.silent_cost = input_yang_obj.silent_cost
        
    if input_yang_obj.dis_name._changed():
        input_yang_obj.dis_name = input_yang_obj.dis_name
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_srlgs(input_yang_obj.srlgs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_mesh_group(input_yang_obj.mesh_group, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_suppress_flapping(input_yang_obj.suppress_flapping, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_timer(input_yang_obj.timer, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_broadcast(input_yang_obj.broadcast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_p2p(input_yang_obj.p2p, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_hello_auths(input_yang_obj.hello_auths, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_afs(input_yang_obj.afs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit_disp_data(input_yang_obj.disp_data, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circuits(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circuits

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.circuit.iteritems():
        interface_obj = translated_yang_obj.isis.interfaces.interface.add(name=k)
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits_circuit(listInst, interface_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_attach_bit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/attach-bit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.adv_control._changed():
        input_yang_obj.adv_control = input_yang_obj.adv_control
        
    if input_yang_obj.avoid_learn._changed():
        input_yang_obj.avoid_learn = input_yang_obj.avoid_learn
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_preference(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/preference

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_import_routes_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/import-routes/import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.cost_type._changed():
        input_yang_obj.cost_type = input_yang_obj.cost_type
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.route_policy_name._changed():
        input_yang_obj.route_policy_name = input_yang_obj.route_policy_name
        
    if input_yang_obj.level_type._changed():
        input_yang_obj.level_type = input_yang_obj.level_type
        
    if input_yang_obj.inherit_cost._changed():
        input_yang_obj.inherit_cost = input_yang_obj.inherit_cost
        
    if input_yang_obj.permit_ibgp._changed():
        input_yang_obj.permit_ibgp = input_yang_obj.permit_ibgp
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_import_routes_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_leak_route_level2_to_level1(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/leak-route-level2-to-level1

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.route_policy_name._changed():
        input_yang_obj.route_policy_name = input_yang_obj.route_policy_name
        
    if input_yang_obj.allow_filter._changed():
        input_yang_obj.allow_filter = input_yang_obj.allow_filter
        
    if input_yang_obj.allow_updown._changed():
        input_yang_obj.allow_updown = input_yang_obj.allow_updown
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_leak_route_level1_to_level2(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/leak-route-level1-to-level2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.allow_filter._changed():
        input_yang_obj.allow_filter = input_yang_obj.allow_filter
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_traffic_eng(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/traffic-eng

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_level1._changed():
        input_yang_obj.enable_level1 = input_yang_obj.enable_level1
        
    if input_yang_obj.enable_level2._changed():
        input_yang_obj.enable_level2 = input_yang_obj.enable_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_bfd(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/bfd

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.frr_binding._changed():
        input_yang_obj.frr_binding = input_yang_obj.frr_binding
        
    if input_yang_obj.min_rx._changed():
        input_yang_obj.min_rx = input_yang_obj.min_rx
        
    if input_yang_obj.min_tx._changed():
        input_yang_obj.min_tx = input_yang_obj.min_tx
        
    if input_yang_obj.detect_multiplier._changed():
        input_yang_obj.detect_multiplier = input_yang_obj.detect_multiplier
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ldp_sync(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ldp-sync

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.mpls_binding._changed():
        input_yang_obj.mpls_binding = input_yang_obj.mpls_binding
        
    if input_yang_obj.hold_down_timer._changed():
        input_yang_obj.hold_down_timer = input_yang_obj.hold_down_timer
        
    if input_yang_obj.timer._changed():
        input_yang_obj.timer = input_yang_obj.timer
        
    if input_yang_obj.infinite._changed():
        input_yang_obj.infinite = input_yang_obj.infinite
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_mpls_ldp_global(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/mpls-ldp-global

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auto_flag._changed():
        input_yang_obj.auto_flag = input_yang_obj.auto_flag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_prefix_prioritys_prefix_priority(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/prefix-prioritys/prefix-priority

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.ip_prefix._changed():
        input_yang_obj.ip_prefix = input_yang_obj.ip_prefix
        
    if input_yang_obj.ipv6_prefix._changed():
        input_yang_obj.ipv6_prefix = input_yang_obj.ipv6_prefix
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_prefix_prioritys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/prefix-prioritys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.prefix_priority.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_prefix_prioritys_prefix_priority(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr_remote_lfa(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/frr/remote-lfa

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.rlfa_level1._changed():
        input_yang_obj.rlfa_level1 = input_yang_obj.rlfa_level1
        
    if input_yang_obj.rlfa_level2._changed():
        input_yang_obj.rlfa_level2 = input_yang_obj.rlfa_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr_tilfa(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/frr/tilfa

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enable_level1._changed():
        input_yang_obj.enable_level1 = input_yang_obj.enable_level1
        
    if input_yang_obj.enable_level2._changed():
        input_yang_obj.enable_level2 = input_yang_obj.enable_level2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/frr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.lfa_level1._changed():
        input_yang_obj.lfa_level1 = input_yang_obj.lfa_level1
        
    if input_yang_obj.lfa_level2._changed():
        input_yang_obj.lfa_level2 = input_yang_obj.lfa_level2
        
    if input_yang_obj.ecmp_level1._changed():
        input_yang_obj.ecmp_level1 = input_yang_obj.ecmp_level1
        
    if input_yang_obj.ecmp_level2._changed():
        input_yang_obj.ecmp_level2 = input_yang_obj.ecmp_level2
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr_remote_lfa(input_yang_obj.remote_lfa, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr_tilfa(input_yang_obj.tilfa, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_attach_bit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/attach-bit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.adv_control._changed():
        input_yang_obj.adv_control = input_yang_obj.adv_control
        
    if input_yang_obj.avoid_learn._changed():
        input_yang_obj.avoid_learn = input_yang_obj.avoid_learn
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_preference(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/preference

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_import_routes_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/import-routes/import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.route_policy_name._changed():
        input_yang_obj.route_policy_name = input_yang_obj.route_policy_name
        
    if input_yang_obj.level_type._changed():
        input_yang_obj.level_type = input_yang_obj.level_type
        
    if input_yang_obj.inherit_cost._changed():
        input_yang_obj.inherit_cost = input_yang_obj.inherit_cost
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_import_routes_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_leak_route_level2_to_level1(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/leak-route-level2-to-level1

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.route_policy_name._changed():
        input_yang_obj.route_policy_name = input_yang_obj.route_policy_name
        
    if input_yang_obj.allow_filter._changed():
        input_yang_obj.allow_filter = input_yang_obj.allow_filter
        
    if input_yang_obj.allow_updown._changed():
        input_yang_obj.allow_updown = input_yang_obj.allow_updown
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_leak_route_level1_to_level2(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/leak-route-level1-to-level2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.allow_filter._changed():
        input_yang_obj.allow_filter = input_yang_obj.allow_filter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_import_routes_ipv4_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv4-import-routes/ipv4-import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.internal_cost._changed():
        input_yang_obj.internal_cost = input_yang_obj.internal_cost
        
    if input_yang_obj.external_cost._changed():
        input_yang_obj.external_cost = input_yang_obj.external_cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv4-import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_import_routes_ipv4_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_route_statisticss_route_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/route-statisticss/route-statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.v4_learnt_num._changed():
        input_yang_obj.v4_learnt_num = input_yang_obj.v4_learnt_num
        
    if input_yang_obj.v6_learnt_num._changed():
        input_yang_obj.v6_learnt_num = input_yang_obj.v6_learnt_num
        
    if input_yang_obj.v4_critical_num._changed():
        input_yang_obj.v4_critical_num = input_yang_obj.v4_critical_num
        
    if input_yang_obj.v4_high_num._changed():
        input_yang_obj.v4_high_num = input_yang_obj.v4_high_num
        
    if input_yang_obj.v4_medium_num._changed():
        input_yang_obj.v4_medium_num = input_yang_obj.v4_medium_num
        
    if input_yang_obj.v4_low_num._changed():
        input_yang_obj.v4_low_num = input_yang_obj.v4_low_num
        
    if input_yang_obj.v6_critical_num._changed():
        input_yang_obj.v6_critical_num = input_yang_obj.v6_critical_num
        
    if input_yang_obj.v6_high_num._changed():
        input_yang_obj.v6_high_num = input_yang_obj.v6_high_num
        
    if input_yang_obj.v6_medium_num._changed():
        input_yang_obj.v6_medium_num = input_yang_obj.v6_medium_num
        
    if input_yang_obj.v6_low_num._changed():
        input_yang_obj.v6_low_num = input_yang_obj.v6_low_num
        
    if input_yang_obj.v4_forward_num._changed():
        input_yang_obj.v4_forward_num = input_yang_obj.v4_forward_num
        
    if input_yang_obj.v6_forward_num._changed():
        input_yang_obj.v6_forward_num = input_yang_obj.v6_forward_num
        
    if input_yang_obj.v4_added2rm._changed():
        input_yang_obj.v4_added2rm = input_yang_obj.v4_added2rm
        
    if input_yang_obj.v4_unadded2rm._changed():
        input_yang_obj.v4_unadded2rm = input_yang_obj.v4_unadded2rm
        
    if input_yang_obj.v6_added2rm._changed():
        input_yang_obj.v6_added2rm = input_yang_obj.v6_added2rm
        
    if input_yang_obj.v6_unadded2rm._changed():
        input_yang_obj.v6_unadded2rm = input_yang_obj.v6_unadded2rm
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_route_statisticss(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/route-statisticss

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.route_statistics.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_route_statisticss_route_statistics(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_routes_ipv4_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv4-routes/ipv4-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.internal_cost._changed():
        input_yang_obj.internal_cost = input_yang_obj.internal_cost
        
    if input_yang_obj.external_cost._changed():
        input_yang_obj.external_cost = input_yang_obj.external_cost
        
    if input_yang_obj.interface_name._changed():
        input_yang_obj.interface_name = input_yang_obj.interface_name
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv4-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_routes_ipv4_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv6_routes_ipv6_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv6-routes/ipv6-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.interface_name._changed():
        input_yang_obj.interface_name = input_yang_obj.interface_name
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv6_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology/ipv6-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv6_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv6_routes_ipv6_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys/topology

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.topo_name._changed():
        input_yang_obj.topo_name = input_yang_obj.topo_name
        
    if input_yang_obj.max_load_balancing._changed():
        input_yang_obj.max_load_balancing = input_yang_obj.max_load_balancing
        
    if input_yang_obj.auto_cost._changed():
        input_yang_obj.auto_cost = input_yang_obj.auto_cost
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_attach_bit(input_yang_obj.attach_bit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_preference(input_yang_obj.preference, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_import_routes(input_yang_obj.import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_leak_route_level2_to_level1(input_yang_obj.leak_route_level2_to_level1, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_leak_route_level1_to_level2(input_yang_obj.leak_route_level1_to_level2, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_import_routes(input_yang_obj.ipv4_import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_route_statisticss(input_yang_obj.route_statisticss, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv4_routes(input_yang_obj.ipv4_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology_ipv6_routes(input_yang_obj.ipv6_routes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/topologys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys_topology(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_import_routes_ipv4_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv4-import-routes/ipv4-import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.internal_cost._changed():
        input_yang_obj.internal_cost = input_yang_obj.internal_cost
        
    if input_yang_obj.external_cost._changed():
        input_yang_obj.external_cost = input_yang_obj.external_cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv4-import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_import_routes_ipv4_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_route_statisticss_route_statistics(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/route-statisticss/route-statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.v4_learnt_num._changed():
        input_yang_obj.v4_learnt_num = input_yang_obj.v4_learnt_num
        
    if input_yang_obj.v6_learnt_num._changed():
        input_yang_obj.v6_learnt_num = input_yang_obj.v6_learnt_num
        
    if input_yang_obj.v4_critical_num._changed():
        input_yang_obj.v4_critical_num = input_yang_obj.v4_critical_num
        
    if input_yang_obj.v4_high_num._changed():
        input_yang_obj.v4_high_num = input_yang_obj.v4_high_num
        
    if input_yang_obj.v4_medium_num._changed():
        input_yang_obj.v4_medium_num = input_yang_obj.v4_medium_num
        
    if input_yang_obj.v4_low_num._changed():
        input_yang_obj.v4_low_num = input_yang_obj.v4_low_num
        
    if input_yang_obj.v6_critical_num._changed():
        input_yang_obj.v6_critical_num = input_yang_obj.v6_critical_num
        
    if input_yang_obj.v6_high_num._changed():
        input_yang_obj.v6_high_num = input_yang_obj.v6_high_num
        
    if input_yang_obj.v6_medium_num._changed():
        input_yang_obj.v6_medium_num = input_yang_obj.v6_medium_num
        
    if input_yang_obj.v6_low_num._changed():
        input_yang_obj.v6_low_num = input_yang_obj.v6_low_num
        
    if input_yang_obj.v4_forward_num._changed():
        input_yang_obj.v4_forward_num = input_yang_obj.v4_forward_num
        
    if input_yang_obj.v6_forward_num._changed():
        input_yang_obj.v6_forward_num = input_yang_obj.v6_forward_num
        
    if input_yang_obj.v4_added2rm._changed():
        input_yang_obj.v4_added2rm = input_yang_obj.v4_added2rm
        
    if input_yang_obj.v4_unadded2rm._changed():
        input_yang_obj.v4_unadded2rm = input_yang_obj.v4_unadded2rm
        
    if input_yang_obj.v6_added2rm._changed():
        input_yang_obj.v6_added2rm = input_yang_obj.v6_added2rm
        
    if input_yang_obj.v6_unadded2rm._changed():
        input_yang_obj.v6_unadded2rm = input_yang_obj.v6_unadded2rm
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_route_statisticss(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/route-statisticss

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.route_statistics.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_route_statisticss_route_statistics(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_routes_ipv4_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv4-routes/ipv4-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.internal_cost._changed():
        input_yang_obj.internal_cost = input_yang_obj.internal_cost
        
    if input_yang_obj.external_cost._changed():
        input_yang_obj.external_cost = input_yang_obj.external_cost
        
    if input_yang_obj.interface_name._changed():
        input_yang_obj.interface_name = input_yang_obj.interface_name
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv4-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_routes_ipv4_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv6_routes_ipv6_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv6-routes/ipv6-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.interface_name._changed():
        input_yang_obj.interface_name = input_yang_obj.interface_name
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv6_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/ipv6-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv6_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv6_routes_ipv6_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_srv6_avoid_microloop(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/srv6/avoid-microloop

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.delay_value._changed():
        input_yang_obj.delay_value = input_yang_obj.delay_value
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af_srv6(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af/srv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    translated_yang_obj.isis.srv6_cfg.enable = True
    translated_yang_obj.isis.srv6_cfg.persistent_end_x_sid = True

    if input_yang_obj.default_locator._changed():
        translated_yang_obj.isis.srv6_cfg.default_locator = input_yang_obj.default_locator
        
    if input_yang_obj.locator_name._changed():
        translated_yang_obj.isis.srv6_cfg.locator_name = input_yang_obj.locator_name
        
    if input_yang_obj.auto_sid._changed():
        input_yang_obj.auto_sid = input_yang_obj.auto_sid
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_srv6_avoid_microloop(input_yang_obj.avoid_microloop, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    if input_yang_obj.ipv6_base_topo._changed():
        input_yang_obj.ipv6_base_topo = input_yang_obj.ipv6_base_topo
        
    if input_yang_obj.apply_qppb._changed():
        input_yang_obj.apply_qppb = input_yang_obj.apply_qppb
        
    if input_yang_obj.max_load_balancing._changed():
        input_yang_obj.max_load_balancing = input_yang_obj.max_load_balancing
        
    if input_yang_obj.auto_cost._changed():
        input_yang_obj.auto_cost = input_yang_obj.auto_cost
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    if input_yang_obj.cost_level1._changed():
        input_yang_obj.cost_level1 = input_yang_obj.cost_level1
        
    if input_yang_obj.cost_level2._changed():
        input_yang_obj.cost_level2 = input_yang_obj.cost_level2
        
    if input_yang_obj.bfd_bit_error._changed():
        input_yang_obj.bfd_bit_error = input_yang_obj.bfd_bit_error
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_attach_bit(input_yang_obj.attach_bit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_preference(input_yang_obj.preference, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_import_routes(input_yang_obj.import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_leak_route_level2_to_level1(input_yang_obj.leak_route_level2_to_level1, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_leak_route_level1_to_level2(input_yang_obj.leak_route_level1_to_level2, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_traffic_eng(input_yang_obj.traffic_eng, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_bfd(input_yang_obj.bfd, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ldp_sync(input_yang_obj.ldp_sync, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_mpls_ldp_global(input_yang_obj.mpls_ldp_global, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_prefix_prioritys(input_yang_obj.prefix_prioritys, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_frr(input_yang_obj.frr, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_topologys(input_yang_obj.topologys, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_import_routes(input_yang_obj.ipv4_import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_route_statisticss(input_yang_obj.route_statisticss, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv4_routes(input_yang_obj.ipv4_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_ipv6_routes(input_yang_obj.ipv6_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af_srv6(input_yang_obj.srv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.af.iteritems():
        address_family_type = ""
        if (k == "ipv6-unicast"):
            address_family_type = "ipv6"
        elif (k == "ipv4-unicast"):
            address_family_type = "ipv4"
        address_family_obj = translated_yang_obj.isis.address_families.address_family_list.add(address_family=address_family_type)
        address_family_obj.enable = True
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs_af(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_avoid_micro_loop(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/avoid-micro-loop

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.frr_enable._changed():
        input_yang_obj.frr_enable = input_yang_obj.frr_enable
        
    if input_yang_obj.frr_rib_update_delay._changed():
        input_yang_obj.frr_rib_update_delay = input_yang_obj.frr_rib_update_delay
        
    if input_yang_obj.sr_enable._changed():
        input_yang_obj.sr_enable = input_yang_obj.sr_enable
        
    if input_yang_obj.sr_rib_update_delay._changed():
        input_yang_obj.sr_rib_update_delay = input_yang_obj.sr_rib_update_delay
        
    if input_yang_obj.te_tunnel_enable._changed():
        input_yang_obj.te_tunnel_enable = input_yang_obj.te_tunnel_enable
        
    if input_yang_obj.te_tunnel_delay._changed():
        input_yang_obj.te_tunnel_delay = input_yang_obj.te_tunnel_delay
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circ_datas_circ_data(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circ-datas/circ-data

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.v4_cost_level_1._changed():
        input_yang_obj.v4_cost_level_1 = input_yang_obj.v4_cost_level_1
        
    if input_yang_obj.v4_cost_level_2._changed():
        input_yang_obj.v4_cost_level_2 = input_yang_obj.v4_cost_level_2
        
    if input_yang_obj.v6_cost_level_1._changed():
        input_yang_obj.v6_cost_level_1 = input_yang_obj.v6_cost_level_1
        
    if input_yang_obj.v6_cost_level_2._changed():
        input_yang_obj.v6_cost_level_2 = input_yang_obj.v6_cost_level_2
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_circ_datas(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/circ-datas

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.circ_data.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_circ_datas_circ_data(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_bfd_sessions_bfd_session(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/bfd-sessions/bfd-session

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    if input_yang_obj.min_tx._changed():
        input_yang_obj.min_tx = input_yang_obj.min_tx
        
    if input_yang_obj.min_rx._changed():
        input_yang_obj.min_rx = input_yang_obj.min_rx
        
    if input_yang_obj.mul_number._changed():
        input_yang_obj.mul_number = input_yang_obj.mul_number
        
    if input_yang_obj.system_id._changed():
        input_yang_obj.system_id = input_yang_obj.system_id
        
    if input_yang_obj.circuit_name._changed():
        input_yang_obj.circuit_name = input_yang_obj.circuit_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_bfd_sessions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/bfd-sessions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.bfd_session.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_bfd_sessions_bfd_session(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv4_addrs_ipv4_addr(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/ipv4-addrs/ipv4-addr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv4_addrs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/ipv4-addrs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_addr.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv4_addrs_ipv4_addr(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv6_global_addrs_ipv6_global_addr(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/ipv6-global-addrs/ipv6-global-addr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv6_global_addrs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/ipv6-global-addrs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv6_global_addr.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv6_global_addrs_ipv6_global_addr(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_endxs_endx(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/endxs/endx

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer_endxs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer/endxs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endx.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_endxs_endx(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_peers_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers/peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.host_name._changed():
        input_yang_obj.host_name = input_yang_obj.host_name
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.area_addr._changed():
        input_yang_obj.area_addr = input_yang_obj.area_addr
        
    if input_yang_obj.up_time._changed():
        input_yang_obj.up_time = input_yang_obj.up_time
        
    if input_yang_obj.up_time_stamp._changed():
        input_yang_obj.up_time_stamp = input_yang_obj.up_time_stamp
        
    if input_yang_obj.adj_mt_id._changed():
        input_yang_obj.adj_mt_id = input_yang_obj.adj_mt_id
        
    if input_yang_obj.local_mt_id._changed():
        input_yang_obj.local_mt_id = input_yang_obj.local_mt_id
        
    if input_yang_obj.protocol._changed():
        input_yang_obj.protocol = input_yang_obj.protocol
        
    if input_yang_obj.restart_capable._changed():
        input_yang_obj.restart_capable = input_yang_obj.restart_capable
        
    if input_yang_obj.suppressed_adj._changed():
        input_yang_obj.suppressed_adj = input_yang_obj.suppressed_adj
        
    if input_yang_obj.adj_sid._changed():
        input_yang_obj.adj_sid = input_yang_obj.adj_sid
        
    if input_yang_obj.ipv6_link_local_addr._changed():
        input_yang_obj.ipv6_link_local_addr = input_yang_obj.ipv6_link_local_addr
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv4_addrs(input_yang_obj.ipv4_addrs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_ipv6_global_addrs(input_yang_obj.ipv6_global_addrs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer_endxs(input_yang_obj.endxs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.peer.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers_peer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsdbs_lsdb(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsdbs/lsdb

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.seqence_number._changed():
        input_yang_obj.seqence_number = input_yang_obj.seqence_number
        
    if input_yang_obj.check_sum._changed():
        input_yang_obj.check_sum = input_yang_obj.check_sum
        
    if input_yang_obj.lsp_length._changed():
        input_yang_obj.lsp_length = input_yang_obj.lsp_length
        
    if input_yang_obj.att._changed():
        input_yang_obj.att = input_yang_obj.att
        
    if input_yang_obj.partition._changed():
        input_yang_obj.partition = input_yang_obj.partition
        
    if input_yang_obj.overload._changed():
        input_yang_obj.overload = input_yang_obj.overload
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.local_lsp._changed():
        input_yang_obj.local_lsp = input_yang_obj.local_lsp
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site_lsdbs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site/lsdbs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.lsdb.iteritems():
        innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsdbs_lsdb(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites_site(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites/site

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    translated_yang_obj.isis.enable = True
        
    if input_yang_obj.level._changed():
        if (input_yang_obj.level == "level-1-2"):
            translated_yang_obj.isis.level_type = "level-all"
        else:
            translated_yang_obj.isis.level_type = input_yang_obj.level
        
    if input_yang_obj.shutdown._changed():
        input_yang_obj.shutdown = input_yang_obj.shutdown
        
    if input_yang_obj.cost_style._changed():
        input_yang_obj.cost_style = input_yang_obj.cost_style
        
    if input_yang_obj.relax_spf_limit._changed():
        input_yang_obj.relax_spf_limit = input_yang_obj.relax_spf_limit
        
    if input_yang_obj.is_name._changed():
        input_yang_obj.is_name = input_yang_obj.is_name
        
    if input_yang_obj.direct_inherit._changed():
        input_yang_obj.direct_inherit = input_yang_obj.direct_inherit
        
    if input_yang_obj.adv_one_intf_addr._changed():
        input_yang_obj.adv_one_intf_addr = input_yang_obj.adv_one_intf_addr
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsp_fragments_extend(input_yang_obj.lsp_fragments_extend, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_poi_tlv(input_yang_obj.poi_tlv, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsdb_limit(input_yang_obj.lsdb_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_suppress_flapping(input_yang_obj.suppress_flapping, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_timer(input_yang_obj.timer, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsp_length(input_yang_obj.lsp_length, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_flash_flood(input_yang_obj.flash_flood, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_set_overload(input_yang_obj.set_overload, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsp_lifetime(input_yang_obj.lsp_lifetime, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_bgp_ls(input_yang_obj.bgp_ls, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_extern_ability(input_yang_obj.extern_ability, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_srgbs(input_yang_obj.srgbs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_net_entitys(input_yang_obj.net_entitys, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsp_auths(input_yang_obj.lsp_auths, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circuits(input_yang_obj.circuits, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_afs(input_yang_obj.afs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_avoid_micro_loop(input_yang_obj.avoid_micro_loop, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_circ_datas(input_yang_obj.circ_datas, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_bfd_sessions(input_yang_obj.bfd_sessions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_peers(input_yang_obj.peers, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_isis_sites_site_lsdbs(input_yang_obj.lsdbs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis_sites(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis/sites

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        isis_name = "isis" + str(listInst.id)
        isis_obj = translated_yang_obj.routing.control_plane_protocols.control_plane_protocol.add(type="isis", name=isis_name)
        innerobj = _translate__network_instance_instances_instance_isis_sites_site(listInst, isis_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_isis(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/isis

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_isis_sites(input_yang_obj.sites, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_encapsulation(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/encapsulation

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        translated_yang_obj.routing.srv6.encapsulation.source_address = input_yang_obj.source_address
        
    if input_yang_obj.hop_limit._changed():
        translated_yang_obj.routing.srv6.encapsulation.ip_ttl_propagation = False
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_ends_end(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/ends/end

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """

    translated_yang_obj.end_behavior_type = "End"
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_ends(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/ends

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end.iteritems():
        end_obj = translated_yang_obj.static.local_sids.sid.add(opcode=ipv62dec(k))
        innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_ends_end(listInst, end_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_otps_end_otp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-otps/end-otp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_otps(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-otps

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_otp.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_otps_end_otp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_xs_end_x(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-xs/end-x

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.flavor._changed():
        input_yang_obj.flavor = input_yang_obj.flavor
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_xs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-xs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_x.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_xs_end_x(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_dt4s_end_dt4(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-dt4s/end-dt4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.end_behavior_type = "End.DT4"

    if input_yang_obj.vpn_name._changed():
        input_yang_obj.vpn_name = input_yang_obj.vpn_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_dt4s(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes/end-dt4s

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_dt4.iteritems():
        enddt4_obj = translated_yang_obj.static.local_sids.sid.add(opcode=ipv62dec(listInst.value))
        innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_dt4s_end_dt4(listInst, enddt4_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator_opcodes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator/opcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_ends(input_yang_obj.ends, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_otps(input_yang_obj.end_otps, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_xs(input_yang_obj.end_xs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes_end_dt4s(input_yang_obj.end_dt4s, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators_locator(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators/locator

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.enable = True

    if input_yang_obj.prefix._changed():
        translated_yang_obj.prefix.address = input_yang_obj.prefix
        
    if input_yang_obj.prefix_length._changed():
        translated_yang_obj.prefix.length = input_yang_obj.prefix_length
        
    if input_yang_obj.static_length._changed():
        input_yang_obj.static_length = input_yang_obj.static_length
        
    if input_yang_obj.args_length._changed():
        input_yang_obj.args_length = input_yang_obj.args_length
        
    if input_yang_obj.default_._changed():
        translated_yang_obj.is_default = input_yang_obj.default_
        
    innerobj = _translate__network_instance_instances_instance_srv6_locators_locator_opcodes(input_yang_obj.opcodes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_locators(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/locators

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        locator_obj = translated_yang_obj.routing.srv6.locators.locator.add(name=k)
        innerobj = _translate__network_instance_instances_instance_srv6_locators_locator(listInst, locator_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_ends_end(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/ends/end

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.flavor._changed():
        input_yang_obj.flavor = input_yang_obj.flavor
        
    if input_yang_obj.locator_name._changed():
        input_yang_obj.locator_name = input_yang_obj.locator_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_ends(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/ends

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_local_sids_ends_end(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_otps_end_otp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-otps/end-otp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.locator_name._changed():
        input_yang_obj.locator_name = input_yang_obj.locator_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_otps(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-otps

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_otp.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_otps_end_otp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x_next_hops_next_hop(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-xs/end-x/next-hops/next-hop

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x_next_hops(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-xs/end-x/next-hops

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x_next_hops_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-xs/end-x

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.flavor._changed():
        input_yang_obj.flavor = input_yang_obj.flavor
        
    if input_yang_obj.locator_name._changed():
        input_yang_obj.locator_name = input_yang_obj.locator_name
        
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x_next_hops(input_yang_obj.next_hops, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_xs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-xs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_x.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_xs_end_x(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_dt4s_end_dt4(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-dt4s/end-dt4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vpn_name._changed():
        input_yang_obj.vpn_name = input_yang_obj.vpn_name
        
    if input_yang_obj.locator_name._changed():
        input_yang_obj.locator_name = input_yang_obj.locator_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids_end_dt4s(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids/end-dt4s

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.end_dt4.iteritems():
        innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_dt4s_end_dt4(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6_local_sids(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6/local-sids

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids_ends(input_yang_obj.ends, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_otps(input_yang_obj.end_otps, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_xs(input_yang_obj.end_xs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids_end_dt4s(input_yang_obj.end_dt4s, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_srv6(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/srv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        translated_yang_obj.routing.srv6.enable = input_yang_obj.enable
        
    if input_yang_obj.te_frr_enable._changed():
        input_yang_obj.te_frr_enable = input_yang_obj.te_frr_enable
        
    innerobj = _translate__network_instance_instances_instance_srv6_encapsulation(input_yang_obj.encapsulation, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_locators(input_yang_obj.locators, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_srv6_local_sids(input_yang_obj.local_sids, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_addresses_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-ifs/ipv4-if/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_addresses(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-ifs/ipv4-if/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_unnumbered_if(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-ifs/ipv4-if/unnumbered-if

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-ifs/ipv4-if

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if_unnumbered_if(input_yang_obj.unnumbered_if, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_ifs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-ifs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_if.iteritems():
        interface_obj = translated_yang_obj.interfaces.interface.add(name=k)
        innerobj = _translate__network_instance_instances_instance_ipv4_ifs_ipv4_if(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state_addresses_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-if-states/ipv4-if-state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state_addresses(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-if-states/ipv4-if-state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-if-states/ipv4-if-state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv4_if_states(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv4-if-states

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv4_if_state.iteritems():
        innerobj = _translate__network_instance_instances_instance_ipv4_if_states_ipv4_if_state(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if_addresses_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-ifs/ipv6-if/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if_addresses(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-ifs/ipv6-if/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-ifs/ipv6-if

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    innerobj = _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_ifs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-ifs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv6_if.iteritems():
        innerobj = _translate__network_instance_instances_instance_ipv6_ifs_ipv6_if(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state_addresses_address(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-if-states/ipv6-if-state/addresses/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state_addresses(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-if-states/ipv6-if-state/addresses

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state_addresses_address(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-if-states/ipv6-if-state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state_addresses(input_yang_obj.addresses, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_ipv6_if_states(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/ipv6-if-states

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.ipv6_if_state.iteritems():
        innerobj = _translate__network_instance_instances_instance_ipv6_if_states_ipv6_if_state(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_common(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/common

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auto_frr._changed():
        input_yang_obj.auto_frr = input_yang_obj.auto_frr
        
    if input_yang_obj.tunnel_selector_name._changed():
        input_yang_obj.tunnel_selector_name = input_yang_obj.tunnel_selector_name
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.reflector_cluster_ipv4._changed():
        input_yang_obj.reflector_cluster_ipv4 = input_yang_obj.reflector_cluster_ipv4
        
    if input_yang_obj.reflector_cluster_id._changed():
        input_yang_obj.reflector_cluster_id = input_yang_obj.reflector_cluster_id
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    if input_yang_obj.maximum_load_balancing_ibgp._changed():
        input_yang_obj.maximum_load_balancing_ibgp = input_yang_obj.maximum_load_balancing_ibgp
        
    if input_yang_obj.maximum_load_balancing_ebgp._changed():
        input_yang_obj.maximum_load_balancing_ebgp = input_yang_obj.maximum_load_balancing_ebgp
        
    if input_yang_obj.nexthop_select_depend_type._changed():
        input_yang_obj.nexthop_select_depend_type = input_yang_obj.nexthop_select_depend_type
        
    if input_yang_obj.nexthop_resolve_aigp._changed():
        input_yang_obj.nexthop_resolve_aigp = input_yang_obj.nexthop_resolve_aigp
        
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.summary_automatic._changed():
        input_yang_obj.summary_automatic = input_yang_obj.summary_automatic
        
    if input_yang_obj.nexthop_third_party._changed():
        input_yang_obj.nexthop_third_party = input_yang_obj.nexthop_third_party
        
    if input_yang_obj.best_route_bit_error_detection._changed():
        input_yang_obj.best_route_bit_error_detection = input_yang_obj.best_route_bit_error_detection
        
    if input_yang_obj.supernet_unicast_advertise._changed():
        input_yang_obj.supernet_unicast_advertise = input_yang_obj.supernet_unicast_advertise
        
    if input_yang_obj.supernet_label_advertise._changed():
        input_yang_obj.supernet_label_advertise = input_yang_obj.supernet_label_advertise
        
    if input_yang_obj.lsp_mtu._changed():
        input_yang_obj.lsp_mtu = input_yang_obj.lsp_mtu
        
    if input_yang_obj.label_free_delay._changed():
        input_yang_obj.label_free_delay = input_yang_obj.label_free_delay
        
    if input_yang_obj.bestroute_med_confederation._changed():
        input_yang_obj.bestroute_med_confederation = input_yang_obj.bestroute_med_confederation
        
    if input_yang_obj.bestroute_as_path_ignore._changed():
        input_yang_obj.bestroute_as_path_ignore = input_yang_obj.bestroute_as_path_ignore
        
    if input_yang_obj.determin_med._changed():
        input_yang_obj.determin_med = input_yang_obj.determin_med
        
    if input_yang_obj.best_external._changed():
        input_yang_obj.best_external = input_yang_obj.best_external
        
    if input_yang_obj.add_path_select_num._changed():
        input_yang_obj.add_path_select_num = input_yang_obj.add_path_select_num
        
    if input_yang_obj.load_balanc_igp_metric_ignore._changed():
        input_yang_obj.load_balanc_igp_metric_ignore = input_yang_obj.load_balanc_igp_metric_ignore
        
    if input_yang_obj.load_balanc_as_path_ignore._changed():
        input_yang_obj.load_balanc_as_path_ignore = input_yang_obj.load_balanc_as_path_ignore
        
    if input_yang_obj.load_balanc_as_path_relax._changed():
        input_yang_obj.load_balanc_as_path_relax = input_yang_obj.load_balanc_as_path_relax
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    if input_yang_obj.default_route_import._changed():
        input_yang_obj.default_route_import = input_yang_obj.default_route_import
        
    if input_yang_obj.routerid_neglect._changed():
        input_yang_obj.routerid_neglect = input_yang_obj.routerid_neglect
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_routes_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/import-routes/import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_routes_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_aggregate_routes_aggregate_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/aggregate-routes/aggregate-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.as_set._changed():
        input_yang_obj.as_set = input_yang_obj.as_set
        
    if input_yang_obj.detail_suppressed._changed():
        input_yang_obj.detail_suppressed = input_yang_obj.detail_suppressed
        
    if input_yang_obj.attribute_policy._changed():
        input_yang_obj.attribute_policy = input_yang_obj.attribute_policy
        
    if input_yang_obj.origin_policy._changed():
        input_yang_obj.origin_policy = input_yang_obj.origin_policy
        
    if input_yang_obj.suppress_policy._changed():
        input_yang_obj.suppress_policy = input_yang_obj.suppress_policy
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_aggregate_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/aggregate-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.aggregate_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_aggregate_routes_aggregate_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_network_routes_network_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/network-routes/network-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.non_relay_tunnel._changed():
        input_yang_obj.non_relay_tunnel = input_yang_obj.non_relay_tunnel
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_network_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/network-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.network_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_network_routes_network_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_advertise_route_to_evpns_advertise_route_to_evpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/advertise-route-to-evpns/advertise-route-to-evpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.import_multipath._changed():
        input_yang_obj.import_multipath = input_yang_obj.import_multipath
        
    if input_yang_obj.advertise_route_mode._changed():
        input_yang_obj.advertise_route_mode = input_yang_obj.advertise_route_mode
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_advertise_route_to_evpns(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/advertise-route-to-evpns

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.advertise_route_to_evpn.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_advertise_route_to_evpns_advertise_route_to_evpn(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_ribs_import_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/import-ribs/import-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.include_label_route._changed():
        input_yang_obj.include_label_route = input_yang_obj.include_label_route
        
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_ribs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/import-ribs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_rib.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_ribs_import_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_lsp_options(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast/lsp-options

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ingress_protect_mode_bgp_frr._changed():
        input_yang_obj.ingress_protect_mode_bgp_frr = input_yang_obj.ingress_protect_mode_bgp_frr
        
    if input_yang_obj.maximum_load_balancing_ingress._changed():
        input_yang_obj.maximum_load_balancing_ingress = input_yang_obj.maximum_load_balancing_ingress
        
    if input_yang_obj.maximum_load_balancing_transit._changed():
        input_yang_obj.maximum_load_balancing_transit = input_yang_obj.maximum_load_balancing_transit
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_common(input_yang_obj.common, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_routes(input_yang_obj.import_routes, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_aggregate_routes(input_yang_obj.aggregate_routes, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_network_routes(input_yang_obj.network_routes, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_advertise_route_to_evpns(input_yang_obj.advertise_route_to_evpns, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_import_ribs(input_yang_obj.import_ribs, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast_lsp_options(input_yang_obj.lsp_options, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_common(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/common

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auto_frr._changed():
        input_yang_obj.auto_frr = input_yang_obj.auto_frr
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.reflector_cluster_ipv4._changed():
        input_yang_obj.reflector_cluster_ipv4 = input_yang_obj.reflector_cluster_ipv4
        
    if input_yang_obj.reflector_cluster_id._changed():
        input_yang_obj.reflector_cluster_id = input_yang_obj.reflector_cluster_id
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    if input_yang_obj.maximum_load_balancing_ibgp._changed():
        input_yang_obj.maximum_load_balancing_ibgp = input_yang_obj.maximum_load_balancing_ibgp
        
    if input_yang_obj.maximum_load_balancing_ebgp._changed():
        input_yang_obj.maximum_load_balancing_ebgp = input_yang_obj.maximum_load_balancing_ebgp
        
    if input_yang_obj.explicit_null._changed():
        input_yang_obj.explicit_null = input_yang_obj.explicit_null
        
    if input_yang_obj.nexthop_select_depend_type._changed():
        input_yang_obj.nexthop_select_depend_type = input_yang_obj.nexthop_select_depend_type
        
    if input_yang_obj.nexthop_resolve_aigp._changed():
        input_yang_obj.nexthop_resolve_aigp = input_yang_obj.nexthop_resolve_aigp
        
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.nexthop_third_party._changed():
        input_yang_obj.nexthop_third_party = input_yang_obj.nexthop_third_party
        
    if input_yang_obj.supernet_unicast_advertise._changed():
        input_yang_obj.supernet_unicast_advertise = input_yang_obj.supernet_unicast_advertise
        
    if input_yang_obj.bestroute_med_confederation._changed():
        input_yang_obj.bestroute_med_confederation = input_yang_obj.bestroute_med_confederation
        
    if input_yang_obj.bestroute_as_path_ignore._changed():
        input_yang_obj.bestroute_as_path_ignore = input_yang_obj.bestroute_as_path_ignore
        
    if input_yang_obj.determin_med._changed():
        input_yang_obj.determin_med = input_yang_obj.determin_med
        
    if input_yang_obj.best_external._changed():
        input_yang_obj.best_external = input_yang_obj.best_external
        
    if input_yang_obj.add_path_select_num._changed():
        input_yang_obj.add_path_select_num = input_yang_obj.add_path_select_num
        
    if input_yang_obj.load_balanc_igp_metric_ignore._changed():
        input_yang_obj.load_balanc_igp_metric_ignore = input_yang_obj.load_balanc_igp_metric_ignore
        
    if input_yang_obj.load_balanc_as_path_ignore._changed():
        input_yang_obj.load_balanc_as_path_ignore = input_yang_obj.load_balanc_as_path_ignore
        
    if input_yang_obj.load_balanc_as_path_relax._changed():
        input_yang_obj.load_balanc_as_path_relax = input_yang_obj.load_balanc_as_path_relax
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    if input_yang_obj.default_route_import._changed():
        input_yang_obj.default_route_import = input_yang_obj.default_route_import
        
    if input_yang_obj.routerid_neglect._changed():
        input_yang_obj.routerid_neglect = input_yang_obj.routerid_neglect
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_routes_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/import-routes/import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_routes_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_aggregate_routes_aggregate_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/aggregate-routes/aggregate-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.as_set._changed():
        input_yang_obj.as_set = input_yang_obj.as_set
        
    if input_yang_obj.detail_suppressed._changed():
        input_yang_obj.detail_suppressed = input_yang_obj.detail_suppressed
        
    if input_yang_obj.attribute_policy._changed():
        input_yang_obj.attribute_policy = input_yang_obj.attribute_policy
        
    if input_yang_obj.origin_policy._changed():
        input_yang_obj.origin_policy = input_yang_obj.origin_policy
        
    if input_yang_obj.suppress_policy._changed():
        input_yang_obj.suppress_policy = input_yang_obj.suppress_policy
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_aggregate_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/aggregate-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.aggregate_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_aggregate_routes_aggregate_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_network_routes_network_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/network-routes/network-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_network_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/network-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.network_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_network_routes_network_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_advertise_route_to_evpns_advertise_route_to_evpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/advertise-route-to-evpns/advertise-route-to-evpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.import_multipath._changed():
        input_yang_obj.import_multipath = input_yang_obj.import_multipath
        
    if input_yang_obj.advertise_route_mode._changed():
        input_yang_obj.advertise_route_mode = input_yang_obj.advertise_route_mode
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_advertise_route_to_evpns(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/advertise-route-to-evpns

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.advertise_route_to_evpn.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_advertise_route_to_evpns_advertise_route_to_evpn(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_ribs_import_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/import-ribs/import-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.include_label_route._changed():
        input_yang_obj.include_label_route = input_yang_obj.include_label_route
        
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_ribs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast/import-ribs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_rib.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_ribs_import_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_common(input_yang_obj.common, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_routes(input_yang_obj.import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_aggregate_routes(input_yang_obj.aggregate_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_network_routes(input_yang_obj.network_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_advertise_route_to_evpns(input_yang_obj.advertise_route_to_evpns, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast_import_ribs(input_yang_obj.import_ribs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.policy_vpntarget._changed():
        input_yang_obj.policy_vpntarget = input_yang_obj.policy_vpntarget
        
    if input_yang_obj.reflector_cluster_ipv4._changed():
        input_yang_obj.reflector_cluster_ipv4 = input_yang_obj.reflector_cluster_ipv4
        
    if input_yang_obj.reflector_cluster_id._changed():
        input_yang_obj.reflector_cluster_id = input_yang_obj.reflector_cluster_id
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    if input_yang_obj.auto_frr._changed():
        input_yang_obj.auto_frr = input_yang_obj.auto_frr
        
    if input_yang_obj.tunnel_selector_name._changed():
        input_yang_obj.tunnel_selector_name = input_yang_obj.tunnel_selector_name
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.apply_label_mode._changed():
        input_yang_obj.apply_label_mode = input_yang_obj.apply_label_mode
        
    if input_yang_obj.nexthop_select_depend_type._changed():
        input_yang_obj.nexthop_select_depend_type = input_yang_obj.nexthop_select_depend_type
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.best_external._changed():
        input_yang_obj.best_external = input_yang_obj.best_external
        
    if input_yang_obj.label_free_delay._changed():
        input_yang_obj.label_free_delay = input_yang_obj.label_free_delay
        
    if input_yang_obj.add_path_select_num._changed():
        input_yang_obj.add_path_select_num = input_yang_obj.add_path_select_num
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv6-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.policy_vpntarget._changed():
        input_yang_obj.policy_vpntarget = input_yang_obj.policy_vpntarget
        
    if input_yang_obj.reflector_cluster_ipv4._changed():
        input_yang_obj.reflector_cluster_ipv4 = input_yang_obj.reflector_cluster_ipv4
        
    if input_yang_obj.reflector_cluster_id._changed():
        input_yang_obj.reflector_cluster_id = input_yang_obj.reflector_cluster_id
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    if input_yang_obj.auto_frr._changed():
        input_yang_obj.auto_frr = input_yang_obj.auto_frr
        
    if input_yang_obj.tunnel_selector_name._changed():
        input_yang_obj.tunnel_selector_name = input_yang_obj.tunnel_selector_name
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.apply_label_mode._changed():
        input_yang_obj.apply_label_mode = input_yang_obj.apply_label_mode
        
    if input_yang_obj.nexthop_select_depend_type._changed():
        input_yang_obj.nexthop_select_depend_type = input_yang_obj.nexthop_select_depend_type
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.best_external._changed():
        input_yang_obj.best_external = input_yang_obj.best_external
        
    if input_yang_obj.add_path_select_num._changed():
        input_yang_obj.add_path_select_num = input_yang_obj.add_path_select_num
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_common(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/common

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.auto_frr._changed():
        input_yang_obj.auto_frr = input_yang_obj.auto_frr
        
    if input_yang_obj.tunnel_selector_name._changed():
        input_yang_obj.tunnel_selector_name = input_yang_obj.tunnel_selector_name
        
    if input_yang_obj.tunnel_selector_all._changed():
        input_yang_obj.tunnel_selector_all = input_yang_obj.tunnel_selector_all
        
    if input_yang_obj.nexthop_select_depend_type._changed():
        input_yang_obj.nexthop_select_depend_type = input_yang_obj.nexthop_select_depend_type
        
    if input_yang_obj.always_compare_med._changed():
        input_yang_obj.always_compare_med = input_yang_obj.always_compare_med
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.best_route_bit_error_detection._changed():
        input_yang_obj.best_route_bit_error_detection = input_yang_obj.best_route_bit_error_detection
        
    if input_yang_obj.supernet_label_advertise._changed():
        input_yang_obj.supernet_label_advertise = input_yang_obj.supernet_label_advertise
        
    if input_yang_obj.lsp_mtu._changed():
        input_yang_obj.lsp_mtu = input_yang_obj.lsp_mtu
        
    if input_yang_obj.label_free_delay._changed():
        input_yang_obj.label_free_delay = input_yang_obj.label_free_delay
        
    if input_yang_obj.bestroute_med_confederation._changed():
        input_yang_obj.bestroute_med_confederation = input_yang_obj.bestroute_med_confederation
        
    if input_yang_obj.bestroute_as_path_ignore._changed():
        input_yang_obj.bestroute_as_path_ignore = input_yang_obj.bestroute_as_path_ignore
        
    if input_yang_obj.determin_med._changed():
        input_yang_obj.determin_med = input_yang_obj.determin_med
        
    if input_yang_obj.best_external._changed():
        input_yang_obj.best_external = input_yang_obj.best_external
        
    if input_yang_obj.add_path_select_num._changed():
        input_yang_obj.add_path_select_num = input_yang_obj.add_path_select_num
        
    if input_yang_obj.load_balanc_igp_metric_ignore._changed():
        input_yang_obj.load_balanc_igp_metric_ignore = input_yang_obj.load_balanc_igp_metric_ignore
        
    if input_yang_obj.load_balanc_as_path_ignore._changed():
        input_yang_obj.load_balanc_as_path_ignore = input_yang_obj.load_balanc_as_path_ignore
        
    if input_yang_obj.load_balanc_as_path_relax._changed():
        input_yang_obj.load_balanc_as_path_relax = input_yang_obj.load_balanc_as_path_relax
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    if input_yang_obj.default_route_import._changed():
        input_yang_obj.default_route_import = input_yang_obj.default_route_import
        
    if input_yang_obj.routerid_neglect._changed():
        input_yang_obj.routerid_neglect = input_yang_obj.routerid_neglect
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_routes_import_route(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/import-routes/import-route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_routes(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/import-routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_route.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_routes_import_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_ribs_import_rib(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/import-ribs/import-rib

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.valid_route._changed():
        input_yang_obj.valid_route = input_yang_obj.valid_route
        
    if input_yang_obj.include_label_route._changed():
        input_yang_obj.include_label_route = input_yang_obj.include_label_route
        
    if input_yang_obj.policy_name._changed():
        input_yang_obj.policy_name = input_yang_obj.policy_name
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_ribs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/import-ribs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.import_rib.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_ribs_import_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_lsp_options(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni/lsp-options

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ingress_protect_mode_bgp_frr._changed():
        input_yang_obj.ingress_protect_mode_bgp_frr = input_yang_obj.ingress_protect_mode_bgp_frr
        
    if input_yang_obj.maximum_load_balancing_ingress._changed():
        input_yang_obj.maximum_load_balancing_ingress = input_yang_obj.maximum_load_balancing_ingress
        
    if input_yang_obj.maximum_load_balancing_transit._changed():
        input_yang_obj.maximum_load_balancing_transit = input_yang_obj.maximum_load_balancing_transit
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-labeluni

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_common(input_yang_obj.common, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_routes(input_yang_obj.import_routes, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_import_ribs(input_yang_obj.import_ribs, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni_lsp_options(input_yang_obj.lsp_options, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_multicast_common(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-multicast/common

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.default_med._changed():
        input_yang_obj.default_med = input_yang_obj.default_med
        
    if input_yang_obj.summary_automatic._changed():
        input_yang_obj.summary_automatic = input_yang_obj.summary_automatic
        
    if input_yang_obj.bestroute_med_confederation._changed():
        input_yang_obj.bestroute_med_confederation = input_yang_obj.bestroute_med_confederation
        
    if input_yang_obj.default_local_preference._changed():
        input_yang_obj.default_local_preference = input_yang_obj.default_local_preference
        
    if input_yang_obj.default_route_import._changed():
        input_yang_obj.default_route_import = input_yang_obj.default_route_import
        
    if input_yang_obj.routerid_neglect._changed():
        input_yang_obj.routerid_neglect = input_yang_obj.routerid_neglect
        
    if input_yang_obj.route_select_delay._changed():
        input_yang_obj.route_select_delay = input_yang_obj.route_select_delay
        
    if input_yang_obj.reflect_change_path._changed():
        input_yang_obj.reflect_change_path = input_yang_obj.reflect_change_path
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af/ipv4-multicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_multicast_common(input_yang_obj.common, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_vpn(input_yang_obj.ipv4_vpn, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv6_vpn(input_yang_obj.ipv6_vpn, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_labeluni(input_yang_obj.ipv4_labeluni, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af_ipv4_multicast(input_yang_obj.ipv4_multicast, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.af.iteritems():
        # translated_yang_obj.bgp.global_.as_ = "200"
        innerobj = translated_yang_obj.bgp.global_.afi_safis.afi_safi.add("ipv4-unicast")
        innerobj.enabled = "true"
        # innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs_af(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_fake_as_parameter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/fake-as-parameter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fake_as._changed():
        input_yang_obj.fake_as = input_yang_obj.fake_as
        
    if input_yang_obj.dual_as._changed():
        input_yang_obj.dual_as = input_yang_obj.dual_as
        
    if input_yang_obj.prepend_global_as._changed():
        input_yang_obj.prepend_global_as = input_yang_obj.prepend_global_as
        
    if input_yang_obj.prepend_fake_as._changed():
        input_yang_obj.prepend_fake_as = input_yang_obj.prepend_fake_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_timer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/timer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.keep_alive_time._changed():
        input_yang_obj.keep_alive_time = input_yang_obj.keep_alive_time
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.min_hold_time._changed():
        input_yang_obj.min_hold_time = input_yang_obj.min_hold_time
        
    if input_yang_obj.connect_retry_time._changed():
        input_yang_obj.connect_retry_time = input_yang_obj.connect_retry_time
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_bfd_parameter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/bfd-parameter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.single_hop._changed():
        input_yang_obj.single_hop = input_yang_obj.single_hop
        
    if input_yang_obj.compatible._changed():
        input_yang_obj.compatible = input_yang_obj.compatible
        
    if input_yang_obj.per_link_echo._changed():
        input_yang_obj.per_link_echo = input_yang_obj.per_link_echo
        
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.min_rx_interval._changed():
        input_yang_obj.min_rx_interval = input_yang_obj.min_rx_interval
        
    if input_yang_obj.min_tx_interval._changed():
        input_yang_obj.min_tx_interval = input_yang_obj.min_tx_interval
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_members_member(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/members/member

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_members(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/members

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.member.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_members_member(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_import_filter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/import-filter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    if input_yang_obj.parameter._changed():
        input_yang_obj.parameter = input_yang_obj.parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_export_filter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/export-filter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    if input_yang_obj.parameter._changed():
        input_yang_obj.parameter = input_yang_obj.parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_default_route_match_conditions_default_route_match_condition(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/default-route-match-conditions/default-route-match-condition

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_default_route_match_conditions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/default-route-match-conditions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_match_condition.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_default_route_match_conditions_default_route_match_condition(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.orf_type._changed():
        input_yang_obj.orf_type = input_yang_obj.orf_type
        
    if input_yang_obj.orf_mode._changed():
        input_yang_obj.orf_mode = input_yang_obj.orf_mode
        
    if input_yang_obj.label_route_capability._changed():
        input_yang_obj.label_route_capability = input_yang_obj.label_route_capability
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_import_filter(input_yang_obj.import_filter, translated_yang_obj)
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_export_filter(input_yang_obj.export_filter, translated_yang_obj)
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.default_route_match_mode._changed():
        input_yang_obj.default_route_match_mode = input_yang_obj.default_route_match_mode
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_default_route_match_conditions(input_yang_obj.default_route_match_conditions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_default_route_match_conditions_default_route_match_condition(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-unicast/default-route-match-conditions/default-route-match-condition

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_default_route_match_conditions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-unicast/default-route-match-conditions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_match_condition.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_default_route_match_conditions_default_route_match_condition(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-unicast/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-unicast/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.label_route_capability._changed():
        input_yang_obj.label_route_capability = input_yang_obj.label_route_capability
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.default_route_match_mode._changed():
        input_yang_obj.default_route_match_mode = input_yang_obj.default_route_match_mode
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ipv6_prefix._changed():
        input_yang_obj.import_ipv6_prefix = input_yang_obj.import_ipv6_prefix
        
    if input_yang_obj.export_ipv6_prefix._changed():
        input_yang_obj.export_ipv6_prefix = input_yang_obj.export_ipv6_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_default_route_match_conditions(input_yang_obj.default_route_match_conditions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn_default_route_originates_default_route_originate(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-vpn/default-route-originates/default-route-originate

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn_default_route_originates(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-vpn/default-route-originates

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_originate.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn_default_route_originates_default_route_originate(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.reoriginate_route_enable._changed():
        input_yang_obj.reoriginate_route_enable = input_yang_obj.reoriginate_route_enable
        
    if input_yang_obj.reoriginate_ip_enable._changed():
        input_yang_obj.reoriginate_ip_enable = input_yang_obj.reoriginate_ip_enable
        
    if input_yang_obj.reoriginate_mac_ip_enable._changed():
        input_yang_obj.reoriginate_mac_ip_enable = input_yang_obj.reoriginate_mac_ip_enable
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn_default_route_originates(input_yang_obj.default_route_originates, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv6-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ipv6_prefix._changed():
        input_yang_obj.import_ipv6_prefix = input_yang_obj.import_ipv6_prefix
        
    if input_yang_obj.export_ipv6_prefix._changed():
        input_yang_obj.export_ipv6_prefix = input_yang_obj.export_ipv6_prefix
        
    if input_yang_obj.reoriginate_route_enable._changed():
        input_yang_obj.reoriginate_route_enable = input_yang_obj.reoriginate_route_enable
        
    if input_yang_obj.reoriginate_ipv6_enable._changed():
        input_yang_obj.reoriginate_ipv6_enable = input_yang_obj.reoriginate_ipv6_enable
        
    if input_yang_obj.reoriginate_mac_ipv6_enable._changed():
        input_yang_obj.reoriginate_mac_ipv6_enable = input_yang_obj.reoriginate_mac_ipv6_enable
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-labeluni/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-labeluni/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-labeluni

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af/ipv4-multicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_vpn(input_yang_obj.ipv4_vpn, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv6_vpn(input_yang_obj.ipv6_vpn, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_labeluni(input_yang_obj.ipv4_labeluni, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af_ipv4_multicast(input_yang_obj.ipv4_multicast, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.af.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs_af(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups/peer-group

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.local_if_name._changed():
        input_yang_obj.local_if_name = input_yang_obj.local_if_name
        
    if input_yang_obj.password_type._changed():
        input_yang_obj.password_type = input_yang_obj.password_type
        
    if input_yang_obj.password_text._changed():
        input_yang_obj.password_text = input_yang_obj.password_text
        
    if input_yang_obj.key_chain_name._changed():
        input_yang_obj.key_chain_name = input_yang_obj.key_chain_name
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.group_as._changed():
        input_yang_obj.group_as = input_yang_obj.group_as
        
    if input_yang_obj.local_if_address._changed():
        input_yang_obj.local_if_address = input_yang_obj.local_if_address
        
    if input_yang_obj.tcp_mss._changed():
        input_yang_obj.tcp_mss = input_yang_obj.tcp_mss
        
    if input_yang_obj.ebgp_max_hop._changed():
        input_yang_obj.ebgp_max_hop = input_yang_obj.ebgp_max_hop
        
    if input_yang_obj.valid_ttl_hops._changed():
        input_yang_obj.valid_ttl_hops = input_yang_obj.valid_ttl_hops
        
    if input_yang_obj.tracking_enable._changed():
        input_yang_obj.tracking_enable = input_yang_obj.tracking_enable
        
    if input_yang_obj.tracking_delay_time._changed():
        input_yang_obj.tracking_delay_time = input_yang_obj.tracking_delay_time
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.route_refresh._changed():
        input_yang_obj.route_refresh = input_yang_obj.route_refresh
        
    if input_yang_obj.four_byte_as._changed():
        input_yang_obj.four_byte_as = input_yang_obj.four_byte_as
        
    if input_yang_obj.ignore._changed():
        input_yang_obj.ignore = input_yang_obj.ignore
        
    if input_yang_obj.connect_mode._changed():
        input_yang_obj.connect_mode = input_yang_obj.connect_mode
        
    if input_yang_obj.log_change._changed():
        input_yang_obj.log_change = input_yang_obj.log_change
        
    if input_yang_obj.path_mtu_auto_discovery._changed():
        input_yang_obj.path_mtu_auto_discovery = input_yang_obj.path_mtu_auto_discovery
        
    if input_yang_obj.local_ifnet_disable._changed():
        input_yang_obj.local_ifnet_disable = input_yang_obj.local_ifnet_disable
        
    if input_yang_obj.check_first_as._changed():
        input_yang_obj.check_first_as = input_yang_obj.check_first_as
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_fake_as_parameter(input_yang_obj.fake_as_parameter, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_timer(input_yang_obj.timer, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_bfd_parameter(input_yang_obj.bfd_parameter, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_members(input_yang_obj.members, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group_afs(input_yang_obj.afs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_groups(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-groups

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups_peer_group(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_fake_as_parameter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/fake-as-parameter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.fake_as._changed():
        input_yang_obj.fake_as = input_yang_obj.fake_as
        
    if input_yang_obj.dual_as._changed():
        input_yang_obj.dual_as = input_yang_obj.dual_as
        
    if input_yang_obj.prepend_global_as._changed():
        input_yang_obj.prepend_global_as = input_yang_obj.prepend_global_as
        
    if input_yang_obj.prepend_fake_as._changed():
        input_yang_obj.prepend_fake_as = input_yang_obj.prepend_fake_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_timer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/timer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.keep_alive_time._changed():
        input_yang_obj.keep_alive_time = input_yang_obj.keep_alive_time
        
    if input_yang_obj.hold_time._changed():
        input_yang_obj.hold_time = input_yang_obj.hold_time
        
    if input_yang_obj.min_hold_time._changed():
        input_yang_obj.min_hold_time = input_yang_obj.min_hold_time
        
    if input_yang_obj.connect_retry_time._changed():
        input_yang_obj.connect_retry_time = input_yang_obj.connect_retry_time
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_bfd_parameter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/bfd-parameter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.block._changed():
        input_yang_obj.block = input_yang_obj.block
        
    if input_yang_obj.enable._changed():
        input_yang_obj.enable = input_yang_obj.enable
        
    if input_yang_obj.single_hop._changed():
        input_yang_obj.single_hop = input_yang_obj.single_hop
        
    if input_yang_obj.compatible._changed():
        input_yang_obj.compatible = input_yang_obj.compatible
        
    if input_yang_obj.per_link_echo._changed():
        input_yang_obj.per_link_echo = input_yang_obj.per_link_echo
        
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.min_rx_interval._changed():
        input_yang_obj.min_rx_interval = input_yang_obj.min_rx_interval
        
    if input_yang_obj.min_tx_interval._changed():
        input_yang_obj.min_tx_interval = input_yang_obj.min_tx_interval
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_import_filter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/import-filter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    if input_yang_obj.parameter._changed():
        input_yang_obj.parameter = input_yang_obj.parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_export_filter(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/export-filter

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.name._changed():
        input_yang_obj.name = input_yang_obj.name
        
    if input_yang_obj.parameter._changed():
        input_yang_obj.parameter = input_yang_obj.parameter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_default_route_match_conditions_default_route_match_condition(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/default-route-match-conditions/default-route-match-condition

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_default_route_match_conditions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/default-route-match-conditions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_match_condition.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_default_route_match_conditions_default_route_match_condition(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.orf_type._changed():
        input_yang_obj.orf_type = input_yang_obj.orf_type
        
    if input_yang_obj.orf_mode._changed():
        input_yang_obj.orf_mode = input_yang_obj.orf_mode
        
    if input_yang_obj.label_route_capability._changed():
        input_yang_obj.label_route_capability = input_yang_obj.label_route_capability
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_import_filter(input_yang_obj.import_filter, translated_yang_obj)
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_export_filter(input_yang_obj.export_filter, translated_yang_obj)
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.default_route_match_mode._changed():
        input_yang_obj.default_route_match_mode = input_yang_obj.default_route_match_mode
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_default_route_match_conditions(input_yang_obj.default_route_match_conditions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_default_route_match_conditions_default_route_match_condition(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-unicast/default-route-match-conditions/default-route-match-condition

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_default_route_match_conditions(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-unicast/default-route-match-conditions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_match_condition.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_default_route_match_conditions_default_route_match_condition(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-unicast/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-unicast/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-unicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.label_route_capability._changed():
        input_yang_obj.label_route_capability = input_yang_obj.label_route_capability
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.default_route_match_mode._changed():
        input_yang_obj.default_route_match_mode = input_yang_obj.default_route_match_mode
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ipv6_prefix._changed():
        input_yang_obj.import_ipv6_prefix = input_yang_obj.import_ipv6_prefix
        
    if input_yang_obj.export_ipv6_prefix._changed():
        input_yang_obj.export_ipv6_prefix = input_yang_obj.export_ipv6_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_default_route_match_conditions(input_yang_obj.default_route_match_conditions, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn_default_route_originates_default_route_originate(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-vpn/default-route-originates/default-route-originate

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn_default_route_originates(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-vpn/default-route-originates

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.default_route_originate.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn_default_route_originates_default_route_originate(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.reoriginate_route_enable._changed():
        input_yang_obj.reoriginate_route_enable = input_yang_obj.reoriginate_route_enable
        
    if input_yang_obj.reoriginate_ip_enable._changed():
        input_yang_obj.reoriginate_ip_enable = input_yang_obj.reoriginate_ip_enable
        
    if input_yang_obj.reoriginate_mac_ip_enable._changed():
        input_yang_obj.reoriginate_mac_ip_enable = input_yang_obj.reoriginate_mac_ip_enable
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn_default_route_originates(input_yang_obj.default_route_originates, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_vpn(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv6-vpn

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.nexthop_configure._changed():
        input_yang_obj.nexthop_configure = input_yang_obj.nexthop_configure
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ipv6_prefix._changed():
        input_yang_obj.import_ipv6_prefix = input_yang_obj.import_ipv6_prefix
        
    if input_yang_obj.export_ipv6_prefix._changed():
        input_yang_obj.export_ipv6_prefix = input_yang_obj.export_ipv6_prefix
        
    if input_yang_obj.reoriginate_route_enable._changed():
        input_yang_obj.reoriginate_route_enable = input_yang_obj.reoriginate_route_enable
        
    if input_yang_obj.reoriginate_ipv6_enable._changed():
        input_yang_obj.reoriginate_ipv6_enable = input_yang_obj.reoriginate_ipv6_enable
        
    if input_yang_obj.reoriginate_mac_ipv6_enable._changed():
        input_yang_obj.reoriginate_mac_ipv6_enable = input_yang_obj.reoriginate_mac_ipv6_enable
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni_route_limit(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-labeluni/route-limit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.number._changed():
        input_yang_obj.number = input_yang_obj.number
        
    if input_yang_obj.accept_prefix._changed():
        input_yang_obj.accept_prefix = input_yang_obj.accept_prefix
        
    if input_yang_obj.percent._changed():
        input_yang_obj.percent = input_yang_obj.percent
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.idle_timeout._changed():
        input_yang_obj.idle_timeout = input_yang_obj.idle_timeout
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni_public_as_only(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-labeluni/public-as-only

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.force._changed():
        input_yang_obj.force = input_yang_obj.force
        
    if input_yang_obj.limited._changed():
        input_yang_obj.limited = input_yang_obj.limited
        
    if input_yang_obj.replace._changed():
        input_yang_obj.replace = input_yang_obj.replace
        
    if input_yang_obj.no_skip_as._changed():
        input_yang_obj.no_skip_as = input_yang_obj.no_skip_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-labeluni

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.advertise_community._changed():
        input_yang_obj.advertise_community = input_yang_obj.advertise_community
        
    if input_yang_obj.reflect_client._changed():
        input_yang_obj.reflect_client = input_yang_obj.reflect_client
        
    if input_yang_obj.import_policy._changed():
        input_yang_obj.import_policy = input_yang_obj.import_policy
        
    if input_yang_obj.export_policy._changed():
        input_yang_obj.export_policy = input_yang_obj.export_policy
        
    if input_yang_obj.advertise_ext_community._changed():
        input_yang_obj.advertise_ext_community = input_yang_obj.advertise_ext_community
        
    if input_yang_obj.discard_ext_community._changed():
        input_yang_obj.discard_ext_community = input_yang_obj.discard_ext_community
        
    if input_yang_obj.allow_as_loop._changed():
        input_yang_obj.allow_as_loop = input_yang_obj.allow_as_loop
        
    if input_yang_obj.aigp._changed():
        input_yang_obj.aigp = input_yang_obj.aigp
        
    if input_yang_obj.add_path_mode._changed():
        input_yang_obj.add_path_mode = input_yang_obj.add_path_mode
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni_route_limit(input_yang_obj.route_limit, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni_public_as_only(input_yang_obj.public_as_only, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_multicast(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/ipv4-multicast

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.default_route_advertise._changed():
        input_yang_obj.default_route_advertise = input_yang_obj.default_route_advertise
        
    if input_yang_obj.default_route_advertise_policy._changed():
        input_yang_obj.default_route_advertise_policy = input_yang_obj.default_route_advertise_policy
        
    if input_yang_obj.import_ip_prefix._changed():
        input_yang_obj.import_ip_prefix = input_yang_obj.import_ip_prefix
        
    if input_yang_obj.export_ip_prefix._changed():
        input_yang_obj.export_ip_prefix = input_yang_obj.export_ip_prefix
        
    if input_yang_obj.import_as_path_filter._changed():
        input_yang_obj.import_as_path_filter = input_yang_obj.import_as_path_filter
        
    if input_yang_obj.export_as_path_filter._changed():
        input_yang_obj.export_as_path_filter = input_yang_obj.export_as_path_filter
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af/state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.version._changed():
        input_yang_obj.version = input_yang_obj.version
        
    if input_yang_obj.remote_router_id._changed():
        input_yang_obj.remote_router_id = input_yang_obj.remote_router_id
        
    if input_yang_obj.current_state._changed():
        input_yang_obj.current_state = input_yang_obj.current_state
        
    if input_yang_obj.local_port._changed():
        input_yang_obj.local_port = input_yang_obj.local_port
        
    if input_yang_obj.remote_port._changed():
        input_yang_obj.remote_port = input_yang_obj.remote_port
        
    if input_yang_obj.current_event._changed():
        input_yang_obj.current_event = input_yang_obj.current_event
        
    if input_yang_obj.last_state._changed():
        input_yang_obj.last_state = input_yang_obj.last_state
        
    if input_yang_obj.up_down_duration._changed():
        input_yang_obj.up_down_duration = input_yang_obj.up_down_duration
        
    if input_yang_obj.send_message._changed():
        input_yang_obj.send_message = input_yang_obj.send_message
        
    if input_yang_obj.rpd_capability._changed():
        input_yang_obj.rpd_capability = input_yang_obj.rpd_capability
        
    if input_yang_obj.local_rpd_capability._changed():
        input_yang_obj.local_rpd_capability = input_yang_obj.local_rpd_capability
        
    if input_yang_obj.negotiate_rpd_capability._changed():
        input_yang_obj.negotiate_rpd_capability = input_yang_obj.negotiate_rpd_capability
        
    if input_yang_obj.receive_message._changed():
        input_yang_obj.receive_message = input_yang_obj.receive_message
        
    if input_yang_obj.out_queue._changed():
        input_yang_obj.out_queue = input_yang_obj.out_queue
        
    if input_yang_obj.receive_hold_time._changed():
        input_yang_obj.receive_hold_time = input_yang_obj.receive_hold_time
        
    if input_yang_obj.receive_last_keepalive_time._changed():
        input_yang_obj.receive_last_keepalive_time = input_yang_obj.receive_last_keepalive_time
        
    if input_yang_obj.negotiate_hold_time._changed():
        input_yang_obj.negotiate_hold_time = input_yang_obj.negotiate_hold_time
        
    if input_yang_obj.negotiate_keepalive_time._changed():
        input_yang_obj.negotiate_keepalive_time = input_yang_obj.negotiate_keepalive_time
        
    if input_yang_obj.receive_update_count._changed():
        input_yang_obj.receive_update_count = input_yang_obj.receive_update_count
        
    if input_yang_obj.receive_open_count._changed():
        input_yang_obj.receive_open_count = input_yang_obj.receive_open_count
        
    if input_yang_obj.receive_keepalive_count._changed():
        input_yang_obj.receive_keepalive_count = input_yang_obj.receive_keepalive_count
        
    if input_yang_obj.receive_notification_count._changed():
        input_yang_obj.receive_notification_count = input_yang_obj.receive_notification_count
        
    if input_yang_obj.receive_route_refresh_count._changed():
        input_yang_obj.receive_route_refresh_count = input_yang_obj.receive_route_refresh_count
        
    if input_yang_obj.send_update_count._changed():
        input_yang_obj.send_update_count = input_yang_obj.send_update_count
        
    if input_yang_obj.send_open_count._changed():
        input_yang_obj.send_open_count = input_yang_obj.send_open_count
        
    if input_yang_obj.send_keepalive_count._changed():
        input_yang_obj.send_keepalive_count = input_yang_obj.send_keepalive_count
        
    if input_yang_obj.send_notification_count._changed():
        input_yang_obj.send_notification_count = input_yang_obj.send_notification_count
        
    if input_yang_obj.send_route_refresh_count._changed():
        input_yang_obj.send_route_refresh_count = input_yang_obj.send_route_refresh_count
        
    if input_yang_obj.send_graceful_restart_capability._changed():
        input_yang_obj.send_graceful_restart_capability = input_yang_obj.send_graceful_restart_capability
        
    if input_yang_obj.receive_refresh_capability._changed():
        input_yang_obj.receive_refresh_capability = input_yang_obj.receive_refresh_capability
        
    if input_yang_obj.receive_four_byte_as_capability._changed():
        input_yang_obj.receive_four_byte_as_capability = input_yang_obj.receive_four_byte_as_capability
        
    if input_yang_obj.receive_multi_protocol_capability._changed():
        input_yang_obj.receive_multi_protocol_capability = input_yang_obj.receive_multi_protocol_capability
        
    if input_yang_obj.receive_graceful_restart_capability._changed():
        input_yang_obj.receive_graceful_restart_capability = input_yang_obj.receive_graceful_restart_capability
        
    if input_yang_obj.receive_add_path._changed():
        input_yang_obj.receive_add_path = input_yang_obj.receive_add_path
        
    if input_yang_obj.negotiate_add_path._changed():
        input_yang_obj.negotiate_add_path = input_yang_obj.negotiate_add_path
        
    if input_yang_obj.receive_label_add_path._changed():
        input_yang_obj.receive_label_add_path = input_yang_obj.receive_label_add_path
        
    if input_yang_obj.negotiate_label_add_path._changed():
        input_yang_obj.negotiate_label_add_path = input_yang_obj.negotiate_label_add_path
        
    if input_yang_obj.receive_prefix._changed():
        input_yang_obj.receive_prefix = input_yang_obj.receive_prefix
        
    if input_yang_obj.receive_active_prefix._changed():
        input_yang_obj.receive_active_prefix = input_yang_obj.receive_active_prefix
        
    if input_yang_obj.advertise_prefix._changed():
        input_yang_obj.advertise_prefix = input_yang_obj.advertise_prefix
        
    if input_yang_obj.discard_attribute._changed():
        input_yang_obj.discard_attribute = input_yang_obj.discard_attribute
        
    if input_yang_obj.check_first_as._changed():
        input_yang_obj.check_first_as = input_yang_obj.check_first_as
        
    if input_yang_obj.extend_nexthop_capability._changed():
        input_yang_obj.extend_nexthop_capability = input_yang_obj.extend_nexthop_capability
        
    if input_yang_obj.egress_engineer_capability._changed():
        input_yang_obj.egress_engineer_capability = input_yang_obj.egress_engineer_capability
        
    if input_yang_obj.orf_capability._changed():
        input_yang_obj.orf_capability = input_yang_obj.orf_capability
        
    if input_yang_obj.rely_interface_capability._changed():
        input_yang_obj.rely_interface_capability = input_yang_obj.rely_interface_capability
        
    if input_yang_obj.remote_as._changed():
        input_yang_obj.remote_as = input_yang_obj.remote_as
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs/af

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_unicast(input_yang_obj.ipv4_unicast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_unicast(input_yang_obj.ipv6_unicast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_vpn(input_yang_obj.ipv4_vpn, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv6_vpn(input_yang_obj.ipv6_vpn, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_labeluni(input_yang_obj.ipv4_labeluni, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_ipv4_multicast(input_yang_obj.ipv4_multicast, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af_state(input_yang_obj.state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer/afs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.af.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs_af(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers_peer(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers/peer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        translated_yang_obj.remote_as = input_yang_obj.remote_as
        
    if input_yang_obj.group_name._changed():
        input_yang_obj.group_name = input_yang_obj.group_name
        
    if input_yang_obj.local_if_name._changed():
        input_yang_obj.local_if_name = input_yang_obj.local_if_name
        
    if input_yang_obj.password_type._changed():
        input_yang_obj.password_type = input_yang_obj.password_type
        
    if input_yang_obj.password_text._changed():
        input_yang_obj.password_text = input_yang_obj.password_text
        
    if input_yang_obj.key_chain_name._changed():
        input_yang_obj.key_chain_name = input_yang_obj.key_chain_name
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.local_if_address._changed():
        input_yang_obj.local_if_address = input_yang_obj.local_if_address
        
    if input_yang_obj.ebgp_max_hop._changed():
        input_yang_obj.ebgp_max_hop = input_yang_obj.ebgp_max_hop
        
    if input_yang_obj.tracking_enable._changed():
        input_yang_obj.tracking_enable = input_yang_obj.tracking_enable
        
    if input_yang_obj.tracking_delay_time._changed():
        input_yang_obj.tracking_delay_time = input_yang_obj.tracking_delay_time
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.route_refresh._changed():
        input_yang_obj.route_refresh = input_yang_obj.route_refresh
        
    if input_yang_obj.four_byte_as._changed():
        input_yang_obj.four_byte_as = input_yang_obj.four_byte_as
        
    if input_yang_obj.ignore._changed():
        input_yang_obj.ignore = input_yang_obj.ignore
        
    if input_yang_obj.valid_ttl_hops._changed():
        input_yang_obj.valid_ttl_hops = input_yang_obj.valid_ttl_hops
        
    if input_yang_obj.connect_mode._changed():
        input_yang_obj.connect_mode = input_yang_obj.connect_mode
        
    if input_yang_obj.log_change._changed():
        input_yang_obj.log_change = input_yang_obj.log_change
        
    if input_yang_obj.path_mtu_auto_discovery._changed():
        input_yang_obj.path_mtu_auto_discovery = input_yang_obj.path_mtu_auto_discovery
        
    if input_yang_obj.local_ifnet_disable._changed():
        input_yang_obj.local_ifnet_disable = input_yang_obj.local_ifnet_disable
        
    if input_yang_obj.check_first_as._changed():
        input_yang_obj.check_first_as = input_yang_obj.check_first_as
        
    if input_yang_obj.egress_engineer._changed():
        input_yang_obj.egress_engineer = input_yang_obj.egress_engineer
        
    if input_yang_obj.tcp_mss._changed():
        input_yang_obj.tcp_mss = input_yang_obj.tcp_mss
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_fake_as_parameter(input_yang_obj.fake_as_parameter, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_timer(input_yang_obj.timer, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_bfd_parameter(input_yang_obj.bfd_parameter, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer_afs(input_yang_obj.afs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peers(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.peer.iteritems():
        peer_obj = translated_yang_obj.bgp.neighbors.neighbor.add(k)
        peer_obj.enabled = "true"
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers_peer(listInst, peer_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_bfd_session_states_peer_bfd_session_state(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-bfd-session-states/peer-bfd-session-state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.if_name._changed():
        input_yang_obj.if_name = input_yang_obj.if_name
        
    if input_yang_obj.tx_interval._changed():
        input_yang_obj.tx_interval = input_yang_obj.tx_interval
        
    if input_yang_obj.rx_interval._changed():
        input_yang_obj.rx_interval = input_yang_obj.rx_interval
        
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    if input_yang_obj.global_bfd_enable._changed():
        input_yang_obj.global_bfd_enable = input_yang_obj.global_bfd_enable
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process_peer_bfd_session_states(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process/peer-bfd-session-states

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.peer_bfd_session_state.iteritems():
        innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_bfd_session_states_peer_bfd_session_state(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp_base_process(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp/base-process

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.router_id_auto_select._changed():
        input_yang_obj.router_id_auto_select = input_yang_obj.router_id_auto_select
        
    if input_yang_obj.effect_router_id._changed():
        input_yang_obj.effect_router_id = input_yang_obj.effect_router_id

    control_plane_protocol_obj = translated_yang_obj.routing.control_plane_protocols.control_plane_protocol.add(type="bgp", name="bgp200")
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_afs(input_yang_obj.afs, control_plane_protocol_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_groups(input_yang_obj.peer_groups, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp_base_process_peers(input_yang_obj.peers, control_plane_protocol_obj)
        
    # innerobj = _translate__network_instance_instances_instance_bgp_base_process_peer_bfd_session_states(input_yang_obj.peer_bfd_session_states, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance_bgp(input_yang_obj, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instance/instances/instance/bgp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__network_instance_instances_instance_bgp_base_process(input_yang_obj.base_process, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances_instance(input_yang_obj, translated_yang_obj=None):
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
        
    innerobj = _translate__network_instance_instances_instance_afs(input_yang_obj.afs, translated_yang_obj)
        
    # innerobj = _translate__network_instance_instances_instance_mpls(input_yang_obj.mpls, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_isis(input_yang_obj.isis, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_srv6(input_yang_obj.srv6, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_ipv4_ifs(input_yang_obj.ipv4_ifs, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_ipv4_if_states(input_yang_obj.ipv4_if_states, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_ipv6_ifs(input_yang_obj.ipv6_ifs, translated_yang_obj)
    #
    # innerobj = _translate__network_instance_instances_instance_ipv6_if_states(input_yang_obj.ipv6_if_states, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances_instance_bgp(input_yang_obj.bgp, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance_instances(input_yang_obj, translated_yang_obj=None):
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
        innerobj = _translate__network_instance_instances_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instance(input_yang_obj, translated_yang_obj=None):
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
    
    innerobj = _translate__network_instance_global(input_yang_obj.global_, translated_yang_obj)
        
    innerobj = _translate__network_instance_instances(input_yang_obj.instances, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_network_instance(input_yang_obj, translated_yang_obj=None, xpath=None):
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
    print("huawei ntw script")
    translated_yang_obj = ietf_routing()
    xpath = '/a:routing'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
    target_xpath = XPATH(xpath, ns_map)

    innerobj = _translate__network_instance(input_yang_obj.network_instance, translated_yang_obj)
        
    return [[translated_yang_obj.routing, target_xpath]]
