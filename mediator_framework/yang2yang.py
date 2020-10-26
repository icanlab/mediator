from mediator_translator.l3sm.ietf.vendors.huawei.register.translate_app_register import *

from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder
from pyangbind.lib.yangtypes import safe_name
from lxml import objectify, etree
from copy import deepcopy

def get_translate_pymodule(namespace):
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None

    return PyTranslateReg[0]

def get_translate_yangbinding(namespace):
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None

    return PyTranslateReg[1]

def get_translate_yangmodule(namespace):
    PyTranslateReg = translate_yang_registry.get(namespace)
    if None == PyTranslateReg:
        return None

    return PyTranslateReg[2]


def get_yangobj_namespace(py_yang_obj):
    """
        Note: The "py_yang_obj" should point to the top level node.
    """
    if hasattr(py_yang_obj, "_yang_namespace"):
        return py_yang_obj._yang_namespace

    return None

def get_yangobj_name(py_yang_obj):

    if hasattr(py_yang_obj, "_yang_name"):
        return py_yang_obj._yang_name

    return None

def add_to_dummy_xml(app_xml_node):

    dummy_root_node = objectify.Element("dummy_root")
    dummy_root_node.append(deepcopy(app_xml_node))

    return dummy_root_node

def get_yang_obj_from_xmldoc(top_level_datanode_xml):

    qn = etree.QName(top_level_datanode_xml)
    binding = get_translate_yangbinding(qn.namespace)

    # Check if binding is defined for it. If not, then we cannot convert to OBJ.
    if binding is None:
        return None

    # pyangbind, expects that each app-node has a parent and that app-node has no sibling.
    # So we need to deepcopy to another dummy root and pass that as parent.
    dummy_root_node = add_to_dummy_xml(top_level_datanode_xml)

    module_name = get_translate_yangmodule(qn.namespace)

    # Load the XML and parse the XML. Returns the YANG object corresponding the XML
    return pybindIETFXMLDecoder.load_xml(dummy_root_node, parent=binding, yang_base=module_name)


def translate_to_new_yangobj(module_yang_obj):

    namespace = get_yangobj_namespace(module_yang_obj)
    translate_py = get_translate_pymodule(namespace)

    #Use the APP's function to convert from Input Python YANG object to its own type.
    #translated_obj_list = translate_py.translate_module_data(module_yang_obj)
    api_name  = "_translate__%s" % (safe_name(module_yang_obj._yang_name))

    #The translate API is part of the Yang module's top level object.
    translate_api = getattr(translate_py, api_name)

    translated_obj_list = translate_api(module_yang_obj)

    return translated_obj_list

def translate_to_new_yang_xmldoc(module_yang_obj):

    # Get the list of obj, that we can get from the new yang obj.
    translated_obj_list = translate_to_new_yangobj(module_yang_obj)

    module_xml_doc_list = []

    for translated_obj in translated_obj_list:

        # Convert this YANG object to its corresponding XML-doc
        module_xml_doc = pybindIETFXMLEncoder.encode(translated_obj)
        module_xml_doc_list.append(module_xml_doc)

    return module_xml_doc_list