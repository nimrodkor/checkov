from checkov.graph.terraform.checks_infra.solvers.connections_solvers.base_connection_solver import BaseConnectionSolver
from checkov.graph.terraform.checks_infra.solvers.connections_solvers.connection_exists_solver import ConnectionExistsSolver

class ConnectionNotExistsSolver(BaseConnectionSolver):
    operator = 'not_exists'

    def __init__(self, resource_types, connected_resources_types, vertices_under_resource_types=None, vertices_under_connected_resources_types=None):
        super().__init__(resource_types, connected_resources_types, vertices_under_resource_types, vertices_under_connected_resources_types)

    def run(self, graph_connector):
        connection_exists_solver = ConnectionExistsSolver(self.resource_types, self.connected_resources_types)
        passed, failed = connection_exists_solver.run(graph_connector)
        return failed, passed

