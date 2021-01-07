import sys
from importlib import import_module
from time import time as time
from typing import Iterable
from warnings import warn


def preload(module_names: Iterable[str], show_timing=False):
    """
    Import heavy modules, so that subsequent import statements run quickly.

    Should be called at the very start of your program. The user is informed of
    progress by print statements; this feedback avoids the impression that your
    programming is "hanging" at the start.

    :param module_names:  For example `("numpy", "matplotlib.pyplot")`.
    """
    print("Preloading:", end="\n" if show_timing else " ")
    for i, module_name in enumerate(module_names):
        if module_name in sys.modules:
            warn(
                f'Module "{module_name}" has already been imported. Make sure to import'
                "and call `preload` at the very start of your program, before any other"
                "import statements."
            )

        if show_timing:
            print(f" - {module_name} … ", end="", flush=True)
            t0 = time()
            import_module(module_name)
            Δt = time() - t0
            print(f"({Δt:.2f} s)")
        else:
            print(module_name if i == 0 else f", {module_name}", end="", flush=True)
            import_module(module_name)

    if show_timing:
        print("") # blank line
    else:
        print(".")
