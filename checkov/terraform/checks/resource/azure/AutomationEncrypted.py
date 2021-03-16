from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class AutomationEncrypted(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Automation account variables are encrypted"
        id = "CKV_AZURE_73"
        supported_resources = ['azurerm_automation_variable_bool','azurerm_automation_variable_string', 'azurerm_automation_variable_int', 'azurerm_automation_variable_datetime']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'encrypted' in conf:
            if conf['encrypted'][0]:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = AutomationEncrypted()
