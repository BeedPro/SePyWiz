import unittest
from unittest.mock import patch
from sepywiz.wizard import Wizard


class TestGetMode(unittest.TestCase):
    def setUp(self) -> None:
        self.wizard = Wizard()

    @patch("sepywiz.wizard.print")
    @patch("sepywiz.wizard.input")
    @patch("sepywiz.wizard.os.system")
    def test_valid_inputtest_full_valid_input(self, mock_os_system, mock_input, _):
        mock_os_system.return_value = 0
        mock_input.return_value = "install"
        expected = "i"
        result = self.wizard.get_mode()
        self.assertEqual(expected, result)

    @patch("sepywiz.wizard.print")
    @patch("sepywiz.wizard.input")
    @patch("sepywiz.wizard.os.system")
    def test_valid_short_input(self, mock_os_system, mock_input, _):
        mock_os_system.return_value = 0
        mock_input.return_value = "i"
        expected = "i"
        result = self.wizard.get_mode()
        self.assertEqual(expected, result)

    def test_invalid_input(self):
        pass

    def test_empty_input(self):
        pass


if __name__ == "__main__":
    unittest.main()
