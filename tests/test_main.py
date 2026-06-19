from main import (
    get_app_name,
    get_operating_system,
    get_python_version,
    get_tool_status,
    is_command_available,
)


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


def test_is_command_available_returns_true_for_git() -> None:
    assert is_command_available("git") is True


def test_is_command_available_returns_false_for_missing_command() -> None:
    assert is_command_available("command_that_should_not_exist_12345") is False


def test_get_tool_status_returns_status_for_each_command() -> None:
    statuses = get_tool_status(
        ["git", "command_that_should_not_exist_12345"]
    )

    assert statuses == {
        "git": True,
        "command_that_should_not_exist_12345": False,
    }
