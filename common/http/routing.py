import importlib


class MissingBluePrint(Exception):
    ...


def include(module_path: str, bp_name: str = 'bp'):
    try:
        return getattr(importlib.import_module(module_path), bp_name)
    except AttributeError:
        raise MissingBluePrint(f'Cannot find blueprint in this path: {module_path}')