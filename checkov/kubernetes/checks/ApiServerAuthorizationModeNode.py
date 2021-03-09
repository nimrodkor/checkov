from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check

class ApiServerAuthorizationModeNode(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.2.8
        id = "CKV_K8S_75"
        name = "Ensure that the --authorization-mode argument includes Node"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "kube-apiserver" in conf["command"]:
                for command in conf["command"]:
                    if command.startswith("--authorization-mode"):
                        modes = command.split("=")[1]
                        if "Node" not in modes.split(","):
                            return CheckResult.FAILED
                        break
           
        return CheckResult.PASSED

check = ApiServerAuthorizationModeNode()