from checkov.graph.checks.checks_infra.solvers.attribute_queries.base_attribute_solver import BaseAttributeSolver


class AnyResourceSolver(BaseAttributeSolver):
    operator = 'any'

    def __init__(self, resource_types, attribute, value):
        super().__init__(resource_types=resource_types,
                         attribute=attribute, value=value)

    def _get_operation(self, *args):
        # TODO
        raise NotImplementedError
