from swagger_server.translation_scripts.huawei.route.huaweios.v1 import _translate_huawei_ifm_obj

from swagger_server.yang_bindings import ietf_routing_binding
from swagger_server.translation_scripts.huawei.route.huaweios.v1 import _translate_ietf_routing_obj

from swagger_server.translation_scripts.huawei.route.huaweios.v1 import _translate_huawei_ifm_obj
from swagger_server.yang_bindings import huawei_ifm_binding

translate_yang_registry = {
'/ifm': (_translate_huawei_ifm_obj, huawei_ifm_binding, "huawei_ifm"),
'/routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing")
}