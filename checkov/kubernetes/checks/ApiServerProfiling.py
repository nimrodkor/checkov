from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check

class ApiServerProfiling(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.2.21
        id = "CKV_K8S_90"
        name = "Ensure that the --profiling argument is set to false"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "kube-apiserver" in conf["command"]:
                if "--profiling=true" in conf["command"] or "--profiling=false" not in conf["command"]:
                    return CheckResult.FAILED
           
        return CheckResult.PASSED

check = ApiServerProfiling()