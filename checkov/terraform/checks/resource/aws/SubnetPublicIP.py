from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class SubnetPublicIP(BaseResourceCheck):
    def __init__(self):
        name = "Ensure VPC subnets do not assign a public IP by default"
        id = "CKV_AWS_103"
        supported_resources = ['aws_subnet']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        key="map_public_ip_on_launch"
        if key in conf.keys():
            if not conf[key][0]:
                return CheckResult.PASSED
            return CheckResult.FAILED
        else:
            return CheckResult.PASSED


check = SubnetPublicIP()
