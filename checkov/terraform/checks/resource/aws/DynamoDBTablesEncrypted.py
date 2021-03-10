from abc import ABC

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class DynamoDBTablesEncrypted(BaseResourceCheck):
    def __init__(self):
        name = "Ensure DynamoDB Tables are encrypted"
        id = "CKV_AWS_111"
        supported_resources = ['aws_dynamodb_table']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf, entity_type):
        if 'server_side_encryption' in conf.keys():
            enabled = conf['server_side_encryption'][0]['enabled'][0]
            if enabled:
                return CheckResult.PASSED
            else:
                return CheckResult.FAILED
        return CheckResult.FAILED


check = DynamoDBTablesEncrypted()
