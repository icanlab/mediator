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
- Provide a programmable framework that enables third-party users to load their own transformation scripts, and support the Python.
- Provide the ability to generate code templates that conform to the Mediator framework.
- Provide the ability to issue configurations ,and support 1:1, 1:n and N:m transformations from business models to device models.
- Provide the ability to query configuration and status data, and support the transformation of filter conditions.
- Provide the ability to install, upgrade, uninstall and update the Yang model transformation plug-in

### Multitask-oriented deployment
- Provides services to three types of users：System administrators, network administrators, third-party developers.
- **System administrator:** deploy Mediators, manage local configuration, and query information.
- **Network administrator:** issue configuration, query data, issue maintenance operation and detect notification.
- **Third-party developers:** install development environment, develop Yang translation scripts, test scripts and installation scripts.


##  Usage examples

Mediator is useful for all users to translate netconf/xml messages instantiated from different YANG models. L3VPN Service delivery acts as a use case as following:

### L3VPN Service Delivery
To deliver the L3VPN service within the network management automation architecture, the Controller takes the parameters extracted from the L3NM and translates them into orchestrated configuration of network elements that are part of, e.g., BGP, QoS, Network Instance, IP management, and interface models.

![](https://github.com/qiangzhang0925/images/raw/master/img/f1.png)

### Mediator independent deployment

Mediators, as a model transformation node, can be deployed in user management networks.
![](https://github.com/qiangzhang0925/images/raw/master/img/f3.png)

### Mediator deployed in the controller

Mediator provides the mode scenario of SDK interface to the third-party controller. The script of YANG model transformation is consistent with the independent deployment, and the reliability mode follows the mode of the controller itself.
![](https://github.com/qiangzhang0925/images/raw/master/img/f4.png)

### Mediator deployed in communication equipment

Mediator's Yang model transformation script is deployed on the device. The YANG model's processing script is consistent with the third-party YANG transformation script interface provided on the device.

![](https://github.com/qiangzhang0925/images/raw/master/img/f5.png)
