from swagger_server.yang_bindings.src_yang_bindings import ietf_interfaces_binding

from swagger_server.translation_scripts.src2target import _translate_ietf_interfaces_obj
"""
    The translate_yang_registry dictionary is of the form :
    {Forth_tuple:{ yang_namespace:(Python-Module-For-Translation, Binding-file-of-Yang-Module, Yang-Module-name)}}
    Forth_tuple : (vendor, product, type, version)
    
    'urn:ietf:params:xml:ns:yang:ietf-interfaces':(_translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces")
"""
translate_yang_registry = {('huawei', 'switch', 'S5700', '8.1.30'):
                               {'urn:ietf:params:xml:ns:yang:ietf-interfaces': (
                               _translate_ietf_interfaces_obj, ietf_interfaces_binding, "ietf_interfaces")}
                           }

