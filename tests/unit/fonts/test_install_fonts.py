import unittest
from unittest.mock import patch

from sepywiz.fonts import FontManager


class TestInstallFonts(unittest.TestCase):
    def setUp(self):
        self.font_manager = FontManager()
        self.file_name = "filename"

    @patch("sepywiz.fonts.print")
    @patch("sepywiz.fonts.subprocess.run")
    def test_successful_font_installation(self, mock_subprocess_run, *_):
        mock_subprocess_run.return_value.returncode = 0
        result = self.font_manager._FontManager__install_fonts(self.file_name)  # type: ignore

        self.assertTrue(result)

    @patch("sepywiz.fonts.print")
    @patch("sepywiz.fonts.subprocess.run")
    def test_failed_font_installation(self, mock_subprocess_run, *_):
        mock_subprocess_run.return_value.returncode = 1
        result = self.font_manager._FontManager__install_fonts(self.file_name)  # type: ignore

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
