from networkx.classes.digraph import DiGraph

from checkov.common.graph.checks_infra.enums import SolverType
from checkov.terraform.checks_infra.solvers.connections_solvers.complex_connection_solver import ComplexConnectionSolver
from checkov.terraform.graph_builder.graph_components.attribute_names import CustomAttributes


class AndConnectionSolver(ComplexConnectionSolver):
    operator = 'and'

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
            passed_attributes = [p for p in passed_attributes if
                      p[CustomAttributes.ID] not in [f[CustomAttributes.ID] for f in failed_attributes]]

        passed, failed = passed_attributes, failed_attributes
        connection_queries = self.get_sorted_connection_queries()
        passed_connections, failed_connections = [], []
        for connection_query in connection_queries:
            connection_query.set_vertices(graph_connector, failed_attributes+failed_connections)
            passed_query, failed_query = connection_query.get_operation(graph_connector)
            passed_connections.extend(passed_query)
            failed_connections.extend(failed_query)
            passed_connections = [p for p in passed_connections if
                      p[CustomAttributes.ID] not in [f[CustomAttributes.ID] for f in failed_connections]]

        passed.extend(passed_connections)
        failed.extend(failed_connections)
        passed = [p for p in passed if
                              p[CustomAttributes.ID] not in [f[CustomAttributes.ID] for f in failed]]
        passed = [p for p in passed if
                  p[CustomAttributes.ID] in [pt[CustomAttributes.ID] for pt in passed_attributes] and p[
                      CustomAttributes.ID] in [pt[CustomAttributes.ID] for pt in passed_connections]]

        return self.filter_results(passed, failed)

    def _get_operation(self, *args, **kwargs):
        pass



