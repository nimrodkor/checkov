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
        check_id = "NetworkInterfaceForInstance"
        should_pass = []
        should_fail = ['aws_vpc.other_vpc']
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results)


    # def test_connection_not_found(self):
    #     resources_dir = os.path.join(TEST_DIRNAME, '../../resources/resources_queries/ec2_security_group')
    #     graph, tf_definitions = self.graph_manager.build_graph_from_source_directory(resources_dir)
    #     self.graph_manager.save_graph(graph)
    #     traversal = self.graph_manager.get_reader_traversal()
    #     resources_types = [encode_graph_property_value('aws_instance')]
    #     connected_resources_types = [encode_graph_property_value('aws_vpc')]
    #     connection_exists_query = ConnectionExistsQuery(graph_traversal=traversal, resource_types=resources_types, connected_resources_types=connected_resources_types)
    #     passed, failed = connection_exists_query.run_query()
    #     self.assertEqual(0, len(passed))
    #
    # def test_connections_multiple_resources_types(self):
    #     resources_dir = os.path.join(TEST_DIRNAME, '../../resources/resources_queries/public_virtual_machines')
    #     graph, tf_definitions = self.graph_manager.build_graph_from_source_directory(resources_dir)
    #     self.graph_manager.save_graph(graph)
    #     traversal = self.graph_manager.get_reader_traversal()
    #     resources_types = [encode_graph_property_value('aws_instance')]
    #     connected_resources_types = [encode_graph_property_value('aws_security_group'), encode_graph_property_value('aws_default_security_group')]
    #     connection_exists_query = ConnectionExistsQuery(graph_traversal=traversal,
    #                                                     resource_types=resources_types,
    #                                                     connected_resources_types=connected_resources_types)
    #
    #     expected_to_pass = ['aws_instance.with_open_def_security_groups',
    #                         'aws_instance.with_open_security_groups',
    #                         'aws_instance.with_closed_def_security_groups',
    #                         'aws_security_group.allow_tls',
    #                         'aws_default_security_group.default_security_group_open',
    #                         'aws_default_security_group.default_security_group_closed',
    #                         ]
    #     expected_to_fail = ['aws_instance.with_subnet_public', 'aws_instance.with_subnet_not_public']
    #     passed, failed = connection_exists_query.run_query()
    #     self.assertEqual(6, len(passed))
    #
    #     for p in passed:
    #         if decode_graph_property_value(p[BridgecrewAttributes.ID.value]) not in expected_to_pass:
    #             self.fail(f"{p[BridgecrewAttributes.ID.value]} passed even though it should have failed")
    #
    #     for p in failed:
    #         if decode_graph_property_value(p[BridgecrewAttributes.ID.value]) not in expected_to_fail:
    #             self.fail(f"{p[BridgecrewAttributes.ID.value]} failed even though it should have passed")
