import json

from lxml import etree

from mediator_framework.mediator_core import compute_configuration_by_operation

if __name__ == '__main__':
    with open('ietf_interfaces.json','r') as f:
        json_data = json.load(f)
        neid = 'router 0'
        res = compute_configuration_by_operation(neid, json_data)
        print(etree.tostring(res[0][1], pretty_print=True).decode('utf-8'))