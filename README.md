# Mediator

Mediator is a framework to facilitate the translation of messages instantiated from different YANG models. Mediator provides python APIs for 3rd developers to design their own translation scripts.

## Overview

Mediator consists of a set of components, including session manager, script adaptor, data manager, etc. By invoking appropriate translation scripts, Mediator helps build the communication between the controller and diverse devices from different manufacturers.

![](https://github.com/qiangzhang0925/images/raw/master/img/logical-overview.png)

## Requirements
### dependencies
- Python(python>=3.6)
- pyangbind
- ncclient
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

### Supported features
- Provide a programmable framework that enables third-party users to load their own transformation scripts.
- Provide the ability to generate code templates that conform to the Mediator framework.
- Provide the ability to issue configurations that support 1:1, 1:n, and N:m transformations from business models to device models.
- Provide the ability to query configuration and status data.
- Provide the ability to install, upgrade, uninstall and update the Yang model transformation plugin.

### Multitask-oriented management
- Provides services to three types of users：System administrators, network administrators, third-party developers.
- **System administrator:** deploy Mediators, manage local configuration, and query information.
- **Network administrator:** issue configuration, query data, issue maintenance operation and detect notification.
- **Third-party developers:** install development environment, develop Yang translation scripts, test scripts and installation scripts.

## Deploment

### Independent deployment

Mediators, as a model transformation node, can be deployed in user management networks.

<div align=center>
![](https://github.com/qiangzhang0925/images/raw/master/img/1.png =500x400)
</div>

### Deployed on the controller

Mediator provide SDK interface for mode scenarios of third-party controllers. The script of YANG model transformation is consistent with the independent deployment, and the reliability mode follows the mode of the controller itself.

<div align=center>
![](https://github.com/qiangzhang0925/images/raw/master/img/2.png =500x400)
</div>

### Deployed on the device

Mediator's Yang model transformation script is deployed on the device. The YANG model's processing script is consistent with the third-party YANG transformation script interface provided on the device.

<div align=center>
![](https://github.com/qiangzhang0925/images/raw/master/img/3.png =500x400)
</div>

##  Usage examples
Mediator is useful for all users to translate netconf/xml messages instantiated from different YANG models. L3VPN Service delivery acts as a use case as following:

### L3VPN Service Delivery
To deliver the L3VPN service within the network management automation architecture, the Controller takes the parameters extracted from the L3NM and translates them into orchestrated configuration of network elements that are part of, e.g., BGP, QoS, Network Instance, IP management, and interface models. Mediator implements the translation of IETF's Yang to Huawei Yang.

 <div align=center>
![](https://github.com/qiangzhang0925/images/raw/master/img/4.png =500x400)
</div>


