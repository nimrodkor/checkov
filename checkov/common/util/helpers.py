import os


def _directory_has_init_py(directory):
    """ Check if a given directory contains a file named __init__.py.

    __init__.py is needed to ensure the directory is a Python module, thus
    can be imported.
    """
    if os.path.exists("{}/__init__.py".format(directory)):
        return True
    return False


def _file_can_be_imported(entry):
    """ Verify if a directory entry is a non-magic Python file."""
    if entry.is_file() and not entry.name.startswith('__') and entry.name.endswith('.py'):
        return True
    return False
