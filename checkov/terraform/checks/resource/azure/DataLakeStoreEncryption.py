from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class DataLakeStoreEncryption(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Data Lake Store accounts enables encryption"
        id = "CKV_AZURE_105"
        supported_resources = ['azurerm_data_lake_store']
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'encryption_state' in conf:
            encryption_state = conf['encryption_state'][0]
            if encryption_state == "Disabled":
                return CheckResult.FAILED
        return CheckResult.PASSED


check = DataLakeStoreEncryption()
