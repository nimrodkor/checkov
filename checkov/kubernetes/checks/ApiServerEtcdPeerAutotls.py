from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class ApiServerEtcdPeerAutotls(BaseK8Check):
    def __init__(self):
        # CIS-1.6 2.6
        id = "CKV_K8S_122"
        name = "Ensure that the --peer-auto-tls argument is not set to true"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "etcd" in conf["command"]:
                if "--peer-auto-tls=true" in conf["command"]:
                    return CheckResult.FAILED

        return CheckResult.PASSED


check = ApiServerEtcdPeerAutotls()
