from checkov.common.models.consts import ANY_VALUE
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class CosmosDBDisablesPublicNetwork(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that Azure Cosmos DB disables public network access"
        id = "CKV_AZURE_101"
        supported_resources = ['azurerm_batch_account']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'public_network_access_enabled'

    def get_expected_value(self):
        return False


check = CosmosDBDisablesPublicNetwork()
