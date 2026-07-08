import platform
import shutil


def is_command_available(command: str) -> bool:
    return shutil.which(command) is not None


def get_python_version() -> str:
    return platform.python_version()


def get_app_name() -> str:
    return "Bootcamp Environment Checker"


def get_operating_system() -> str:
    return platform.system()


def get_tool_status(commands: list[str]) -> dict[str, bool]:
    return {command: is_command_available(command) for command in commands}


def main() -> None:
    print(get_app_name())
    print(f"Python version: {get_python_version()}")
    print(f"Operating system: {get_operating_system()}")

    tool_statuses = get_tool_status(["git", "docker"])

    for command, is_available in tool_statuses.items():
        print(f"{command.capitalize()} available: {is_available}")


if __name__ == "__main__":
    main()
