import json

from lxml import etree

from swagger_server.mediator_framework.mediator_core import translate_get_config_content
from swagger_server.mediator_framework.parse import parse_get_config_content


def _test_translate_get_config_content_ietf_interfaces():
    with open('adaptor_get_config_request/ietf_interfaces_get_config.json', 'r') as f:
        json_data = json.load(f)
        neid = 'router 0'
        res = translate_get_config_content(neid, json_data)
        data_list =[]
        for i in res:
            dic = parse_get_config_content(i)
            data_list.append(dic)
    return data_list

if __name__ == '__main__':
    li = _test_translate_get_config_content_ietf_interfaces()
    for i in li:
        print(i)