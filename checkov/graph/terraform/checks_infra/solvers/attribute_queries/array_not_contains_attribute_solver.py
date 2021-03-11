from .array_contains_attribute_solver import ArrayContainsAttributeSolver


class ArrayNotContainsAttributeSolver(ArrayContainsAttributeSolver):
    operator = 'not_contains'

    def __init__(self, resource_types, attribute, value):
        super().__init__(resource_types=resource_types,
                         attribute=attribute, value=value)

    def _get_operation(self, *args):
        # TODO
        raise NotImplementedError
