from mediator_server.yang_bindings.src_yang_bindings import ietf_interfaces_binding
from mediator_server.yang_bindings.src_yang_bindings import ietf_routing_binding
from mediator_server.yang_bindings.src_yang_bindings import ietf_l3vpn_ntw_binding, ietf_network_instance_schema_mount_binding
from mediator_server.yang_bindings.target_yang_bindings import huawei_ifm_binding, huawei_bgp_binding, huawei_network_instance_binding, huawei_network_instance_sm_binding

from mediator_server.translation_scripts.src2target import _translate_ietf_interfaces_interface_obj, _translate_ietf_routing_control_plane_protocol_obj1
from mediator_server.translation_scripts.src2target import _translate_ietf_interfaces_obj
from mediator_server.translation_scripts.src2target import _translate_ietf_interfaces_interface_ipv4_obj
from mediator_server.translation_scripts.src2target import _translate_ietf_routing_obj, _translate_ietf_routing_obj1, _translate_ietf_routing_control_plane_protocol_obj, _translate_ietf_routing_bgp_obj
from mediator_server.translation_scripts.src2target import _translate_ietf_l3vpn_ntw_obj, _translate_ietf_l3vpn_ntw_vpn_service_obj
from mediator_server.translation_scripts.src2target import _translate_ietf_network_instance_obj
from mediator_server.translation_scripts.target2src import _translate_huawei_ifm_obj, _translate_huawei_ifm_obj1
from mediator_server.translation_scripts.target2src import _translate_huawei_bgp_obj, _translate_huawei_bgp_obj1
from mediator_server.translation_scripts.target2src import _translate_huawei_network_instance_obj, _translate_huawei_network_instance_obj1, _translate_huawei_network_instance_obj2

"""
    The translate_yang_registry dictionary is of the form :
    {Forth_tuple:{ yang_namespace:(Python-Module-For-Translation, Binding-file-of-Yang-Module, Yang-Module-name)}}
    Forth_tuple : (vendor, product, type, version)
    
    'urn:ietf:params:xml:ns:yang:ietf-interfaces':(_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces")
"""
translate_yang_registry = {('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2'):
                               {
                                # ietf-interfaces scripts
                                '/a:interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces"),
                                '/ietf-interfaces:interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces"),
                                '/ietf-interfaces:interfaces/interface': (_translate_ietf_interfaces_interface_obj, ietf_interfaces_binding, "yc_interfaces_ietf_interfaces__interfaces"),
                                '/ietf-interfaces:interfaces/interface/ietf-ip:ipv4': (_translate_ietf_interfaces_interface_ipv4_obj, ietf_interfaces_binding, "yc_interface_ietf_interfaces__interfaces_interface"),
                                # ietf-routing scripts
                                # schema-mount script --> ietf
                                '/ietf-routing:routing': (_translate_ietf_routing_obj1, ietf_network_instance_schema_mount_binding, "ietf_routing"),
                                '/ietf-routing:routing/control-plane-protocols/control-plane-protocol': (_translate_ietf_routing_control_plane_protocol_obj1, ietf_network_instance_schema_mount_binding, "yc_control_plane_protocols_ietf_routing__routing_control_plane_protocols"),
                                '/a:routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
                                # '/ietf-routing:routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
                                # '/ietf-routing:routing/control-plane-protocols/control-plane-protocol': (_translate_ietf_routing_control_plane_protocol_obj, ietf_routing_binding, "yc_control_plane_protocols_ietf_routing__routing_control_plane_protocols"),
                                '/ietf-routing:routing/control-plane-protocols/control-plane-protocol/ietf-bgp:bgp': (_translate_ietf_routing_bgp_obj, ietf_routing_binding, "yc_control_plane_protocol_ietf_routing__routing_control_plane_protocols_control_plane_protocol"),
                                # ietf-l3vpn-ntw scripts
                                '/a:l3vpn-ntw': (_translate_ietf_l3vpn_ntw_obj, ietf_l3vpn_ntw_binding, "ietf_l3vpn_ntw"),
                                '/ietf-l3vpn-ntw:l3vpn-ntw': (_translate_ietf_l3vpn_ntw_obj, ietf_l3vpn_ntw_binding, "ietf_l3vpn_ntw"),
                                '/ietf-l3vpn-ntw:l3vpn-ntw/vpn-services/vpn-service': (_translate_ietf_l3vpn_ntw_vpn_service_obj, ietf_l3vpn_ntw_binding, "yc_vpn_services_ietf_l3vpn_ntw__l3vpn_ntw_vpn_services"),
                                # ietf-network-instance scripts
                                '/ietf-network-instance:network-instances': (_translate_ietf_network_instance_obj, ietf_network_instance_schema_mount_binding, "ietf_network_instance"),
                                # huawei-ifm scripts
                                '/huawei-ifm:ifm': (_translate_huawei_ifm_obj, huawei_ifm_binding, "huawei_ifm"),
                                '/huawei-ifm:ifm1': (_translate_huawei_ifm_obj1, huawei_ifm_binding, "huawei_ifm"),
                                # huawei-bgp scripts
                                '/huawei-bgp:bgp': (_translate_huawei_bgp_obj, huawei_bgp_binding, "huawei_bgp"),
                                '/huawei-bgp:bgp1': (_translate_huawei_bgp_obj1, huawei_bgp_binding, "huawei_bgp"),
                                # huawei-network-instance scripts
                                # '/huawei-network-instance:network-instance': (_translate_huawei_network_instance_obj, huawei_bgp_binding, "huawei_network_instance"),
                                # '/huawei-network-instance:network-instance1': (_translate_huawei_network_instance_obj1, huawei_bgp_binding, "huawei_network_instance")
                                # schema-mount script --> huawei
                                '/huawei-network-instance:network-instance': (_translate_huawei_network_instance_obj2, huawei_network_instance_sm_binding, "huawei_network_instance"),
                               }
                           }

