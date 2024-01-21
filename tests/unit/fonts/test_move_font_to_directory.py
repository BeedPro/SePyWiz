import unittest
from unittest.mock import call, patch
from sepywiz.fonts import FontManager


class TestMoveFontToDirectory(unittest.TestCase):
    def setUp(self) -> None:
        self.font_manager = FontManager()
        self.font_dir = "font_des"
        self.file_name = "filename"
        self.extracted_file_path = "extracted"

    @patch("sepywiz.fonts.print")
    @patch("sepywiz.fonts.shutil.move")
    @patch("sepywiz.fonts.os.listdir")
    @patch("sepywiz.fonts.os.makedirs")
    def test_move_font_files(
        self, mock_os_makedirs, mock_os_listdir, mock_shutil_move, *_
    ):
        extracted_files = [
            "font1.ttf",
            "font2.ttf",
        ]
        calls = [
            call(f"{self.extracted_file_path}/font1.ttf", f"{self.font_dir}/font1.ttf"),
            call(f"{self.extracted_file_path}/font2.ttf", f"{self.font_dir}/font2.ttf"),
        ]
        mock_os_makedirs.return_value = None
        mock_os_listdir.return_value = extracted_files
        mock_shutil_move.return_value = None

        result = self.font_manager._FontManager__move_font_to_directory(self.file_name, self.extracted_file_path, self.font_dir)  # type: ignore
        mock_os_makedirs.assert_called_once_with(self.font_dir, exist_ok=True)
        mock_os_listdir.assert_called_once_with(self.extracted_file_path)
        mock_shutil_move.assert_has_calls(calls)

        self.assertTrue(result)

    @patch("sepywiz.fonts.print")
    @patch("sepywiz.fonts.shutil.move")
    @patch("sepywiz.fonts.os.listdir")
    @patch("sepywiz.fonts.os.makedirs")
    def test_ignore_non_font_files(
        self, mock_os_makedirs, mock_os_listdir, mock_shutil_move, *_
    ):
        extracted_files = [
            "font1.ttf",
            "font2.ttf",
            "font1.text",
            "font2.text",
        ]
        calls = [
            call(f"{self.extracted_file_path}/font1.ttf", f"{self.font_dir}/font1.ttf"),
            call(f"{self.extracted_file_path}/font2.ttf", f"{self.font_dir}/font2.ttf"),
        ]
        mock_os_makedirs.return_value = None
        mock_os_listdir.return_value = extracted_files
        mock_shutil_move.return_value = None

        result = self.font_manager._FontManager__move_font_to_directory(self.file_name, self.extracted_file_path, self.font_dir)  # type: ignore
        mock_os_makedirs.assert_called_once_with(self.font_dir, exist_ok=True)
        mock_os_listdir.assert_called_once_with(self.extracted_file_path)
        mock_shutil_move.assert_has_calls(calls)

        self.assertTrue(result)

    @patch("sepywiz.fonts.print")
    @patch("sepywiz.fonts.shutil.move")
    @patch("sepywiz.fonts.os.listdir")
    @patch("sepywiz.fonts.os.makedirs")
    def test_only_non_font_files(
        self, mock_os_makedirs, mock_os_listdir, mock_shutil_move, *_
    ):
        extracted_files = [
            "font1.text",
            "font2.text",
        ]
        mock_os_makedirs.return_value = None
        mock_os_listdir.return_value = extracted_files
        mock_shutil_move.return_value = None

        result = self.font_manager._FontManager__move_font_to_directory(self.file_name, self.extracted_file_path, self.font_dir)  # type: ignore
        mock_os_makedirs.assert_called_once_with(self.font_dir, exist_ok=True)
        mock_os_listdir.assert_called_once_with(self.extracted_file_path)
        mock_shutil_move.assert_not_called()

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
