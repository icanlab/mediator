from yang_bindings.src_yang_bindings import ietf_interfaces_binding

from translation_scripts.src2target import _translate_ietf_interfaces_obj
"""
    The translate_yang_registry dictionary is of the form :
    {Yang-Module-namespace : (Python-Module-For-Translation, Binding-file-of-Yang-Module, Yang-Module-name)}


   'urn:ietf:params:xml:ns:yang:ietf-routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf-routing"),
"""
translate_yang_registry = {'urn:ietf:params:xml:ns:yang:ietf-interfaces': (_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces")}


