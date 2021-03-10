import unittest
import hcl2

from checkov.common.models.enums import CheckResult
from checkov.terraform.checks.resource.azure.LogAnalyticsStorageInsightsTableNames import check


class TestLogAnalyticsStorageInsightsTableNames(unittest.TestCase):

    def test_failure(self):
        hcl_res = hcl2.loads("""
                    resource "azurerm_log_analytics_storage_insights" "example" {
                      name                = "someName"
                      resource_group_name = azurerm_resource_group.example.name
                      workspace_id        = azurerm_log_analytics_workspace.example.id
                    
                      storage_account_id  = azurerm_storage_account.example.id
                      storage_account_key = azurerm_storage_account.example.primary_access_key
                    }
                """)
        resource_conf = hcl_res['resource'][0]['azurerm_log_analytics_storage_insights']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        hcl_res = hcl2.loads("""
                    resource "azurerm_log_analytics_storage_insights" "example" {
                      name                = "someName"
                      resource_group_name = azurerm_resource_group.example.name
                      workspace_id        = azurerm_log_analytics_workspace.example.id
                    
                      storage_account_id  = azurerm_storage_account.example.id
                      storage_account_key = azurerm_storage_account.example.primary_access_key
                      table_names= ["name1","name2"]
                    }
                """)
        resource_conf = hcl_res['resource'][0]['azurerm_log_analytics_storage_insights']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()
