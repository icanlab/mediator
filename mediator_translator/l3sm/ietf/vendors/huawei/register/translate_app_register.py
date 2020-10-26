
# Import APP translator
from ..scripts import _translate_ietf_interfaces_obj
from ..scripts import _translate_ietf_routing_obj
from ..scripts import _translate_ietf_l3vpn_ntw_obj

# # Import yang bindings
from mediator_translator.l3sm.ietf.yang_bindings import ietf_interfaces_binding
from mediator_translator.l3sm.ietf.yang_bindings import ietf_routing_binding
from mediator_translator.l3sm.ietf.yang_bindings import ietf_l3vpn_ntw_binding

"""
    The translate_yang_registry dictionary is of the form :
    {Yang-Module-namespace : (Python-Module-For-Translation, Binding-file-of-Yang-Module, Yang-Module-name)}


   'urn:ietf:params:xml:ns:yang:ietf-routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf-routing"),
   'http://www.huawei.com/netconf/vrp/huawei-segripv6': (_translate_huawei_segripv6_obj, huawei_srv6_binding, "huawei-segripv6"),
"""
translate_yang_registry = {'urn:ietf:params:xml:ns:yang:ietf-interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces"),
                           'urn:ietf:params:xml:ns:yang:ietf-routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
                           'urn:ietf:params:xml:ns:yang:ietf-l3vpn-ntw': (_translate_ietf_l3vpn_ntw_obj, ietf_l3vpn_ntw_binding, "ietf_l3vpn_ntw")}


