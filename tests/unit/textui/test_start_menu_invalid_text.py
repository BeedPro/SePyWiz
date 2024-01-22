import unittest
from sepywiz.config import Config
from sepywiz.textui import TextUI


class TestStartMenuInvalidText(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        self.textui = TextUI()
        self.__colors = self.config.get_colors()

    def test_correct_start_menu_message(self):
        message = (
            "You have chosen an invalid option. Please enter a valid option\n"
            f"Valid options: [bold]([{self.__colors['teal']}]I[/{self.__colors['teal']}])[/bold]nstall, "
            f"[bold]([{self.__colors['blue']}]F[/{self.__colors['blue']}])[/bold]onts, "
            f"[bold]([{self.__colors['grey']}]S[/{self.__colors['grey']}])[/bold]ync, "
            f"[bold]([{self.__colors['black']}]D[/{self.__colors['black']}])[/bold]elete or "
            f"[bold]([{self.__colors['pink']}]Q[/{self.__colors['pink']}])[/bold]uit"
        )

        result = self.textui.get_start_menu_invalid_text()

        self.assertEqual(result, message)


if __name__ == "__main__":
    unittest.main()
