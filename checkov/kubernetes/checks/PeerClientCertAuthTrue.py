from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class PeerClientCertAuthTrue(BaseK8Check):

    def __init__(self):
        name = "Ensure that the --peer-client-cert-auth argument is set to true"
        id = "CKV_K8S_121"
        supported_kind = ['Pod']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def get_resource_id(self, conf):
        print(conf)
        print('================')
        # return f'{conf["parent"]} - {conf["name"]}'
        return "containers"

    def scan_spec_conf(self, conf, entity_type=None):
        return CheckResult.FAILED


check = PeerClientCertAuthTrue()
