import platform


def get_python_version() -> str:
    return platform.python_version()


def get_app_name() -> str:
    return "Bootcamp Environment Checker"


def get_operating_system() -> str:
    return platform.system()


def main() -> None:
    print(get_app_name())
    print(f"Python version: {get_python_version()}")
    print(f"Operating system: {get_operating_system()}")


if __name__ == "__main__":
    main()
