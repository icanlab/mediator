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

- RFC 5277: NETCONF Event Notification
- RFC 6020: YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF) 
- RFC 6022: YANG Module for NETCONF Monitoring
- RFC 6241: Network Configuration Protocol
- RFC 6470: Network Configuration Protocol (NETCONF) Base Notifications
- RFC 7317: A YANG Data Model for System Management
- RFC 7950: The YANG 1.1 Data Modeling Languages
- RFC 7952: Defining and Using Metadata with YANGs
- RFC 8017: PKCS #1: RSA Encryption Version 1.5
- RFC 8040: RESTCONF Protocols
- RFC 8341: Network Configuration Access Control Model
- RFC 8528: YANG Schema Mount
- RFC 8791: YANG Data Structure Extensions
- YANG Model Conversion：draft-yby-yang-model-conversion-00
- The use cases of yang model conversion：draft-yby-netmod-usecase-of-ymc-00

## Features
### object-oriented
- Provides services to three types of users：System administrators, network administrators, third-party developers.
- System administrator has the ability to deploy Mediators, manage local configuration, and query information.
- Network administrator has the ability to issue configuration, query data, issue maintenance operation and detect notification.
- Third-party developers can use Mediators to install development environment, develop Yang translation scripts, test scripts and installation scripts.

### Specific function
- Mediator framework: provide runtime 
- Serialization and deserialization: convert YANG modules to Python Object, and vice versa.
- Convert the XML message corresponding to the third-party YANG model to the XML message corresponding to the native YANG model.
- Provide script scheduling during translation.

##  Usage examples

