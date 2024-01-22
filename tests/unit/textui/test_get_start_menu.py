import unittest
from sepywiz.config import Config
from sepywiz.textui import TextUI


class TestGetStartMenu(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        self.textui = TextUI()
        self.__colors = self.config.get_colors()

    def test_correct_start_menu_message(self):
        message = (
            f"Welcome to [{self.__colors['orange']}]SePyWiz[/{self.__colors['orange']}]\n"
            "This is the setup wizard for installation, syncing, repairing and also deletion.\n"
            f"  - [bold]([{self.__colors['teal']}]I[/{self.__colors['teal']}])[/bold]nstallation\n"
            f"  - [bold]([{self.__colors['blue']}]F[/{self.__colors['blue']}])[/bold]onts [Install fonts, by default this installs the Jetbrains font]\n"
            f"  - [bold]([{self.__colors['grey']}]S[/{self.__colors['grey']}])[/bold]ync Laptop/Desktop dotfiles and apps\n"
            f"  - [bold]([{self.__colors['black']}]D[/{self.__colors['black']}])[/bold]elete back to fresh [Not implemented]\n"
            f"  - [bold]([{self.__colors['pink']}]Q[/{self.__colors['pink']}])[/bold]uit"
        )

        result = self.textui.get_start_menu_text()

        self.assertEqual(result, message)


if __name__ == "__main__":
    unittest.main()
