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
- RFC 7950: The YANG 1.1 Data Modeling Languages
- RFC 7952: Defining and Using Metadata with YANGs
- RFC 8040: RESTCONF Protocols
- RFC 8791: YANG Data Structure Extensions

## Features

- Validate YANG modules
- Serialization and deserialization, convert YANG modules to XML, and XML to YANG modules.
- Convert the XML message corresponding to the third-party YANG model to the XML message corresponding to the native YANG model.
- Provide script scheduling during translation.


##  Usage


## Examples


## Other resources
