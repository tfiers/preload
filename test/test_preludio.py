from _pytest.capture import CaptureFixture


def test(capsys: CaptureFixture):
    """ Make sure no errors are raised when using package as intended. """

    # Prevent pytest from swallowing stdout
    with capsys.disabled():
        from preludio import preload_with_feedback

        preload_with_feedback(["sys", "os.path"])
