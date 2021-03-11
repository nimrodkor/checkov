from checkov.graph.terraform.checks_infra.solvers.attribute_queries.base_attribute_solver import BaseAttributeSolver


class NotStartingWithAttributeSolver(BaseAttributeSolver):
    operator = 'not_starting_with'

    def __init__(self, resource_types, attribute, value):
        super().__init__(resource_types=resource_types,
                         attribute=attribute, value=value)

    def _get_operation(self):
        # TODO
        raise NotImplementedError
