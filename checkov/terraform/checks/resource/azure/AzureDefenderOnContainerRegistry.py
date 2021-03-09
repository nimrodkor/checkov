from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class AzureDefenderOnContainerRegistry(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Azure Defender is set to On for Container Registries"
        id = "CKV2_AZURE_7"
        supported_resources = ['azurerm_security_center_subscription_pricing']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        return CheckResult.PASSED if conf.get('resource_type')[0] != 'ContainerRegistry' \
                                     or conf.get('tier')[0] == 'Standard' else CheckResult.FAILED


check = AzureDefenderOnContainerRegistry()
