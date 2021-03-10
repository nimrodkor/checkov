from checkov.common.models.consts import ANY_VALUE
from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class LogAnalyticsStorageInsightsTableNames(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure Storage logging is enabled for Blob service for read requests"
        id = "CKV_AZURE_59"
        supported_resources = ['azurerm_log_analytics_storage_insights']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'table_names'

    def get_expected_value(self):
        return ANY_VALUE


check = LogAnalyticsStorageInsightsTableNames()
