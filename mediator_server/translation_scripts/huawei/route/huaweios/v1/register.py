from mediator_server.translation_scripts.huawei.route.huaweios.v1 import _translate_ietf_routing_obj

from mediator_server.yang_bindings import huawei_ifm_binding
from mediator_server.translation_scripts.huawei.route.huaweios.v1 import _translate_huawei_ifm_obj

from mediator_server.translation_scripts.huawei.route.huaweios.v1 import _translate_ietf_routing_obj
from mediator_server.yang_bindings import ietf_routing_binding

translate_yang_registry = {
'/routing': (_translate_ietf_routing_obj, ietf_routing_binding, "ietf_routing"),
'/ifm': (_translate_huawei_ifm_obj, huawei_ifm_binding, "huawei_ifm")
}