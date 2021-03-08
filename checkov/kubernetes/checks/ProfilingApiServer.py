from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check

class ProfilingApiServer(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.2.21
        id = "CKV2_K8S_42"
        name = "Ensure that the --profiling argument is set to false (Scored)"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['pod']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def scan_spec_conf(self, conf):
        results = []
        if "spec" in conf:
            if "containers" in conf["spec"]:
                for container in conf["spec"]["containers"]:
                    if "command" in container:
                        if "--profiling=false" in container["command"]:
                            results.append(True)
                        else results.append(False)
                    else results.append(False)
           
        return CheckResult.FAILED if False in results else CheckResult.PASSED

check = ProfilingApiServer()