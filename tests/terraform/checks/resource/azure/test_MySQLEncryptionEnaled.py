import unittest

import hcl2

from checkov.terraform.checks.resource.azure.PostgersSQLEncryptionEnaled import check
from checkov.common.models.enums import CheckResult


class TestMySQLEncryptionEnaled(unittest.TestCase):

    def test_failure_1(self):
        hcl_res = hcl2.loads("""
            resource "azurerm_mysql_server" "example" {
              name                = "example-psqlserver"
              location            = azurerm_resource_group.example.location
              resource_group_name = azurerm_resource_group.example.name
            
              administrator_login          = "psqladminun"
              administrator_login_password = "H@Sh1CoR3!"
            
              sku_name   = "GP_Gen5_4"
              version    = "9.6"
              storage_mb = 640000
            
              backup_retention_days        = 7
              infrastructure_encryption_enabled = false
              auto_grow_enabled            = true
              public_network_access_enabled    = true
              ssl_enforcement_enabled          = true
              ssl_minimal_tls_version_enforced = "TLS1_2"
            }
        """)
        resource_conf = hcl_res['resource'][0]['azurerm_mysql_server']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_failure_2(self):
        hcl_res = hcl2.loads("""
            resource "azurerm_mysql_server" "example" {
              name                = "example-psqlserver"
              location            = azurerm_resource_group.example.location
              resource_group_name = azurerm_resource_group.example.name
              administrator_login          = "psqladminun"
              administrator_login_password = "H@Sh1CoR3!"
              sku_name   = "GP_Gen5_4"
              version    = "9.6"
              storage_mb = 640000
              backup_retention_days        = 7
              auto_grow_enabled            = true
              ssl_enforcement_enabled          = true
              ssl_minimal_tls_version_enforced = "TLS1_2"
            }
                """)
        resource_conf = hcl_res['resource'][0]['azurerm_mysql_server']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        hcl_res = hcl2.loads("""
            resource "azurerm_mysql_server" "example" {
              name                = "example-psqlserver"
              location            = azurerm_resource_group.example.location
              resource_group_name = azurerm_resource_group.example.name
              administrator_login          = "psqladminun"
              administrator_login_password = "H@Sh1CoR3!"
              sku_name   = "GP_Gen5_4"
              version    = "9.6"
              storage_mb = 640000
              backup_retention_days        = 7
              infrastructure_encryption_enabled = true
              auto_grow_enabled            = true
              public_network_access_enabled    = false
              ssl_enforcement_enabled          = true
              ssl_minimal_tls_version_enforced = "TLS1_2"
            }
                """)
        resource_conf = hcl_res['resource'][0]['azurerm_mysql_server']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()