import os
import unittest
from unittest.mock import call, patch
from sepywiz.appiman import AppImageManager


class TestPrepareDirectories(unittest.TestCase):
    def setUp(self) -> None:
        self.prepare_directories = (
            AppImageManager()._AppImageManager__prepare_directories  # type: ignore
        )
        self.dir_name = "filename"

    @patch("sepywiz.appiman.os.makedirs")
    @patch("sepywiz.appiman.os.path.exists")
    def test_valid_filename_without_extension(
        self, mock_os_path_exists, mock_os_makedirs
    ):
        filename = "filename"
        expected = os.path.expanduser(f"~/.local/AppImages/{self.dir_name}")
        app_image_default_dir = os.path.expanduser("~/.local/AppImages/")
        app_images_folder = os.path.expanduser(f"~/.local/AppImages/{self.dir_name}/")
        expected_calls = [call(app_image_default_dir), call(app_images_folder)]
        mock_os_path_exists.return_value = False
        result = self.prepare_directories(filename)
        mock_os_makedirs.assert_has_calls(expected_calls)
        self.assertEqual(result, expected)

    @patch("sepywiz.appiman.os.makedirs")
    @patch("sepywiz.appiman.os.path.exists")
    def test_valid_filename_with_extension(self, mock_os_path_exists, mock_os_makedirs):
        filename = "filename.AppImage"
        expected = os.path.expanduser(f"~/.local/AppImages/{self.dir_name}")
        app_image_default_dir = os.path.expanduser("~/.local/AppImages/")
        app_images_folder = os.path.expanduser(f"~/.local/AppImages/{self.dir_name}/")
        expected_calls = [call(app_image_default_dir), call(app_images_folder)]
        mock_os_path_exists.return_value = False
        result = self.prepare_directories(filename)
        mock_os_makedirs.assert_has_calls(expected_calls)
        self.assertEqual(result, expected)

    def test_empty_filename(self):
        filename = ""
        with self.assertRaises(ValueError) as context:
            self.prepare_directories(filename)
        self.assertEqual(str(context.exception), "File name given is empty")


if __name__ == "__main__":
    unittest.main()
