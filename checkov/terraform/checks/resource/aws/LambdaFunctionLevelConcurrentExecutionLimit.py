from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class LambdaFunctionLevelConcurrentExecutionLimit(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that AWS Lambda function is configured for function-level concurrent execution limit"
        id = "CKV_AWS_115"
        supported_resources = ['aws_lambda_function']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "reserved_concurrent_executions"

    def get_expected_value(self):
        return "0"


check = LambdaFunctionLevelConcurrentExecutionLimit()
