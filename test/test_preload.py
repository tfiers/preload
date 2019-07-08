# fmt: off

MODULES = ["matplotlib.pyplot", "scipy.signal"]


def normal_usage():
    from preload import preload
    preload(MODULES)
    print("Hello")


def test_normal_usage(capsys):
    # Prevent pytest from swallowing stdout, so we can see what it looks like
    # for the user.
    with capsys.disabled():
        from preload import __version__
        print(f"Preload version {__version__}")
        import sys
        for module in MODULES:
            assert module not in sys.modules
        normal_usage()
        for module in MODULES:
            assert module in sys.modules


# Avoid PyCharm removing the unused import:
# noinspection PyUnresolvedReferences
def test_already_imported():
    from preload import preload
    import pytest
    import scipy
    with pytest.warns(UserWarning, match="already been imported"):
        preload(["scipy"])


if __name__ == '__main__':
    normal_usage()
