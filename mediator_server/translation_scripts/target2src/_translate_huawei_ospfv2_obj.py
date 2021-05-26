from mediator_server.yang_bindings.target_yang_bindings.huawei_network_instance_sm_binding import *


def _translate__ospfv2_check_rt_id(input_yang_obj: yc_check_rt_id_huawei_ospfv2__ospfv2_check_rt_id, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/check-rt-id

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.conflict_flag._changed():
        input_yang_obj.conflict_flag = input_yang_obj.conflict_flag
        
    return translated_yang_obj

def _translate__ospfv2_session_car(input_yang_obj: yc_session_car_huawei_ospfv2__ospfv2_session_car, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/session-car

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.cir_interval._changed():
        input_yang_obj.cir_interval = input_yang_obj.cir_interval
        
    if input_yang_obj.cbs_interval._changed():
        input_yang_obj.cbs_interval = input_yang_obj.cbs_interval
        
    if input_yang_obj.pir_interval._changed():
        input_yang_obj.pir_interval = input_yang_obj.pir_interval
        
    if input_yang_obj.pbs_interval._changed():
        input_yang_obj.pbs_interval = input_yang_obj.pbs_interval
        
    return translated_yang_obj

def _translate__ospfv2_maxage_lsa_protect(input_yang_obj: yc_maxage_lsa_protect_huawei_ospfv2__ospfv2_maxage_lsa_protect, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/maxage-lsa-protect

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_suppress_flap_intf(input_yang_obj: yc_suppress_flap_intf_huawei_ospfv2__ospfv2_suppress_flap_intf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/suppress-flap-intf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_mib_binding(input_yang_obj: yc_mib_binding_huawei_ospfv2__ospfv2_mib_binding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/mib-binding

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.process_id._changed():
        input_yang_obj.process_id = input_yang_obj.process_id
        
    return translated_yang_obj

def _translate__ospfv2_flush_source_trace(input_yang_obj: yc_flush_source_trace_huawei_ospfv2__ospfv2_flush_source_trace, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/flush-source-trace

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.vlink_enable._changed():
        input_yang_obj.vlink_enable = input_yang_obj.vlink_enable
        
    if input_yang_obj.port._changed():
        input_yang_obj.port = input_yang_obj.port
        
    if input_yang_obj.vlink_port._changed():
        input_yang_obj.vlink_port = input_yang_obj.vlink_port
        
    return translated_yang_obj

def _translate__ospfv2(input_yang_obj: yc_ospfv2_huawei_ospfv2__ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2_check_rt_id(input_yang_obj.check_rt_id, translated_yang_obj)
        
    innerobj = _translate__ospfv2_session_car(input_yang_obj.session_car, translated_yang_obj)
        
    innerobj = _translate__ospfv2_maxage_lsa_protect(input_yang_obj.maxage_lsa_protect, translated_yang_obj)
        
    innerobj = _translate__ospfv2_suppress_flap_intf(input_yang_obj.suppress_flap_intf, translated_yang_obj)
        
    innerobj = _translate__ospfv2_mib_binding(input_yang_obj.mib_binding, translated_yang_obj)
        
    innerobj = _translate__ospfv2_flush_source_trace(input_yang_obj.flush_source_trace, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ospfv2(input_yang_obj: huawei_ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2(input_yang_obj.ospfv2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ospfv2_check_rt_id(input_yang_obj: yc_check_rt_id_huawei_ospfv2__ospfv2_check_rt_id, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/check-rt-id

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.conflict_flag._changed():
        input_yang_obj.conflict_flag = input_yang_obj.conflict_flag
        
    return translated_yang_obj

def _translate__ospfv2_session_car(input_yang_obj: yc_session_car_huawei_ospfv2__ospfv2_session_car, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/session-car

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.cir_interval._changed():
        input_yang_obj.cir_interval = input_yang_obj.cir_interval
        
    if input_yang_obj.cbs_interval._changed():
        input_yang_obj.cbs_interval = input_yang_obj.cbs_interval
        
    if input_yang_obj.pir_interval._changed():
        input_yang_obj.pir_interval = input_yang_obj.pir_interval
        
    if input_yang_obj.pbs_interval._changed():
        input_yang_obj.pbs_interval = input_yang_obj.pbs_interval
        
    return translated_yang_obj

def _translate__ospfv2_maxage_lsa_protect(input_yang_obj: yc_maxage_lsa_protect_huawei_ospfv2__ospfv2_maxage_lsa_protect, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/maxage-lsa-protect

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_suppress_flap_intf(input_yang_obj: yc_suppress_flap_intf_huawei_ospfv2__ospfv2_suppress_flap_intf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/suppress-flap-intf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_mib_binding(input_yang_obj: yc_mib_binding_huawei_ospfv2__ospfv2_mib_binding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/mib-binding

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.process_id._changed():
        input_yang_obj.process_id = input_yang_obj.process_id
        
    return translated_yang_obj

def _translate__ospfv2_flush_source_trace(input_yang_obj: yc_flush_source_trace_huawei_ospfv2__ospfv2_flush_source_trace, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/flush-source-trace

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.vlink_enable._changed():
        input_yang_obj.vlink_enable = input_yang_obj.vlink_enable
        
    if input_yang_obj.port._changed():
        input_yang_obj.port = input_yang_obj.port
        
    if input_yang_obj.vlink_port._changed():
        input_yang_obj.vlink_port = input_yang_obj.vlink_port
        
    return translated_yang_obj

def _translate__ospfv2(input_yang_obj: yc_ospfv2_huawei_ospfv2__ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2_check_rt_id(input_yang_obj.check_rt_id, translated_yang_obj)
        
    innerobj = _translate__ospfv2_session_car(input_yang_obj.session_car, translated_yang_obj)
        
    innerobj = _translate__ospfv2_maxage_lsa_protect(input_yang_obj.maxage_lsa_protect, translated_yang_obj)
        
    innerobj = _translate__ospfv2_suppress_flap_intf(input_yang_obj.suppress_flap_intf, translated_yang_obj)
        
    innerobj = _translate__ospfv2_mib_binding(input_yang_obj.mib_binding, translated_yang_obj)
        
    innerobj = _translate__ospfv2_flush_source_trace(input_yang_obj.flush_source_trace, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ospfv2(input_yang_obj: huawei_ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2(input_yang_obj.ospfv2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ospfv2_check_rt_id(input_yang_obj: yc_check_rt_id_huawei_ospfv2__ospfv2_check_rt_id, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/check-rt-id

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.conflict_flag._changed():
        input_yang_obj.conflict_flag = input_yang_obj.conflict_flag
        
    return translated_yang_obj

def _translate__ospfv2_session_car(input_yang_obj: yc_session_car_huawei_ospfv2__ospfv2_session_car, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/session-car

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.cir_interval._changed():
        input_yang_obj.cir_interval = input_yang_obj.cir_interval
        
    if input_yang_obj.cbs_interval._changed():
        input_yang_obj.cbs_interval = input_yang_obj.cbs_interval
        
    if input_yang_obj.pir_interval._changed():
        input_yang_obj.pir_interval = input_yang_obj.pir_interval
        
    if input_yang_obj.pbs_interval._changed():
        input_yang_obj.pbs_interval = input_yang_obj.pbs_interval
        
    return translated_yang_obj

def _translate__ospfv2_maxage_lsa_protect(input_yang_obj: yc_maxage_lsa_protect_huawei_ospfv2__ospfv2_maxage_lsa_protect, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/maxage-lsa-protect

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_suppress_flap_intf(input_yang_obj: yc_suppress_flap_intf_huawei_ospfv2__ospfv2_suppress_flap_intf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/suppress-flap-intf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_mib_binding(input_yang_obj: yc_mib_binding_huawei_ospfv2__ospfv2_mib_binding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/mib-binding

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.process_id._changed():
        input_yang_obj.process_id = input_yang_obj.process_id
        
    return translated_yang_obj

def _translate__ospfv2_flush_source_trace(input_yang_obj: yc_flush_source_trace_huawei_ospfv2__ospfv2_flush_source_trace, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/flush-source-trace

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.vlink_enable._changed():
        input_yang_obj.vlink_enable = input_yang_obj.vlink_enable
        
    if input_yang_obj.port._changed():
        input_yang_obj.port = input_yang_obj.port
        
    if input_yang_obj.vlink_port._changed():
        input_yang_obj.vlink_port = input_yang_obj.vlink_port
        
    return translated_yang_obj

def _translate__ospfv2(input_yang_obj: yc_ospfv2_huawei_ospfv2__ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2_check_rt_id(input_yang_obj.check_rt_id, translated_yang_obj)
        
    innerobj = _translate__ospfv2_session_car(input_yang_obj.session_car, translated_yang_obj)
        
    innerobj = _translate__ospfv2_maxage_lsa_protect(input_yang_obj.maxage_lsa_protect, translated_yang_obj)
        
    innerobj = _translate__ospfv2_suppress_flap_intf(input_yang_obj.suppress_flap_intf, translated_yang_obj)
        
    innerobj = _translate__ospfv2_mib_binding(input_yang_obj.mib_binding, translated_yang_obj)
        
    innerobj = _translate__ospfv2_flush_source_trace(input_yang_obj.flush_source_trace, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ospfv2(input_yang_obj: huawei_ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2(input_yang_obj.ospfv2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ospfv2_check_rt_id(input_yang_obj: yc_check_rt_id_huawei_ospfv2__ospfv2_check_rt_id, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/check-rt-id

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.conflict_flag._changed():
        input_yang_obj.conflict_flag = input_yang_obj.conflict_flag
        
    return translated_yang_obj

def _translate__ospfv2_session_car(input_yang_obj: yc_session_car_huawei_ospfv2__ospfv2_session_car, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/session-car

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.cir_interval._changed():
        input_yang_obj.cir_interval = input_yang_obj.cir_interval
        
    if input_yang_obj.cbs_interval._changed():
        input_yang_obj.cbs_interval = input_yang_obj.cbs_interval
        
    if input_yang_obj.pir_interval._changed():
        input_yang_obj.pir_interval = input_yang_obj.pir_interval
        
    if input_yang_obj.pbs_interval._changed():
        input_yang_obj.pbs_interval = input_yang_obj.pbs_interval
        
    return translated_yang_obj

def _translate__ospfv2_maxage_lsa_protect(input_yang_obj: yc_maxage_lsa_protect_huawei_ospfv2__ospfv2_maxage_lsa_protect, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/maxage-lsa-protect

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_suppress_flap_intf(input_yang_obj: yc_suppress_flap_intf_huawei_ospfv2__ospfv2_suppress_flap_intf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/suppress-flap-intf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.disable._changed():
        input_yang_obj.disable = input_yang_obj.disable
        
    return translated_yang_obj

def _translate__ospfv2_mib_binding(input_yang_obj: yc_mib_binding_huawei_ospfv2__ospfv2_mib_binding, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/mib-binding

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.process_id._changed():
        input_yang_obj.process_id = input_yang_obj.process_id
        
    return translated_yang_obj

def _translate__ospfv2_flush_source_trace(input_yang_obj: yc_flush_source_trace_huawei_ospfv2__ospfv2_flush_source_trace, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2/flush-source-trace

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.vlink_enable._changed():
        input_yang_obj.vlink_enable = input_yang_obj.vlink_enable
        
    if input_yang_obj.port._changed():
        input_yang_obj.port = input_yang_obj.port
        
    if input_yang_obj.vlink_port._changed():
        input_yang_obj.vlink_port = input_yang_obj.vlink_port
        
    return translated_yang_obj

def _translate__ospfv2(input_yang_obj: yc_ospfv2_huawei_ospfv2__ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2_check_rt_id(input_yang_obj.check_rt_id, translated_yang_obj)
        
    innerobj = _translate__ospfv2_session_car(input_yang_obj.session_car, translated_yang_obj)
        
    innerobj = _translate__ospfv2_maxage_lsa_protect(input_yang_obj.maxage_lsa_protect, translated_yang_obj)
        
    innerobj = _translate__ospfv2_suppress_flap_intf(input_yang_obj.suppress_flap_intf, translated_yang_obj)
        
    innerobj = _translate__ospfv2_mib_binding(input_yang_obj.mib_binding, translated_yang_obj)
        
    innerobj = _translate__ospfv2_flush_source_trace(input_yang_obj.flush_source_trace, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_ospfv2(input_yang_obj: huawei_ospfv2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-ospfv2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__ospfv2(input_yang_obj.ospfv2, translated_yang_obj)
        
    return translated_yang_obj
