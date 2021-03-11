from checkov.graph.checks.checks_infra.solvers.attribute_queries.base_attribute_solver import BaseAttributeSolver
from checkov.graph.checks.checks_infra.solvers.base_solver import VERTEX


class EqualsAttributeSolver(BaseAttributeSolver):
    operator = 'equals'

    def __init__(self, resource_types, attribute, value):
        super().__init__(resource_types=resource_types,
                         attribute=attribute, value=value)

    def _get_operation(self, **kwargs):
        return kwargs[VERTEX].get(kwargs["attribute"]) == self.value
