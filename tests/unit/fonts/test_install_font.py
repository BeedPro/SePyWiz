import unittest
from unittest.case import skip
from unittest.mock import patch

from sepywiz.fonts import FontManager


class TestInstallFont(unittest.TestCase):
    def setUp(self) -> None:
        self.font_manager = FontManager()

    @patch.object(FontManager, "_FontManager__download_font", return_value=True)
    @patch.object(
        FontManager, "_FontManager__unzip_font", return_value=["font1.ttf", "font2.ttf"]
    )
    @patch.object(
        FontManager, "_FontManager__move_font_to_directory", return_value=True
    )
    @patch.object(FontManager, "_FontManager__install_fonts", return_value=True)
    def test_valid_url_filename(
        self, mock_install_fonts, mock_move, mock_unzip, mock_download
    ):
        url = "https://example.com/font.zip"
        file_name = "font_name"

        result = self.font_manager.install_font(url, file_name)

        mock_download.assert_called_once_with(url, file_name)
        mock_unzip.assert_called_once_with(file_name)
        mock_move.assert_called_once_with(
            file_name, "~/Downloads/font_name", "~/.local/share/fonts"
        )
        mock_install_fonts.assert_called_once_with(file_name)
        self.assertTrue(result)

    @skip("Not implemented")
    def test_invalid_url(self):
        pass

    @skip("Not implemented")
    def test_invalid_filename(self):
        pass

    @skip("Not implemented")
    def test_empty_url(self):
        pass

    @skip("Not implemented")
    def test_empty_filename(self):
        pass

    @skip("Not implemented")
    def test_font_install_fail(self):
        pass

    @skip("Not implemented")
    def test_valid_url_filename_failed_move(self):
        pass


if __name__ == "__main__":
    unittest.main()
