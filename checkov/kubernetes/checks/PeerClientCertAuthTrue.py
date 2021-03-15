from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class PeerClientCertAuthTrue(BaseK8Check):

    def __init__(self):
        name = "Ensure that the --peer-client-cert-auth argument is set to true"
        id = "CKV_K8S_121"
        supported_kind = ['containers']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def get_resource_id(self, conf):
        if "namespace" in conf["metadata"]:
            return "{}.{}.{}".format(conf["kind"], conf["metadata"]["name"], conf["metadata"]["namespace"])
        else:
            return "{}.{}.default".format(conf["kind"], conf["metadata"]["name"])

    def scan_spec_conf(self, conf, entity_type=None):
        # check if name is etcd if not return unknown
        # check containers for --peer shit is set to true
        print('============')
        print(conf)
        print('============')
        return CheckResult.FAILED


check = PeerClientCertAuthTrue()
