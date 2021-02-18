from lxml import etree
import json

from mediator_framework.mediator_core import compare_dc_configuration

if __name__ == '__main__':
    expected_dc = """
        <ifm>
          <interfaces>
            <interface>
              <name>GigabitEthernet 3/0/1</name>
              <ipv4>
                <addresses>
                  <address>
                    <ip>192.0.2.2</ip>
                    <mask>255.255.255.255</mask>
                    <type>main</type>
                  </address>
                </addresses>
              </ipv4>
            </interface>
          </interfaces>
        </ifm>
        """
    parse = etree.XMLParser(remove_blank_text=True)
    config0 = etree.XML(expected_dc, parse)
    config1 = etree.parse("dc_configuration.xml", parse)
    root = {}
    path = ''
    root = compare_dc_configuration(config0, config1, root, path)
    res =[]
    res.append(root)
    print(json.dumps(res, indent=4))  # final output