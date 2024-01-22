from typing import List
import os
from rich import print
from rich.console import Console
from sepywiz.config import Config
from sepywiz.fonts import FontManager
from sepywiz.appiman import AppImageManager
from sepywiz.packman import PackageManager
from sepywiz.textui import TextUI

console: Console = Console(color_system="truecolor")
config: Config = Config()


class Wizard:
    """
    A class representing a wizard for managing various tasks such as package installation, font installation, synchronization, and more.

    Attributes:
        __config (Config): An instance of the Config class for configuration management.
        __textui (TextUI): An instance of the TextUI class for handling text-based user interface.
        __font_manager (FontManager): An instance of the FontManager class for font-related tasks.
        __package_manager (PackageManager): An instance of the PackageManager class for package management.
        __appimage_manager (AppImageManager): An instance of the AppImageManager class for AppImage handling.

    Methods:
        get_mode(): Get the mode choice from the user.
        sync(): Perform synchronization tasks.
        delete(): Perform deletion tasks.
        quit(): Quit the wizard.
        install_apps(): Perform installation tasks for packages and AppImages.
        main(): Main method for running the wizard based on the selected mode.
    """

    def __init__(self) -> None:
        """
        Initialize the Wizard object and its dependencies.

        This constructor initializes the Wizard class and creates instances of the
        Config, TextUI, FontManager, PackageManager, and AppImageManager classes to
        manage various tasks.
        """
        self.__config: Config = Config()
        self.__textui: TextUI = TextUI()
        self.__font_manager: FontManager = FontManager()
        self.__package_manager: PackageManager = PackageManager()
        self.__appimage_manager: AppImageManager = AppImageManager()

    def get_mode(self):
        """
        Get the mode choice from the user.

        Returns:
        str: The selected mode as a lowercase character.
        """
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

    def sync(self):
        """
        Not implemented
        """
        print("The sync mode has been chosen")

    def delete(self):
        """
        Not implemented
        """
        print("The delete mode has been chosen")

    def quit(self):
        """
        Prints the exit message on program exit
        """
        print("You have chosen to quit the wizard")
        print("Quitting...")
        print("Quitting completed")

    def install_apps(self):
        """
        Perform installation tasks for packages and AppImages.

        This method handles the installation of packages and AppImages based on user input.
        """
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
        """
        Main method for running the wizard based on the selected mode.

        This method is responsible for running the wizard based on the selected mode
        and handles various actions accordingly.
        """
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
            self.sync()
        elif mode == "d":
            self.delete()
        elif mode == "q":
            self.quit()
        else:
            print("Invalid mode has been selected, please rerun the script")


if __name__ == "__main__":
    wizard: Wizard = Wizard()
    wizard.main()
