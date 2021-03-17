from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class MariaDBGeoBackupEnabled(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that MariaDB server enables geo-redundant backups"
        id = "CKV_AZURE_129"
        supported_resources = ['azurerm_mariadb_server']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'geo_redundant_backup_enabled' not in conf: 
            return CheckResult.FAILED
        else:
            if  conf['geo_redundant_backup_enabled'][0]:
                return CheckResult.PASSED
            else:
                return CheckResult.FAILED

    

check = MariaDBGeoBackupEnabled()
