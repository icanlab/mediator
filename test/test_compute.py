import json

from lxml import etree
import re

from mediator_framework.mediator_core import parse_keyvalue_all

if __name__ == "__main__":
    with open('ietf_interfaces.json', 'r') as f:  # open the json file
        json_data = json.load(f)
        root = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})  # add the config element
        path = ''
        ns = {}
        n = 0
        parse_keyvalue_all(json_data, root, path, ns, n)
        print(ns)
        # print("data is:\n", etree.tostring(root, pretty_print=True).decode("utf8"))