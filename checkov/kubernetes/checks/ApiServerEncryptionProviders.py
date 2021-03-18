
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class ApiServerEncryptionProviders(BaseK8Check):
    def __init__(self):
        # CIS-1.6 1.2.34
        id = "CKV_K8S_104"
        name = "Ensure that the --encryption-provider-config argument is set"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories,
                         supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        keys = []
        values = []
        if "command" in conf:
            for cmd in conf["command"]:
                if "=" in cmd:
                    firstEqual = cmd.index("=")
                    [key, value] = [cmd[:firstEqual], cmd[firstEqual+1:]]
                    keys.append(key)
                    values.append(value)
                else:
                    keys.append(cmd)
                    values.append(None)

        if "kube-apiserver" in keys and "--encryption-provider-config" not in keys:
            return CheckResult.FAILED

        return CheckResult.PASSED


check = ApiServerEncryptionProviders()
