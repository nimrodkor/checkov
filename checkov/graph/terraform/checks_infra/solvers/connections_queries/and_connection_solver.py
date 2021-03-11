from checkov.graph.terraform.checks_infra.solvers.connections_queries.complex_connection_solver import ComplexConnectionSolver


class AndConnectionSolver(ComplexConnectionSolver):
    operator = 'and'

    def __init__(self, queries, operator):
        super().__init__(queries, operator)

    def get_operation(self, **kwargs):
        # TODO
        raise NotImplementedError

    def filter_results(self, traversal):
        # TODO
        raise NotImplementedError
