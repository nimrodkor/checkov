from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class KubeletReadOnlyPort(BaseK8Check):
    def __init__(self):
        # CIS-1.6 4.2.4
        id = "CKV_K8S_141"
        name = "Ensure that the --read-only-port argument is set to 0"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "kubelet" in conf["command"]:            
                if "--read-only-port=0" not in conf["command"]:
                    return CheckResult.FAILED

        return CheckResult.PASSED


check = KubeletReadOnlyPort()
