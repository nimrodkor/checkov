from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class AzureDefenderOnAppServices(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Azure Defender is set to On for App Service"
        id = "CKV2_AZURE_2"
        supported_resources = ['azurerm_security_center_subscription_pricing']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if conf.get('resource_type')[0] == 'AppServices':
            if conf.get('tier')[0] == 'Standard':
                return CheckResult.PASSED
            return CheckResult.FAILED

        return CheckResult.PASSED


check = AzureDefenderOnAppServices()