from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check

class EtcdPeerCertAndKey(BaseK8Check):
    def __init__(self):
        # CIS-1.6 2.4
        id = "CKV_K8S_119"
        name = "Ensure that the --peer-cert-file and --peer-key-file arguments are set as appropriate"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def get_resource_id(self, conf):
        return f'{conf["parent"]} - {conf["name"]}'

    def scan_spec_conf(self, conf):
        if conf.get("command") is not None:
            if "etcd" in conf["command"]:
                hasCertCommand = False
                hasKeyCommand = False
                for command in conf["command"]:
                    if command.startswith("--peer-cert-file"):
                        hasCertCommand = True
                    elif command.startswith("--peer-key-file"):
                        hasKeyCommand = True
                    if hasCertCommand and hasKeyCommand:
                        return CheckResult.PASSED
                return CheckResult.FAILED
           
        return CheckResult.PASSED

check = EtcdPeerCertAndKey()