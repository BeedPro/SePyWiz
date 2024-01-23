import subprocess
from .config import Config


class PackageManager:
    """
    A class for managing package installation on a Debian-based system using APT.

        Attributes:
        __config (Config): An instance of the Config class for package configuration.

        Methods:
        install_packages(): Install a list of packages defined in the configuration.
    """

    def __init__(self) -> None:
        """
        Initialize the PackageManager object.

        This constructor initializes the PackageManager class and creates an instance
        of the Config class to manage package configuration.
        """
        self.__config: Config = Config()

    def __is_package_installed(self, name: str) -> bool:
        """
        Check if a package is already installed.

        Args:
        name (str): The name of the package to check.

        Returns:
        bool: True if the package is installed, False otherwise.
        """
        if not name:
            raise ValueError("Name is an empty string")
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
        """
        Install a package using APT.

        Args:
        name (str): The name of the package to install.

        Returns:
        bool: True if the package was successfully installed, False otherwise.
        """
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
        """
        Install a list of packages defined in the configuration.

        This method retrieves the list of packages to install from the Config class
        and iterates through them, checking if each package is already installed or
        installing it if not.
        """
        packages_to_install = self.__config.get_packages_to_install()
        for package in packages_to_install:
            if self.__is_package_installed(package):
                print(f"Package {package} has already been installed")
            else:
                self.__install_package(package)
