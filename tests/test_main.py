from main import get_app_name, get_python_version, get_operating_system


def test_get_app_name() -> None:
    assert get_app_name() == "Bootcamp Environment Checker"


def test_get_python_version_returns_a_version_string() -> None:
    version = get_python_version()

    assert isinstance(version, str)
    assert version.count(".") >= 1


def test_get_operating_system_returns_a_nonempty_string() -> None:
    operating_system = get_operating_system()

    assert isinstance(operating_system, str)
    assert operating_system
