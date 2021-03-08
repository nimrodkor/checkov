from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class ConfigConfigurationAggregator(BaseResourceCheck):
    def __init__(self):
        name = "Ensure AWS Config is enabled in all regions"
        id = "CKV2_AWS_6"
        supported_resources = ['aws_config_configuration_aggregator']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for account_aggregation_source /  organization_aggregation_source
            at aws_config_configuration_aggregator:
            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/config_configuration_aggregator#account-based-aggregation
        :param conf: aws_config_configuration_aggregator configuration
        :return: <CheckResult>
        """
        self.evaluated_keys = ["account_aggregation_source", "organization_aggregation_source"]

        if "account_aggregation_source" in conf:
            current_regions = []
            for sublist in conf.get("account_aggregation_source", {})[0].get("regions"):
                for item in sublist:
                    current_regions.append(item)
            regions = ["us-east-2", "us-east-1", "us-west-1", "us-west-2"]  # do i need to set all of the regions?
            if set(current_regions) == set(regions):
                return CheckResult.PASSED
            return CheckResult.FAILED
        if "organization_aggregation_source":
            if conf.get("organization_aggregation_source", {})[0].get("all_regions"):
                return CheckResult.PASSED
            return CheckResult.FAILED


check = ConfigConfigurationAggregator()
