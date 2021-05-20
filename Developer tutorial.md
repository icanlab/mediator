## Developer Tutorial
Instructions and examples to help you get statrted.  

Follow the step-by-step instructions, you can build your own mediator which can translate the YANG-based messages to target format you want.

### Prerequisites
- Python develop environment(python>=3.6)
- Python IDE e.g. PyCharm (optional)
- pyangbind

### Pull sample code from github
``` 
$ git clone https://github.com/icanlab/mediator_example.git
```

### Install requirement.txt
Execute the command below in root dir
```
$ pip install -r requirement.txt
```

### Patch the pyangbind.patch in root directory
There are three files need to be modified in pyangbind, including serialise.py yangtypes.py in lib dir and pybind.py in plugin dir
```
$ pacth -p1 < pyangbind.patch
```

### Develop your own translation scripts
# translation_package
> Take the translation between ietf-interfaces and huawei-ifm for example
- create translation_pack dir in your workspace 
 ```
 $ mkdir translation_pack
 ```
- use pyangbind to transfer YANG model to pyangbind object
```
$ export PYBINDPLUGIN=`/usr/bin/env python -c \
'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
$ $ pyang --plugindir $PYBINDPLUGIN -f pybind -o ietf_interfaces_binding.py yang_modules/ietf-interfaces.yang yang_modules/ietf-ip.yang
```
* Parameters
    - $PYBINDPLUGIN i--> the location of pyangbind plugin.
    - ietf_interfaces_binding.py --> the desired python object file.
    -  yang_modules/ietf-interfaces.yang --> the path of YANG models involved in translation.

- pyangbind will generate two python files
    - **ietf_interfaces_binding.py** --> python object which are corresponding to YANG model
    - **_translate_ietf_interfaces_obj.py** --> the translation template

- modify translation template(take ietf-interfaces to huawei-ifm for example): 
    - First, new hauwei_ifm() as translated_obj
    ```python
    translated_yang_obj = huawei_ifm()

    list, innerobj = _translate__interfaces(input_yang_obj.interfaces, translated_yang_obj)
    ```
    - Then,  call different child funtions to complete the mapping logic
    ```python
        for k, listInst in input_yang_obj.interface.iteritems():
        interface_obj = translated_yang_obj.ifm.interfaces.interface.add(name=k)
        inner_obj = _translate__interfaces_interface(listInst, interface_obj)
        # ipv4 = _translate__interfaces_interface_ipv4(listInst,interface_obj)
        list_obj.append(translated_yang_obj)
    ```

### Build your register.yml and pack the translation files
- register.yml example:
```yaml
---
trans_info:
  vendor:
    huawei
  product:
    route
  type:
    huaweios
  version:
    v1
trans_point_path:
  /ietf-interfaces:interfaces
script_name:
  _translate_ietf_interfaces_obj
binding_name:
  ietf_interfaces_binding
module_name:
  ietf_interfaces
```
- pack the translation files, including:
    - _translate_ietf_interfaces_obj.py
    - ietf_interfaces_binding.py
    - huawei_ifm_binding.py
    - register.yml

### Use the translation scripts you developed in mediator framework
- enter the mediator_server dir and execute the unpack.py
```
python unpack.py your_workspace/translation_pack.zip
```
your_workspace/translation_pcak.zip is the the direcoty of translation scripts you developed(unpack support zip and rar form).

- start up the mediator server, then scan.py will copy your translation srcipts into target directory automatically, and generate the register.py
```
python -m mediator_server
```

- you can check whether your translation script works by constrcting the XML input like this:
```xml
<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface xc:operation="merge">
            <name>GigabitEthernet 3/0/1</name>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xc:operation="create">
                <ip>192.0.3.1</ip>
                <prefix-length>32</prefix-length>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
```
