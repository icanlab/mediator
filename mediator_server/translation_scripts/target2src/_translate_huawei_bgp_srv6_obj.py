from mediator_server.mediator_framework.adaptor import XPATH
from mediator_server.yang_bindings.src_yang_bindings.ietf_105_binding import ietf_routing
from mediator_server.yang_bindings.target_yang_bindings.huawei_bgp_binding_105 import *


def _translate__bgp_bgpcomm_bgpSite(input_yang_obj: yc_bgpSite_huawei_bgp__bgp_bgpcomm_bgpSite, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpSite

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
    
    if input_yang_obj.bgpVersion._changed():
        input_yang_obj.bgpVersion = input_yang_obj.bgpVersion
        
    if input_yang_obj.bgpEnable._changed():
        input_yang_obj.bgpEnable = input_yang_obj.bgpEnable

    translated_yang_obj.bgp.global_.as_ = 100

    if input_yang_obj.asNumber._changed():
        input_yang_obj.asNumber = input_yang_obj.asNumber

    if input_yang_obj.gracefulRestart._changed():
        input_yang_obj.gracefulRestart = input_yang_obj.gracefulRestart
        
    if input_yang_obj.timeWaitForRib._changed():
        input_yang_obj.timeWaitForRib = input_yang_obj.timeWaitForRib
        
    if input_yang_obj.asPathLimit._changed():
        input_yang_obj.asPathLimit = input_yang_obj.asPathLimit
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    if input_yang_obj.confedIdNumber._changed():
        input_yang_obj.confedIdNumber = input_yang_obj.confedIdNumber
        
    if input_yang_obj.confedNonstanded._changed():
        input_yang_obj.confedNonstanded = input_yang_obj.confedNonstanded
        
    if input_yang_obj.bgpRidAutoSel._changed():
        input_yang_obj.bgpRidAutoSel = input_yang_obj.bgpRidAutoSel
        
    if input_yang_obj.keepAllRoutes._changed():
        input_yang_obj.keepAllRoutes = input_yang_obj.keepAllRoutes
        
    if input_yang_obj.memoryLimit._changed():
        input_yang_obj.memoryLimit = input_yang_obj.memoryLimit
        
    if input_yang_obj.grPeerReset._changed():
        input_yang_obj.grPeerReset = input_yang_obj.grPeerReset
        
    if input_yang_obj.isShutdown._changed():
        input_yang_obj.isShutdown = input_yang_obj.isShutdown
        
    if input_yang_obj.pathAttrErrCap._changed():
        input_yang_obj.pathAttrErrCap = input_yang_obj.pathAttrErrCap
        
    if input_yang_obj.suppressInterval._changed():
        input_yang_obj.suppressInterval = input_yang_obj.suppressInterval
        
    if input_yang_obj.holdInterval._changed():
        input_yang_obj.holdInterval = input_yang_obj.holdInterval
        
    if input_yang_obj.clearInterval._changed():
        input_yang_obj.clearInterval = input_yang_obj.clearInterval
        
    if input_yang_obj.restartTime._changed():
        input_yang_obj.restartTime = input_yang_obj.restartTime
        
    if input_yang_obj.lowestPriority._changed():
        input_yang_obj.lowestPriority = input_yang_obj.lowestPriority
        
    if input_yang_obj.delayTime._changed():
        input_yang_obj.delayTime = input_yang_obj.delayTime
        
    if input_yang_obj.localIfnetMtu._changed():
        input_yang_obj.localIfnetMtu = input_yang_obj.localIfnetMtu
        
    if input_yang_obj.private4byteAs._changed():
        input_yang_obj.private4byteAs = input_yang_obj.private4byteAs
        
    if input_yang_obj.localCrossNoMed._changed():
        input_yang_obj.localCrossNoMed = input_yang_obj.localCrossNoMed
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers_peerMember(input_yang_obj: yc_peerMember_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers_peerMember, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup/peerMembers/peerMember

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

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers(input_yang_obj: yc_peerMembers_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup/peerMembers

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
    
    for k, listInst in input_yang_obj.peerMember.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers_peerMember(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupBfd(input_yang_obj: yc_peerGroupBfd_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupBfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup/peerGroupBfd

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
    
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.isBfdEnable._changed():
        input_yang_obj.isBfdEnable = input_yang_obj.isBfdEnable
        
    if input_yang_obj.rxInterval._changed():
        input_yang_obj.rxInterval = input_yang_obj.rxInterval
        
    if input_yang_obj.txInterval._changed():
        input_yang_obj.txInterval = input_yang_obj.txInterval
        
    if input_yang_obj.isSingleHop._changed():
        input_yang_obj.isSingleHop = input_yang_obj.isSingleHop
        
    if input_yang_obj.bfdCompatible._changed():
        input_yang_obj.bfdCompatible = input_yang_obj.bfdCompatible
        
    if input_yang_obj.perLinkEcho._changed():
        input_yang_obj.perLinkEcho = input_yang_obj.perLinkEcho
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys_peerGroupSslPolicy(input_yang_obj: yc_peerGroupSslPolicy_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys_peerGroupSslPolicy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup/peerGroupSslPolicys/peerGroupSslPolicy

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
    
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.sslCertificate._changed():
        input_yang_obj.sslCertificate = input_yang_obj.sslCertificate
        
    if input_yang_obj.sslPolicyName._changed():
        input_yang_obj.sslPolicyName = input_yang_obj.sslPolicyName
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys(input_yang_obj: yc_peerGroupSslPolicys_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup/peerGroupSslPolicys

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
    
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys_peerGroupSslPolicy(input_yang_obj.peerGroupSslPolicy, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup(input_yang_obj: yc_bgpPeerGroup_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups/bgpPeerGroup

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
    
    if input_yang_obj.groupType._changed():
        input_yang_obj.groupType = input_yang_obj.groupType
        
    if input_yang_obj.groupAs._changed():
        input_yang_obj.groupAs = input_yang_obj.groupAs
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.fakeAs._changed():
        input_yang_obj.fakeAs = input_yang_obj.fakeAs
        
    if input_yang_obj.dualAs._changed():
        input_yang_obj.dualAs = input_yang_obj.dualAs
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.routeRefresh._changed():
        input_yang_obj.routeRefresh = input_yang_obj.routeRefresh
        
    if input_yang_obj.fourByteAs._changed():
        input_yang_obj.fourByteAs = input_yang_obj.fourByteAs
        
    if input_yang_obj.isIgnore._changed():
        input_yang_obj.isIgnore = input_yang_obj.isIgnore
        
    if input_yang_obj.localIfName._changed():
        input_yang_obj.localIfName = input_yang_obj.localIfName
        
    if input_yang_obj.localIfAddress._changed():
        input_yang_obj.localIfAddress = input_yang_obj.localIfAddress
        
    if input_yang_obj.ebgpMaxHop._changed():
        input_yang_obj.ebgpMaxHop = input_yang_obj.ebgpMaxHop
        
    if input_yang_obj.validTtlHops._changed():
        input_yang_obj.validTtlHops = input_yang_obj.validTtlHops
        
    if input_yang_obj.connectMode._changed():
        input_yang_obj.connectMode = input_yang_obj.connectMode
        
    if input_yang_obj.isLogChange._changed():
        input_yang_obj.isLogChange = input_yang_obj.isLogChange
        
    if input_yang_obj.pswdType._changed():
        input_yang_obj.pswdType = input_yang_obj.pswdType
        
    if input_yang_obj.pswdCipherText._changed():
        input_yang_obj.pswdCipherText = input_yang_obj.pswdCipherText
        
    if input_yang_obj.keepAliveTime._changed():
        input_yang_obj.keepAliveTime = input_yang_obj.keepAliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.pathMTUD._changed():
        input_yang_obj.pathMTUD = input_yang_obj.pathMTUD
        
    if input_yang_obj.trackingEnable._changed():
        input_yang_obj.trackingEnable = input_yang_obj.trackingEnable
        
    if input_yang_obj.trackDelayTime._changed():
        input_yang_obj.trackDelayTime = input_yang_obj.trackDelayTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.tcpMSS._changed():
        input_yang_obj.tcpMSS = input_yang_obj.tcpMSS
        
    if input_yang_obj.mplsLocalIfnetDisable._changed():
        input_yang_obj.mplsLocalIfnetDisable = input_yang_obj.mplsLocalIfnetDisable
        
    if input_yang_obj.prependGlobalAs._changed():
        input_yang_obj.prependGlobalAs = input_yang_obj.prependGlobalAs
        
    if input_yang_obj.prependFakeAs._changed():
        input_yang_obj.prependFakeAs = input_yang_obj.prependFakeAs
        
    if input_yang_obj.pathAttrDiscardIdMap._changed():
        input_yang_obj.pathAttrDiscardIdMap = input_yang_obj.pathAttrDiscardIdMap
        
    if input_yang_obj.pathAttrWithdrawIdMap._changed():
        input_yang_obj.pathAttrWithdrawIdMap = input_yang_obj.pathAttrWithdrawIdMap
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerMembers(input_yang_obj.peerMembers, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupBfd(input_yang_obj.peerGroupBfd, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup_peerGroupSslPolicys(input_yang_obj.peerGroupSslPolicys, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups(input_yang_obj: yc_bgpPeerGroups_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeerGroups

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
    
    for k, listInst in input_yang_obj.bgpPeerGroup.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups_bgpPeerGroup(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos_peerLogInfo(input_yang_obj: yc_peerLogInfo_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos_peerLogInfo, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/peerLogInfos/peerLogInfo

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
    
    if input_yang_obj.stateEvent._changed():
        input_yang_obj.stateEvent = input_yang_obj.stateEvent
        
    if input_yang_obj.errorCode._changed():
        input_yang_obj.errorCode = input_yang_obj.errorCode
        
    if input_yang_obj.errorSubCode._changed():
        input_yang_obj.errorSubCode = input_yang_obj.errorSubCode
        
    if input_yang_obj.notification._changed():
        input_yang_obj.notification = input_yang_obj.notification
        
    if input_yang_obj.logDateTime._changed():
        input_yang_obj.logDateTime = input_yang_obj.logDateTime
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos(input_yang_obj: yc_peerLogInfos_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/peerLogInfos

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
    
    for k, listInst in input_yang_obj.peerLogInfo.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos_peerLogInfo(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerBfd(input_yang_obj: yc_peerBfd_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerBfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/peerBfd

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
    
    if input_yang_obj.isBfdBlock._changed():
        input_yang_obj.isBfdBlock = input_yang_obj.isBfdBlock
        
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.isBfdEnable._changed():
        input_yang_obj.isBfdEnable = input_yang_obj.isBfdEnable
        
    if input_yang_obj.rxInterval._changed():
        input_yang_obj.rxInterval = input_yang_obj.rxInterval
        
    if input_yang_obj.txInterval._changed():
        input_yang_obj.txInterval = input_yang_obj.txInterval
        
    if input_yang_obj.isSingleHop._changed():
        input_yang_obj.isSingleHop = input_yang_obj.isSingleHop
        
    if input_yang_obj.bfdCompatible._changed():
        input_yang_obj.bfdCompatible = input_yang_obj.bfdCompatible
        
    if input_yang_obj.perLinkEcho._changed():
        input_yang_obj.perLinkEcho = input_yang_obj.perLinkEcho
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces_relyStateInterface(input_yang_obj: yc_relyStateInterface_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces_relyStateInterface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/relyStateInterfaces/relyStateInterface

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

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces(input_yang_obj: yc_relyStateInterfaces_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/relyStateInterfaces

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
    
    for k, listInst in input_yang_obj.relyStateInterface.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces_relyStateInterface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys_peerSslPolicy(input_yang_obj: yc_peerSslPolicy_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys_peerSslPolicy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/peerSslPolicys/peerSslPolicy

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
    
    if input_yang_obj.role._changed():
        input_yang_obj.role = input_yang_obj.role
        
    if input_yang_obj.effectRole._changed():
        input_yang_obj.effectRole = input_yang_obj.effectRole
        
    if input_yang_obj.sslCertificate._changed():
        input_yang_obj.sslCertificate = input_yang_obj.sslCertificate
        
    if input_yang_obj.effectSslCertificate._changed():
        input_yang_obj.effectSslCertificate = input_yang_obj.effectSslCertificate
        
    if input_yang_obj.configSslPolicyName._changed():
        input_yang_obj.configSslPolicyName = input_yang_obj.configSslPolicyName
        
    if input_yang_obj.effectSslPolicyName._changed():
        input_yang_obj.effectSslPolicyName = input_yang_obj.effectSslPolicyName
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys(input_yang_obj: yc_peerSslPolicys_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer/peerSslPolicys

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
    
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys_peerSslPolicy(input_yang_obj.peerSslPolicy, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer(input_yang_obj: yc_bgpPeer_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers/bgpPeer

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
    
    if input_yang_obj.groupName._changed():
        input_yang_obj.groupName = input_yang_obj.groupName
        
    if input_yang_obj.remoteAs._changed():
        input_yang_obj.remoteAs = input_yang_obj.remoteAs
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.fakeAs._changed():
        input_yang_obj.fakeAs = input_yang_obj.fakeAs
        
    if input_yang_obj.dualAs._changed():
        input_yang_obj.dualAs = input_yang_obj.dualAs
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.routeRefresh._changed():
        input_yang_obj.routeRefresh = input_yang_obj.routeRefresh
        
    if input_yang_obj.fourByteAs._changed():
        input_yang_obj.fourByteAs = input_yang_obj.fourByteAs
        
    if input_yang_obj.isIgnore._changed():
        input_yang_obj.isIgnore = input_yang_obj.isIgnore
        
    if input_yang_obj.localIfName._changed():
        input_yang_obj.localIfName = input_yang_obj.localIfName
        
    if input_yang_obj.localIfAddress._changed():
        input_yang_obj.localIfAddress = input_yang_obj.localIfAddress
        
    if input_yang_obj.ebgpMaxHop._changed():
        input_yang_obj.ebgpMaxHop = input_yang_obj.ebgpMaxHop
        
    if input_yang_obj.validTtlHops._changed():
        input_yang_obj.validTtlHops = input_yang_obj.validTtlHops
        
    if input_yang_obj.connectMode._changed():
        input_yang_obj.connectMode = input_yang_obj.connectMode
        
    if input_yang_obj.isLogChange._changed():
        input_yang_obj.isLogChange = input_yang_obj.isLogChange
        
    if input_yang_obj.pswdType._changed():
        input_yang_obj.pswdType = input_yang_obj.pswdType
        
    if input_yang_obj.pswdCipherText._changed():
        input_yang_obj.pswdCipherText = input_yang_obj.pswdCipherText
        
    if input_yang_obj.keepAliveTime._changed():
        input_yang_obj.keepAliveTime = input_yang_obj.keepAliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.pathMTUD._changed():
        input_yang_obj.pathMTUD = input_yang_obj.pathMTUD
        
    if input_yang_obj.trackingEnable._changed():
        input_yang_obj.trackingEnable = input_yang_obj.trackingEnable
        
    if input_yang_obj.trackDelayTime._changed():
        input_yang_obj.trackDelayTime = input_yang_obj.trackDelayTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.tcpMSS._changed():
        input_yang_obj.tcpMSS = input_yang_obj.tcpMSS
        
    if input_yang_obj.mplsLocalIfnetDisable._changed():
        input_yang_obj.mplsLocalIfnetDisable = input_yang_obj.mplsLocalIfnetDisable
        
    if input_yang_obj.prependGlobalAs._changed():
        input_yang_obj.prependGlobalAs = input_yang_obj.prependGlobalAs
        
    if input_yang_obj.prependFakeAs._changed():
        input_yang_obj.prependFakeAs = input_yang_obj.prependFakeAs
        
    if input_yang_obj.pathAttrDiscardIdMap._changed():
        input_yang_obj.pathAttrDiscardIdMap = input_yang_obj.pathAttrDiscardIdMap
        
    if input_yang_obj.pathAttrWithdrawIdMap._changed():
        input_yang_obj.pathAttrWithdrawIdMap = input_yang_obj.pathAttrWithdrawIdMap
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    if input_yang_obj.egressEngineer._changed():
        input_yang_obj.egressEngineer = input_yang_obj.egressEngineer
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerLogInfos(input_yang_obj.peerLogInfos, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerBfd(input_yang_obj.peerBfd, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_relyStateInterfaces(input_yang_obj.relyStateInterfaces, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer_peerSslPolicys(input_yang_obj.peerSslPolicys, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers(input_yang_obj: yc_bgpPeers_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpPeers

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
    
    for k, listInst in input_yang_obj.bgpPeer.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers_bgpPeer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators_locator(input_yang_obj: yc_locator_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators_locator, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpVrfAFs/bgpVrfAF/locators/locator

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
    
    if input_yang_obj.autoSid._changed():
        input_yang_obj.autoSid = input_yang_obj.autoSid
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators(input_yang_obj: yc_locators_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpVrfAFs/bgpVrfAF/locators

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
    
    for k, listInst in input_yang_obj.locator.iteritems():
        translated_yang_obj.ipv4_unicast.segment_routing.srv6.sid_alloc_mode = k
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators_locator(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF(input_yang_obj: yc_bgpVrfAF_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpVrfAFs/bgpVrfAF

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
    
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF_locators(input_yang_obj.locators, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs(input_yang_obj: yc_bgpVrfAFs_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf/bgpVrfAFs

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
    
    for k, listInst in input_yang_obj.bgpVrfAF.iteritems():
        afi_safi_obj = translated_yang_obj
        if k == "ipv4uni":
            afi_safi_obj = translated_yang_obj.bgp.global_.afi_safis.afi_safi.add("ipv4-unicast")
            afi_safi_obj.enabled = "true"
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs_bgpVrfAF(listInst, afi_safi_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs_bgpVrf(input_yang_obj: yc_bgpVrf_huawei_bgp__bgp_bgpcomm_bgpVrfs_bgpVrf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs/bgpVrf

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
    
    if input_yang_obj.vrfSession._changed():
        input_yang_obj.vrfSession = input_yang_obj.vrfSession
        
    if input_yang_obj.vrfRidAutoSel._changed():
        input_yang_obj.vrfRidAutoSel = input_yang_obj.vrfRidAutoSel
        
    if input_yang_obj.routerId._changed():
        input_yang_obj.routerId = input_yang_obj.routerId
        
    if input_yang_obj.effectRouterId._changed():
        input_yang_obj.effectRouterId = input_yang_obj.effectRouterId
        
    if input_yang_obj.keepaliveTime._changed():
        input_yang_obj.keepaliveTime = input_yang_obj.keepaliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.defaultAfType._changed():
        input_yang_obj.defaultAfType = input_yang_obj.defaultAfType
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeerGroups(input_yang_obj.bgpPeerGroups, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpPeers(input_yang_obj.bgpPeers, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf_bgpVrfAFs(input_yang_obj.bgpVrfAFs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm_bgpVrfs(input_yang_obj: yc_bgpVrfs_huawei_bgp__bgp_bgpcomm_bgpVrfs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm/bgpVrfs

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
    
    for k, listInst in input_yang_obj.bgpVrf.iteritems():
        innerobj = _translate__bgp_bgpcomm_bgpVrfs_bgpVrf(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpcomm(input_yang_obj: yc_bgpcomm_huawei_bgp__bgp_bgpcomm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpcomm

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
    
    innerobj = _translate__bgp_bgpcomm_bgpSite(input_yang_obj.bgpSite, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpcomm_bgpVrfs(input_yang_obj.bgpVrfs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiSites_bgpMultiSite(input_yang_obj: yc_bgpMultiSite_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiSites_bgpMultiSite, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiSites/bgpMultiSite

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
    
    if input_yang_obj.bgpVersion._changed():
        input_yang_obj.bgpVersion = input_yang_obj.bgpVersion
        
    if input_yang_obj.asNumber._changed():
        input_yang_obj.asNumber = input_yang_obj.asNumber
        
    if input_yang_obj.gracefulRestart._changed():
        input_yang_obj.gracefulRestart = input_yang_obj.gracefulRestart
        
    if input_yang_obj.timeWaitForRib._changed():
        input_yang_obj.timeWaitForRib = input_yang_obj.timeWaitForRib
        
    if input_yang_obj.asPathLimit._changed():
        input_yang_obj.asPathLimit = input_yang_obj.asPathLimit
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    if input_yang_obj.confedIdNumber._changed():
        input_yang_obj.confedIdNumber = input_yang_obj.confedIdNumber
        
    if input_yang_obj.confedNonstanded._changed():
        input_yang_obj.confedNonstanded = input_yang_obj.confedNonstanded
        
    if input_yang_obj.bgpRidAutoSel._changed():
        input_yang_obj.bgpRidAutoSel = input_yang_obj.bgpRidAutoSel
        
    if input_yang_obj.keepAllRoutes._changed():
        input_yang_obj.keepAllRoutes = input_yang_obj.keepAllRoutes
        
    if input_yang_obj.memoryLimit._changed():
        input_yang_obj.memoryLimit = input_yang_obj.memoryLimit
        
    if input_yang_obj.grPeerReset._changed():
        input_yang_obj.grPeerReset = input_yang_obj.grPeerReset
        
    if input_yang_obj.isShutdown._changed():
        input_yang_obj.isShutdown = input_yang_obj.isShutdown
        
    if input_yang_obj.suppressInterval._changed():
        input_yang_obj.suppressInterval = input_yang_obj.suppressInterval
        
    if input_yang_obj.holdInterval._changed():
        input_yang_obj.holdInterval = input_yang_obj.holdInterval
        
    if input_yang_obj.clearInterval._changed():
        input_yang_obj.clearInterval = input_yang_obj.clearInterval
        
    if input_yang_obj.private4byteAs._changed():
        input_yang_obj.private4byteAs = input_yang_obj.private4byteAs
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiSites(input_yang_obj: yc_bgpMultiSites_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiSites, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiSites

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
    
    for k, listInst in input_yang_obj.bgpMultiSite.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiSites_bgpMultiSite(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup_peerGroupBfd(input_yang_obj: yc_peerGroupBfd_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup_peerGroupBfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeerGroups/bgpMultiPeerGroup/peerGroupBfd

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
    
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.isBfdEnable._changed():
        input_yang_obj.isBfdEnable = input_yang_obj.isBfdEnable
        
    if input_yang_obj.rxInterval._changed():
        input_yang_obj.rxInterval = input_yang_obj.rxInterval
        
    if input_yang_obj.txInterval._changed():
        input_yang_obj.txInterval = input_yang_obj.txInterval
        
    if input_yang_obj.isSingleHop._changed():
        input_yang_obj.isSingleHop = input_yang_obj.isSingleHop
        
    if input_yang_obj.bfdCompatible._changed():
        input_yang_obj.bfdCompatible = input_yang_obj.bfdCompatible
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup(input_yang_obj: yc_bgpMultiPeerGroup_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeerGroups/bgpMultiPeerGroup

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
    
    if input_yang_obj.groupType._changed():
        input_yang_obj.groupType = input_yang_obj.groupType
        
    if input_yang_obj.groupAs._changed():
        input_yang_obj.groupAs = input_yang_obj.groupAs
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.fakeAs._changed():
        input_yang_obj.fakeAs = input_yang_obj.fakeAs
        
    if input_yang_obj.dualAs._changed():
        input_yang_obj.dualAs = input_yang_obj.dualAs
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.routeRefresh._changed():
        input_yang_obj.routeRefresh = input_yang_obj.routeRefresh
        
    if input_yang_obj.fourByteAs._changed():
        input_yang_obj.fourByteAs = input_yang_obj.fourByteAs
        
    if input_yang_obj.isIgnore._changed():
        input_yang_obj.isIgnore = input_yang_obj.isIgnore
        
    if input_yang_obj.localIfName._changed():
        input_yang_obj.localIfName = input_yang_obj.localIfName
        
    if input_yang_obj.localIfAddress._changed():
        input_yang_obj.localIfAddress = input_yang_obj.localIfAddress
        
    if input_yang_obj.ebgpMaxHop._changed():
        input_yang_obj.ebgpMaxHop = input_yang_obj.ebgpMaxHop
        
    if input_yang_obj.validTtlHops._changed():
        input_yang_obj.validTtlHops = input_yang_obj.validTtlHops
        
    if input_yang_obj.connectMode._changed():
        input_yang_obj.connectMode = input_yang_obj.connectMode
        
    if input_yang_obj.isLogChange._changed():
        input_yang_obj.isLogChange = input_yang_obj.isLogChange
        
    if input_yang_obj.pswdType._changed():
        input_yang_obj.pswdType = input_yang_obj.pswdType
        
    if input_yang_obj.pswdCipherText._changed():
        input_yang_obj.pswdCipherText = input_yang_obj.pswdCipherText
        
    if input_yang_obj.keepAliveTime._changed():
        input_yang_obj.keepAliveTime = input_yang_obj.keepAliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.trackingEnable._changed():
        input_yang_obj.trackingEnable = input_yang_obj.trackingEnable
        
    if input_yang_obj.trackDelayTime._changed():
        input_yang_obj.trackDelayTime = input_yang_obj.trackDelayTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.tcpMSS._changed():
        input_yang_obj.tcpMSS = input_yang_obj.tcpMSS
        
    if input_yang_obj.mplsLocalIfnetDisable._changed():
        input_yang_obj.mplsLocalIfnetDisable = input_yang_obj.mplsLocalIfnetDisable
        
    if input_yang_obj.prependGlobalAs._changed():
        input_yang_obj.prependGlobalAs = input_yang_obj.prependGlobalAs
        
    if input_yang_obj.prependFakeAs._changed():
        input_yang_obj.prependFakeAs = input_yang_obj.prependFakeAs
        
    if input_yang_obj.pathAttrDiscardIdMap._changed():
        input_yang_obj.pathAttrDiscardIdMap = input_yang_obj.pathAttrDiscardIdMap
        
    if input_yang_obj.pathAttrWithdrawIdMap._changed():
        input_yang_obj.pathAttrWithdrawIdMap = input_yang_obj.pathAttrWithdrawIdMap
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup_peerGroupBfd(input_yang_obj.peerGroupBfd, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups(input_yang_obj: yc_bgpMultiPeerGroups_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeerGroups

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
    
    for k, listInst in input_yang_obj.bgpMultiPeerGroup.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups_bgpMultiPeerGroup(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer_peerBfd(input_yang_obj: yc_peerBfd_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer_peerBfd, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeers/bgpMultiPeer/peerBfd

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
    
    if input_yang_obj.isBfdBlock._changed():
        input_yang_obj.isBfdBlock = input_yang_obj.isBfdBlock
        
    if input_yang_obj.multiplier._changed():
        input_yang_obj.multiplier = input_yang_obj.multiplier
        
    if input_yang_obj.isBfdEnable._changed():
        input_yang_obj.isBfdEnable = input_yang_obj.isBfdEnable
        
    if input_yang_obj.rxInterval._changed():
        input_yang_obj.rxInterval = input_yang_obj.rxInterval
        
    if input_yang_obj.txInterval._changed():
        input_yang_obj.txInterval = input_yang_obj.txInterval
        
    if input_yang_obj.isSingleHop._changed():
        input_yang_obj.isSingleHop = input_yang_obj.isSingleHop
        
    if input_yang_obj.bfdCompatible._changed():
        input_yang_obj.bfdCompatible = input_yang_obj.bfdCompatible
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer(input_yang_obj: yc_bgpMultiPeer_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeers/bgpMultiPeer

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
    
    if input_yang_obj.groupName._changed():
        input_yang_obj.groupName = input_yang_obj.groupName
        
    if input_yang_obj.remoteAs._changed():
        input_yang_obj.remoteAs = input_yang_obj.remoteAs
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.fakeAs._changed():
        input_yang_obj.fakeAs = input_yang_obj.fakeAs
        
    if input_yang_obj.dualAs._changed():
        input_yang_obj.dualAs = input_yang_obj.dualAs
        
    if input_yang_obj.conventional._changed():
        input_yang_obj.conventional = input_yang_obj.conventional
        
    if input_yang_obj.routeRefresh._changed():
        input_yang_obj.routeRefresh = input_yang_obj.routeRefresh
        
    if input_yang_obj.fourByteAs._changed():
        input_yang_obj.fourByteAs = input_yang_obj.fourByteAs
        
    if input_yang_obj.isIgnore._changed():
        input_yang_obj.isIgnore = input_yang_obj.isIgnore
        
    if input_yang_obj.localIfName._changed():
        input_yang_obj.localIfName = input_yang_obj.localIfName
        
    if input_yang_obj.localIfAddress._changed():
        input_yang_obj.localIfAddress = input_yang_obj.localIfAddress
        
    if input_yang_obj.ebgpMaxHop._changed():
        input_yang_obj.ebgpMaxHop = input_yang_obj.ebgpMaxHop
        
    if input_yang_obj.validTtlHops._changed():
        input_yang_obj.validTtlHops = input_yang_obj.validTtlHops
        
    if input_yang_obj.connectMode._changed():
        input_yang_obj.connectMode = input_yang_obj.connectMode
        
    if input_yang_obj.isLogChange._changed():
        input_yang_obj.isLogChange = input_yang_obj.isLogChange
        
    if input_yang_obj.pswdType._changed():
        input_yang_obj.pswdType = input_yang_obj.pswdType
        
    if input_yang_obj.pswdCipherText._changed():
        input_yang_obj.pswdCipherText = input_yang_obj.pswdCipherText
        
    if input_yang_obj.keepAliveTime._changed():
        input_yang_obj.keepAliveTime = input_yang_obj.keepAliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.checkFirstAs._changed():
        input_yang_obj.checkFirstAs = input_yang_obj.checkFirstAs
        
    if input_yang_obj.keyChainName._changed():
        input_yang_obj.keyChainName = input_yang_obj.keyChainName
        
    if input_yang_obj.trackingEnable._changed():
        input_yang_obj.trackingEnable = input_yang_obj.trackingEnable
        
    if input_yang_obj.trackDelayTime._changed():
        input_yang_obj.trackDelayTime = input_yang_obj.trackDelayTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.tcpMSS._changed():
        input_yang_obj.tcpMSS = input_yang_obj.tcpMSS
        
    if input_yang_obj.mplsLocalIfnetDisable._changed():
        input_yang_obj.mplsLocalIfnetDisable = input_yang_obj.mplsLocalIfnetDisable
        
    if input_yang_obj.prependGlobalAs._changed():
        input_yang_obj.prependGlobalAs = input_yang_obj.prependGlobalAs
        
    if input_yang_obj.prependFakeAs._changed():
        input_yang_obj.prependFakeAs = input_yang_obj.prependFakeAs
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer_peerBfd(input_yang_obj.peerBfd, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers(input_yang_obj: yc_bgpMultiPeers_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiPeers

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
    
    for k, listInst in input_yang_obj.bgpMultiPeer.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers_bgpMultiPeer(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres_peerGroupAFCraPre(input_yang_obj: yc_peerGroupAFCraPre_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres_peerGroupAFCraPre, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs/peerGroupAF/peerGroupAFCraPres/peerGroupAFCraPre

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

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres(input_yang_obj: yc_peerGroupAFCraPres_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs/peerGroupAF/peerGroupAFCraPres

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
    
    for k, listInst in input_yang_obj.peerGroupAFCraPre.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres_peerGroupAFCraPre(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers_peerAFMember(input_yang_obj: yc_peerAFMember_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers_peerAFMember, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs/peerGroupAF/peerAFMembers/peerAFMember

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

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers(input_yang_obj: yc_peerAFMembers_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs/peerGroupAF/peerAFMembers

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
    
    for k, listInst in input_yang_obj.peerAFMember.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers_peerAFMember(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF(input_yang_obj: yc_peerGroupAF_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs/peerGroupAF

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
    
    if input_yang_obj.groupType._changed():
        input_yang_obj.groupType = input_yang_obj.groupType
        
    if input_yang_obj.advertiseRemoteNexthop._changed():
        input_yang_obj.advertiseRemoteNexthop = input_yang_obj.advertiseRemoteNexthop
        
    if input_yang_obj.advertiseCommunity._changed():
        input_yang_obj.advertiseCommunity = input_yang_obj.advertiseCommunity
        
    if input_yang_obj.advertiseExtCommunity._changed():
        input_yang_obj.advertiseExtCommunity = input_yang_obj.advertiseExtCommunity
        
    if input_yang_obj.discardExtCommunity._changed():
        input_yang_obj.discardExtCommunity = input_yang_obj.discardExtCommunity
        
    if input_yang_obj.allowAsLoopEnable._changed():
        input_yang_obj.allowAsLoopEnable = input_yang_obj.allowAsLoopEnable
        
    if input_yang_obj.allowAsLoopLimit._changed():
        input_yang_obj.allowAsLoopLimit = input_yang_obj.allowAsLoopLimit
        
    if input_yang_obj.keepAllRoutes._changed():
        input_yang_obj.keepAllRoutes = input_yang_obj.keepAllRoutes
        
    if input_yang_obj.nextHopConfigure._changed():
        input_yang_obj.nextHopConfigure = input_yang_obj.nextHopConfigure
        
    if input_yang_obj.preferredValue._changed():
        input_yang_obj.preferredValue = input_yang_obj.preferredValue
        
    if input_yang_obj.publicAsOnly._changed():
        input_yang_obj.publicAsOnly = input_yang_obj.publicAsOnly
        
    if input_yang_obj.publicAsOnlyForce._changed():
        input_yang_obj.publicAsOnlyForce = input_yang_obj.publicAsOnlyForce
        
    if input_yang_obj.publicAsOnlyLimited._changed():
        input_yang_obj.publicAsOnlyLimited = input_yang_obj.publicAsOnlyLimited
        
    if input_yang_obj.publicAsOnlyReplace._changed():
        input_yang_obj.publicAsOnlyReplace = input_yang_obj.publicAsOnlyReplace
        
    if input_yang_obj.publicAsOnlySkipPeerAs._changed():
        input_yang_obj.publicAsOnlySkipPeerAs = input_yang_obj.publicAsOnlySkipPeerAs
        
    if input_yang_obj.routeLimit._changed():
        input_yang_obj.routeLimit = input_yang_obj.routeLimit
        
    if input_yang_obj.routeLimitPercent._changed():
        input_yang_obj.routeLimitPercent = input_yang_obj.routeLimitPercent
        
    if input_yang_obj.routeLimitType._changed():
        input_yang_obj.routeLimitType = input_yang_obj.routeLimitType
        
    if input_yang_obj.routeLimitIdleTimeout._changed():
        input_yang_obj.routeLimitIdleTimeout = input_yang_obj.routeLimitIdleTimeout
        
    if input_yang_obj.rtUpdtInterval._changed():
        input_yang_obj.rtUpdtInterval = input_yang_obj.rtUpdtInterval
        
    if input_yang_obj.reflectClient._changed():
        input_yang_obj.reflectClient = input_yang_obj.reflectClient
        
    if input_yang_obj.substituteAsEnable._changed():
        input_yang_obj.substituteAsEnable = input_yang_obj.substituteAsEnable
        
    if input_yang_obj.importRtPolicyName._changed():
        input_yang_obj.importRtPolicyName = input_yang_obj.importRtPolicyName
        
    if input_yang_obj.exportRtPolicyName._changed():
        input_yang_obj.exportRtPolicyName = input_yang_obj.exportRtPolicyName
        
    if input_yang_obj.importPrefFiltName._changed():
        input_yang_obj.importPrefFiltName = input_yang_obj.importPrefFiltName
        
    if input_yang_obj.exportPrefFiltName._changed():
        input_yang_obj.exportPrefFiltName = input_yang_obj.exportPrefFiltName
        
    if input_yang_obj.importAsPathNameOrNum._changed():
        input_yang_obj.importAsPathNameOrNum = input_yang_obj.importAsPathNameOrNum
        
    if input_yang_obj.exportAsPathNameOrNum._changed():
        input_yang_obj.exportAsPathNameOrNum = input_yang_obj.exportAsPathNameOrNum
        
    if input_yang_obj.importAclNameOrNum._changed():
        input_yang_obj.importAclNameOrNum = input_yang_obj.importAclNameOrNum
        
    if input_yang_obj.exportAclNameOrNum._changed():
        input_yang_obj.exportAclNameOrNum = input_yang_obj.exportAclNameOrNum
        
    if input_yang_obj.ipprefixOrfEnable._changed():
        input_yang_obj.ipprefixOrfEnable = input_yang_obj.ipprefixOrfEnable
        
    if input_yang_obj.isNonstdIpprefixMod._changed():
        input_yang_obj.isNonstdIpprefixMod = input_yang_obj.isNonstdIpprefixMod
        
    if input_yang_obj.orftype._changed():
        input_yang_obj.orftype = input_yang_obj.orftype
        
    if input_yang_obj.orfMode._changed():
        input_yang_obj.orfMode = input_yang_obj.orfMode
        
    if input_yang_obj.soostring._changed():
        input_yang_obj.soostring = input_yang_obj.soostring
        
    if input_yang_obj.defaultRtAdvEnable._changed():
        input_yang_obj.defaultRtAdvEnable = input_yang_obj.defaultRtAdvEnable
        
    if input_yang_obj.defaultRtAdvPolicy._changed():
        input_yang_obj.defaultRtAdvPolicy = input_yang_obj.defaultRtAdvPolicy
        
    if input_yang_obj.defaultRtMatchMode._changed():
        input_yang_obj.defaultRtMatchMode = input_yang_obj.defaultRtMatchMode
        
    if input_yang_obj.labelRouteCapability._changed():
        input_yang_obj.labelRouteCapability = input_yang_obj.labelRouteCapability
        
    if input_yang_obj.addPathMode._changed():
        input_yang_obj.addPathMode = input_yang_obj.addPathMode
        
    if input_yang_obj.advAddPathNum._changed():
        input_yang_obj.advAddPathNum = input_yang_obj.advAddPathNum
        
    if input_yang_obj.originAsValid._changed():
        input_yang_obj.originAsValid = input_yang_obj.originAsValid
        
    if input_yang_obj.updatePktStandardCompatible._changed():
        input_yang_obj.updatePktStandardCompatible = input_yang_obj.updatePktStandardCompatible
        
    if input_yang_obj.advertiseIrb._changed():
        input_yang_obj.advertiseIrb = input_yang_obj.advertiseIrb
        
    if input_yang_obj.advertiseArp._changed():
        input_yang_obj.advertiseArp = input_yang_obj.advertiseArp
        
    if input_yang_obj.splitGroupName._changed():
        input_yang_obj.splitGroupName = input_yang_obj.splitGroupName
        
    if input_yang_obj.advertiseIrbv6._changed():
        input_yang_obj.advertiseIrbv6 = input_yang_obj.advertiseIrbv6
        
    if input_yang_obj.advertiseND._changed():
        input_yang_obj.advertiseND = input_yang_obj.advertiseND
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerGroupAFCraPres(input_yang_obj.peerGroupAFCraPres, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF_peerAFMembers(input_yang_obj.peerAFMembers, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs(input_yang_obj: yc_peerGroupAFs_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerGroupAFs

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
    
    for k, listInst in input_yang_obj.peerGroupAF.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs_peerGroupAF(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres_peerAFCraPre(input_yang_obj: yc_peerAFCraPre_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres_peerAFCraPre, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerAFs/peerAF/peerAFCraPres/peerAFCraPre

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

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres(input_yang_obj: yc_peerAFCraPres_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerAFs/peerAF/peerAFCraPres

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
    
    for k, listInst in input_yang_obj.peerAFCraPre.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres_peerAFCraPre(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF(input_yang_obj: yc_peerAF_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerAFs/peerAF

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
    
    if input_yang_obj.peerGroupName._changed():
        input_yang_obj.peerGroupName = input_yang_obj.peerGroupName
        
    if input_yang_obj.labelRouteCapability._changed():
        input_yang_obj.labelRouteCapability = input_yang_obj.labelRouteCapability
        
    if input_yang_obj.advertiseIrb._changed():
        input_yang_obj.advertiseIrb = input_yang_obj.advertiseIrb
        
    if input_yang_obj.advertiseArp._changed():
        input_yang_obj.advertiseArp = input_yang_obj.advertiseArp
        
    if input_yang_obj.advertiseIrbv6._changed():
        input_yang_obj.advertiseIrbv6 = input_yang_obj.advertiseIrbv6
        
    if input_yang_obj.advertiseND._changed():
        input_yang_obj.advertiseND = input_yang_obj.advertiseND
        
    if input_yang_obj.staticGrTimerValue._changed():
        input_yang_obj.staticGrTimerValue = input_yang_obj.staticGrTimerValue
        
    if input_yang_obj.advertiseRemoteNexthop._changed():
        input_yang_obj.advertiseRemoteNexthop = input_yang_obj.advertiseRemoteNexthop
        
    if input_yang_obj.advertiseCommunity._changed():
        input_yang_obj.advertiseCommunity = input_yang_obj.advertiseCommunity
        
    if input_yang_obj.advertiseExtCommunity._changed():
        input_yang_obj.advertiseExtCommunity = input_yang_obj.advertiseExtCommunity
        
    if input_yang_obj.discardExtCommunity._changed():
        input_yang_obj.discardExtCommunity = input_yang_obj.discardExtCommunity
        
    if input_yang_obj.allowAsLoopEnable._changed():
        input_yang_obj.allowAsLoopEnable = input_yang_obj.allowAsLoopEnable
        
    if input_yang_obj.allowAsLoopLimit._changed():
        input_yang_obj.allowAsLoopLimit = input_yang_obj.allowAsLoopLimit
        
    if input_yang_obj.keepAllRoutes._changed():
        input_yang_obj.keepAllRoutes = input_yang_obj.keepAllRoutes
        
    if input_yang_obj.nextHopConfigure._changed():
        input_yang_obj.nextHopConfigure = input_yang_obj.nextHopConfigure
        
    if input_yang_obj.preferredValue._changed():
        input_yang_obj.preferredValue = input_yang_obj.preferredValue
        
    if input_yang_obj.publicAsOnly._changed():
        input_yang_obj.publicAsOnly = input_yang_obj.publicAsOnly
        
    if input_yang_obj.publicAsOnlyForce._changed():
        input_yang_obj.publicAsOnlyForce = input_yang_obj.publicAsOnlyForce
        
    if input_yang_obj.publicAsOnlyLimited._changed():
        input_yang_obj.publicAsOnlyLimited = input_yang_obj.publicAsOnlyLimited
        
    if input_yang_obj.publicAsOnlyReplace._changed():
        input_yang_obj.publicAsOnlyReplace = input_yang_obj.publicAsOnlyReplace
        
    if input_yang_obj.publicAsOnlySkipPeerAs._changed():
        input_yang_obj.publicAsOnlySkipPeerAs = input_yang_obj.publicAsOnlySkipPeerAs
        
    if input_yang_obj.routeLimit._changed():
        input_yang_obj.routeLimit = input_yang_obj.routeLimit
        
    if input_yang_obj.routeLimitPercent._changed():
        input_yang_obj.routeLimitPercent = input_yang_obj.routeLimitPercent
        
    if input_yang_obj.routeLimitType._changed():
        input_yang_obj.routeLimitType = input_yang_obj.routeLimitType
        
    if input_yang_obj.routeLimitIdleTimeout._changed():
        input_yang_obj.routeLimitIdleTimeout = input_yang_obj.routeLimitIdleTimeout
        
    if input_yang_obj.rtUpdtInterval._changed():
        input_yang_obj.rtUpdtInterval = input_yang_obj.rtUpdtInterval
        
    if input_yang_obj.redirectIP._changed():
        input_yang_obj.redirectIP = input_yang_obj.redirectIP
        
    if input_yang_obj.redirectIPVaildation._changed():
        input_yang_obj.redirectIPVaildation = input_yang_obj.redirectIPVaildation
        
    if input_yang_obj.reflectClient._changed():
        input_yang_obj.reflectClient = input_yang_obj.reflectClient
        
    if input_yang_obj.substituteAsEnable._changed():
        input_yang_obj.substituteAsEnable = input_yang_obj.substituteAsEnable
        
    if input_yang_obj.importRtPolicyName._changed():
        input_yang_obj.importRtPolicyName = input_yang_obj.importRtPolicyName
        
    if input_yang_obj.exportRtPolicyName._changed():
        input_yang_obj.exportRtPolicyName = input_yang_obj.exportRtPolicyName
        
    if input_yang_obj.importPrefFiltName._changed():
        input_yang_obj.importPrefFiltName = input_yang_obj.importPrefFiltName
        
    if input_yang_obj.exportPrefFiltName._changed():
        input_yang_obj.exportPrefFiltName = input_yang_obj.exportPrefFiltName
        
    if input_yang_obj.importAsPathNameOrNum._changed():
        input_yang_obj.importAsPathNameOrNum = input_yang_obj.importAsPathNameOrNum
        
    if input_yang_obj.exportAsPathNameOrNum._changed():
        input_yang_obj.exportAsPathNameOrNum = input_yang_obj.exportAsPathNameOrNum
        
    if input_yang_obj.importAclNameOrNum._changed():
        input_yang_obj.importAclNameOrNum = input_yang_obj.importAclNameOrNum
        
    if input_yang_obj.exportAclNameOrNum._changed():
        input_yang_obj.exportAclNameOrNum = input_yang_obj.exportAclNameOrNum
        
    if input_yang_obj.ipprefixOrfEnable._changed():
        input_yang_obj.ipprefixOrfEnable = input_yang_obj.ipprefixOrfEnable
        
    if input_yang_obj.isNonstdIpprefixMod._changed():
        input_yang_obj.isNonstdIpprefixMod = input_yang_obj.isNonstdIpprefixMod
        
    if input_yang_obj.orftype._changed():
        input_yang_obj.orftype = input_yang_obj.orftype
        
    if input_yang_obj.orfMode._changed():
        input_yang_obj.orfMode = input_yang_obj.orfMode
        
    if input_yang_obj.soostring._changed():
        input_yang_obj.soostring = input_yang_obj.soostring
        
    if input_yang_obj.defaultRtAdvEnable._changed():
        input_yang_obj.defaultRtAdvEnable = input_yang_obj.defaultRtAdvEnable
        
    if input_yang_obj.defaultRtAdvPolicy._changed():
        input_yang_obj.defaultRtAdvPolicy = input_yang_obj.defaultRtAdvPolicy
        
    if input_yang_obj.defaultRtMatchMode._changed():
        input_yang_obj.defaultRtMatchMode = input_yang_obj.defaultRtMatchMode
        
    if input_yang_obj.addPathMode._changed():
        input_yang_obj.addPathMode = input_yang_obj.addPathMode
        
    if input_yang_obj.advAddPathNum._changed():
        input_yang_obj.advAddPathNum = input_yang_obj.advAddPathNum
        
    if input_yang_obj.originAsValid._changed():
        input_yang_obj.originAsValid = input_yang_obj.originAsValid
        
    if input_yang_obj.updatePktStandardCompatible._changed():
        input_yang_obj.updatePktStandardCompatible = input_yang_obj.updatePktStandardCompatible
        
    if input_yang_obj.reoriginatedRtEnableDc._changed():
        input_yang_obj.reoriginatedRtEnableDc = input_yang_obj.reoriginatedRtEnableDc
        
    if input_yang_obj.ipRtEnableDc._changed():
        input_yang_obj.ipRtEnableDc = input_yang_obj.ipRtEnableDc
        
    if input_yang_obj.splitGroupName._changed():
        input_yang_obj.splitGroupName = input_yang_obj.splitGroupName
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF_peerAFCraPres(input_yang_obj.peerAFCraPres, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs(input_yang_obj: yc_peerAFs_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/peerAFs

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
    
    for k, listInst in input_yang_obj.peerAF.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs_peerAF(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes_importRoute(input_yang_obj: yc_importRoute_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes_importRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/importRoutes/importRoute

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
    
    if input_yang_obj.importRoutePolicy._changed():
        input_yang_obj.importRoutePolicy = input_yang_obj.importRoutePolicy
        
    if input_yang_obj.medNew._changed():
        input_yang_obj.medNew = input_yang_obj.medNew
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes(input_yang_obj: yc_importRoutes_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/importRoutes

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
    
    for k, listInst in input_yang_obj.importRoute.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes_importRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes_networkRoute(input_yang_obj: yc_networkRoute_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes_networkRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/networkRoutes/networkRoute

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
    
    if input_yang_obj.networkPolicy._changed():
        input_yang_obj.networkPolicy = input_yang_obj.networkPolicy
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes(input_yang_obj: yc_networkRoutes_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/networkRoutes

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
    
    for k, listInst in input_yang_obj.networkRoute.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes_networkRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes_aggregateRoute(input_yang_obj: yc_aggregateRoute_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes_aggregateRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/aggregateRoutes/aggregateRoute

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
    
    if input_yang_obj.asSetEnable._changed():
        input_yang_obj.asSetEnable = input_yang_obj.asSetEnable
        
    if input_yang_obj.detailSuppressed._changed():
        input_yang_obj.detailSuppressed = input_yang_obj.detailSuppressed
        
    if input_yang_obj.attributePolicy._changed():
        input_yang_obj.attributePolicy = input_yang_obj.attributePolicy
        
    if input_yang_obj.originPolicy._changed():
        input_yang_obj.originPolicy = input_yang_obj.originPolicy
        
    if input_yang_obj.suppressPolicy._changed():
        input_yang_obj.suppressPolicy = input_yang_obj.suppressPolicy
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes(input_yang_obj: yc_aggregateRoutes_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/aggregateRoutes

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
    
    for k, listInst in input_yang_obj.aggregateRoute.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes_aggregateRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes_dampRoute(input_yang_obj: yc_dampRoute_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes_dampRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/dampRoutes/dampRoute

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
    
    if input_yang_obj.dampPolicyName._changed():
        input_yang_obj.dampPolicyName = input_yang_obj.dampPolicyName
        
    if input_yang_obj.updateStandard._changed():
        input_yang_obj.updateStandard = input_yang_obj.updateStandard
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes(input_yang_obj: yc_dampRoutes_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/dampRoutes

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
    
    for k, listInst in input_yang_obj.dampRoute.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes_dampRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys_filterPolicy(input_yang_obj: yc_filterPolicy_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys_filterPolicy, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/filterPolicys/filterPolicy

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
    
    if input_yang_obj.aclNameOrNum._changed():
        input_yang_obj.aclNameOrNum = input_yang_obj.aclNameOrNum
        
    if input_yang_obj.preFlt4Name._changed():
        input_yang_obj.preFlt4Name = input_yang_obj.preFlt4Name
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys(input_yang_obj: yc_filterPolicys_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/filterPolicys

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
    
    for k, listInst in input_yang_obj.filterPolicy.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys_filterPolicy(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports_instanceImport(input_yang_obj: yc_instanceImport_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports_instanceImport, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/instanceImports/instanceImport

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
    
    if input_yang_obj.policyName._changed():
        input_yang_obj.policyName = input_yang_obj.policyName
        
    if input_yang_obj.validRtEnable._changed():
        input_yang_obj.validRtEnable = input_yang_obj.validRtEnable
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports(input_yang_obj: yc_instanceImports_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/instanceImports

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
    
    for k, listInst in input_yang_obj.instanceImport.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports_instanceImport(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes_bgpAdvRoute(input_yang_obj: yc_bgpAdvRoute_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes_bgpAdvRoute, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/bgpAdvRoutes/bgpAdvRoute

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
    
    if input_yang_obj.importMultipath._changed():
        input_yang_obj.importMultipath = input_yang_obj.importMultipath
        
    if input_yang_obj.advRouteMode._changed():
        input_yang_obj.advRouteMode = input_yang_obj.advRouteMode
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes(input_yang_obj: yc_bgpAdvRoutes_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF/bgpAdvRoutes

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
    
    for k, listInst in input_yang_obj.bgpAdvRoute.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes_bgpAdvRoute(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF(input_yang_obj: yc_bgpMultiVrfAF_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs/bgpMultiVrfAF

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
    
    if input_yang_obj.nexthopDelayTime._changed():
        input_yang_obj.nexthopDelayTime = input_yang_obj.nexthopDelayTime
        
    if input_yang_obj.noCriticalNexthopDelayTime._changed():
        input_yang_obj.noCriticalNexthopDelayTime = input_yang_obj.noCriticalNexthopDelayTime
        
    if input_yang_obj.vrfAsNum._changed():
        input_yang_obj.vrfAsNum = input_yang_obj.vrfAsNum
        
    if input_yang_obj.maxLoadIbgpNum._changed():
        input_yang_obj.maxLoadIbgpNum = input_yang_obj.maxLoadIbgpNum
        
    if input_yang_obj.ibgpEcmpNexthopChanged._changed():
        input_yang_obj.ibgpEcmpNexthopChanged = input_yang_obj.ibgpEcmpNexthopChanged
        
    if input_yang_obj.maxLoadEbgpNum._changed():
        input_yang_obj.maxLoadEbgpNum = input_yang_obj.maxLoadEbgpNum
        
    if input_yang_obj.ebgpEcmpNexthopChanged._changed():
        input_yang_obj.ebgpEcmpNexthopChanged = input_yang_obj.ebgpEcmpNexthopChanged
        
    if input_yang_obj.maximumLoadBalance._changed():
        input_yang_obj.maximumLoadBalance = input_yang_obj.maximumLoadBalance
        
    if input_yang_obj.ecmpNexthopChanged._changed():
        input_yang_obj.ecmpNexthopChanged = input_yang_obj.ecmpNexthopChanged
        
    if input_yang_obj.eibgpLoadBalan._changed():
        input_yang_obj.eibgpLoadBalan = input_yang_obj.eibgpLoadBalan
        
    if input_yang_obj.eibgpEcmpNexthopChanged._changed():
        input_yang_obj.eibgpEcmpNexthopChanged = input_yang_obj.eibgpEcmpNexthopChanged
        
    if input_yang_obj.defaultLocalPref._changed():
        input_yang_obj.defaultLocalPref = input_yang_obj.defaultLocalPref
        
    if input_yang_obj.defaultMed._changed():
        input_yang_obj.defaultMed = input_yang_obj.defaultMed
        
    if input_yang_obj.defaultRtImportEnable._changed():
        input_yang_obj.defaultRtImportEnable = input_yang_obj.defaultRtImportEnable
        
    if input_yang_obj.loadBalancingAsPathRelax._changed():
        input_yang_obj.loadBalancingAsPathRelax = input_yang_obj.loadBalancingAsPathRelax
        
    if input_yang_obj.routerId._changed():
        input_yang_obj.routerId = input_yang_obj.routerId
        
    if input_yang_obj.vrfRidAutoSel._changed():
        input_yang_obj.vrfRidAutoSel = input_yang_obj.vrfRidAutoSel
        
    if input_yang_obj.nexthopThirdParty._changed():
        input_yang_obj.nexthopThirdParty = input_yang_obj.nexthopThirdParty
        
    if input_yang_obj.summaryAutomatic._changed():
        input_yang_obj.summaryAutomatic = input_yang_obj.summaryAutomatic
        
    if input_yang_obj.autoFrrEnable._changed():
        input_yang_obj.autoFrrEnable = input_yang_obj.autoFrrEnable
        
    if input_yang_obj.loadBalancingAsPathIgnore._changed():
        input_yang_obj.loadBalancingAsPathIgnore = input_yang_obj.loadBalancingAsPathIgnore
        
    if input_yang_obj.ribOnlyEnable._changed():
        input_yang_obj.ribOnlyEnable = input_yang_obj.ribOnlyEnable
        
    if input_yang_obj.ribOnlyPolicyName._changed():
        input_yang_obj.ribOnlyPolicyName = input_yang_obj.ribOnlyPolicyName
        
    if input_yang_obj.activeRouteAdvertise._changed():
        input_yang_obj.activeRouteAdvertise = input_yang_obj.activeRouteAdvertise
        
    if input_yang_obj.asPathNeglect._changed():
        input_yang_obj.asPathNeglect = input_yang_obj.asPathNeglect
        
    if input_yang_obj.medNoneAsMaximum._changed():
        input_yang_obj.medNoneAsMaximum = input_yang_obj.medNoneAsMaximum
        
    if input_yang_obj.routerIdNeglect._changed():
        input_yang_obj.routerIdNeglect = input_yang_obj.routerIdNeglect
        
    if input_yang_obj.igpMetricIgnore._changed():
        input_yang_obj.igpMetricIgnore = input_yang_obj.igpMetricIgnore
        
    if input_yang_obj.alwaysCompareMed._changed():
        input_yang_obj.alwaysCompareMed = input_yang_obj.alwaysCompareMed
        
    if input_yang_obj.determinMed._changed():
        input_yang_obj.determinMed = input_yang_obj.determinMed
        
    if input_yang_obj.preferenceExternal._changed():
        input_yang_obj.preferenceExternal = input_yang_obj.preferenceExternal
        
    if input_yang_obj.preferenceInternal._changed():
        input_yang_obj.preferenceInternal = input_yang_obj.preferenceInternal
        
    if input_yang_obj.preferenceLocal._changed():
        input_yang_obj.preferenceLocal = input_yang_obj.preferenceLocal
        
    if input_yang_obj.prefrencePolicyName._changed():
        input_yang_obj.prefrencePolicyName = input_yang_obj.prefrencePolicyName
        
    if input_yang_obj.reflectBetweenClient._changed():
        input_yang_obj.reflectBetweenClient = input_yang_obj.reflectBetweenClient
        
    if input_yang_obj.reflectorClusterId._changed():
        input_yang_obj.reflectorClusterId = input_yang_obj.reflectorClusterId
        
    if input_yang_obj.reflectorClusterIpv4._changed():
        input_yang_obj.reflectorClusterIpv4 = input_yang_obj.reflectorClusterIpv4
        
    if input_yang_obj.rrFilterNumber._changed():
        input_yang_obj.rrFilterNumber = input_yang_obj.rrFilterNumber
        
    if input_yang_obj.policyVpnTarget._changed():
        input_yang_obj.policyVpnTarget = input_yang_obj.policyVpnTarget
        
    if input_yang_obj.nextHopSelDependType._changed():
        input_yang_obj.nextHopSelDependType = input_yang_obj.nextHopSelDependType
        
    if input_yang_obj.nhpRelayRoutePolicyName._changed():
        input_yang_obj.nhpRelayRoutePolicyName = input_yang_obj.nhpRelayRoutePolicyName
        
    if input_yang_obj.ebgpIfSensitive._changed():
        input_yang_obj.ebgpIfSensitive = input_yang_obj.ebgpIfSensitive
        
    if input_yang_obj.ibgpIfSensitive._changed():
        input_yang_obj.ibgpIfSensitive = input_yang_obj.ibgpIfSensitive
        
    if input_yang_obj.reflectChgPath._changed():
        input_yang_obj.reflectChgPath = input_yang_obj.reflectChgPath
        
    if input_yang_obj.slowPeerDet._changed():
        input_yang_obj.slowPeerDet = input_yang_obj.slowPeerDet
        
    if input_yang_obj.slowPeerThVal._changed():
        input_yang_obj.slowPeerThVal = input_yang_obj.slowPeerThVal
        
    if input_yang_obj.addPathSelNum._changed():
        input_yang_obj.addPathSelNum = input_yang_obj.addPathSelNum
        
    if input_yang_obj.routeSelDelay._changed():
        input_yang_obj.routeSelDelay = input_yang_obj.routeSelDelay
        
    if input_yang_obj.originAsValidEnable._changed():
        input_yang_obj.originAsValidEnable = input_yang_obj.originAsValidEnable
        
    if input_yang_obj.originAsValid._changed():
        input_yang_obj.originAsValid = input_yang_obj.originAsValid
        
    if input_yang_obj.allowInvalidAs._changed():
        input_yang_obj.allowInvalidAs = input_yang_obj.allowInvalidAs
        
    if input_yang_obj.policyExtCommEnable._changed():
        input_yang_obj.policyExtCommEnable = input_yang_obj.policyExtCommEnable
        
    if input_yang_obj.policyQPPBEnable._changed():
        input_yang_obj.policyQPPBEnable = input_yang_obj.policyQPPBEnable
        
    if input_yang_obj.supernetUniAdv._changed():
        input_yang_obj.supernetUniAdv = input_yang_obj.supernetUniAdv
        
    if input_yang_obj.supernetLabelAdv._changed():
        input_yang_obj.supernetLabelAdv = input_yang_obj.supernetLabelAdv
        
    if input_yang_obj.ingressLspPolicyName._changed():
        input_yang_obj.ingressLspPolicyName = input_yang_obj.ingressLspPolicyName
        
    if input_yang_obj.originatorPrior._changed():
        input_yang_obj.originatorPrior = input_yang_obj.originatorPrior
        
    if input_yang_obj.lowestPriority._changed():
        input_yang_obj.lowestPriority = input_yang_obj.lowestPriority
        
    if input_yang_obj.relayDelayEnable._changed():
        input_yang_obj.relayDelayEnable = input_yang_obj.relayDelayEnable
        
    if input_yang_obj.irbAsymmetric._changed():
        input_yang_obj.irbAsymmetric = input_yang_obj.irbAsymmetric
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerGroupAFs(input_yang_obj.peerGroupAFs, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_peerAFs(input_yang_obj.peerAFs, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_importRoutes(input_yang_obj.importRoutes, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_networkRoutes(input_yang_obj.networkRoutes, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_aggregateRoutes(input_yang_obj.aggregateRoutes, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_dampRoutes(input_yang_obj.dampRoutes, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_filterPolicys(input_yang_obj.filterPolicys, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_instanceImports(input_yang_obj.instanceImports, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF_bgpAdvRoutes(input_yang_obj.bgpAdvRoutes, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs(input_yang_obj: yc_bgpMultiVrfAFs_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf/bgpMultiVrfAFs

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
    
    for k, listInst in input_yang_obj.bgpMultiVrfAF.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs_bgpMultiVrfAF(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf(input_yang_obj: yc_bgpMultiVrf_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs/bgpMultiVrf

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
    
    if input_yang_obj.vrfRidAutoSel._changed():
        input_yang_obj.vrfRidAutoSel = input_yang_obj.vrfRidAutoSel
        
    if input_yang_obj.routerId._changed():
        input_yang_obj.routerId = input_yang_obj.routerId
        
    if input_yang_obj.effectRouterId._changed():
        input_yang_obj.effectRouterId = input_yang_obj.effectRouterId
        
    if input_yang_obj.keepaliveTime._changed():
        input_yang_obj.keepaliveTime = input_yang_obj.keepaliveTime
        
    if input_yang_obj.holdTime._changed():
        input_yang_obj.holdTime = input_yang_obj.holdTime
        
    if input_yang_obj.minHoldTime._changed():
        input_yang_obj.minHoldTime = input_yang_obj.minHoldTime
        
    if input_yang_obj.connRetryTime._changed():
        input_yang_obj.connRetryTime = input_yang_obj.connRetryTime
        
    if input_yang_obj.defaultAfType._changed():
        input_yang_obj.defaultAfType = input_yang_obj.defaultAfType
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeerGroups(input_yang_obj.bgpMultiPeerGroups, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiPeers(input_yang_obj.bgpMultiPeers, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf_bgpMultiVrfAFs(input_yang_obj.bgpMultiVrfAFs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs(input_yang_obj: yc_bgpMultiVrfs_huawei_bgp__bgp_bgpmultiinstcomm_bgpMultiVrfs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm/bgpMultiVrfs

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
    
    for k, listInst in input_yang_obj.bgpMultiVrf.iteritems():
        innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs_bgpMultiVrf(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp_bgpmultiinstcomm(input_yang_obj: yc_bgpmultiinstcomm_huawei_bgp__bgp_bgpmultiinstcomm, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp/bgpmultiinstcomm

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
    
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiSites(input_yang_obj.bgpMultiSites, translated_yang_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm_bgpMultiVrfs(input_yang_obj.bgpMultiVrfs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__bgp(input_yang_obj: yc_bgp_huawei_bgp__bgp, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /bgp

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
    control_plane_protocol_obj = translated_yang_obj.routing.control_plane_protocols.control_plane_protocol.add(type="bgp", name="bgp1")

    innerobj = _translate__bgp_bgpcomm(input_yang_obj.bgpcomm, control_plane_protocol_obj)
        
    innerobj = _translate__bgp_bgpmultiinstcomm(input_yang_obj.bgpmultiinstcomm, translated_yang_obj)
        
    return translated_yang_obj

def _translate__huawei_bgp(input_yang_obj: huawei_bgp, translated_yang_obj=None, xpath=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /huawei-bgp

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
    print("IETF105 huawei bgp script!")
    translated_yang_obj = ietf_routing()
    innerobj = _translate__bgp(input_yang_obj.bgp, translated_yang_obj)
    xpath = '/a:routing'
    ns_map = {'a': 'urn:ietf:params:xml:ns:yang:ietf-routing'}
    target_xpath = XPATH(xpath, ns_map)
        
    return [[translated_yang_obj.routing, target_xpath]]
