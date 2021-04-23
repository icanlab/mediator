## End-to-end test tutorial
> Instructions and examples to help you establish the end-to-end test.

In this tutorial, we take ansible as controller, and use [netopeer2](https://github.com/CESNET/netopeer2) to simulate device function.

### Install Mediator-ne-plugin
Follow the [mediator-ne-plugin tutorial](https://github.com/icanlab/mediator-ne-plugin/blob/main/README.md) to install mediator-ne-plugin.  
Mediator-ne-plugin provides the following functions:
- Connect devices
- Call mediator to translate messages
- Cache data

### Install Mediator
Follow the [mediator develop tutorial](https://github.com/icanlab/mediator/blob/dev/Developer%20tutorial.md) to install mediator which provides the function of translating messgaes.

### Install Mediator Controller
Follow the [mediator-controller tutorial](https://github.com/icanlab/mediator-controller/blob/main/README.md) to install mediator controller.  
Mediator controller provides the following functions:
- Data interface for mediator
- Datastore management

### End to end test example

Send `get-config` or `edit-config` via `ansible-playbook`.

#### get-config

Write playbook `get-config.yml`:

```yaml
---
- name: ietf-interfaces_config
  hosts: netopeer2
  connection: netconf
  gather_facts: no
  vars:
    netconf:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ ansible_user }}"
      password: "{{ ansible_ssh_pass }}"
      transport: netconf

  tasks:
    - name: ietf-interfaces_full
        ietf-interfaces_config:
        operation_type: get-config
        interfaces: []
        provider: "{{ netconf }}"
```

Send `get-config` by running playbook:

```
ansible-playbook -vvv get-config.yml
```

#### edit-config

Write playbook `edit-config.yml`:

```yaml
---
- name: ietf-interfaces_config
  hosts: netopeer2
  connection: netconf
  gather_facts: no
  vars:
    netconf:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ ansible_user }}"
      password: "{{ ansible_ssh_pass }}"
      transport: netconf

  tasks:
    - name: ietf-interfaces_full
        ietf-interfaces_config:
        operation_type: config
        operation_specs:
            - path: "/config/interfaces/interface[name=\"GigabitEthernet 3/0/1\"]"
            operation: merge
            - path: "/config/interfaces/interface[name=\"GigabitEthernet 3/0/1\"]/ipv4"
            operation: merge
        interfaces:
            - interface:
                name: "GigabitEthernet 3/0/1"
                type: "ianaift:ethernetCsmacd"
                ipv4:
                - address:
                    ip: "192.0.2.3"
                    prefix-length: 32
        provider: "{{ netconf }}"
```

Send `edit-config` by running playbook:

```
ansible-playbook -vvv edit-config.yml
```