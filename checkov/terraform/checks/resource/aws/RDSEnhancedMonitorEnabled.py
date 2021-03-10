from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_negative_value_check import BaseResourceNegativeValueCheck


class RDSEnhancedMonitorEnabled(BaseResourceNegativeValueCheck):
    def __init__(self):
        name = "Ensure that enhanced monitoring is enabled for Amazon RDS instances"
        id = "CKV_AWS_118"
        supported_resources = ['aws_db_instance']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_attribute_result=CheckResult.FAILED)

    def get_inspected_key(self):
        return 'monitoring_interval'

    def get_forbidden_values(self):
        return [0]


check = RDSEnhancedMonitorEnabled()
