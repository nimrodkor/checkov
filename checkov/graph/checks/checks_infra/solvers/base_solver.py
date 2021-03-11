from abc import abstractmethod

VERTEX = 'vertex'

class BaseSolver:
    operator = ''

    def __init__(self, query_type):
        self.query_type = query_type

    @abstractmethod
    def get_operation(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def _get_operation(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError()

