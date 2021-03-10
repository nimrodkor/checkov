import unittest

import hcl2

from checkov.terraform.checks.resource.aws.CloudwatchLogGroupEncryption import check
from checkov.common.models.enums import CheckResult


class TestCloudwatchLogGroupEncryption(unittest.TestCase):

    def test_failure(self):
        hcl_res = hcl2.loads("""
                resource "aws_cloudwatch_log_group" "test_failed" {
                      name = "Yada"
                    }
                """)
        resource_conf = hcl_res['resource'][0]['aws_cloudwatch_log_group']['test_failed']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)


    def test_success(self):
        hcl_res = hcl2.loads("""
              resource "aws_cloudwatch_log_group" "test_success" {
                        name = "Yada"
                        kms_key_id = "arn:aws:kms:us-west-2:123456789012:key/02efk00b-a10f-4a4f-8c60-90f8e2812f97"
                    }
                """)
        resource_conf = hcl_res['resource'][0]['aws_cloudwatch_log_group']['test_success']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()
