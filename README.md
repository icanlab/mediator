# Mediator

Mediator is a framework to facilitate the translation of netconf/xml messages instantiated from different YANG models. Mediator provides python language APIs for 3rd developers to design their own translate scripts.

Mediator can be integrated with Ansible plugin, or interacts with network controller through netconf protocol, to build the communication between the controller and diverse devices from different manufacturers.

## Overview
![](https://github.com/qiangzhang0925/images/raw/master/img/logical-overview%20(2).png)

## Requirements
### dependencies
- Python(python>=3.6)
- pyangbind
- ncclient
- ansible
- lxml

####  Optional
- doxygen (for generating documentation)

## Compatibility

- RFC 6020: YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF) 
- RFC 6022: YANG Module for NETCONF Monitoring
- RFC 6241: Network Configuration Protocol
- RFC 6470: Network Configuration Protocol (NETCONF) Base Notifications
- RFC 7317: A YANG Data Model for System Management
- RFC 7950: The YANG 1.1 Data Modeling Languages
- RFC 7952: Defining and Using Metadata with YANGs
- RFC 8040: RESTCONF Protocols
- RFC 8341: Network Configuration Access Control Model
- RFC 8528: YANG Schema Mount
- RFC 8791: YANG Data Structure Extensions
- draft-yby-yang-model-conversion-00：YANG Model Conversion
- draft-yby-netmod-usecase-of-ymc-00：The use cases of yang model conversion

## Features
### Role-oriented
- Provides services to three types of users：System administrators, network administrators, third-party developers.
- **System administrator:** deploy Mediators, manage local configuration, and query information.
- **Network administrator:** issue configuration, query data, issue maintenance operation and detect notification.
- **Third-party developers:** install development environment, develop Yang translation scripts, test scripts and installation scripts.

### Mediator framework
- **Mediator framework:** provide runtime 
- **Serialization and deserialization:** convert YANG modules to Python Object, and vice versa.
- **Translate Scripts/Data Manager/Script Manger:** Translation between netconf/xml messages instantiated from different YANG models（third-party/native）.
- **Script Adaptor:** Provide script scheduling during translation.

## L2VPN/L3VPN Service Delivery
In reference to Figure 1, the following steps are performed to deliver the L3VPN service within the network management automation architecture.
1. The Customer requests to create two sites relying upon L3SM with each site having one network access connectivity, for example:

  - Site A: network-access A, link-capacity = 20 Mbps, class "foo", guaranteed-capacity-percent = 10, average-one-way-delay = 70 ms.

  - Site B: network-access B, link-capacity = 30 Mbps, class "foo1", guaranteed-capacity-percent = 15, average-one-way-delay = 60 ms.

2. The Orchestrator extracts the service parameters from the L3SM. Then, it uses them as input to the Service Mapping to translate them into an orchestrated configuration parameters (e.g., RD, RT, VRF) that are part of the L3NM specified in [I-D.ietf-opsawg-l3sm-l3nm].

3. The Controller takes the orchestrated configuration parameters in the L3NM and translates them into orchestrated configuration of network elements that are part of, e.g., BGP, QoS, Network Instance, IP management, and interface models.

[I-D.ogondio-opsawg-uni-topology] can be used for representing, managing, and controlling the User Network Interface (UNI) topology.

![](https://github.com/qiangzhang0925/images/raw/master/img/f4.png)

L3NM inherits some of data elements from the L3SM.  Nevertheless, the L3NM as currently designed in [I-D.ietf-opsawg-l3sm-l3nm] does not expose some information to the above layer such as the capabilities of an underlying network (which can be used to drive service order handling) or notifications (to notify subscribers about specific events or degradations as per agreed SLAs).  Some of this information can be provided using, e.g., [I-D.www-opsawg-yang-vpn-service-pm].  A target overall model is depicted in Figure 2.

![](https://github.com/qiangzhang0925/images/raw/master/img/f5.png)

Note that a similar analysis can be performed for Layer 2 VPNs (L2VPNs).  A L2VPN Service Model (L2SM) is defined in [RFC8466], while the L2VPN Network YANG Model (L2NM) is specified in [I-D.ietf-opsawg-l2nm].

##  Usage examples

Mediator is useful for all users to translate netconf/xml messages instantiated from different YANG models. The following use cases show how to use it:

### Use case for vendors

Matching between vendor's private model and operator's models.
![](https://github.com/qiangzhang0925/images/raw/master/img/f1.png)

### Use case for operators

Matching between operator's private model to vendor's models.
![](https://github.com/qiangzhang0925/images/raw/master/img/f2.png)

### Use case for multiple Yang model organizations

![](https://github.com/qiangzhang0925/images/raw/master/img/f3.png)
