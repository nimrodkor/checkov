import unittest

from checkov.common.models.enums import CheckResult
from checkov.terraform.checks.resource.aws.APIGatewayCacheEnable import check


class TestAPIGatewayCacheEnable(unittest.TestCase):

    def test_failure(self):
        resource_conf = {'rest_api_id': ['${example_id}']}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        resource_conf = {'rest_api_id': ['${example_id}'],
                         'cache_cluster_enabled': [True]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

if __name__ == '__main__':
    unittest.main()
