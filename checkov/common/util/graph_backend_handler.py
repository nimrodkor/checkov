import logging
import os
from enum import Enum
import importlib
from checkov.common.util.helpers import _directory_has_init_py, _file_can_be_imported
import sys

logger = logging.getLogger(__name__)

GRAPH_BACKEND = os.environ.get('GRAPH_BACKEND', 'NETWORKX')


class GraphBackends(Enum):
    TINKERPOP = 'tinkerpop'
    NETWORKX = 'networkx'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


DEFAULT_BACKEND_PACKAGES = {
    GraphBackends.NETWORKX.value: {'module_path': 'graph/db_connectors/networkx',
                                   'class_name': 'NetworkxConnector'}
}


class GraphBackendHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.backends_metadata = {backend: {} for backend, _ in GraphBackends.__members__.items()}
        self.graph_connector = None

    def load_graph_connector(self, args):
        backend_module_path = backend_class_name = ''
        if len(args.graph_backend.split(':')) == 2:
            backend_module_path, backend_class_name = args.graph_backend.split(':')
        else:
            chosen_backend = args.graph_backend
            if chosen_backend in DEFAULT_BACKEND_PACKAGES:
                backend_module_path = DEFAULT_BACKEND_PACKAGES[chosen_backend]['module_path']
                backend_class_name = DEFAULT_BACKEND_PACKAGES[chosen_backend]['class_name']
        directory = os.path.expanduser(os.path.abspath(backend_module_path))
        self.logger.debug(f"Loading graph backend connector from {directory}")
        sys.path.insert(1, directory)

        with os.scandir(directory) as directory_content:
            if not _directory_has_init_py(directory):
                self.logger.info(f"No __init__.py found in {directory}.")
            else:
                for entry in directory_content:
                    if _file_can_be_imported(entry):
                        try:
                            module_name = entry.name.replace('.py', '')
                            self.logger.debug(f"Importing graph db connector {module_name}")
                            module = importlib.import_module(module_name)
                            self.graph_connector = getattr(module, backend_class_name)()
                        except ModuleNotFoundError as e:
                            self.logger.error(f"Failed to import {backend_module_path}/{module_name}, {e}")
                            exit(1)
                        except AttributeError as e:
                            self.logger.error(f"Class name is not found on file {module_name}, {e}")
                            exit(1)
