from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class SchedulerBindAddress(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.4.2
        id = "CKV_K8S_115"
        name = "Ensure that the --bind-address argument is set to 127.0.0.1"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if "command" in conf:
            if "kube-scheduler" in conf["command"]:     
                for cmd in conf["command"]:
                    if "=" in cmd:
                        [key,value] = cmd.split("=")
                        if key == "--bind-address" and value == "127.0.0.1":
                            return CheckResult.PASSED

        return CheckResult.FAILED


check = SchedulerBindAddress()
