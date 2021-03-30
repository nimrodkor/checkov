import unittest

from dockerfile_parse import DockerfileParser

from checkov.common.models.enums import CheckResult
from checkov.dockerfile.checks.UserExists import check


class TestUserExists(unittest.TestCase):

    def test_failure(self):
        dfp = DockerfileParser()
        dfp.content = """\
        From  base
        LABEL foo="bar baz"
        """
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual((CheckResult.FAILED,None), scan_result)

    def test_success(self):
        dfp = DockerfileParser()
        dfp.content = """\
        From  base
        LABEL foo="bar baz"
        USER  me
        HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1 
        """
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual((CheckResult.FAILED,None), scan_result)
