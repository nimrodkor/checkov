from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class MySQLGeoBackupEnabled(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that My SQL server enables geo-redundant backups"
        id = "CKV_AZURE_94"
        supported_resources = ['azurerm_mysql_server']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'geo_redundant_backup_enabled'

    def get_expected_value(self):
        """
        Returns the default expected value, governed by provider best practices
        """
        return True


check = MySQLGeoBackupEnabled()