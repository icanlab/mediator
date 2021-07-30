case_1 = """<?xml version=\"1.0\" ?>
        <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <edit-config>
                <target>
                    <running/>
                </target>
                <default-operation>merge</default-operation>
                <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
                   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                       <interface xc:operation="merge">
                          <name>GigabitEthernet 3/0/1</name>
                          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                             <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                                <ip>192.0.2.2</ip>
                                <prefix-length>32</prefix-length>
                             </address>
                          </ipv4>
                       </interface>
                       <interface xc:operation="delete">
                          <name>GigabitEthernet 3/0/2</name>
                          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                             <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                                <ip>192.0.3.2</ip>
                                <prefix-length>32</prefix-length>
                             </address>
                          </ipv4>
                       </interface>
                       <interface>
                          <name>GigabitEthernet 3/0/3</name>
                          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                             <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                                <ip>192.0.4.2</ip>
                                <prefix-length>32</prefix-length>
                             </address>
                          </ipv4>
                       </interface>
                    </interfaces>
                </config>
            </edit-config>
        </rpc>
       """




