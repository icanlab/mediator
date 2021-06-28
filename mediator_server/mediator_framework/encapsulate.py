from lxml import etree
import re


class XPATH(etree.XPath):
    def __init__(self, path, namespaces=None):
        super(XPATH, self).__init__(path, namespaces=namespaces)
        self.namespaces = namespaces


def get_xpath(path, ns_map):
    xpath = XPATH(path, ns_map)
    return xpath


def encapsulate(xpath, el):
    # print(xpath.path, xpath.namespaces, el)
    path = xpath.path
    ns = xpath.namespaces
    path_list = [x for x in path.split('/') if x != '']
    flags = []
    for i, s in enumerate(path_list):  # to deal with the key
        if len(s) == 1:
            flags.append(i)
    flags.reverse()
    for flag in flags:
        path_list[flag - 1] = path_list[flag - 1] + '/' + path_list[flag] + '/' + path_list[flag + 1]
        del path_list[flag]
        del path_list[flag]
    if len(path_list) > 1:
        # print("go to 1")
        if '=' in path_list[0]:
            path = path_list[0].split('[')[0]
            top_node = etree.Element(path.split(':')[-1], nsmap={None: ns[path.split(':')[0]]})
        else:
            top_node = etree.Element(path_list[0].split(':')[-1], nsmap={None: ns[path_list[0].split(':')[0]]})
        temp = top_node
        del path_list[0]
        for index, item in enumerate(path_list):
            if index == len(path_list) - 1:
                break
            namespace = ns[item.split(':')[0]]
            if '=' in item:
                node_tag = re.split(':|\[', item)[1]
                key = re.split(':|\]', item)[-2]
                key_tag = re.split('=', key)[0]
                key_value = re.split('=|\"', key)[2]
                temp = etree.SubElement(temp, node_tag, nsmap={None: namespace})
                key_node = etree.SubElement(temp, key_tag)
                key_node.text = key_value
            else:
                node_tag = item.split(':')[-1]
                temp = etree.SubElement(temp, node_tag, nsmap={None: namespace})
        temp.append(el)
    else:
        # print("go to 2")
        top_node = el
    return top_node


# if __name__ == "__main__":
#     p = '/a:interfaces/a:interface[a:name="GigabitEthernet 3/0/3"]/b:ipv4/b:address[b:ip="192.0.4.2"]'
#     n = {'xc': 'urn:ietf:params:xml:ns:netconf:base:1.0', 'a': 'urn:ietf:params:xml:ns:yang:ietf-interfaces',
#                   'b': 'urn:ietf:params:xml:ns:yang:ietf-ip'}
#     xpath = get_xpath(p, n)
#     parse = etree.XMLParser(remove_blank_text=True)
#     message = etree.fromstring(data1.data.encode('utf-8'), parser=parse)
#     result = encapsulate(xpath, message)
#     print("result:\n", etree.tostring(result))
