from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class KubeControllerManagerTerminatedPods(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.2.1
        id = "CKV_K8S_106"
        name = "Ensure that the --terminated-pod-gc-threshold argument is set as appropriate"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "kube-controller-manager" in conf["command"]:
                index_of_terminated_pod_gc_threshold = [n for n, l in enumerate(conf["command"])
                                                        if l.startswith('--terminated-pod-gc-threshold')]
                if len(index_of_terminated_pod_gc_threshold) > 0:
                    threshold = conf["command"][index_of_terminated_pod_gc_threshold[0]].split("=")
                    if int(threshold[1]) > 0:
                        return CheckResult.PASSED
                    else:
                        return CheckResult.FAILED
                return CheckResult.FAILED
        return CheckResult.PASSED


check = KubeControllerManagerTerminatedPods()
