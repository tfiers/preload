import sys
from importlib import import_module
from time import time
from typing import Iterable
from warnings import warn


def preload(module_names: Iterable[str]):
    """
    Import heavy modules, so that subsequent import statements run quickly.
    Should be called at the very start of your program. The user is informed of
    progress by print statements; this feedback avoids the impression that your
    programming is "hanging" at the start.
    
    :param module_names:  For example ("scipy.signal", "matplotlib.pyplot").
    """
    print("Importing:")
    for module_name in module_names:
        if module_name not in sys.modules:
            print(f" - {module_name}.. ", end="", flush=True)
            t0 = time()
            import_module(module_name)
            print(f"✓ ({time() - t0:.2f}s)")
        else:
            warn(
                f"""Module "{module_name}" has already been imported. Make sure
                to import and call "preload_with_feedback" before any other
                import statements."""
            )
