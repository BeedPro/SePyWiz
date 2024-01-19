import subprocess
from config import Config


class PackageManager:
    def __init__(self) -> None:
        self.__config = Config()

    def __is_package_installed(self, name: str) -> bool:
        try:
            subprocess.run(
                ["dpkg", "-l", name],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def __install_package(self, name: str) -> bool:
        result: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["sudo", "apt", "install", "-y", name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode == 0:
            print(f"{name} has been successfully installed.")
            return True
        else:
            print(f"Error installing {name}. Return code: {result.returncode}")
            print(result.stderr.decode("utf-8"))
            return False

    def install_packages(self):
        packages_to_install = self.__config.get_packages_to_install()
        for package in packages_to_install:
            if self.__is_package_installed(package):
                print(f"Package {package} has already been installed")
            else:
                self.__install_package(package)
