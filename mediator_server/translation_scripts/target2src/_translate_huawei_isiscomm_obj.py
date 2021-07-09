from mediator_server.mediator_framework.adaptor import XPATH
from mediator_server.yang_bindings.src_yang_bindings.ietf_105_binding import ietf_routing
from mediator_server.yang_bindings.target_yang_bindings.huawei_isiscomm_binding import *


def _translate__isiscomm_isSites_isSite_isLspAgeRefresh(input_yang_obj: yc_isLspAgeRefresh_huawei_isiscomm__isiscomm_isSites_isSite_isLspAgeRefresh, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLspAgeRefresh

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.isLspAgeRefreshEnable._changed():
        input_yang_obj.isLspAgeRefreshEnable = input_yang_obj.isLspAgeRefreshEnable
        
    if input_yang_obj.lspAgeRefreshMaxAge._changed():
        input_yang_obj.lspAgeRefreshMaxAge = input_yang_obj.lspAgeRefreshMaxAge
        
    if input_yang_obj.lspAgeRefreshValue._changed():
        input_yang_obj.lspAgeRefreshValue = input_yang_obj.lspAgeRefreshValue
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isBgpLs(input_yang_obj: yc_isBgpLs_huawei_isiscomm__isiscomm_isSites_isSite_isBgpLs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isBgpLs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.l1BgpLsEnable._changed():
        input_yang_obj.l1BgpLsEnable = input_yang_obj.l1BgpLsEnable
        
    if input_yang_obj.l2BgpLsEnable._changed():
        input_yang_obj.l2BgpLsEnable = input_yang_obj.l2BgpLsEnable
        
    if input_yang_obj.identifier._changed():
        input_yang_obj.identifier = input_yang_obj.identifier
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLspGenIntelliTimer(input_yang_obj: yc_isLspGenIntelliTimer_huawei_isiscomm__isiscomm_isSites_isSite_isLspGenIntelliTimer, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLspGenIntelliTimer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.level1LspGenMaxInterval._changed():
        input_yang_obj.level1LspGenMaxInterval = input_yang_obj.level1LspGenMaxInterval
        
    if input_yang_obj.level2LspGenMaxInterval._changed():
        input_yang_obj.level2LspGenMaxInterval = input_yang_obj.level2LspGenMaxInterval
        
    if input_yang_obj.level1LspGenInitInterval._changed():
        input_yang_obj.level1LspGenInitInterval = input_yang_obj.level1LspGenInitInterval
        
    if input_yang_obj.level2LspGenInitInterval._changed():
        input_yang_obj.level2LspGenInitInterval = input_yang_obj.level2LspGenInitInterval
        
    if input_yang_obj.level1LspGenIncrInterval._changed():
        input_yang_obj.level1LspGenIncrInterval = input_yang_obj.level1LspGenIncrInterval
        
    if input_yang_obj.level2LspGenIncrInterval._changed():
        input_yang_obj.level2LspGenIncrInterval = input_yang_obj.level2LspGenIncrInterval
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isFlashFlood(input_yang_obj: yc_isFlashFlood_huawei_isiscomm__isiscomm_isSites_isSite_isFlashFlood, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isFlashFlood

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.level1FlashFloodEnable._changed():
        input_yang_obj.level1FlashFloodEnable = input_yang_obj.level1FlashFloodEnable
        
    if input_yang_obj.level2FlashFloodEnable._changed():
        input_yang_obj.level2FlashFloodEnable = input_yang_obj.level2FlashFloodEnable
        
    if input_yang_obj.level1FlashFloodLspNum._changed():
        input_yang_obj.level1FlashFloodLspNum = input_yang_obj.level1FlashFloodLspNum
        
    if input_yang_obj.level2FlashFloodLspNum._changed():
        input_yang_obj.level2FlashFloodLspNum = input_yang_obj.level2FlashFloodLspNum
        
    if input_yang_obj.level1FlashFloodMaxTime._changed():
        input_yang_obj.level1FlashFloodMaxTime = input_yang_obj.level1FlashFloodMaxTime
        
    if input_yang_obj.level2FlashFloodMaxTime._changed():
        input_yang_obj.level2FlashFloodMaxTime = input_yang_obj.level2FlashFloodMaxTime
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isOverloadSet(input_yang_obj: yc_isOverloadSet_huawei_isiscomm__isiscomm_isSites_isSite_isOverloadSet, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isOverloadSet

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.stdOverloadType._changed():
        input_yang_obj.stdOverloadType = input_yang_obj.stdOverloadType
        
    if input_yang_obj.stdOverloadWaitType._changed():
        input_yang_obj.stdOverloadWaitType = input_yang_obj.stdOverloadWaitType
        
    if input_yang_obj.stdOverloadNbrSysId._changed():
        input_yang_obj.stdOverloadNbrSysId = input_yang_obj.stdOverloadNbrSysId
        
    if input_yang_obj.stdOverloadTimeout1._changed():
        input_yang_obj.stdOverloadTimeout1 = input_yang_obj.stdOverloadTimeout1
        
    if input_yang_obj.stdOverloadTimeout2._changed():
        input_yang_obj.stdOverloadTimeout2 = input_yang_obj.stdOverloadTimeout2
        
    if input_yang_obj.stdOverloadInterlevel._changed():
        input_yang_obj.stdOverloadInterlevel = input_yang_obj.stdOverloadInterlevel
        
    if input_yang_obj.stdOverloadExternal._changed():
        input_yang_obj.stdOverloadExternal = input_yang_obj.stdOverloadExternal
        
    if input_yang_obj.stdOverloadSendSaBit._changed():
        input_yang_obj.stdOverloadSendSaBit = input_yang_obj.stdOverloadSendSaBit
        
    if input_yang_obj.stdOverloadSaBitTime._changed():
        input_yang_obj.stdOverloadSaBitTime = input_yang_obj.stdOverloadSaBitTime
        
    if input_yang_obj.stdOverloadRtDelayTime._changed():
        input_yang_obj.stdOverloadRtDelayTime = input_yang_obj.stdOverloadRtDelayTime
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLdpSyncdSet(input_yang_obj: yc_isLdpSyncdSet_huawei_isiscomm__isiscomm_isSites_isSite_isLdpSyncdSet, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLdpSyncdSet

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ldpSyncEnable._changed():
        input_yang_obj.ldpSyncEnable = input_yang_obj.ldpSyncEnable
        
    if input_yang_obj.ldpSyncBind._changed():
        input_yang_obj.ldpSyncBind = input_yang_obj.ldpSyncBind
        
    if input_yang_obj.ldpSyncTimerEnable._changed():
        input_yang_obj.ldpSyncTimerEnable = input_yang_obj.ldpSyncTimerEnable
        
    if input_yang_obj.ldpSyncTimer._changed():
        input_yang_obj.ldpSyncTimer = input_yang_obj.ldpSyncTimer
        
    if input_yang_obj.ldpSyncHDTimerEnable._changed():
        input_yang_obj.ldpSyncHDTimerEnable = input_yang_obj.ldpSyncHDTimerEnable
        
    if input_yang_obj.ldpSyncHDTimer._changed():
        input_yang_obj.ldpSyncHDTimer = input_yang_obj.ldpSyncHDTimer
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isExternAbility(input_yang_obj: yc_isExternAbility_huawei_isiscomm__isiscomm_isSites_isSite_isExternAbility, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isExternAbility

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.adjStrictCheck._changed():
        input_yang_obj.adjStrictCheck = input_yang_obj.adjStrictCheck
        
    if input_yang_obj.ecmpPrefer._changed():
        input_yang_obj.ecmpPrefer = input_yang_obj.ecmpPrefer
        
    if input_yang_obj.optChecksum._changed():
        input_yang_obj.optChecksum = input_yang_obj.optChecksum
        
    if input_yang_obj.attAdvControl._changed():
        input_yang_obj.attAdvControl = input_yang_obj.attAdvControl
        
    if input_yang_obj.attAvoidLearn._changed():
        input_yang_obj.attAvoidLearn = input_yang_obj.attAvoidLearn
        
    if input_yang_obj.vClusterEnable._changed():
        input_yang_obj.vClusterEnable = input_yang_obj.vClusterEnable
        
    if input_yang_obj.vAccessEnable._changed():
        input_yang_obj.vAccessEnable = input_yang_obj.vAccessEnable
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isAvoidMicroLoopSet(input_yang_obj: yc_isAvoidMicroLoopSet_huawei_isiscomm__isiscomm_isSites_isSite_isAvoidMicroLoopSet, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isAvoidMicroLoopSet

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.frrAvoidLoopDisable._changed():
        input_yang_obj.frrAvoidLoopDisable = input_yang_obj.frrAvoidLoopDisable
        
    if input_yang_obj.ribUpdateDelayValue._changed():
        input_yang_obj.ribUpdateDelayValue = input_yang_obj.ribUpdateDelayValue
        
    if input_yang_obj.srAvoidLoopEnable._changed():
        input_yang_obj.srAvoidLoopEnable = input_yang_obj.srAvoidLoopEnable
        
    if input_yang_obj.srDelayAvoidLoopVal._changed():
        input_yang_obj.srDelayAvoidLoopVal = input_yang_obj.srDelayAvoidLoopVal
        
    if input_yang_obj.teTnlUloopEnable._changed():
        input_yang_obj.teTnlUloopEnable = input_yang_obj.teTnlUloopEnable
        
    if input_yang_obj.teTnlUloopDelay._changed():
        input_yang_obj.teTnlUloopDelay = input_yang_obj.teTnlUloopDelay
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLocalMtSets_isLocalMtSet(input_yang_obj: yc_isLocalMtSet_huawei_isiscomm__isiscomm_isSites_isSite_isLocalMtSets_isLocalMtSet, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLocalMtSets/isLocalMtSet

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.localMtEnable._changed():
        input_yang_obj.localMtEnable = input_yang_obj.localMtEnable
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.aclNumOrName._changed():
        input_yang_obj.aclNumOrName = input_yang_obj.aclNumOrName
        
    if input_yang_obj.ipPrefix._changed():
        input_yang_obj.ipPrefix = input_yang_obj.ipPrefix
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLocalMtSets(input_yang_obj: yc_isLocalMtSets_huawei_isiscomm__isiscomm_isSites_isSite_isLocalMtSets, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLocalMtSets

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isLocalMtSets_isLocalMtSet(input_yang_obj.isLocalMtSet, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isAreaIds_isAreaId(input_yang_obj: yc_isAreaId_huawei_isiscomm__isiscomm_isSites_isSite_isAreaIds_isAreaId, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isAreaIds/isAreaId

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isAreaIds(input_yang_obj: yc_isAreaIds_huawei_isiscomm__isiscomm_isSites_isSite_isAreaIds, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isAreaIds

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isAreaId.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isAreaIds_isAreaId(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isNetEntitys_isNetEntity(input_yang_obj: yc_isNetEntity_huawei_isiscomm__isiscomm_isSites_isSite_isNetEntitys_isNetEntity, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isNetEntitys/isNetEntity

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isNetEntitys(input_yang_obj: yc_isNetEntitys_huawei_isiscomm__isiscomm_isSites_isSite_isNetEntitys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isNetEntitys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isNetEntity.iteritems():
        translated_yang_obj.isis.system_id = k[2:6] + '.' + k[6:10] + '.' + k[10:14]
        translated_yang_obj.isis.area_address = k[0:2]
        innerobj = _translate__isiscomm_isSites_isSite_isNetEntitys_isNetEntity(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLspAuthtications_isLspAuthtication(input_yang_obj: yc_isLspAuthtication_huawei_isiscomm__isiscomm_isSites_isSite_isLspAuthtications_isLspAuthtication, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLspAuthtications/isLspAuthtication

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.passwordType._changed():
        input_yang_obj.passwordType = input_yang_obj.passwordType
        
    if input_yang_obj.simplePassword._changed():
        input_yang_obj.simplePassword = input_yang_obj.simplePassword
        
    if input_yang_obj.md5Password._changed():
        input_yang_obj.md5Password = input_yang_obj.md5Password
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.serviceType._changed():
        input_yang_obj.serviceType = input_yang_obj.serviceType
        
    if input_yang_obj.authenUsage._changed():
        input_yang_obj.authenUsage = input_yang_obj.authenUsage
        
    if input_yang_obj.keyId._changed():
        input_yang_obj.keyId = input_yang_obj.keyId
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLspAuthtications(input_yang_obj: yc_isLspAuthtications_huawei_isiscomm__isiscomm_isSites_isSite_isLspAuthtications, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLspAuthtications

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isLspAuthtication.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isLspAuthtications_isLspAuthtication(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isNameTables_isNameTable(input_yang_obj: yc_isNameTable_huawei_isiscomm__isiscomm_isSites_isSite_isNameTables_isNameTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isNameTables/isNameTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.hostName._changed():
        input_yang_obj.hostName = input_yang_obj.hostName
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isNameTables(input_yang_obj: yc_isNameTables_huawei_isiscomm__isiscomm_isSites_isSite_isNameTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isNameTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isNameTable.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isNameTables_isNameTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isVirtualSystems_isVirtualSystem(input_yang_obj: yc_isVirtualSystem_huawei_isiscomm__isiscomm_isSites_isSite_isVirtualSystems_isVirtualSystem, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isVirtualSystems/isVirtualSystem

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isVirtualSystems(input_yang_obj: yc_isVirtualSystems_huawei_isiscomm__isiscomm_isSites_isSite_isVirtualSystems, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isVirtualSystems

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isVirtualSystem.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isVirtualSystems_isVirtualSystem(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSrgbs_isSrgb(input_yang_obj: yc_isSrgb_huawei_isiscomm__isiscomm_isSites_isSite_isSrgbs_isSrgb, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSrgbs/isSrgb

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isSrgbs(input_yang_obj: yc_isSrgbs_huawei_isiscomm__isiscomm_isSites_isSite_isSrgbs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSrgbs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isSrgb.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSrgbs_isSrgb(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications_isHelloAuthtication(input_yang_obj: yc_isHelloAuthtication_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications_isHelloAuthtication, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits/isCircuit/isHelloAuthtications/isHelloAuthtication

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.passwordType._changed():
        input_yang_obj.passwordType = input_yang_obj.passwordType
        
    if input_yang_obj.simplePassword._changed():
        input_yang_obj.simplePassword = input_yang_obj.simplePassword
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.md5Password._changed():
        input_yang_obj.md5Password = input_yang_obj.md5Password
        
    if input_yang_obj.serviceType._changed():
        input_yang_obj.serviceType = input_yang_obj.serviceType
        
    if input_yang_obj.sendOnly._changed():
        input_yang_obj.sendOnly = input_yang_obj.sendOnly
        
    if input_yang_obj.keyId._changed():
        input_yang_obj.keyId = input_yang_obj.keyId
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications(input_yang_obj: yc_isHelloAuthtications_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits/isCircuit/isHelloAuthtications

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isHelloAuthtication.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications_isHelloAuthtication(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs_isSrlg(input_yang_obj: yc_isSrlg_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs_isSrlg, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits/isCircuit/isSrlgs/isSrlg

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs(input_yang_obj: yc_isSrlgs_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits/isCircuit/isSrlgs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isSrlg.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs_isSrlg(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isCircuits_isCircuit(input_yang_obj: yc_isCircuit_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits_isCircuit, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits/isCircuit

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv4Enable._changed():
        input_yang_obj.ipv4Enable = input_yang_obj.ipv4Enable
        
    if input_yang_obj.ipv6Enable._changed():
        input_yang_obj.ipv6Enable = input_yang_obj.ipv6Enable
        
    if input_yang_obj.circuitLevelType._changed():
        input_yang_obj.circuitLevelType = input_yang_obj.circuitLevelType
        
    if input_yang_obj.typeP2pEnable._changed():
        input_yang_obj.typeP2pEnable = input_yang_obj.typeP2pEnable
        
    if input_yang_obj.snpaCheck._changed():
        input_yang_obj.snpaCheck = input_yang_obj.snpaCheck
        
    if input_yang_obj.silentEnable._changed():
        input_yang_obj.silentEnable = input_yang_obj.silentEnable
        
    if input_yang_obj.silentCost._changed():
        input_yang_obj.silentCost = input_yang_obj.silentCost
        
    if input_yang_obj.level1CsnpInterval._changed():
        input_yang_obj.level1CsnpInterval = input_yang_obj.level1CsnpInterval
        
    if input_yang_obj.level2CsnpInterval._changed():
        input_yang_obj.level2CsnpInterval = input_yang_obj.level2CsnpInterval
        
    if input_yang_obj.throttleTimer._changed():
        input_yang_obj.throttleTimer = input_yang_obj.throttleTimer
        
    if input_yang_obj.throttleCount._changed():
        input_yang_obj.throttleCount = input_yang_obj.throttleCount
        
    if input_yang_obj.level1HelloTimer._changed():
        input_yang_obj.level1HelloTimer = input_yang_obj.level1HelloTimer
        
    if input_yang_obj.level2HelloTimer._changed():
        input_yang_obj.level2HelloTimer = input_yang_obj.level2HelloTimer
        
    if input_yang_obj.level1HoldMultiplier._changed():
        input_yang_obj.level1HoldMultiplier = input_yang_obj.level1HoldMultiplier
        
    if input_yang_obj.level2HoldMultiplier._changed():
        input_yang_obj.level2HoldMultiplier = input_yang_obj.level2HoldMultiplier
        
    if input_yang_obj.disName._changed():
        input_yang_obj.disName = input_yang_obj.disName
        
    if input_yang_obj.level1DisPriority._changed():
        input_yang_obj.level1DisPriority = input_yang_obj.level1DisPriority
        
    if input_yang_obj.level2DisPriority._changed():
        input_yang_obj.level2DisPriority = input_yang_obj.level2DisPriority
        
    if input_yang_obj.p2pPeerIPIgnore._changed():
        input_yang_obj.p2pPeerIPIgnore = input_yang_obj.p2pPeerIPIgnore
        
    if input_yang_obj.p2pNegotiationMode._changed():
        input_yang_obj.p2pNegotiationMode = input_yang_obj.p2pNegotiationMode
        
    if input_yang_obj.p2pHelloTimer._changed():
        input_yang_obj.p2pHelloTimer = input_yang_obj.p2pHelloTimer
        
    if input_yang_obj.p2pHoldMulti._changed():
        input_yang_obj.p2pHoldMulti = input_yang_obj.p2pHoldMulti
        
    if input_yang_obj.lspRetransmitInterval._changed():
        input_yang_obj.lspRetransmitInterval = input_yang_obj.lspRetransmitInterval
        
    if input_yang_obj.pPPOsicpCheckEnable._changed():
        input_yang_obj.pPPOsicpCheckEnable = input_yang_obj.pPPOsicpCheckEnable
        
    if input_yang_obj.ldpAutoBlock._changed():
        input_yang_obj.ldpAutoBlock = input_yang_obj.ldpAutoBlock
        
    if input_yang_obj.helloMode._changed():
        input_yang_obj.helloMode = input_yang_obj.helloMode
        
    if input_yang_obj.level1Cost._changed():
        input_yang_obj.level1Cost = input_yang_obj.level1Cost
        
    if input_yang_obj.level2Cost._changed():
        input_yang_obj.level2Cost = input_yang_obj.level2Cost
        
    if input_yang_obj.ldpSyncState._changed():
        input_yang_obj.ldpSyncState = input_yang_obj.ldpSyncState
        
    if input_yang_obj.ldpSyncTimerEnable._changed():
        input_yang_obj.ldpSyncTimerEnable = input_yang_obj.ldpSyncTimerEnable
        
    if input_yang_obj.ldpSyncTimer._changed():
        input_yang_obj.ldpSyncTimer = input_yang_obj.ldpSyncTimer
        
    if input_yang_obj.ldpSyncHDTimerEnable._changed():
        input_yang_obj.ldpSyncHDTimerEnable = input_yang_obj.ldpSyncHDTimerEnable
        
    if input_yang_obj.ldpSyncHDTimer._changed():
        input_yang_obj.ldpSyncHDTimer = input_yang_obj.ldpSyncHDTimer
        
    if input_yang_obj.ldpSynInfinite._changed():
        input_yang_obj.ldpSynInfinite = input_yang_obj.ldpSynInfinite
        
    if input_yang_obj.level1FrrBlock._changed():
        input_yang_obj.level1FrrBlock = input_yang_obj.level1FrrBlock
        
    if input_yang_obj.level2FrrBlock._changed():
        input_yang_obj.level2FrrBlock = input_yang_obj.level2FrrBlock
        
    if input_yang_obj.level1RemoteLFA._changed():
        input_yang_obj.level1RemoteLFA = input_yang_obj.level1RemoteLFA
        
    if input_yang_obj.level2RemoteLFA._changed():
        input_yang_obj.level2RemoteLFA = input_yang_obj.level2RemoteLFA
        
    if input_yang_obj.l1TilfaDisable._changed():
        input_yang_obj.l1TilfaDisable = input_yang_obj.l1TilfaDisable
        
    if input_yang_obj.l2TilfaDisable._changed():
        input_yang_obj.l2TilfaDisable = input_yang_obj.l2TilfaDisable
        
    if input_yang_obj.peerFlapSuppressEnable._changed():
        input_yang_obj.peerFlapSuppressEnable = input_yang_obj.peerFlapSuppressEnable
        
    if input_yang_obj.peerFlapSuppressDetectInterval._changed():
        input_yang_obj.peerFlapSuppressDetectInterval = input_yang_obj.peerFlapSuppressDetectInterval
        
    if input_yang_obj.peerFlapSuppressThreshold._changed():
        input_yang_obj.peerFlapSuppressThreshold = input_yang_obj.peerFlapSuppressThreshold
        
    if input_yang_obj.peerFlapSuppressResumeInterval._changed():
        input_yang_obj.peerFlapSuppressResumeInterval = input_yang_obj.peerFlapSuppressResumeInterval
        
    if input_yang_obj.peerFlapSuppressHoldDown._changed():
        input_yang_obj.peerFlapSuppressHoldDown = input_yang_obj.peerFlapSuppressHoldDown
        
    if input_yang_obj.peerFlapSuppressDownInterval._changed():
        input_yang_obj.peerFlapSuppressDownInterval = input_yang_obj.peerFlapSuppressDownInterval
        
    if input_yang_obj.peerFlapSuppressHoldMaxCost._changed():
        input_yang_obj.peerFlapSuppressHoldMaxCost = input_yang_obj.peerFlapSuppressHoldMaxCost
        
    if input_yang_obj.peerFlapSuppressStatus._changed():
        input_yang_obj.peerFlapSuppressStatus = input_yang_obj.peerFlapSuppressStatus
        
    if input_yang_obj.peerFlapCount._changed():
        input_yang_obj.peerFlapCount = input_yang_obj.peerFlapCount
        
    if input_yang_obj.peerFlapThreshold._changed():
        input_yang_obj.peerFlapThreshold = input_yang_obj.peerFlapThreshold
        
    if input_yang_obj.peerFlapSuppressTimer._changed():
        input_yang_obj.peerFlapSuppressTimer = input_yang_obj.peerFlapSuppressTimer
        
    if input_yang_obj.peerFlapSuppressRemainTimer._changed():
        input_yang_obj.peerFlapSuppressRemainTimer = input_yang_obj.peerFlapSuppressRemainTimer
        
    if input_yang_obj.meshGroupState._changed():
        input_yang_obj.meshGroupState = input_yang_obj.meshGroupState
        
    if input_yang_obj.meshGroupNumber._changed():
        input_yang_obj.meshGroupNumber = input_yang_obj.meshGroupNumber
        
    if input_yang_obj.incrCost._changed():
        input_yang_obj.incrCost = input_yang_obj.incrCost
        
    if input_yang_obj.incrCostIpv6._changed():
        input_yang_obj.incrCostIpv6 = input_yang_obj.incrCostIpv6
        
    if input_yang_obj.circuitId._changed():
        input_yang_obj.circuitId = input_yang_obj.circuitId
        
    if input_yang_obj.circuitMTU._changed():
        input_yang_obj.circuitMTU = input_yang_obj.circuitMTU
        
    if input_yang_obj.circuitL1IsDis._changed():
        input_yang_obj.circuitL1IsDis = input_yang_obj.circuitL1IsDis
        
    if input_yang_obj.circuitL2IsDis._changed():
        input_yang_obj.circuitL2IsDis = input_yang_obj.circuitL2IsDis
        
    if input_yang_obj.v4Status._changed():
        input_yang_obj.v4Status = input_yang_obj.v4Status
        
    if input_yang_obj.mtuState._changed():
        input_yang_obj.mtuState = input_yang_obj.mtuState
        
    if input_yang_obj.linkState._changed():
        input_yang_obj.linkState = input_yang_obj.linkState
        
    if input_yang_obj.ipState._changed():
        input_yang_obj.ipState = input_yang_obj.ipState
        
    if input_yang_obj.v6Status._changed():
        input_yang_obj.v6Status = input_yang_obj.v6Status
        
    if input_yang_obj.mtuV6State._changed():
        input_yang_obj.mtuV6State = input_yang_obj.mtuV6State
        
    if input_yang_obj.linkV6State._changed():
        input_yang_obj.linkV6State = input_yang_obj.linkV6State
        
    if input_yang_obj.ipV6State._changed():
        input_yang_obj.ipV6State = input_yang_obj.ipV6State
        
    if input_yang_obj.vcState._changed():
        input_yang_obj.vcState = input_yang_obj.vcState
        
    if input_yang_obj.level1Conser._changed():
        input_yang_obj.level1Conser = input_yang_obj.level1Conser
        
    if input_yang_obj.level2Conser._changed():
        input_yang_obj.level2Conser = input_yang_obj.level2Conser
        
    if input_yang_obj.p2pConser._changed():
        input_yang_obj.p2pConser = input_yang_obj.p2pConser
        
    if input_yang_obj.purgeSourceTraceBlock._changed():
        input_yang_obj.purgeSourceTraceBlock = input_yang_obj.purgeSourceTraceBlock
        
    innerobj = _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isHelloAuthtications(input_yang_obj.isHelloAuthtications, translated_yang_obj)
        
    if input_yang_obj.peerHoldMaxCostTimer._changed():
        input_yang_obj.peerHoldMaxCostTimer = input_yang_obj.peerHoldMaxCostTimer
        
    innerobj = _translate__isiscomm_isSites_isSite_isCircuits_isCircuit_isSrlgs(input_yang_obj.isSrlgs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isCircuits(input_yang_obj: yc_isCircuits_huawei_isiscomm__isiscomm_isSites_isSite_isCircuits, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isCircuits

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isCircuit.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isCircuits_isCircuit(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights_isNextHopWeight(input_yang_obj: yc_isNextHopWeight_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights_isNextHopWeight, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isNextHopWeights/isNextHopWeight

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.weight._changed():
        input_yang_obj.weight = input_yang_obj.weight
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights(input_yang_obj: yc_isNextHopWeights_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isNextHopWeights

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isNextHopWeight.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights_isNextHopWeight(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes_isSummaryRoute(input_yang_obj: yc_isSummaryRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes_isSummaryRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isSummaryRoutes/isSummaryRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.levelType._changed():
        input_yang_obj.levelType = input_yang_obj.levelType
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.genNull0Route._changed():
        input_yang_obj.genNull0Route = input_yang_obj.genNull0Route
        
    if input_yang_obj.avoidFeadBack._changed():
        input_yang_obj.avoidFeadBack = input_yang_obj.avoidFeadBack
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes(input_yang_obj: yc_isSummaryRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isSummaryRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isSummaryRoute.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes_isSummaryRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes_isDefaultRoute(input_yang_obj: yc_isDefaultRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes_isDefaultRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDefaultRoutes/isDefaultRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.defaultMode._changed():
        input_yang_obj.defaultMode = input_yang_obj.defaultMode
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.levelType._changed():
        input_yang_obj.levelType = input_yang_obj.levelType
        
    if input_yang_obj.avoidLearning._changed():
        input_yang_obj.avoidLearning = input_yang_obj.avoidLearning
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes(input_yang_obj: yc_isDefaultRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDefaultRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes_isDefaultRoute(input_yang_obj.isDefaultRoute, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes_isImportRoute(input_yang_obj: yc_isImportRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes_isImportRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isImportRoutes/isImportRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.costType._changed():
        input_yang_obj.costType = input_yang_obj.costType
        
    if input_yang_obj.cost._changed():
        input_yang_obj.cost = input_yang_obj.cost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    if input_yang_obj.levelType._changed():
        input_yang_obj.levelType = input_yang_obj.levelType
        
    if input_yang_obj.inheritCost._changed():
        input_yang_obj.inheritCost = input_yang_obj.inheritCost
        
    if input_yang_obj.permitIbgp._changed():
        input_yang_obj.permitIbgp = input_yang_obj.permitIbgp
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes(input_yang_obj: yc_isImportRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isImportRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isImportRoute.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes_isImportRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports_isFilterImport(input_yang_obj: yc_isFilterImport_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports_isFilterImport, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFilterImports/isFilterImport

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.aclNumOrName._changed():
        input_yang_obj.aclNumOrName = input_yang_obj.aclNumOrName
        
    if input_yang_obj.acl6NumOrName._changed():
        input_yang_obj.acl6NumOrName = input_yang_obj.acl6NumOrName
        
    if input_yang_obj.ipPrefix._changed():
        input_yang_obj.ipPrefix = input_yang_obj.ipPrefix
        
    if input_yang_obj.ipv6Prefix._changed():
        input_yang_obj.ipv6Prefix = input_yang_obj.ipv6Prefix
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports(input_yang_obj: yc_isFilterImports_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFilterImports

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports_isFilterImport(input_yang_obj.isFilterImport, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports_isFilterExport(input_yang_obj: yc_isFilterExport_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports_isFilterExport, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFilterExports/isFilterExport

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.aclNumOrName._changed():
        input_yang_obj.aclNumOrName = input_yang_obj.aclNumOrName
        
    if input_yang_obj.acl6NumOrName._changed():
        input_yang_obj.acl6NumOrName = input_yang_obj.acl6NumOrName
        
    if input_yang_obj.ipPrefix._changed():
        input_yang_obj.ipPrefix = input_yang_obj.ipPrefix
        
    if input_yang_obj.ipv6Prefix._changed():
        input_yang_obj.ipv6Prefix = input_yang_obj.ipv6Prefix
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports(input_yang_obj: yc_isFilterExports_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFilterExports

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isFilterExport.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports_isFilterExport(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s_isLeakRouteLevel2ToLevel1(input_yang_obj: yc_isLeakRouteLevel2ToLevel1_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s_isLeakRouteLevel2ToLevel1, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLeakRouteLevel2ToLevel1s/isLeakRouteLevel2ToLevel1

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    if input_yang_obj.aclNumOrName._changed():
        input_yang_obj.aclNumOrName = input_yang_obj.aclNumOrName
        
    if input_yang_obj.acl6NumOrName._changed():
        input_yang_obj.acl6NumOrName = input_yang_obj.acl6NumOrName
        
    if input_yang_obj.ipPrefix._changed():
        input_yang_obj.ipPrefix = input_yang_obj.ipPrefix
        
    if input_yang_obj.ipv6Prefix._changed():
        input_yang_obj.ipv6Prefix = input_yang_obj.ipv6Prefix
        
    if input_yang_obj.allowFilter._changed():
        input_yang_obj.allowFilter = input_yang_obj.allowFilter
        
    if input_yang_obj.allowUpdown._changed():
        input_yang_obj.allowUpdown = input_yang_obj.allowUpdown
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s(input_yang_obj: yc_isLeakRouteLevel2ToLevel1s_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLeakRouteLevel2ToLevel1s

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s_isLeakRouteLevel2ToLevel1(input_yang_obj.isLeakRouteLevel2ToLevel1, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s_isLeakRouteLevel1ToLevel2(input_yang_obj: yc_isLeakRouteLevel1ToLevel2_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s_isLeakRouteLevel1ToLevel2, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLeakRouteLevel1ToLevel2s/isLeakRouteLevel1ToLevel2

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    if input_yang_obj.aclNumOrName._changed():
        input_yang_obj.aclNumOrName = input_yang_obj.aclNumOrName
        
    if input_yang_obj.acl6NumOrName._changed():
        input_yang_obj.acl6NumOrName = input_yang_obj.acl6NumOrName
        
    if input_yang_obj.ipPrefix._changed():
        input_yang_obj.ipPrefix = input_yang_obj.ipPrefix
        
    if input_yang_obj.ipv6Prefix._changed():
        input_yang_obj.ipv6Prefix = input_yang_obj.ipv6Prefix
        
    if input_yang_obj.leakEnableFlag._changed():
        input_yang_obj.leakEnableFlag = input_yang_obj.leakEnableFlag
        
    if input_yang_obj.allowFilter._changed():
        input_yang_obj.allowFilter = input_yang_obj.allowFilter
        
    if input_yang_obj.nosidflag._changed():
        input_yang_obj.nosidflag = input_yang_obj.nosidflag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s(input_yang_obj: yc_isLeakRouteLevel1ToLevel2s_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLeakRouteLevel1ToLevel2s

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s_isLeakRouteLevel1ToLevel2(input_yang_obj.isLeakRouteLevel1ToLevel2, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys_isRoutePriority(input_yang_obj: yc_isRoutePriority_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys_isRoutePriority, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isRoutePrioritys/isRoutePriority

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.useflag._changed():
        input_yang_obj.useflag = input_yang_obj.useflag
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    if input_yang_obj.ipprefix._changed():
        input_yang_obj.ipprefix = input_yang_obj.ipprefix
        
    if input_yang_obj.ipv6prefix._changed():
        input_yang_obj.ipv6prefix = input_yang_obj.ipv6prefix
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys(input_yang_obj: yc_isRoutePrioritys_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isRoutePrioritys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isRoutePriority.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys_isRoutePriority(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences_isPreference(input_yang_obj: yc_isPreference_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences_isPreference, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isPreferences/isPreference

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.preferenceValue._changed():
        input_yang_obj.preferenceValue = input_yang_obj.preferenceValue
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences(input_yang_obj: yc_isPreferences_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isPreferences

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences_isPreference(input_yang_obj.isPreference, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isRlfa(input_yang_obj: yc_isRlfa_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isRlfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFrr/isRlfa

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.rlfaLevel1Enable._changed():
        input_yang_obj.rlfaLevel1Enable = input_yang_obj.rlfaLevel1Enable
        
    if input_yang_obj.rlfaLevel1MaxCost._changed():
        input_yang_obj.rlfaLevel1MaxCost = input_yang_obj.rlfaLevel1MaxCost
        
    if input_yang_obj.rlfaLevel1IpPrefix._changed():
        input_yang_obj.rlfaLevel1IpPrefix = input_yang_obj.rlfaLevel1IpPrefix
        
    if input_yang_obj.rlfaLevel2Enable._changed():
        input_yang_obj.rlfaLevel2Enable = input_yang_obj.rlfaLevel2Enable
        
    if input_yang_obj.rlfaLevel2MaxCost._changed():
        input_yang_obj.rlfaLevel2MaxCost = input_yang_obj.rlfaLevel2MaxCost
        
    if input_yang_obj.rlfaLevel2IpPrefix._changed():
        input_yang_obj.rlfaLevel2IpPrefix = input_yang_obj.rlfaLevel2IpPrefix
        
    if input_yang_obj.rlfaLevel1LdpType._changed():
        input_yang_obj.rlfaLevel1LdpType = input_yang_obj.rlfaLevel1LdpType
        
    if input_yang_obj.rlfaLevel2LdpType._changed():
        input_yang_obj.rlfaLevel2LdpType = input_yang_obj.rlfaLevel2LdpType
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isFrrTieBreak(input_yang_obj: yc_isFrrTieBreak_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isFrrTieBreak, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFrr/isFrrTieBreak

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.l1nodeProtectPrefer._changed():
        input_yang_obj.l1nodeProtectPrefer = input_yang_obj.l1nodeProtectPrefer
        
    if input_yang_obj.l1lowcostPrefer._changed():
        input_yang_obj.l1lowcostPrefer = input_yang_obj.l1lowcostPrefer
        
    if input_yang_obj.l1nonEcmpPrefer._changed():
        input_yang_obj.l1nonEcmpPrefer = input_yang_obj.l1nonEcmpPrefer
        
    if input_yang_obj.l1srlgDisjointPrefer._changed():
        input_yang_obj.l1srlgDisjointPrefer = input_yang_obj.l1srlgDisjointPrefer
        
    if input_yang_obj.l2nodeProtectPrefer._changed():
        input_yang_obj.l2nodeProtectPrefer = input_yang_obj.l2nodeProtectPrefer
        
    if input_yang_obj.l2lowcostPrefer._changed():
        input_yang_obj.l2lowcostPrefer = input_yang_obj.l2lowcostPrefer
        
    if input_yang_obj.l2nonEcmpPrefer._changed():
        input_yang_obj.l2nonEcmpPrefer = input_yang_obj.l2nonEcmpPrefer
        
    if input_yang_obj.l2srlgDisjointPrefer._changed():
        input_yang_obj.l2srlgDisjointPrefer = input_yang_obj.l2srlgDisjointPrefer
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isTilfa(input_yang_obj: yc_isTilfa_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isTilfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFrr/isTilfa

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.tilfaL1Enable._changed():
        input_yang_obj.tilfaL1Enable = input_yang_obj.tilfaL1Enable
        
    if input_yang_obj.tilfaL2Enable._changed():
        input_yang_obj.tilfaL2Enable = input_yang_obj.tilfaL2Enable
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isIpv6Tilfa(input_yang_obj: yc_isIpv6Tilfa_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isIpv6Tilfa, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFrr/isIpv6Tilfa

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv6TilfaL1Enable._changed():
        input_yang_obj.ipv6TilfaL1Enable = input_yang_obj.ipv6TilfaL1Enable
        
    if input_yang_obj.ipv6TilfaL2Enable._changed():
        input_yang_obj.ipv6TilfaL2Enable = input_yang_obj.ipv6TilfaL2Enable
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr(input_yang_obj: yc_isFrr_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isFrr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.frrEnable._changed():
        input_yang_obj.frrEnable = input_yang_obj.frrEnable
        
    if input_yang_obj.policyType._changed():
        input_yang_obj.policyType = input_yang_obj.policyType
        
    if input_yang_obj.routePolicyName._changed():
        input_yang_obj.routePolicyName = input_yang_obj.routePolicyName
        
    if input_yang_obj.routeFilterNameEntity._changed():
        input_yang_obj.routeFilterNameEntity = input_yang_obj.routeFilterNameEntity
        
    if input_yang_obj.lfaLevel1Enable._changed():
        input_yang_obj.lfaLevel1Enable = input_yang_obj.lfaLevel1Enable
        
    if input_yang_obj.lfaLevel2Enable._changed():
        input_yang_obj.lfaLevel2Enable = input_yang_obj.lfaLevel2Enable
        
    if input_yang_obj.ecmpLevel1Enable._changed():
        input_yang_obj.ecmpLevel1Enable = input_yang_obj.ecmpLevel1Enable
        
    if input_yang_obj.ecmpLevel2Enable._changed():
        input_yang_obj.ecmpLevel2Enable = input_yang_obj.ecmpLevel2Enable
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isRlfa(input_yang_obj.isRlfa, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isFrrTieBreak(input_yang_obj.isFrrTieBreak, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isTilfa(input_yang_obj.isTilfa, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr_isIpv6Tilfa(input_yang_obj.isIpv6Tilfa, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt_isPrefixSid(input_yang_obj: yc_isPrefixSid_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt_isPrefixSid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isCircMts/isCircMt/isPrefixSid

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefixSidType._changed():
        input_yang_obj.prefixSidType = input_yang_obj.prefixSidType
        
    if input_yang_obj.prefixLabel._changed():
        input_yang_obj.prefixLabel = input_yang_obj.prefixLabel
        
    if input_yang_obj.nodeFlag._changed():
        input_yang_obj.nodeFlag = input_yang_obj.nodeFlag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt(input_yang_obj: yc_isCircMt_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isCircMts/isCircMt

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.level1Cost._changed():
        input_yang_obj.level1Cost = input_yang_obj.level1Cost
        
    if input_yang_obj.level2Cost._changed():
        input_yang_obj.level2Cost = input_yang_obj.level2Cost
        
    if input_yang_obj.level1Tag._changed():
        input_yang_obj.level1Tag = input_yang_obj.level1Tag
        
    if input_yang_obj.level2Tag._changed():
        input_yang_obj.level2Tag = input_yang_obj.level2Tag
        
    if input_yang_obj.suppressReach._changed():
        input_yang_obj.suppressReach = input_yang_obj.suppressReach
        
    if input_yang_obj.bfdEnable._changed():
        input_yang_obj.bfdEnable = input_yang_obj.bfdEnable
        
    if input_yang_obj.bfdStaticEn._changed():
        input_yang_obj.bfdStaticEn = input_yang_obj.bfdStaticEn
        
    if input_yang_obj.bfdBlockEn._changed():
        input_yang_obj.bfdBlockEn = input_yang_obj.bfdBlockEn
        
    if input_yang_obj.bfdMinRx._changed():
        input_yang_obj.bfdMinRx = input_yang_obj.bfdMinRx
        
    if input_yang_obj.bfdMinTx._changed():
        input_yang_obj.bfdMinTx = input_yang_obj.bfdMinTx
        
    if input_yang_obj.bfdMultiplierNumber._changed():
        input_yang_obj.bfdMultiplierNumber = input_yang_obj.bfdMultiplierNumber
        
    if input_yang_obj.tosExpValue._changed():
        input_yang_obj.tosExpValue = input_yang_obj.tosExpValue
        
    if input_yang_obj.frrBindingFlag._changed():
        input_yang_obj.frrBindingFlag = input_yang_obj.frrBindingFlag
        
    if input_yang_obj.level1FrrBlock._changed():
        input_yang_obj.level1FrrBlock = input_yang_obj.level1FrrBlock
        
    if input_yang_obj.level2FrrBlock._changed():
        input_yang_obj.level2FrrBlock = input_yang_obj.level2FrrBlock
        
    if input_yang_obj.level1RemoteLFA._changed():
        input_yang_obj.level1RemoteLFA = input_yang_obj.level1RemoteLFA
        
    if input_yang_obj.level2RemoteLFA._changed():
        input_yang_obj.level2RemoteLFA = input_yang_obj.level2RemoteLFA
        
    if input_yang_obj.l1TilfaDisable._changed():
        input_yang_obj.l1TilfaDisable = input_yang_obj.l1TilfaDisable
        
    if input_yang_obj.l2TilfaDisable._changed():
        input_yang_obj.l2TilfaDisable = input_yang_obj.l2TilfaDisable
        
    if input_yang_obj.l1Ipv6TilfaDisable._changed():
        input_yang_obj.l1Ipv6TilfaDisable = input_yang_obj.l1Ipv6TilfaDisable
        
    if input_yang_obj.l2Ipv6TilfaDisable._changed():
        input_yang_obj.l2Ipv6TilfaDisable = input_yang_obj.l2Ipv6TilfaDisable
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt_isPrefixSid(input_yang_obj.isPrefixSid, translated_yang_obj)
        
    if input_yang_obj.bfdBitErrCfg._changed():
        input_yang_obj.bfdBitErrCfg = input_yang_obj.bfdBitErrCfg
        
    if input_yang_obj.incrCost._changed():
        input_yang_obj.incrCost = input_yang_obj.incrCost
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts(input_yang_obj: yc_isCircMts_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isCircMts

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isCircMt.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts_isCircMt(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss_isDispRouteStatistics(input_yang_obj: yc_isDispRouteStatistics_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss_isDispRouteStatistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispRouteStatisticss/isDispRouteStatistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.v4LearntRtNum._changed():
        input_yang_obj.v4LearntRtNum = input_yang_obj.v4LearntRtNum
        
    if input_yang_obj.v6LearntRtNum._changed():
        input_yang_obj.v6LearntRtNum = input_yang_obj.v6LearntRtNum
        
    if input_yang_obj.v4CriticalRtNum._changed():
        input_yang_obj.v4CriticalRtNum = input_yang_obj.v4CriticalRtNum
        
    if input_yang_obj.v4HighRtNum._changed():
        input_yang_obj.v4HighRtNum = input_yang_obj.v4HighRtNum
        
    if input_yang_obj.v4MediumRtNum._changed():
        input_yang_obj.v4MediumRtNum = input_yang_obj.v4MediumRtNum
        
    if input_yang_obj.v4LowRtNum._changed():
        input_yang_obj.v4LowRtNum = input_yang_obj.v4LowRtNum
        
    if input_yang_obj.v6CriticalRtNum._changed():
        input_yang_obj.v6CriticalRtNum = input_yang_obj.v6CriticalRtNum
        
    if input_yang_obj.v6HighRtNum._changed():
        input_yang_obj.v6HighRtNum = input_yang_obj.v6HighRtNum
        
    if input_yang_obj.v6MediumRtNum._changed():
        input_yang_obj.v6MediumRtNum = input_yang_obj.v6MediumRtNum
        
    if input_yang_obj.v6LowRtNum._changed():
        input_yang_obj.v6LowRtNum = input_yang_obj.v6LowRtNum
        
    if input_yang_obj.v4ForwardRtNum._changed():
        input_yang_obj.v4ForwardRtNum = input_yang_obj.v4ForwardRtNum
        
    if input_yang_obj.v6ForwardRtNum._changed():
        input_yang_obj.v6ForwardRtNum = input_yang_obj.v6ForwardRtNum
        
    if input_yang_obj.v4RtAdded2RM._changed():
        input_yang_obj.v4RtAdded2RM = input_yang_obj.v4RtAdded2RM
        
    if input_yang_obj.v4RtUnAdded2RM._changed():
        input_yang_obj.v4RtUnAdded2RM = input_yang_obj.v4RtUnAdded2RM
        
    if input_yang_obj.v6RtAdded2RM._changed():
        input_yang_obj.v6RtAdded2RM = input_yang_obj.v6RtAdded2RM
        
    if input_yang_obj.v6RtUnAdded2RM._changed():
        input_yang_obj.v6RtUnAdded2RM = input_yang_obj.v6RtUnAdded2RM
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss(input_yang_obj: yc_isDispRouteStatisticss_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispRouteStatisticss

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispRouteStatistics.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss_isDispRouteStatistics(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes_isDispV4Route(input_yang_obj: yc_isDispV4Route_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes_isDispV4Route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV4Routes/isDispV4Route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.intCost._changed():
        input_yang_obj.intCost = input_yang_obj.intCost
        
    if input_yang_obj.extCost._changed():
        input_yang_obj.extCost = input_yang_obj.extCost
        
    if input_yang_obj.exitInterfaceName._changed():
        input_yang_obj.exitInterfaceName = input_yang_obj.exitInterfaceName
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes(input_yang_obj: yc_isDispV4Routes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV4Routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispV4Route.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes_isDispV4Route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes_isDispV6Route(input_yang_obj: yc_isDispV6Route_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes_isDispV6Route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV6Routes/isDispV6Route

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.exitInterfaceName._changed():
        input_yang_obj.exitInterfaceName = input_yang_obj.exitInterfaceName
        
    if input_yang_obj.costValue._changed():
        input_yang_obj.costValue = input_yang_obj.costValue
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes(input_yang_obj: yc_isDispV6Routes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV6Routes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispV6Route.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes_isDispV6Route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes_isDispV4ImportRoute(input_yang_obj: yc_isDispV4ImportRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes_isDispV4ImportRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV4ImportRoutes/isDispV4ImportRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.intCost._changed():
        input_yang_obj.intCost = input_yang_obj.intCost
        
    if input_yang_obj.extCost._changed():
        input_yang_obj.extCost = input_yang_obj.extCost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes(input_yang_obj: yc_isDispV4ImportRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV4ImportRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispV4ImportRoute.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes_isDispV4ImportRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes_isDispV6ImportRoute(input_yang_obj: yc_isDispV6ImportRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes_isDispV6ImportRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV6ImportRoutes/isDispV6ImportRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.intCost._changed():
        input_yang_obj.intCost = input_yang_obj.intCost
        
    if input_yang_obj.tag._changed():
        input_yang_obj.tag = input_yang_obj.tag
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes(input_yang_obj: yc_isDispV6ImportRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispV6ImportRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispV6ImportRoute.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes_isDispV6ImportRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes_isDispMigpRoute(input_yang_obj: yc_isDispMigpRoute_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes_isDispMigpRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispMigpRoutes/isDispMigpRoute

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.intCost._changed():
        input_yang_obj.intCost = input_yang_obj.intCost
        
    if input_yang_obj.extCost._changed():
        input_yang_obj.extCost = input_yang_obj.extCost
        
    if input_yang_obj.exitInterfaceName._changed():
        input_yang_obj.exitInterfaceName = input_yang_obj.exitInterfaceName
        
    if input_yang_obj.flags._changed():
        input_yang_obj.flags = input_yang_obj.flags
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes(input_yang_obj: yc_isDispMigpRoutes_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isDispMigpRoutes

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispMigpRoute.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes_isDispMigpRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts_isLinkGroupPort(input_yang_obj: yc_isLinkGroupPort_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts_isLinkGroupPort, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLinkGroupPorts/isLinkGroupPort

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts(input_yang_obj: yc_isLinkGroupPorts_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isLinkGroupPorts

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isLinkGroupPort.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts_isLinkGroupPort(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSrLspTrig(input_yang_obj: yc_isSrLspTrig_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSrLspTrig, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT/isSrLspTrig

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.srLspTrigType._changed():
        input_yang_obj.srLspTrigType = input_yang_obj.srLspTrigType
        
    if input_yang_obj.ipPrefixName._changed():
        input_yang_obj.ipPrefixName = input_yang_obj.ipPrefixName
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT(input_yang_obj: yc_isSiteMT_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs_isSiteMT, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs/isSiteMT

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.topologyName._changed():
        input_yang_obj.topologyName = input_yang_obj.topologyName
        
    if input_yang_obj.spfPriority._changed():
        input_yang_obj.spfPriority = input_yang_obj.spfPriority
        
    if input_yang_obj.maxLoadBalancing._changed():
        input_yang_obj.maxLoadBalancing = input_yang_obj.maxLoadBalancing
        
    if input_yang_obj.autoCostEnable._changed():
        input_yang_obj.autoCostEnable = input_yang_obj.autoCostEnable
        
    if input_yang_obj.autoCostEnableCompatible._changed():
        input_yang_obj.autoCostEnableCompatible = input_yang_obj.autoCostEnableCompatible
        
    if input_yang_obj.bandwidth._changed():
        input_yang_obj.bandwidth = input_yang_obj.bandwidth
        
    if input_yang_obj.level1Cost._changed():
        input_yang_obj.level1Cost = input_yang_obj.level1Cost
        
    if input_yang_obj.level2Cost._changed():
        input_yang_obj.level2Cost = input_yang_obj.level2Cost
        
    if input_yang_obj.overloadType._changed():
        input_yang_obj.overloadType = input_yang_obj.overloadType
        
    if input_yang_obj.overloadWaitType._changed():
        input_yang_obj.overloadWaitType = input_yang_obj.overloadWaitType
        
    if input_yang_obj.overloadNbrSysId._changed():
        input_yang_obj.overloadNbrSysId = input_yang_obj.overloadNbrSysId
        
    if input_yang_obj.overloadTimeout1._changed():
        input_yang_obj.overloadTimeout1 = input_yang_obj.overloadTimeout1
        
    if input_yang_obj.overloadTimeout2._changed():
        input_yang_obj.overloadTimeout2 = input_yang_obj.overloadTimeout2
        
    if input_yang_obj.overloadInterlevel._changed():
        input_yang_obj.overloadInterlevel = input_yang_obj.overloadInterlevel
        
    if input_yang_obj.overloadExternal._changed():
        input_yang_obj.overloadExternal = input_yang_obj.overloadExternal
        
    if input_yang_obj.level1TagValue._changed():
        input_yang_obj.level1TagValue = input_yang_obj.level1TagValue
        
    if input_yang_obj.level2TagValue._changed():
        input_yang_obj.level2TagValue = input_yang_obj.level2TagValue
        
    if input_yang_obj.allCircBfdOn._changed():
        input_yang_obj.allCircBfdOn = input_yang_obj.allCircBfdOn
        
    if input_yang_obj.frrBindingFlag._changed():
        input_yang_obj.frrBindingFlag = input_yang_obj.frrBindingFlag
        
    if input_yang_obj.bfdMinRx._changed():
        input_yang_obj.bfdMinRx = input_yang_obj.bfdMinRx
        
    if input_yang_obj.bfdMinTx._changed():
        input_yang_obj.bfdMinTx = input_yang_obj.bfdMinTx
        
    if input_yang_obj.bfdMultNum._changed():
        input_yang_obj.bfdMultNum = input_yang_obj.bfdMultNum
        
    if input_yang_obj.tosExpValue._changed():
        input_yang_obj.tosExpValue = input_yang_obj.tosExpValue
        
    if input_yang_obj.allCircBfdBitErrOn._changed():
        input_yang_obj.allCircBfdBitErrOn = input_yang_obj.allCircBfdBitErrOn
        
    if input_yang_obj.mtIndex._changed():
        input_yang_obj.mtIndex = input_yang_obj.mtIndex
        
    if input_yang_obj.attAdvControl._changed():
        input_yang_obj.attAdvControl = input_yang_obj.attAdvControl
        
    if input_yang_obj.attAvoidLearn._changed():
        input_yang_obj.attAvoidLearn = input_yang_obj.attAvoidLearn
        
    if input_yang_obj.applyQppb._changed():
        input_yang_obj.applyQppb = input_yang_obj.applyQppb
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isNextHopWeights(input_yang_obj.isNextHopWeights, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSummaryRoutes(input_yang_obj.isSummaryRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDefaultRoutes(input_yang_obj.isDefaultRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isImportRoutes(input_yang_obj.isImportRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterImports(input_yang_obj.isFilterImports, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFilterExports(input_yang_obj.isFilterExports, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel2ToLevel1s(input_yang_obj.isLeakRouteLevel2ToLevel1s, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLeakRouteLevel1ToLevel2s(input_yang_obj.isLeakRouteLevel1ToLevel2s, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isRoutePrioritys(input_yang_obj.isRoutePrioritys, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isPreferences(input_yang_obj.isPreferences, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isFrr(input_yang_obj.isFrr, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isCircMts(input_yang_obj.isCircMts, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispRouteStatisticss(input_yang_obj.isDispRouteStatisticss, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4Routes(input_yang_obj.isDispV4Routes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6Routes(input_yang_obj.isDispV6Routes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV4ImportRoutes(input_yang_obj.isDispV4ImportRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispV6ImportRoutes(input_yang_obj.isDispV6ImportRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isDispMigpRoutes(input_yang_obj.isDispMigpRoutes, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isLinkGroupPorts(input_yang_obj.isLinkGroupPorts, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT_isSrLspTrig(input_yang_obj.isSrLspTrig, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSiteMTs(input_yang_obj: yc_isSiteMTs_huawei_isiscomm__isiscomm_isSites_isSite_isSiteMTs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSiteMTs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isSiteMT.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs_isSiteMT(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispLsdbs_isDispLsdb(input_yang_obj: yc_isDispLsdb_huawei_isiscomm__isiscomm_isSites_isSite_isDispLsdbs_isDispLsdb, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispLsdbs/isDispLsdb

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.seqenceNumber._changed():
        input_yang_obj.seqenceNumber = input_yang_obj.seqenceNumber
        
    if input_yang_obj.checkSum._changed():
        input_yang_obj.checkSum = input_yang_obj.checkSum
        
    if input_yang_obj.lspLength._changed():
        input_yang_obj.lspLength = input_yang_obj.lspLength
        
    if input_yang_obj.attBit._changed():
        input_yang_obj.attBit = input_yang_obj.attBit
        
    if input_yang_obj.partitionBit._changed():
        input_yang_obj.partitionBit = input_yang_obj.partitionBit
        
    if input_yang_obj.overloadBit._changed():
        input_yang_obj.overloadBit = input_yang_obj.overloadBit
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.isLocalLsp._changed():
        input_yang_obj.isLocalLsp = input_yang_obj.isLocalLsp
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispLsdbs(input_yang_obj: yc_isDispLsdbs_huawei_isiscomm__isiscomm_isSites_isSite_isDispLsdbs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispLsdbs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispLsdb.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispLsdbs_isDispLsdb(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs_isPeerIpv4Addr(input_yang_obj: yc_isPeerIpv4Addr_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs_isPeerIpv4Addr, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isPeerIpv4Addrs/isPeerIpv4Addr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs(input_yang_obj: yc_isPeerIpv4Addrs_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isPeerIpv4Addrs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isPeerIpv4Addr.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs_isPeerIpv4Addr(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs_isPeerIpv6GlbAddr(input_yang_obj: yc_isPeerIpv6GlbAddr_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs_isPeerIpv6GlbAddr, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isPeerIpv6GlbAddrs/isPeerIpv6GlbAddr

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs(input_yang_obj: yc_isPeerIpv6GlbAddrs_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isPeerIpv6GlbAddrs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isPeerIpv6GlbAddr.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs_isPeerIpv6GlbAddr(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids_isEndXSid(input_yang_obj: yc_isEndXSid_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids_isEndXSid, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isEndXSids/isEndXSid

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
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

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids(input_yang_obj: yc_isEndXSids_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer/isEndXSids

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isEndXSid.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids_isEndXSid(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer(input_yang_obj: yc_isDispPeer_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers_isDispPeer, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers/isDispPeer

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.hostName._changed():
        input_yang_obj.hostName = input_yang_obj.hostName
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.priority._changed():
        input_yang_obj.priority = input_yang_obj.priority
        
    if input_yang_obj.areaAddress._changed():
        input_yang_obj.areaAddress = input_yang_obj.areaAddress
        
    if input_yang_obj.upTime._changed():
        input_yang_obj.upTime = input_yang_obj.upTime
        
    if input_yang_obj.upTimeStamp._changed():
        input_yang_obj.upTimeStamp = input_yang_obj.upTimeStamp
        
    if input_yang_obj.adjMtId._changed():
        input_yang_obj.adjMtId = input_yang_obj.adjMtId
        
    if input_yang_obj.localMtId._changed():
        input_yang_obj.localMtId = input_yang_obj.localMtId
        
    if input_yang_obj.protocol._changed():
        input_yang_obj.protocol = input_yang_obj.protocol
        
    if input_yang_obj.restartCapable._changed():
        input_yang_obj.restartCapable = input_yang_obj.restartCapable
        
    if input_yang_obj.suppressedAdj._changed():
        input_yang_obj.suppressedAdj = input_yang_obj.suppressedAdj
        
    if input_yang_obj.adjSid._changed():
        input_yang_obj.adjSid = input_yang_obj.adjSid
        
    if input_yang_obj.peerIpv6Address._changed():
        input_yang_obj.peerIpv6Address = input_yang_obj.peerIpv6Address
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv4Addrs(input_yang_obj.isPeerIpv4Addrs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isPeerIpv6GlbAddrs(input_yang_obj.isPeerIpv6GlbAddrs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer_isEndXSids(input_yang_obj.isEndXSids, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispPeers(input_yang_obj: yc_isDispPeers_huawei_isiscomm__isiscomm_isSites_isSite_isDispPeers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispPeers

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispPeer.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispPeers_isDispPeer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispCircs_isDispCirc(input_yang_obj: yc_isDispCirc_huawei_isiscomm__isiscomm_isSites_isSite_isDispCircs_isDispCirc, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispCircs/isDispCirc

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv4L1Cost._changed():
        input_yang_obj.ipv4L1Cost = input_yang_obj.ipv4L1Cost
        
    if input_yang_obj.ipv4L2Cost._changed():
        input_yang_obj.ipv4L2Cost = input_yang_obj.ipv4L2Cost
        
    if input_yang_obj.ipv6L1Cost._changed():
        input_yang_obj.ipv6L1Cost = input_yang_obj.ipv6L1Cost
        
    if input_yang_obj.ipv6L2Cost._changed():
        input_yang_obj.ipv6L2Cost = input_yang_obj.ipv6L2Cost
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispCircs(input_yang_obj: yc_isDispCircs_huawei_isiscomm__isiscomm_isSites_isSite_isDispCircs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispCircs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispCirc.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispCircs_isDispCirc(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispLspStatisticss_isDispLspStatistics(input_yang_obj: yc_isDispLspStatistics_huawei_isiscomm__isiscomm_isSites_isSite_isDispLspStatisticss_isDispLspStatistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispLspStatisticss/isDispLspStatistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.usedFragsNumber._changed():
        input_yang_obj.usedFragsNumber = input_yang_obj.usedFragsNumber
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispLspStatisticss(input_yang_obj: yc_isDispLspStatisticss_huawei_isiscomm__isiscomm_isSites_isSite_isDispLspStatisticss, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispLspStatisticss

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispLspStatistics.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispLspStatisticss_isDispLspStatistics(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispBfdSessions_isDispBfdSession(input_yang_obj: yc_isDispBfdSession_huawei_isiscomm__isiscomm_isSites_isSite_isDispBfdSessions_isDispBfdSession, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispBfdSessions/isDispBfdSession

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.bfdState._changed():
        input_yang_obj.bfdState = input_yang_obj.bfdState
        
    if input_yang_obj.bfdMinTx._changed():
        input_yang_obj.bfdMinTx = input_yang_obj.bfdMinTx
        
    if input_yang_obj.bfdMinRx._changed():
        input_yang_obj.bfdMinRx = input_yang_obj.bfdMinRx
        
    if input_yang_obj.bfdMulNumber._changed():
        input_yang_obj.bfdMulNumber = input_yang_obj.bfdMulNumber
        
    if input_yang_obj.systemId._changed():
        input_yang_obj.systemId = input_yang_obj.systemId
        
    if input_yang_obj.circuitName._changed():
        input_yang_obj.circuitName = input_yang_obj.circuitName
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispBfdSessions(input_yang_obj: yc_isDispBfdSessions_huawei_isiscomm__isiscomm_isSites_isSite_isDispBfdSessions, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispBfdSessions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispBfdSession.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispBfdSessions_isDispBfdSession(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispBfdBitErrSessions_isDispBfdBitErrSession(input_yang_obj: yc_isDispBfdBitErrSession_huawei_isiscomm__isiscomm_isSites_isSite_isDispBfdBitErrSessions_isDispBfdBitErrSession, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispBfdBitErrSessions/isDispBfdBitErrSession

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.bfdState._changed():
        input_yang_obj.bfdState = input_yang_obj.bfdState
        
    if input_yang_obj.systemId._changed():
        input_yang_obj.systemId = input_yang_obj.systemId
        
    if input_yang_obj.circuitName._changed():
        input_yang_obj.circuitName = input_yang_obj.circuitName
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispBfdBitErrSessions(input_yang_obj: yc_isDispBfdBitErrSessions_huawei_isiscomm__isiscomm_isSites_isSite_isDispBfdBitErrSessions, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispBfdBitErrSessions

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispBfdBitErrSession.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispBfdBitErrSessions_isDispBfdBitErrSession(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispNameTables_isDispNameTable(input_yang_obj: yc_isDispNameTable_huawei_isiscomm__isiscomm_isSites_isSite_isDispNameTables_isDispNameTable, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispNameTables/isDispNameTable

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.hostName._changed():
        input_yang_obj.hostName = input_yang_obj.hostName
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispNameTables(input_yang_obj: yc_isDispNameTables_huawei_isiscomm__isiscomm_isSites_isSite_isDispNameTables, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispNameTables

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispNameTable.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispNameTables_isDispNameTable(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLinkGroups_isLinkGroup(input_yang_obj: yc_isLinkGroup_huawei_isiscomm__isiscomm_isSites_isSite_isLinkGroups_isLinkGroup, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLinkGroups/isLinkGroup

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.minMembers._changed():
        input_yang_obj.minMembers = input_yang_obj.minMembers
        
    if input_yang_obj.revertMembers._changed():
        input_yang_obj.revertMembers = input_yang_obj.revertMembers
        
    if input_yang_obj.costOffset._changed():
        input_yang_obj.costOffset = input_yang_obj.costOffset
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isLinkGroups(input_yang_obj: yc_isLinkGroups_huawei_isiscomm__isiscomm_isSites_isSite_isLinkGroups, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isLinkGroups

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isLinkGroup.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isLinkGroups_isLinkGroup(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispVirtualAccs_isDispVirtualAcc(input_yang_obj: yc_isDispVirtualAcc_huawei_isiscomm__isiscomm_isSites_isSite_isDispVirtualAccs_isDispVirtualAcc, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispVirtualAccs/isDispVirtualAcc

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.routerID._changed():
        input_yang_obj.routerID = input_yang_obj.routerID
        
    if input_yang_obj.apID._changed():
        input_yang_obj.apID = input_yang_obj.apID
        
    if input_yang_obj.apRole._changed():
        input_yang_obj.apRole = input_yang_obj.apRole
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispVirtualAccs(input_yang_obj: yc_isDispVirtualAccs_huawei_isiscomm__isiscomm_isSites_isSite_isDispVirtualAccs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispVirtualAccs

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispVirtualAcc.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispVirtualAccs_isDispVirtualAcc(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSegrCfg(input_yang_obj: yc_isSegrCfg_huawei_isiscomm__isiscomm_isSites_isSite_isSegrCfg, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSegrCfg

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.isAutoAdjSid._changed():
        input_yang_obj.isAutoAdjSid = input_yang_obj.isAutoAdjSid
        
    if input_yang_obj.isSrmsRecvFlag._changed():
        input_yang_obj.isSrmsRecvFlag = input_yang_obj.isSrmsRecvFlag
        
    if input_yang_obj.isSrmsSendFlag._changed():
        input_yang_obj.isSrmsSendFlag = input_yang_obj.isSrmsSendFlag
        
    if input_yang_obj.isAdvStaticSid._changed():
        input_yang_obj.isAdvStaticSid = input_yang_obj.isAdvStaticSid
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispMapSvrInfos_isDispMapSvrInfo(input_yang_obj: yc_isDispMapSvrInfo_huawei_isiscomm__isiscomm_isSites_isSite_isDispMapSvrInfos_isDispMapSvrInfo, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispMapSvrInfos/isDispMapSvrInfo

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.advSystemId._changed():
        input_yang_obj.advSystemId = input_yang_obj.advSystemId
        
    if input_yang_obj.sidValue._changed():
        input_yang_obj.sidValue = input_yang_obj.sidValue
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispMapSvrInfos(input_yang_obj: yc_isDispMapSvrInfos_huawei_isiscomm__isiscomm_isSites_isSite_isDispMapSvrInfos, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispMapSvrInfos

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispMapSvrInfo.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispMapSvrInfos_isDispMapSvrInfo(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isSrv6Cfg(input_yang_obj: yc_isSrv6Cfg_huawei_isiscomm__isiscomm_isSites_isSite_isSrv6Cfg, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isSrv6Cfg

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.isis.srv6_cfg.enable = "true"

    if input_yang_obj.defaultLocator._changed():
        translated_yang_obj.isis.srv6_cfg.default_locator = input_yang_obj.defaultLocator
        
    if input_yang_obj.locatorName._changed():
        translated_yang_obj.isis.srv6_cfg.locator_name = input_yang_obj.locatorName
        
    if input_yang_obj.autoSid._changed():
        translated_yang_obj.isis.srv6_cfg.persistent_end_x_sid = input_yang_obj.autoSid
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isIPv6SrAvoidMicroLoopSet(input_yang_obj: yc_isIPv6SrAvoidMicroLoopSet_huawei_isiscomm__isiscomm_isSites_isSite_isIPv6SrAvoidMicroLoopSet, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isIPv6SrAvoidMicroLoopSet

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.ipv6SrAvoidLoopEnable._changed():
        input_yang_obj.ipv6SrAvoidLoopEnable = input_yang_obj.ipv6SrAvoidLoopEnable
        
    if input_yang_obj.ipv6SrAvoidLoopDelayVal._changed():
        input_yang_obj.ipv6SrAvoidLoopDelayVal = input_yang_obj.ipv6SrAvoidLoopDelayVal
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispFrrSummrys_isDispFrrSummry(input_yang_obj: yc_isDispFrrSummry_huawei_isiscomm__isiscomm_isSites_isSite_isDispFrrSummrys_isDispFrrSummry, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispFrrSummrys/isDispFrrSummry

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.criticalCnt._changed():
        input_yang_obj.criticalCnt = input_yang_obj.criticalCnt
        
    if input_yang_obj.criticalProtCnt._changed():
        input_yang_obj.criticalProtCnt = input_yang_obj.criticalProtCnt
        
    if input_yang_obj.highCnt._changed():
        input_yang_obj.highCnt = input_yang_obj.highCnt
        
    if input_yang_obj.highProtCnt._changed():
        input_yang_obj.highProtCnt = input_yang_obj.highProtCnt
        
    if input_yang_obj.mediumCnt._changed():
        input_yang_obj.mediumCnt = input_yang_obj.mediumCnt
        
    if input_yang_obj.mediumProtCnt._changed():
        input_yang_obj.mediumProtCnt = input_yang_obj.mediumProtCnt
        
    if input_yang_obj.lowCnt._changed():
        input_yang_obj.lowCnt = input_yang_obj.lowCnt
        
    if input_yang_obj.lowProtCnt._changed():
        input_yang_obj.lowProtCnt = input_yang_obj.lowProtCnt
        
    if input_yang_obj.totalCnt._changed():
        input_yang_obj.totalCnt = input_yang_obj.totalCnt
        
    if input_yang_obj.totalProtCnt._changed():
        input_yang_obj.totalProtCnt = input_yang_obj.totalProtCnt
        
    if input_yang_obj.criticalCover._changed():
        input_yang_obj.criticalCover = input_yang_obj.criticalCover
        
    if input_yang_obj.highCover._changed():
        input_yang_obj.highCover = input_yang_obj.highCover
        
    if input_yang_obj.mediumCover._changed():
        input_yang_obj.mediumCover = input_yang_obj.mediumCover
        
    if input_yang_obj.lowCover._changed():
        input_yang_obj.lowCover = input_yang_obj.lowCover
        
    if input_yang_obj.totalCover._changed():
        input_yang_obj.totalCover = input_yang_obj.totalCover
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite_isDispFrrSummrys(input_yang_obj: yc_isDispFrrSummrys_huawei_isiscomm__isiscomm_isSites_isSite_isDispFrrSummrys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite/isDispFrrSummrys

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isDispFrrSummry.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite_isDispFrrSummrys_isDispFrrSummry(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites_isSite(input_yang_obj: yc_isSite_huawei_isiscomm__isiscomm_isSites_isSite, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites/isSite

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    translated_yang_obj.isis.enable = "true"

    if input_yang_obj.multiIID._changed():
        input_yang_obj.multiIID = input_yang_obj.multiIID
        
    if input_yang_obj.vpnName._changed():
        input_yang_obj.vpnName = input_yang_obj.vpnName
        
    if input_yang_obj.isLevel._changed():
        translated_yang_obj.isis.level_type = input_yang_obj.isLevel
        
    if input_yang_obj.lspMaxAge._changed():
        input_yang_obj.lspMaxAge = input_yang_obj.lspMaxAge
        
    if input_yang_obj.lspRefreshInterval._changed():
        input_yang_obj.lspRefreshInterval = input_yang_obj.lspRefreshInterval
        
    if input_yang_obj.shutDownEnable._changed():
        input_yang_obj.shutDownEnable = input_yang_obj.shutDownEnable
        
    if input_yang_obj.costStyle._changed():
        input_yang_obj.costStyle = input_yang_obj.costStyle
        
    if input_yang_obj.relaxSpfLimit._changed():
        input_yang_obj.relaxSpfLimit = input_yang_obj.relaxSpfLimit
        
    if input_yang_obj.linkQuaDeteEn._changed():
        input_yang_obj.linkQuaDeteEn = input_yang_obj.linkQuaDeteEn
        
    if input_yang_obj.spfMaxInterval._changed():
        input_yang_obj.spfMaxInterval = input_yang_obj.spfMaxInterval
        
    if input_yang_obj.spfInitInterval._changed():
        input_yang_obj.spfInitInterval = input_yang_obj.spfInitInterval
        
    if input_yang_obj.spfIncrInterval._changed():
        input_yang_obj.spfIncrInterval = input_yang_obj.spfIncrInterval
        
    if input_yang_obj.level1lspLengthOrig._changed():
        input_yang_obj.level1lspLengthOrig = input_yang_obj.level1lspLengthOrig
        
    if input_yang_obj.level2lspLengthOrig._changed():
        input_yang_obj.level2lspLengthOrig = input_yang_obj.level2lspLengthOrig
        
    if input_yang_obj.lspReceiveLength._changed():
        input_yang_obj.lspReceiveLength = input_yang_obj.lspReceiveLength
        
    if input_yang_obj.level1LspFragExtEnable._changed():
        input_yang_obj.level1LspFragExtEnable = input_yang_obj.level1LspFragExtEnable
        
    if input_yang_obj.level2LspFragExtEnable._changed():
        input_yang_obj.level2LspFragExtEnable = input_yang_obj.level2LspFragExtEnable
        
    if input_yang_obj.level1LspFragExtMode._changed():
        input_yang_obj.level1LspFragExtMode = input_yang_obj.level1LspFragExtMode
        
    if input_yang_obj.level2LspFragExtMode._changed():
        input_yang_obj.level2LspFragExtMode = input_yang_obj.level2LspFragExtMode
        
    if input_yang_obj.localSymbolicName._changed():
        input_yang_obj.localSymbolicName = input_yang_obj.localSymbolicName
        
    if input_yang_obj.stdAutoCostEnable._changed():
        input_yang_obj.stdAutoCostEnable = input_yang_obj.stdAutoCostEnable
        
    if input_yang_obj.stdAutoCostEnableCompatible._changed():
        input_yang_obj.stdAutoCostEnableCompatible = input_yang_obj.stdAutoCostEnableCompatible
        
    if input_yang_obj.stdbandwidth._changed():
        input_yang_obj.stdbandwidth = input_yang_obj.stdbandwidth
        
    if input_yang_obj.stdLevel1Cost._changed():
        input_yang_obj.stdLevel1Cost = input_yang_obj.stdLevel1Cost
        
    if input_yang_obj.stdLevel2Cost._changed():
        input_yang_obj.stdLevel2Cost = input_yang_obj.stdLevel2Cost
        
    if input_yang_obj.baseTopoType._changed():
        input_yang_obj.baseTopoType = input_yang_obj.baseTopoType
        
    if input_yang_obj.ldpAutoCfg._changed():
        input_yang_obj.ldpAutoCfg = input_yang_obj.ldpAutoCfg
        
    if input_yang_obj.poiEnable._changed():
        input_yang_obj.poiEnable = input_yang_obj.poiEnable
        
    if input_yang_obj.poiAlways._changed():
        input_yang_obj.poiAlways = input_yang_obj.poiAlways
        
    if input_yang_obj.lsdbLimit._changed():
        input_yang_obj.lsdbLimit = input_yang_obj.lsdbLimit
        
    if input_yang_obj.lsdbLimitNum._changed():
        input_yang_obj.lsdbLimitNum = input_yang_obj.lsdbLimitNum
        
    if input_yang_obj.lsdbThresUpper._changed():
        input_yang_obj.lsdbThresUpper = input_yang_obj.lsdbThresUpper
        
    if input_yang_obj.lsdbThresLower._changed():
        input_yang_obj.lsdbThresLower = input_yang_obj.lsdbThresLower
        
    if input_yang_obj.directInherit._changed():
        input_yang_obj.directInherit = input_yang_obj.directInherit
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.peerFlappingSuppress._changed():
        input_yang_obj.peerFlappingSuppress = input_yang_obj.peerFlappingSuppress
        
    if input_yang_obj.isSREnableMPLS._changed():
        input_yang_obj.isSREnableMPLS = input_yang_obj.isSREnableMPLS
        
    if input_yang_obj.bwConstraint._changed():
        input_yang_obj.bwConstraint = input_yang_obj.bwConstraint
        
    if input_yang_obj.loMultiplier._changed():
        input_yang_obj.loMultiplier = input_yang_obj.loMultiplier
        
    if input_yang_obj.unresvBwSubPool._changed():
        input_yang_obj.unresvBwSubPool = input_yang_obj.unresvBwSubPool
        
    if input_yang_obj.purgeLspDelayVal._changed():
        input_yang_obj.purgeLspDelayVal = input_yang_obj.purgeLspDelayVal
        
    if input_yang_obj.advOneIntfAddr._changed():
        input_yang_obj.advOneIntfAddr = input_yang_obj.advOneIntfAddr
        
    innerobj = _translate__isiscomm_isSites_isSite_isLspAgeRefresh(input_yang_obj.isLspAgeRefresh, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isBgpLs(input_yang_obj.isBgpLs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isLspGenIntelliTimer(input_yang_obj.isLspGenIntelliTimer, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isFlashFlood(input_yang_obj.isFlashFlood, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isOverloadSet(input_yang_obj.isOverloadSet, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isLdpSyncdSet(input_yang_obj.isLdpSyncdSet, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isExternAbility(input_yang_obj.isExternAbility, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isAvoidMicroLoopSet(input_yang_obj.isAvoidMicroLoopSet, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isLocalMtSets(input_yang_obj.isLocalMtSets, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isAreaIds(input_yang_obj.isAreaIds, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isNetEntitys(input_yang_obj.isNetEntitys, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isLspAuthtications(input_yang_obj.isLspAuthtications, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isNameTables(input_yang_obj.isNameTables, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isVirtualSystems(input_yang_obj.isVirtualSystems, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSrgbs(input_yang_obj.isSrgbs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isCircuits(input_yang_obj.isCircuits, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSiteMTs(input_yang_obj.isSiteMTs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispLsdbs(input_yang_obj.isDispLsdbs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispPeers(input_yang_obj.isDispPeers, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispCircs(input_yang_obj.isDispCircs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispLspStatisticss(input_yang_obj.isDispLspStatisticss, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispBfdSessions(input_yang_obj.isDispBfdSessions, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispBfdBitErrSessions(input_yang_obj.isDispBfdBitErrSessions, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispNameTables(input_yang_obj.isDispNameTables, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isLinkGroups(input_yang_obj.isLinkGroups, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispVirtualAccs(input_yang_obj.isDispVirtualAccs, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSegrCfg(input_yang_obj.isSegrCfg, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispMapSvrInfos(input_yang_obj.isDispMapSvrInfos, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isSrv6Cfg(input_yang_obj.isSrv6Cfg, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isIPv6SrAvoidMicroLoopSet(input_yang_obj.isIPv6SrAvoidMicroLoopSet, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isSites_isSite_isDispFrrSummrys(input_yang_obj.isDispFrrSummrys, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isSites(input_yang_obj: yc_isSites_huawei_isiscomm__isiscomm_isSites, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isSites

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.isSite.iteritems():
        innerobj = _translate__isiscomm_isSites_isSite(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__isiscomm_isisGlobalCfg(input_yang_obj: yc_isisGlobalCfg_huawei_isiscomm__isiscomm_isisGlobalCfg, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isisGlobalCfg

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.lspSeqOverAutoRvFlag._changed():
        input_yang_obj.lspSeqOverAutoRvFlag = input_yang_obj.lspSeqOverAutoRvFlag
        
    if input_yang_obj.sysIdConflictAutoRvFlag._changed():
        input_yang_obj.sysIdConflictAutoRvFlag = input_yang_obj.sysIdConflictAutoRvFlag
        
    if input_yang_obj.purgeLspProtectEnable._changed():
        input_yang_obj.purgeLspProtectEnable = input_yang_obj.purgeLspProtectEnable
        
    if input_yang_obj.purgeSourceTraceEnable._changed():
        input_yang_obj.purgeSourceTraceEnable = input_yang_obj.purgeSourceTraceEnable
        
    if input_yang_obj.purgeSourceTracePort._changed():
        input_yang_obj.purgeSourceTracePort = input_yang_obj.purgeSourceTracePort
        
    return translated_yang_obj

def _translate__isiscomm_isisGlobalStat(input_yang_obj: yc_isisGlobalStat_huawei_isiscomm__isiscomm_isisGlobalStat, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm/isisGlobalStat

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.globalPubNodeNumber._changed():
        input_yang_obj.globalPubNodeNumber = input_yang_obj.globalPubNodeNumber
        
    if input_yang_obj.globalPubPeerNumber._changed():
        input_yang_obj.globalPubPeerNumber = input_yang_obj.globalPubPeerNumber
        
    return translated_yang_obj

def _translate__isiscomm(input_yang_obj: yc_isiscomm_huawei_isiscomm__isiscomm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /isiscomm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    isiscomm_obj = translated_yang_obj.routing.control_plane_protocols.control_plane_protocol.add(type="isis", name="is-is-1")

    innerobj = _translate__isiscomm_isSites(input_yang_obj.isSites, isiscomm_obj)
        
    innerobj = _translate__isiscomm_isisGlobalCfg(input_yang_obj.isisGlobalCfg, translated_yang_obj)
        
    innerobj = _translate__isiscomm_isisGlobalStat(input_yang_obj.isisGlobalStat, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_isiscomm(input_yang_obj: huawei_isiscomm, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-isiscomm

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    print("IETF105 huawei isiscomm script!")
    translated_yang_obj = ietf_routing()
    innerobj = _translate__isiscomm(input_yang_obj.isiscomm, translated_yang_obj)
    xpath = '/a:routing'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
    target_xpath = XPATH(xpath, ns_map)

    return [[translated_yang_obj.routing, target_xpath]]