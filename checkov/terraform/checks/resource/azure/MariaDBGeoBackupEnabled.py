from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class MariaDBGeoBackupEnabled(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that MariaDB server enables geo-redundant backups"
        id = "CKV_AZURE_129"
        supported_resources = ['azurerm_mariadb_server']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'geo_redundant_backup_enabled'

    def get_expected_value(self):
        return True
    

check = MariaDBGeoBackupEnabled()
