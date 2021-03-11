import re

from checkov.graph.checks.checks_infra.enums import SolverType
from checkov.graph.checks.checks_infra.solvers.base_solver import BaseSolver

WILDCARD_PATTERN = re.compile(r"(\S+[.][*][.]*)+")


class BaseAttributeSolver(BaseSolver):
    operator = ''

    def __init__(self, resource_types, attribute, value):
        super().__init__(SolverType.ATTRIBUTE)
        self.resource_types = resource_types
        self.attribute = attribute
        self.value = value

    def run(self, graph_connector):
        # TODO
        return [], []

    def get_operation(self, **kwargs):
        # TODO
        raise NotImplementedError

    def _get_operation(self, *args):
        pass
