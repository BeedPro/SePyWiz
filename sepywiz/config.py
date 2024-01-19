import os
import json
from typing import Any, Dict, List


class Config:
    """
    Config is a class for managing configuration settings for SePyWiz.

    Attributes:
        None

    Methods:
        None
    """

    def __init__(self) -> None:
        """
        Initialize the Config instance with default configuration settings.
        """
        self.__colors: Dict[str, str] = {
            "orange": "#FFC170",
            "black": "#696363",
            "teal": "#84DCCF",
            "blue": "#A6D9F7",
            "grey": "#BCCCE0",
            "pink": "#BF98A0",
        }
        self.__app_install_path: str = "data/applications_to_install.json"
        self.__pack_man_name: str = "apt_packages"
        self.__data: Any = self.__load_data()
        self.__menu_options: List[str] = [
            "i",
            "f",
            "s",
            "d",
            "q",
            "install",
            "fonts",
            "sync",
            "delete",
            "quit",
        ]
        self.__install_options: List[str] = ["p", "a"]

    def __load_data(self) -> Any:
        """
        Load configuration data from a JSON file if it exists, or return an empty dictionary if the file is not found.

        Returns:
            Any: Configuration data loaded from the JSON file or an empty dictionary.
        """
        if os.path.exists(self.__app_install_path):
            with open(self.__app_install_path, "r") as json_file:
                return json.load(json_file)
        else:
            return {}

    def get_packages_to_install(self) -> Any:
        """
        Get a list of packages to install from the configuration data.

        Returns:
            Any: A list of packages to install.
        """
        return self.__data.get(self.__pack_man_name, [])

    def get_colors(self) -> Dict[str, str]:
        """
        Get a dictionary of color names and their corresponding hexadecimal values.

        Returns:
            Dict[str, str]: A dictionary containing color names as keys and hexadecimal color values as values.
        """
        return self.__colors

    def get_valid_menu_options(self) -> List[str]:
        """
        Get a list of valid menu options for the application.

        Returns:
            List[str]: A list of valid menu options.
        """
        return self.__menu_options

    def get_valid_install_options(self) -> List[str]:
        """
        Get a list of valid installation options for packages.

        Returns:
            List[str]: A list of valid installation options.
        """
        return self.__install_options
