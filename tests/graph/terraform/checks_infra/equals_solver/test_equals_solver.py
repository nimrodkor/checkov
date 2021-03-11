import os
from unittest import TestCase

from checkov.graph.graph_builder.graph_components.attribute_names import SourceTypes
from checkov.graph.terraform.checks_infra.nx_checks_parser import NXGraphCheckParser
from checkov.graph.terraform.runner import Runner
from checkov.graph.terraform.checks_infra.registry import Registry
from checkov.runner_filter import RunnerFilter
from tests.graph.terraform.checks_infra.utils import verify_report

TEST_DIRNAME = os.path.dirname(os.path.realpath(__file__))


class TestEqualsSolver(TestCase):
    def setUp(self):
        os.environ['UNIQUE_TAG'] = ''
        os.environ['STRATEGY_TYPE'] = 'partition'
        os.environ['CHECK_PUBLIC_PRIVATE'] = "true"
        self.source = SourceTypes.TERRAFORM
        self.registry = Registry(parser=NXGraphCheckParser(), checks_dir=TEST_DIRNAME)
        self.runner = Runner(checks_registry=self.registry)
        self.runner_filter = RunnerFilter(checks="RUN_ONLY_GRAPH")

    def run_test(self, root_folder, expected_results):
        report = self.runner.run(root_folder=root_folder, runner_filter=self.runner_filter)
        verification_results = verify_report(report=report, expected_results=expected_results)
        self.assertIsNone(verification_results, verification_results)

    def test_equals_solver_simple(self):
        root_folder = os.path.realpath(os.path.join(TEST_DIRNAME,
                                                    '../../resources/public_security_groups'))
        check_id = "PublicDBSG"
        should_pass = ['aws_db_security_group.aws_db_security_group_private']
        should_fail = ['aws_db_security_group.aws_db_security_group_public']
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results)

    def test_equals_solver_wildcard(self):
        root_folder = os.path.realpath(os.path.join(TEST_DIRNAME,
                                                    '../../resources/security_group_multiple_rules'))
        check_id = "SGPorts"
        should_pass = ['aws_security_group.sg1']
        should_fail = ['aws_security_group.sg2']
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results)
