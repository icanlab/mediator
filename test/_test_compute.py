import json

from lxml import etree

from mediator_framework.mediator_core import compute_configuration_by_operation

def _test_compute_ietf_interfaces():
    with open('input_op_list/ietf_interfaces.json', 'r') as f:
        json_data = json.load(f)
        neid = 'router 0'
        res = compute_configuration_by_operation(neid, json_data)
        print(etree.tostring(res[0][1], pretty_print=True).decode('utf-8'))

if __name__ == '__main__':
    _test_compute_ietf_interfaces()