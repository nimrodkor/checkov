from checkov.graph.terraform.checks_infra.solvers.connections_solvers.base_connection_solver import BaseConnectionSolver
from networkx.classes.digraph import DiGraph
from networkx import edge_dfs
from checkov.graph.graph_builder.graph_components.attribute_names import CustomAttributes


class ConnectionExistsSolver(BaseConnectionSolver):
    operator = 'exists'

    def __init__(self, resource_types, connected_resources_types, vertices_under_resource_types=None, vertices_under_connected_resources_types=None):
        super().__init__(resource_types, connected_resources_types, vertices_under_resource_types, vertices_under_connected_resources_types)

    def run(self, graph_connector: DiGraph):
        passed, failed = [], []
        for u, v in edge_dfs(graph_connector):
            origin_attributes = graph_connector.nodes(data=True)[u]
            destination_attributes = graph_connector.nodes(data=True)[v]
            origin_type = origin_attributes.get(CustomAttributes.RESOURCE_TYPE)
            destination_type = destination_attributes.get(CustomAttributes.RESOURCE_TYPE)
            if origin_type in self.resource_types and destination_type in self.connected_resources_types:
                passed.extend([origin_attributes, destination_attributes])
            else:
                failed.extend([origin_attributes, destination_attributes])
        for v, v_data in graph_connector.nodes(data=True):
            if graph_connector.degree(v) == 0:
                failed.append(v_data)
        # TODO handle output value
        return passed, failed
