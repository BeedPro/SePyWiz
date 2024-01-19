import os
import json
from typing import Any, Dict, List


class Config:
    def __init__(self) -> None:
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
        if os.path.exists(self.__app_install_path):
            with open(self.__app_install_path, "r") as json_file:
                return json.load(json_file)
        else:
            return {}

    def get_packages_to_install(self) -> Any:
        return self.__data.get(self.__pack_man_name, [])

    def get_colors(self) -> Dict[str, str]:
        return self.__colors

    def get_valid_menu_options(self) -> List[str]:
        return self.__menu_options

    def get_valid_install_options(self) -> List[str]:
        return self.__install_options
