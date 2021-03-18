from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class PostgersSQLEncryptionEnaled(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that PostgreSQL server enables infrastructure encryption"
        id = "CKV_AZURE_96"
        supported_resources = ['azurerm_postgresql_server']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'infrastructure_encryption_enabled'

    def get_expected_value(self):
        """
        Returns the default expected value, governed by provider best practices
        """
        return True


check = PostgersSQLEncryptionEnaled()