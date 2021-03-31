from abc import abstractmethod

from checkov.common.graph.checks_infra.enums import SolverType
from checkov.terraform.checks_infra.solvers.connections_solvers.base_connection_solver import BaseConnectionSolver
from networkx.classes.digraph import DiGraph

from checkov.terraform.graph_builder.graph_components.attribute_names import CustomAttributes


class ComplexConnectionSolver(BaseConnectionSolver):
    operator = ''

    def __init__(self, queries, operator):
        self.solver_type = SolverType.COMPLEX_CONNECTION
        if queries is None:
            queries = []
        self.queries = queries
        self.operator = operator

        resource_types = []
        connected_resources_types = []
        for sub_query in self.queries:
            if sub_query.solver_type in [SolverType.CONNECTION, SolverType.COMPLEX_CONNECTION]:
                resource_types.extend(sub_query.resource_types)
                connected_resources_types.extend(sub_query.connected_resources_types)
            elif sub_query.solver_type in [SolverType.ATTRIBUTE]:
                resource_types.extend(sub_query.resource_types)
        resource_types = list(set(resource_types))
        connected_resources_types = list(set(connected_resources_types))

        super().__init__(resource_types, connected_resources_types)

    @staticmethod
    def filter_duplicates(checks):
        return list({check[CustomAttributes.ID]: check for check in checks}.values())

    def filter_results(self, passed: list, failed: list):
        filters = []
        filter_queries = [sub_query for sub_query in self.queries if sub_query.solver_type == SolverType.FILTER]
        for sub_query in filter_queries:
            filters.append(sub_query._get_operation())
        if filters:
            for query_filter in filters:
                passed = list(filter(query_filter, passed))
                failed = list(filter(query_filter, failed))
        passed = self.filter_duplicates(passed)
        failed = self.filter_duplicates(failed)
        return passed, failed

    def get_sorted_connection_queries(self):
        connection_queries = [sub_query for sub_query in self.queries if
                              sub_query.solver_type in [SolverType.CONNECTION, SolverType.COMPLEX_CONNECTION]]
        filter_queries = [sub_query for sub_query in self.queries if sub_query.solver_type == SolverType.FILTER]

        resource_types_to_filter = []
        for filter_query in filter_queries:
            if filter_query.query_attribute == 'resource_type':
                resource_types_to_filter.extend(filter_query.query_value)

        sorted_connection_queries = []
        connection_queries_with_filtered_resource_types = []
        for connection_query in connection_queries:
            if any(r in resource_types_to_filter for r in connection_query.resource_types + connection_query.connected_resources_types):
                connection_queries_with_filtered_resource_types.append(connection_query)
            else:
                sorted_connection_queries.append(connection_query)

        sorted_connection_queries.extend(connection_queries_with_filtered_resource_types)
        return sorted_connection_queries

    def run_attribute_queries(self, graph_connector):
        attribute_queries = [sub_query for sub_query in self.queries if
                             sub_query.solver_type in [SolverType.ATTRIBUTE, SolverType.COMPLEX]]
        passed_attributes, failed_attributes = [], []
        for attribute_query in attribute_queries:
            passed_query, failed_query = attribute_query.run(graph_connector)
            passed_attributes.extend(passed_query)
            failed_attributes.extend(failed_query)
        return passed_attributes, failed_attributes
