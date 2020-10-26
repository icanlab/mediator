
import ncclient
from ncclient import manager, capabilities, operations
from lxml import objectify, etree
import copy

from mediator_framework import yang2yang


# Macro definitions.
BASE_NS_1_0 = "urn:ietf:params:xml:ns:netconf:base:1.0"
OPER_GET_CONFIG = 1
OPER_EDIT_CONFIG = 2

def parse_xml_rsp(result_xml):

    print('In parse xml rsp:\n',result_xml)

    xml_bytes = bytes(bytearray(result_xml, encoding = 'utf-8'))

    # using a custom parser to strip comments (so we don't handle them later)
    parser = objectify.makeparser(remove_comments=True, remove_blank_text=True)
    doc = objectify.fromstring(xml_bytes, parser=parser)
    return doc


def get_datanode_in_rpcreply(rpcreply):
    doc = parse_xml_rsp(rpcreply)

    for child in doc.getchildren():
        # Check with the qualified name for 'data'
        data_node = "{%s}data" % BASE_NS_1_0
        if data_node == child.tag:
            return child, doc

    return None, None


def add_children(parent_node, xml_doc_list):
    for xml_doc in xml_doc_list:
        parent_node.append(xml_doc)

    return

def create_filternode_xmlstr(xml_doc_list):

    filterNode = etree.Element("filter",  type="subtree", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    add_children(filterNode, xml_doc_list)
    return etree.tostring(filterNode, pretty_print=True).decode("utf8")

def create_confignode_xmlstr(xml_doc_list):

    configNode = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    add_children(configNode, xml_doc_list)
    return etree.tostring(configNode, pretty_print=True).decode("utf8")

def call_ncclient(operation_type, xml_doc_list):

    ispass = False
    replyxml = None

    m = manager.connect(host="10.18.105.180", port="10422", username="netconf",password = "Root@123",  hostkey_verify=False, device_params={'name': 'huaweiyang'})

    if (operation_type == OPER_GET_CONFIG):
        filterNodeStr = create_filternode_xmlstr(xml_doc_list)
        print('filterNode str', filterNodeStr)

        try:
            result = m.get_config(source='running', filter=filterNodeStr)
            ispass = True
            replyxml = result.xml
        except operations.rpc.RPCError as err:
            print('dir of RPC error', dir(err), err._message , '\n', err.path, '\n', ncclient.xml_.to_xml(err.xml))
            errpath = "{%s}error-path" % BASE_NS_1_0
            raw = err.xml
            for subele in raw:
                if errpath == subele.tag:
                    print('error-path:', ncclient.xml_.to_xml(subele))
            ispass = False
            replyxml = err.xml
        finally:
            m.close_session()

    elif (operation_type == OPER_EDIT_CONFIG):

        configNode = create_confignode_xmlstr(xml_doc_list)
        print('configNode str', configNode)

        try:
            result = m.edit_config(target='running', config=configNode) # type: operations.RPCReply
            ispass = result.ok
            replyxml = result.xml
        except operations.rpc.RPCError as err:
            print('dir of RPC error', dir(err), err._message , '\n', err.path, '\n', ncclient.xml_.to_xml(err.xml))
            errpath = "{%s}error-path" % BASE_NS_1_0
            raw = err.xml
            for subele in raw:
                if errpath == subele.tag:
                    print('error-path:', ncclient.xml_.to_xml(subele))
            ispass = False
            replyxml = err.xml
        finally:
            m.close_session()

    return ispass, replyxml

def call_ncclient_ex(operation_type, xmlstr):

    ispass = False
    replyxml = None

    m = manager.connect(host="10.18.105.180", port="10422", username="netconf",password = "Root@123",  hostkey_verify=False, device_params={'name': 'huaweiyang'})

    if (operation_type == OPER_GET_CONFIG):
        print('filterNode str', xmlstr)

        try:
            result = m.get_config(source='running', filter=xmlstr)
            ispass = True
            replyxml = result.xml
        except operations.rpc.RPCError as err:
            print('dir of RPC error', dir(err), err._message , '\n', err.path, '\n', ncclient.xml_.to_xml(err.xml))
            errpath = "{%s}error-path" % BASE_NS_1_0
            raw = err.xml
            for subele in raw:
                if errpath == subele.tag:
                    print('error-path:', ncclient.xml_.to_xml(subele))
            ispass = False
            replyxml = err.xml
        finally:
            m.close_session()

    elif (operation_type == OPER_EDIT_CONFIG):

        print('configNode str', xmlstr)

        try:
            result = m.edit_config(target='running', config=xmlstr) # type: operations.RPCReply
            ispass = result.ok
            replyxml = result.xml
        except operations.rpc.RPCError as err:
            print('dir of RPC error', dir(err), err._message , '\n', err.path, '\n', ncclient.xml_.to_xml(err.xml))
            errpath = "{%s}error-path" % BASE_NS_1_0
            raw = err.xml
            for subele in raw:
                if errpath == subele.tag:
                    print('error-path:', ncclient.xml_.to_xml(subele))
            ispass = False
            replyxml = err.xml
        finally:
            m.close_session()

    return ispass, replyxml


def get_rpc_oper_info(xml_root):

    getconfig = "{%s}get-config" % BASE_NS_1_0
    editconfig = "{%s}edit-config" % BASE_NS_1_0

    for child in xml_root.getchildren():
        if getconfig == child.tag:
            return OPER_GET_CONFIG, child
        elif editconfig == child.tag:
            return OPER_EDIT_CONFIG, child
        else:
            return None, None

    return None, None


def get_filternode_for_get_config(operNode):
    for child in operNode.getchildren():
        if ("{urn:ietf:params:xml:ns:netconf:base:1.0}filter" == child.tag):
            return child
    return None



def get_confignode_for_edit_config(operNode):
    for child in operNode.getchildren():
        if ("{urn:ietf:params:xml:ns:netconf:base:1.0}config" == child.tag):
            return child
    return None


def get_appnode_for_edit_config(operNode):
    for child in operNode.getchildren():
        if ("{urn:ietf:params:xml:ns:netconf:base:1.0}config" == child.tag):
            for grandchild in child.getchildren():
                appnode = grandchild
                return appnode
    return None



def parse_xmlreq(xmlreq):
    print('In parse xmlreq:\n',xmlreq)


    # using a custom parser to strip comments (so we don't handle them later)
    parser = objectify.makeparser(remove_comments=True, remove_blank_text=True)
    xml_root = objectify.fromstring(xmlreq, parser=parser)
    return xml_root

def translate_query_datanodersp_content(datanode):
    need_translate = False
    translated_node = None

    translated_node = etree.Element("data",  nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})

    for appnode in datanode.getchildren():
        #Use the namespace of the nodes and get the Python Yang Object for this XML node.
        module_yang_obj = yang2yang.get_yang_obj_from_xmldoc(appnode)
        print(module_yang_obj)

        if module_yang_obj != None:
            need_translate = True

            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = yang2yang.translate_to_new_yang_xmldoc(module_yang_obj)
            add_children(translated_node, module_xml_doc_list)

    # Return translated, if we have translated anything.
    if need_translate is True:
        return True, translated_node
    else :
        return False, datanode

def translate_query_filternode_content(filterNode):
    need_translate = False

    translated_filter = etree.Element("filter",  type="subtree", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})


    for appnode in filterNode.getchildren():
        #Use the namespace of the nodes and get the Python Yang Object for this XML node.
        module_yang_obj = yang2yang.get_yang_obj_from_xmldoc(appnode)

        if module_yang_obj != None:
            need_translate = True

            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = yang2yang.translate_to_new_yang_xmldoc(module_yang_obj)
            add_children(translated_filter, module_xml_doc_list)

    # Return translated, if we have translated anything.
    if need_translate is True:
        return True, translated_filter
    else :
        return False, filterNode

def translate_edit_confignode_content(configNode):
    need_translate = False
    translated_node = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})

    for appnode in configNode.getchildren():
        #Use the namespace of the nodes and get the Python Yang Object for this XML node.
        # print(etree.tostring(appnode))
        module_yang_obj = yang2yang.get_yang_obj_from_xmldoc(appnode)
        if module_yang_obj != None:
            need_translate = True

            # translate this yang-obj to the new yang-obj and get its xml-doc.
            module_xml_doc_list = yang2yang.translate_to_new_yang_xmldoc(module_yang_obj)
            add_children(translated_node, module_xml_doc_list)

    # Return translated, if we have translated anything.
    if need_translate is True:
        return True, translated_node
    else :
        return False, configNode

def translate_query_filter_content(filterstr):
    filterNode = parse_xmlreq(filterstr)

    translated, translated_filter = translate_query_filternode_content(filterNode)
    if translated == True:
        return etree.tostring(translated_filter, pretty_print=True).decode("utf8")
    else:
        return filterstr


def translate_edit_config_content(configstr):
    configNode = parse_xmlreq(configstr)

    translated, translated_node = translate_edit_confignode_content(configNode)
    if translated == True:
        return etree.tostring(translated_node, pretty_print=True).decode("utf8")
    else:
        return configstr


def translate_rpcreply_data(rpcreply):
    datanode, rpcreply_node = get_datanode_in_rpcreply(rpcreply)

    translated, translated_datanode =  translate_query_datanodersp_content(datanode)
    if translated is False:
        return rpcreply
    else:
        for child in rpcreply_node.getchildren():
            if ("{urn:ietf:params:xml:ns:netconf:base:1.0}data" == child.tag):
                # Remove the "data" node child and add the newly created one.
                rpcreply_node.remove(child)
                rpcreply_node.append(copy.deepcopy(translated_datanode))
                return etree.tostring(rpcreply_node, pretty_print=True).decode("utf8")

        return None

def translate_get_config_request(operNode):

    filterNode = get_filternode_for_get_config(operNode)

    translated, translated_filter = translate_query_filternode_content(filterNode)
    xmlstr = etree.tostring(translated_filter, pretty_print=True).decode("utf8")

    #Send XML doc to NCC
    ifpass, result_xml = call_ncclient_ex(OPER_GET_CONFIG, xmlstr)
    if ifpass == False:
        return False, result_xml
    """
    # Use the namespace of the nodes and get the Python Yang Object for this XML node.
    datanode, rpcreply_node = get_datanode_in_rpcreply(result_xml)

    translated, translated_datanode =  translate_query_datanodersp_content(datanode)

    if translated is True:
        translated_mod_rsp = etree.tostring(translated_datanode, pretty_print=True).decode("utf8")
    else:
        translated_mod_rsp = etree.tostring(datanode, pretty_print=True).decode("utf8")
        """
    translated_mod_rsp = translate_rpcreply_data(result_xml)

    return True, translated_mod_rsp

def translate_edit_config(operNode):

    appnode = get_appnode_for_edit_config(operNode)
    print('AppNode:', appnode.tag)

    #Use the namespace of the nodes and get the Python Yang Object for this XML node.
    module_yang_obj = yang2yang.get_yang_obj_from_xmldoc(appnode)

    # translate this yang-obj to the new yang-obj and get its xml-doc.
    module_xml_doc_list = yang2yang.translate_to_new_yang_xmldoc(module_yang_obj)

    #Send XML doc to NCC
    ifpass, result_xml = call_ncclient(OPER_EDIT_CONFIG, module_xml_doc_list)
    if ifpass == False:
        return False, result_xml

    print('Edit config is success!!!')

    return True, None


def translate_rpc_request(operationType, operNode):

    if OPER_GET_CONFIG == operationType:
        return translate_get_config_request(operNode)

    elif OPER_EDIT_CONFIG == operationType:
        return translate_edit_config(operNode)


def netconf_translate_req_xmldoc(xml_doc):

    operationType, operNode = get_rpc_oper_info(xml_doc)
    print("operationType, dataNode", operationType, operNode.tag)

    return translate_rpc_request(operationType, operNode)



def netconf_translate_req_xmlstr(xml_req):

    xml_root = parse_xmlreq(xml_req)

    return netconf_translate_req_xmldoc(xml_root)


