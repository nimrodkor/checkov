from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class StorageAccountEnablesSecureTransfer(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that storage account enables secure transfer"
        id = "CKV_AZURE_135"
        supported_resources = ['azurerm_storage_account']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "enable_https_traffic_only"

    def scan_resource_conf(self, conf):
        enable_https_traffic_only = conf.get("enable_https_traffic_only", [True])
        if enable_https_traffic_only[0]:
            return CheckResult.PASSED
        return CheckResult.FAILED


check = StorageAccountEnablesSecureTransfer()
