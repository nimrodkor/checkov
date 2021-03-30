import unittest

from dockerfile_parse import DockerfileParser

from checkov.common.models.enums import CheckResult
from checkov.dockerfile.checks.AddExists import check


class TestAddExists(unittest.TestCase):

    def test_failure(self):
        dfp = DockerfileParser()
        dfp.content = """\
        From  base
        LABEL foo="bar baz"
        ADD http://example.com/package.zip /temp
        USER  me"""
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual((CheckResult.FAILED), scan_result[0])

    def test_success(self):
        dfp = DockerfileParser()
        dfp.content = """\
        From  base
        LABEL foo="bar baz"
        USER  me
        HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1 
        """
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual((CheckResult.PASSED,None), scan_result)
