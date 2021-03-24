import os
from tests.graph.terraform.checks_infra.test_base import TestBaseSolver

TEST_DIRNAME = os.path.dirname(os.path.realpath(__file__))


class ConnectionSolver(TestBaseSolver):
    def setUp(self):
        self.checks_dir = TEST_DIRNAME
        super(ConnectionSolver, self).setUp()

    def test_connection_found(self):
        root_folder = '../../../resources/ec2_instance_network_interfaces'
        check_id = "NetworkInterfaceForInstance"
        should_pass = ['aws_instance.foo']
        should_fail = []
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results)

    def test_connection_not_found(self):
        root_folder = '../../../resources/ec2_instance_network_interfaces'
        check_id = "NoNetworkInterfaceForInstance"
        should_pass = ['aws_subnet.my_subnet', 'aws_vpc.my_vpc', 'aws_network_interface.foo', 'aws_subnet.my_subnet', 'aws_network_interface.goo', 'aws_subnet.my_subnet', 'aws_instance.bar', 'aws_vpc.other_vpc']
        should_fail = ['aws_instance.foo', 'aws_network_interface.foo']
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results)