from networkx.classes.digraph import DiGraph
from checkov.common.graph.checks_infra.enums import SolverType
from checkov.terraform.checks_infra.solvers.connections_solvers.complex_connection_solver import ComplexConnectionSolver
from checkov.terraform.graph_builder.graph_components.attribute_names import CustomAttributes


class OrConnectionSolver(ComplexConnectionSolver):
    operator = 'or'

    def __init__(self, queries, operator):
        super().__init__(queries, operator)

    def get_operation(self, graph_connector: DiGraph):
        attribute_queries = [sub_query for sub_query in self.queries if
                             sub_query.solver_type in [SolverType.ATTRIBUTE, SolverType.COMPLEX]]
        passed_attributes, failed_attributes = [], []
        for attribute_query in attribute_queries:
            passed_query, failed_query = attribute_query.run(graph_connector)
            passed_attributes.extend(passed_query)
            failed_attributes.extend(failed_query)
            failed_attributes = [f for f in failed_attributes if
                                 f[CustomAttributes.ID] not in [p[CustomAttributes.ID] for p in passed_attributes]]

        passed, failed = passed_attributes, failed_attributes
        connection_queries = [sub_query for sub_query in self.queries if
                              sub_query.solver_type in [SolverType.CONNECTION, SolverType.COMPLEX_CONNECTION]]
        passed_connections, failed_connections = [], []
        failed_by_hash = {}
        for connection_query in connection_queries:
            connection_query.set_vertices(graph_connector, [])
            passed_query, failed_query = connection_query.get_operation(graph_connector)
            passed_connections.extend(passed_query)
            for f in failed_query:
                if f[CustomAttributes.ID] not in [p[CustomAttributes.ID] for p in passed_connections]:
                    if not failed_by_hash.get(f[CustomAttributes.HASH]):
                        failed_by_hash[f[CustomAttributes.HASH]] = {"v": f, "count": 0}
                    failed_by_hash[f[CustomAttributes.HASH]]["count"] += 1

        for data in failed_by_hash.values():
            if data["count"] == len(connection_queries) or data["v"] not in passed_connections:
                failed.append(data["v"])

        passed.extend(passed_connections)
        failed = [f for f in failed if
                  f[CustomAttributes.ID] not in [p[CustomAttributes.ID] for p in passed]]

        return self.filter_results(passed, failed)
