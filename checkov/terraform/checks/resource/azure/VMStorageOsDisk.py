from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class VMStorageOsDisk(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Virtual Machines use managed disks"
        id = "CKV_AZURE_92"
        supported_resources = ['azurerm_virtual_machine']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        storage_os_disk = conf.get('storage_os_disk')
        storage_data_disk = conf.get('storage_data_disk')
        if storage_os_disk and 'vhd_uri' in storage_os_disk[0]:
            return CheckResult.PASSED
        if storage_data_disk and 'vhd_uri' in storage_data_disk[0]:
            return CheckResult.PASSED
        return CheckResult.FAILED


check = VMStorageOsDisk()
