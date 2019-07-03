from _pytest.capture import CaptureFixture


def test(capsys: CaptureFixture):
    """ Make sure no errors are raised when using package as intended. """

    # Prevent pytest from swallowing stdout
    with capsys.disabled():
        from preludio import preload_with_feedback, __version__

        print(f"Preludio version: {__version__}")
        preload_with_feedback(["sys", "os.path"])
