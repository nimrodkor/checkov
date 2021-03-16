from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class FunctionAppsAccessibleOverHttps(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure Disks are encrypted at rest"
        id = "CKV_AZURE_51"
        supported_resources = ['azurerm_function_app']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'https_only'

    def get_expected_value(self):
        return True


check = FunctionAppsAccessibleOverHttps()
