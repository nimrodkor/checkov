from checkov.cloudformation.checks.resource.base_resource_value_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class ELBCrossZoneEnable(BaseResourceCheck):

    def __init__(self):
        name = "Ensure that ELB is cross-zone-load-balancing enabled"
        id = "CKV_AWS_138"
        supported_resources = ['aws_elb']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "cross_zone_load_balancing" in conf:
            if conf["cross_zone_load_balancing"] == False:
                # No addonProfiles option to configure
                return CheckResult.FAILED

        return CheckResult.PASSED


check = ELBCrossZoneEnable()
