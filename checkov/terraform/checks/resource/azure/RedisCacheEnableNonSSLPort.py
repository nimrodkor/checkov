from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class RedisCacheEnableNonSSLPort(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that only SSL are enabled for Cache for Redis"
        id = "CKV_AZURE_91"
        supported_resources = ['azurerm_redis_cache']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "enable_non_ssl_port" in conf:
            if conf['enable_non_ssl_port'][0]:
                return CheckResult.FAILED
        return CheckResult.PASSED


check = RedisCacheEnableNonSSLPort()
