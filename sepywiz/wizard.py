from typing import List
import os
from rich import print
from rich.console import Console
from config import Config
from fonts import FontManager
from appiman import AppImageManager
from packman import PackageManager
from textui import TextUI

console: Console = Console(color_system="truecolor")
config: Config = Config()


class Wizard:
    def __init__(self) -> None:
        self.__config: Config = Config()
        self.__textui: TextUI = TextUI()
        self.__font_manager: FontManager = FontManager()
        self.__package_manager: PackageManager = PackageManager()
        self.__appimage_manager: AppImageManager = AppImageManager()

    def get_mode(self):
        valid_menu_options: List[str] = self.__config.get_valid_menu_options()
        os.system("clear")
        print(self.__textui.get_start_menu_text())
        mode: str = input(">>> ")
        while mode.lower() not in valid_menu_options:
            print(self.__textui.get_start_menu_invalid_text())
            mode: str = input(">>> ")
        if len(mode) > 1:
            return mode[0].lower()
        return mode.lower()

    def wizard_sync(self):
        print("The sync mode has been chosen")

    def wizard_delete(self):
        print("The delete mode has been chosen")

    def wizard_quit(self):
        print("You have chosen to quit the wizard")
        print("Quitting...")
        print("Quitting completed")

    def install_apps(self):
        print("You have choosen Installation")
        print("(P)ackages, (A)ppImages, (Q)uit")
        choice: str = input(">>> ").lower()[0]
        valid_install_options: List[str] = config.get_valid_install_options()
        while choice not in valid_install_options:
            print("Not a valid input")
            choice = input(">>> ")
        match choice:
            case "p":
                self.__package_manager.install_packages()
            case "a":
                url: str = input("Enter the url of the AppImage to install\n>>> ")
                name: str = input("Enter the application name you want it as\n>>> ")
                self.__appimage_manager.install_appimage(url, name)
            case _:
                print("Error in selection")

    def main(self):
        mode: str = self.get_mode()
        if mode == "i":
            pass
        elif mode == "f":
            url: str = input(
                "Enter the download URL for the font you wish to install\n>>> "
            )
            font_name: str = input(
                "Enter the filename you wish it to be downloaded as\n>>> "
            )
            self.__font_manager.install_font(url, font_name)
        elif mode == "s":
            self.wizard_sync()
        elif mode == "d":
            self.wizard_delete()
        elif mode == "q":
            self.wizard_quit()
        else:
            print("Invalid mode has been selected, please rerun the script")


if __name__ == "__main__":
    wizard: Wizard = Wizard()
    wizard.main()
