from checkov.graph.checks.checks_infra.solvers.attribute_queries.base_attribute_solver import BaseAttributeSolver


class ArrayContainsAttributeSolver(BaseAttributeSolver):
    operator = 'contains'

    def __init__(self, resource_types, attribute, value):
        super().__init__(resource_types=resource_types,
                         attribute=attribute, value=value)

    def _get_operation(self, vertex, attribute):
        return isinstance(vertex.get(attribute), list) and self.value in vertex.get(attribute)

