from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories
from checkov.common.models.consts import ANY_VALUE


class CodeBuildEncrypted(BaseResourceValueCheck):

    def __init__(self):
        name = "Ensure that CodeBuild projects are encrypted"
        id = "CKV_AWS_150"
        supported_resources = ['aws_codebuild_project']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "encryption_key"

    def get_expected_value(self):
        return ANY_VALUE


check = CodeBuildEncrypted()
