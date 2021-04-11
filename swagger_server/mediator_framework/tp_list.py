from swagger_server.yang_bindings.src_yang_bindings import ietf_interfaces_binding
from swagger_server.yang_bindings.src_yang_bindings import ietf_routing_binding
from swagger_server.yang_bindings.src_yang_bindings import ietf_l3vpn_ntw_binding
from swagger_server.yang_bindings.target_yang_bindings import huawei_ifm_binding

from swagger_server.translation_scripts.src2target import _translate_ietf_interfaces_interface_obj
from swagger_server.translation_scripts.src2target import _translate_ietf_interfaces_obj
from swagger_server.translation_scripts.src2target import _translate_ietf_interfaces_interface_ipv4_obj
from swagger_server.translation_scripts.src2target import _translate_ietf_routing_obj
from swagger_server.translation_scripts.src2target import _translate_ietf_l3vpn_ntw_obj
from swagger_server.translation_scripts.target2src import _translate_huawei_ifm_obj
"""
    The translate_yang_registry dictionary is of the form :
    {Forth_tuple:{ yang_namespace:(Python-Module-For-Translation, Binding-file-of-Yang-Module, Yang-Module-name)}}
    Forth_tuple : (vendor, product, type, version)
    
    'urn:ietf:params:xml:ns:yang:ietf-interfaces':(_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces")
"""
translate_yang_registry = {('HUAWEI', 'ROUTER6500', 'HUAWEIOS', '1.0.1111.2'):
                               {'/interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces"),
                                '/routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
                                '/l3vpn-ntw': (_translate_ietf_l3vpn_ntw_obj, ietf_l3vpn_ntw_binding, "ietf_l3vpn_ntw"),
                                '/ifm': (_translate_huawei_ifm_obj, huawei_ifm_binding, "huawei_ifm"),
                                '/ietf-interfaces:interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces"),
                                '/ietf-interfaces:interfaces/interface': (_translate_ietf_interfaces_interface_obj, ietf_interfaces_binding, "yc_interfaces_ietf_interfaces__interfaces"),
                                '/ietf-interfaces:interfaces/interface/ietf-ip:ipv4': (_translate_ietf_interfaces_interface_ipv4_obj, ietf_interfaces_binding, "yc_interface_ietf_interfaces__interfaces_interface"),
                                '/ietf-routing:routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
                                '/ietf-l3vpn-ntw:l3vpn-ntw': (_translate_ietf_l3vpn_ntw_obj, ietf_l3vpn_ntw_binding, "ietf_l3vpn_ntw"),
                                '/huawei-ifm:ifm': (_translate_huawei_ifm_obj, huawei_ifm_binding, "huawei_ifm")}
                           }

