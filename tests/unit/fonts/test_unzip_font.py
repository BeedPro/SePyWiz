import os
import unittest
from unittest.case import skip
from unittest.mock import Mock, patch
from sepywiz.fonts import FontManager


# WARNING: That patch is reversed into the arguments of the test method
class TestUnzipFont(unittest.TestCase):
    def setUp(self):
        self.font_manager = FontManager()
        self.filename = "filename"
        self.extracted_file_path = os.path.expanduser(f"~/Downloads/{self.filename}")

    @patch("sepywiz.fonts.os.path.exists")
    @patch("sepywiz.fonts.os.makedirs")
    @patch("sepywiz.fonts.os.listdir")
    @patch("sepywiz.fonts.zipfile.ZipFile")
    def test_successful_extraction_ending_zip(
        self, mock_zipfile, mock_os_listdir, mock_os_makedirs, mock_os_path_exists
    ):
        mock_os_makedirs.return_value = None
        fake_list = ["file1", "file2", "file3"]
        mock_os_listdir.return_value = fake_list
        mock_os_path_exists.return_value = True
        mock_zipfile.__enter__ = Mock(return_value=fake_list)

        result = self.font_manager._FontManager__unzip_font(self.filename)  # type: ignore

        mock_os_makedirs.assert_called_once_with(
            self.extracted_file_path, exist_ok=True
        )
        mock_os_listdir.assert_called_once_with(self.extracted_file_path)
        self.assertEqual(result, fake_list)

    @patch("sepywiz.fonts.os.path.exists")
    @patch("sepywiz.fonts.os.makedirs")
    @patch("sepywiz.fonts.os.listdir")
    @patch("sepywiz.fonts.zipfile.ZipFile")
    def test_successful_extraction_not_ending_zip(
        self, mock_zipfile, mock_os_listdir, mock_os_makedirs, mock_os_path_exists
    ):
        mock_os_makedirs.return_value = None
        mock_os_path_exists.return_value = True
        fake_list = ["file1", "file2", "file3"]
        mock_os_listdir.return_value = fake_list
        mock_zipfile.__enter__ = Mock(return_value=fake_list)

        result = self.font_manager._FontManager__unzip_font(f"{self.filename}.zip")  # type: ignore

        mock_os_makedirs.assert_called_once_with(
            self.extracted_file_path, exist_ok=True
        )
        mock_os_listdir.assert_called_once_with(self.extracted_file_path)
        self.assertEqual(result, fake_list)

    @patch("sepywiz.fonts.os.path.exists", return_value=False)
    @patch("sepywiz.fonts.os.makedirs", return_value=None)
    @patch("sepywiz.fonts.os.listdir", return_value=None)
    def test_file_not_found(self, *_):
        result = self.font_manager._FontManager__unzip_font(f"{self.filename}.zip")  # type: ignore
        self.assertEqual(result, [])

    # NOTE: Need to add this test to FontManager but do not know how to, I don't know if it has a fail condition
    @skip("I don't understand how to test")
    def test_non_zipfile(self):
        pass

    # NOTE: Need to add this test to FontManager but do not know how to, I don't know if it has a fail condition
    @skip("I don't understand how to test")
    def test_failed_extraction(self):
        pass


if __name__ == "__main__":
    unittest.main()
