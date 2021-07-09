from mediator_server.mediator_framework.adaptor import XPATH
from mediator_server.yang_bindings.src_yang_bindings.ietf_105_binding import ietf_routing
from mediator_server.yang_bindings.target_yang_bindings.huawei_segripv6_binding import *


def _translate__segripv6_srv6Site_encapSource(input_yang_obj: yc_encapSource_huawei_segripv6__segripv6_srv6Site_encapSource, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Site/encapSource

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.encapSrcAddr._changed():
        translated_yang_obj.routing.srv6.encapsulation.source_address = input_yang_obj.encapSrcAddr
        
    if input_yang_obj.encapSrcAddrTTL._changed():
        translated_yang_obj.routing.srv6.encapsulation.ip_ttl_propagation = input_yang_obj.encapSrcAddrTTL
        
    return translated_yang_obj

def _translate__segripv6_srv6Site(input_yang_obj: yc_srv6Site_huawei_segripv6__segripv6_srv6Site, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Site

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.srv6Enable._changed():
        translated_yang_obj.routing.srv6.enable = input_yang_obj.srv6Enable
        
    if input_yang_obj.teEnable._changed():
        input_yang_obj.teEnable = input_yang_obj.teEnable
        
    if input_yang_obj.teFrrEnable._changed():
        input_yang_obj.teFrrEnable = input_yang_obj.teFrrEnable
        
    innerobj = _translate__segripv6_srv6Site_encapSource(input_yang_obj.encapSource, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6RemoteEndOtps_srv6RemoteEndOtp(input_yang_obj: yc_srv6RemoteEndOtp_huawei_segripv6__segripv6_srv6RemoteEndOtps_srv6RemoteEndOtp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6RemoteEndOtps/srv6RemoteEndOtp

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefixLength._changed():
        input_yang_obj.prefixLength = input_yang_obj.prefixLength
        
    return translated_yang_obj

def _translate__segripv6_srv6RemoteEndOtps(input_yang_obj: yc_srv6RemoteEndOtps_huawei_segripv6__segripv6_srv6RemoteEndOtps, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6RemoteEndOtps

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6RemoteEndOtp.iteritems():
        innerobj = _translate__segripv6_srv6RemoteEndOtps_srv6RemoteEndOtp(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes_endOpcode(input_yang_obj: yc_endOpcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes_endOpcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endOpcodes/endOpcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes(input_yang_obj: yc_endOpcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endOpcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endOpcode.iteritems():
        # print(k)
        sid_obj = translated_yang_obj.static.local_sids.sid.add("65")
        sid_obj.end_behavior_type = "End"
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes_endOpcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes_endOtpOpcode(input_yang_obj: yc_endOtpOpcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes_endOtpOpcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endOtpOpcodes/endOtpOpcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes(input_yang_obj: yc_endOtpOpcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endOtpOpcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endOtpOpcode.iteritems():
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes_endOtpOpcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes_endxOpcode(input_yang_obj: yc_endxOpcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes_endxOpcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endxOpcodes/endxOpcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ifName._changed():
        input_yang_obj.ifName = input_yang_obj.ifName
        
    if input_yang_obj.nextHop._changed():
        input_yang_obj.nextHop = input_yang_obj.nextHop
        
    if input_yang_obj.flavor._changed():
        input_yang_obj.flavor = input_yang_obj.flavor
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes(input_yang_obj: yc_endxOpcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endxOpcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endxOpcode.iteritems():
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes_endxOpcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes_endDt4Opcode(input_yang_obj: yc_endDt4Opcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes_endDt4Opcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDt4Opcodes/endDt4Opcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vpnName._changed():
        translated_yang_obj.end_dt4.lookup_table_ipv4 = input_yang_obj.vpnName
        
    if input_yang_obj.protocolType._changed():
        input_yang_obj.protocolType = input_yang_obj.protocolType
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes(input_yang_obj: yc_endDt4Opcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDt4Opcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endDt4Opcode.iteritems():
        # print("Dt4:", k)
        sid_obj = translated_yang_obj.static.local_sids.sid.add("66")
        sid_obj.end_behavior_type = "End.DT4"
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes_endDt4Opcode(listInst, sid_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes_endDt6Opcode(input_yang_obj: yc_endDt6Opcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes_endDt6Opcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDt6Opcodes/endDt6Opcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vpnName._changed():
        input_yang_obj.vpnName = input_yang_obj.vpnName
        
    if input_yang_obj.protocolType._changed():
        input_yang_obj.protocolType = input_yang_obj.protocolType
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes(input_yang_obj: yc_endDt6Opcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDt6Opcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endDt6Opcode.iteritems():
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes_endDt6Opcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes_endDx2Opcode(input_yang_obj: yc_endDx2Opcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes_endDx2Opcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDx2Opcodes/endDx2Opcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.evplID._changed():
        input_yang_obj.evplID = input_yang_obj.evplID
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes(input_yang_obj: yc_endDx2Opcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDx2Opcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endDx2Opcode.iteritems():
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes_endDx2Opcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes_endDx2lOpcode(input_yang_obj: yc_endDx2lOpcode_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes_endDx2lOpcode, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDx2lOpcodes/endDx2lOpcode

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.evplID._changed():
        input_yang_obj.evplID = input_yang_obj.evplID
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes(input_yang_obj: yc_endDx2lOpcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes/endDx2lOpcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endDx2lOpcode.iteritems():
        innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes_endDx2lOpcode(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes(input_yang_obj: yc_srv6Opcodes_huawei_segripv6__segripv6_srv6Locators_srv6Locator_srv6Opcodes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator/srv6Opcodes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOpcodes(input_yang_obj.endOpcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endOtpOpcodes(input_yang_obj.endOtpOpcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endxOpcodes(input_yang_obj.endxOpcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt4Opcodes(input_yang_obj.endDt4Opcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDt6Opcodes(input_yang_obj.endDt6Opcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2Opcodes(input_yang_obj.endDx2Opcodes, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes_endDx2lOpcodes(input_yang_obj.endDx2lOpcodes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators_srv6Locator(input_yang_obj: yc_srv6Locator_huawei_segripv6__segripv6_srv6Locators_srv6Locator, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators/srv6Locator

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.enable = "true"

    if input_yang_obj.ipv6Prefix._changed():
        translated_yang_obj.prefix.address = input_yang_obj.ipv6Prefix
        
    if input_yang_obj.maskLength._changed():
        translated_yang_obj.prefix.length = input_yang_obj.maskLength
        
    if input_yang_obj.static._changed():
        input_yang_obj.static = input_yang_obj.static
        
    if input_yang_obj.staticLength._changed():
        input_yang_obj.staticLength = input_yang_obj.staticLength
        
    if input_yang_obj.args._changed():
        input_yang_obj.args = input_yang_obj.args
        
    if input_yang_obj.argsLength._changed():
        input_yang_obj.argsLength = input_yang_obj.argsLength
        
    if input_yang_obj.defaultFlag._changed():
        translated_yang_obj.is_default = input_yang_obj.defaultFlag
        
    innerobj = _translate__segripv6_srv6Locators_srv6Locator_srv6Opcodes(input_yang_obj.srv6Opcodes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6Locators(input_yang_obj: yc_srv6Locators_huawei_segripv6__segripv6_srv6Locators, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6Locators

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6Locator.iteritems():
        locator_obj = translated_yang_obj.routing.srv6.locators.locator.add(k)
        innerobj = _translate__segripv6_srv6Locators_srv6Locator(listInst, locator_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndForwTables_srv6EndForwTable(input_yang_obj: yc_srv6EndForwTable_huawei_segripv6__segripv6_srv6EndForwTables_srv6EndForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndForwTables/srv6EndForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.endSidFlavor._changed():
        input_yang_obj.endSidFlavor = input_yang_obj.endSidFlavor
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndForwTables(input_yang_obj: yc_srv6EndForwTables_huawei_segripv6__segripv6_srv6EndForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndForwTables_srv6EndForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndOtpForwTables_srv6EndOtpForwTable(input_yang_obj: yc_srv6EndOtpForwTable_huawei_segripv6__segripv6_srv6EndOtpForwTables_srv6EndOtpForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndOtpForwTables/srv6EndOtpForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndOtpForwTables(input_yang_obj: yc_srv6EndOtpForwTables_huawei_segripv6__segripv6_srv6EndOtpForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndOtpForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndOtpForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndOtpForwTables_srv6EndOtpForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos_endXSidNhpInfo(input_yang_obj: yc_endXSidNhpInfo_huawei_segripv6__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos_endXSidNhpInfo, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndXForwTables/srv6EndXForwTable/endXSidNhpInfos/endXSidNhpInfo

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos(input_yang_obj: yc_endXSidNhpInfos_huawei_segripv6__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndXForwTables/srv6EndXForwTable/endXSidNhpInfos

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.endXSidNhpInfo.iteritems():
        innerobj = _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos_endXSidNhpInfo(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable(input_yang_obj: yc_srv6EndXForwTable_huawei_segripv6__segripv6_srv6EndXForwTables_srv6EndXForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndXForwTables/srv6EndXForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.endXSidFlavor._changed():
        input_yang_obj.endXSidFlavor = input_yang_obj.endXSidFlavor
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    innerobj = _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable_endXSidNhpInfos(input_yang_obj.endXSidNhpInfos, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndXForwTables(input_yang_obj: yc_srv6EndXForwTables_huawei_segripv6__segripv6_srv6EndXForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndXForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndXForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndXForwTables_srv6EndXForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDt4ForwTables_srv6EndDt4ForwTable(input_yang_obj: yc_srv6EndDt4ForwTable_huawei_segripv6__segripv6_srv6EndDt4ForwTables_srv6EndDt4ForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDt4ForwTables/srv6EndDt4ForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vpnName._changed():
        input_yang_obj.vpnName = input_yang_obj.vpnName
        
    if input_yang_obj.vpnID._changed():
        input_yang_obj.vpnID = input_yang_obj.vpnID
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDt4ForwTables(input_yang_obj: yc_srv6EndDt4ForwTables_huawei_segripv6__segripv6_srv6EndDt4ForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDt4ForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndDt4ForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndDt4ForwTables_srv6EndDt4ForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDt6ForwTables_srv6EndDt6ForwTable(input_yang_obj: yc_srv6EndDt6ForwTable_huawei_segripv6__segripv6_srv6EndDt6ForwTables_srv6EndDt6ForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDt6ForwTables/srv6EndDt6ForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.vpnName._changed():
        input_yang_obj.vpnName = input_yang_obj.vpnName
        
    if input_yang_obj.vpnID._changed():
        input_yang_obj.vpnID = input_yang_obj.vpnID
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDt6ForwTables(input_yang_obj: yc_srv6EndDt6ForwTables_huawei_segripv6__segripv6_srv6EndDt6ForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDt6ForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndDt6ForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndDt6ForwTables_srv6EndDt6ForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDx2ForwTables_srv6EndDx2ForwTable(input_yang_obj: yc_srv6EndDx2ForwTable_huawei_segripv6__segripv6_srv6EndDx2ForwTables_srv6EndDx2ForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDx2ForwTables/srv6EndDx2ForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.evplID._changed():
        input_yang_obj.evplID = input_yang_obj.evplID
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDx2ForwTables(input_yang_obj: yc_srv6EndDx2ForwTables_huawei_segripv6__segripv6_srv6EndDx2ForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDx2ForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndDx2ForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndDx2ForwTables_srv6EndDx2ForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDx2lForwTables_srv6EndDx2lForwTable(input_yang_obj: yc_srv6EndDx2lForwTable_huawei_segripv6__segripv6_srv6EndDx2lForwTables_srv6EndDx2lForwTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDx2lForwTables/srv6EndDx2lForwTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.evplID._changed():
        input_yang_obj.evplID = input_yang_obj.evplID
        
    if input_yang_obj.locatorName._changed():
        input_yang_obj.locatorName = input_yang_obj.locatorName
        
    if input_yang_obj.locatorID._changed():
        input_yang_obj.locatorID = input_yang_obj.locatorID
        
    return translated_yang_obj

def _translate__segripv6_srv6EndDx2lForwTables(input_yang_obj: yc_srv6EndDx2lForwTables_huawei_segripv6__segripv6_srv6EndDx2lForwTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6/srv6EndDx2lForwTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.srv6EndDx2lForwTable.iteritems():
        innerobj = _translate__segripv6_srv6EndDx2lForwTables_srv6EndDx2lForwTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__segripv6(input_yang_obj: yc_segripv6_huawei_segripv6__segripv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /segripv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__segripv6_srv6Site(input_yang_obj.srv6Site, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6RemoteEndOtps(input_yang_obj.srv6RemoteEndOtps, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6Locators(input_yang_obj.srv6Locators, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndForwTables(input_yang_obj.srv6EndForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndOtpForwTables(input_yang_obj.srv6EndOtpForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndXForwTables(input_yang_obj.srv6EndXForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndDt4ForwTables(input_yang_obj.srv6EndDt4ForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndDt6ForwTables(input_yang_obj.srv6EndDt6ForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndDx2ForwTables(input_yang_obj.srv6EndDx2ForwTables, translated_yang_obj)
        
    innerobj = _translate__segripv6_srv6EndDx2lForwTables(input_yang_obj.srv6EndDx2lForwTables, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_segripv6(input_yang_obj: huawei_segripv6, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-segripv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("IETF105 huawei segripv6 script!")
    translated_yang_obj = ietf_routing()
    innerobj = _translate__segripv6(input_yang_obj.segripv6, translated_yang_obj)
    xpath = '/a:routing'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
    target_xpath = XPATH(xpath, ns_map)

    return [[translated_yang_obj.routing, target_xpath]]
