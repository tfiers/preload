from importlib import import_module
from typing import Iterable


def preload_with_feedback(module_names: Iterable[str]):
    print("Importing:")
    for module_name in module_names:
        print(f" - {module_name}.. ", end="", flush=True)
        import_module(module_name)
        print("✓")
