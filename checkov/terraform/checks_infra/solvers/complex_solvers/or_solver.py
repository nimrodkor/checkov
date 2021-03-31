from checkov.terraform.checks_infra.solvers.complex_solvers.base_complex_solver import BaseComplexSolver
from functools import reduce
from operator import or_


class OrSolver(BaseComplexSolver):
    operator = 'or'

    def __init__(self, queries, resource_types):
        super().__init__(queries, resource_types)

    def _get_operation(self, *args):
        return reduce(or_, args)

    def get_operation(self, vertex):
        for i, query in enumerate(self.queries):
            pred_result = query.get_operation(vertex)
            if pred_result:
                return pred_result
        return False
