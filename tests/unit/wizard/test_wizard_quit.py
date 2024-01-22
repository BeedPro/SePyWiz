import unittest
from unittest.mock import call, patch
from sepywiz.wizard import Wizard


class TestWizardQuit(unittest.TestCase):
    @patch("sepywiz.wizard.print")
    def test_quit_message(self, mock_print):
        wizard = Wizard()
        print_calls = [
            call("You have chosen to quit the wizard"),
            call("Quitting..."),
            call("Quitting completed"),
        ]

        wizard.quit()
        mock_print.assert_has_calls(print_calls)


if __name__ == "__main__":
    unittest.main()
