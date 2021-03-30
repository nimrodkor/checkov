import unittest

from dockerfile_parse import DockerfileParser

from checkov.common.models.enums import CheckResult
from checkov.dockerfile.checks.UpdateNotAlone import check


class TestUpdateNotAlon(unittest.TestCase):

    def test_failure(self):
        dfp = DockerfileParser()
        dfp.content = """\
        RUN apk update
        """
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual(CheckResult.FAILED, scan_result[0])

    def test_success(self):
        dfp = DockerfileParser()
        dfp.content = """\
        RUN apt-get update \
            && apt-get install -y --no-install-recommends foo \
            && echo gooo
        RUN apk update \
            && apk add --no-cache suuu looo
        RUN apk --update add moo
        """
        scan_result = check.scan_entity_conf(dfp.structure)
        self.assertEqual(CheckResult.PASSED, scan_result[0])
