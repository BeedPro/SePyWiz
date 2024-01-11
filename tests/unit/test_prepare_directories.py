import unittest
from unittest.mock import patch
import os
from sepywiz.sepywiz import (
    prepare_directories,
)


class TestPrepareDirectories(unittest.TestCase):
    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("os.path.expanduser", side_effect=lambda x: f"~/.local/AppImages/{x}/")
    def test_prepare_directories_new_folder(
        self, mock_expanduser, mock_os_exists, mock_makedirs
    ):
        # Test case for creating a new folder

        # Arrange
        file_name = "my_app"
        expected_dir_name = "my_app"
        expected_app_images_folder = "~/.local/AppImages/"
        expected_app_image_folder = f"~/.local/AppImages/{expected_dir_name}/"

        # Act
        result = prepare_directories(file_name)

        # Assert
        mock_expanduser.assert_called_with(f"~/.local/AppImages/{expected_dir_name}/")
        mock_makedirs.assert_called_with(expected_app_image_folder)
        self.assertEqual(result, expected_app_image_folder)

    def test_directory_creation(self):
        pass

    def test_existing_directory(self):
        pass

    def test_return_value(self):
        pass


if __name__ == "__main__":
    unittest.main()
