from pyangbind.lib.serialise import pybindIETFXMLEncoder

from yang_bindings.src_yang_bindings.ietf_interfaces_binding import *
from yang_bindings.src_yang_bindings import ietf_interfaces_binding
import pyangbind.lib.pybindJSON as pybindJSON
from translation_scripts.src2target import _translate_ietf_interfaces_obj

def generate_yang_obj():  # generate yang obj
    inobj = ietf_interfaces()
    inobj1 = inobj.interfaces.interface.add(name="GigabitEthernet 3/0/1")
    inobj1.type = "ianaift:ethernetCsmacd"
    inobj3 = inobj1.ipv4.address.add("192.0.2.2")
    inobj3.prefix_length = "32"
    return inobj

def test_decoder_yang_obj():
    json_data = pybindJSON.dumps(generate_yang_obj())
    # print(json_data)
    return pybindJSON.loads(json_data,ietf_interfaces_binding,"ietf-interfaces")


if __name__ == "__main__":
    yangobj = test_decoder_yang_obj()
    translated_obj = _translate_ietf_interfaces_obj._translate__ietf_interfaces(yangobj)
    print("XML格式：\n", pybindIETFXMLEncoder.serialise(translated_obj[0]))
    print("JSON格式：\n", pybindJSON.dumps(translated_obj[0]))