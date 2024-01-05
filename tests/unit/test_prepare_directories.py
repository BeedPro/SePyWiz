import unittest
import os
from unittest.mock import patch
from sepywiz.sepywiz import (
    prepare_directories,
)


class TestPrepareDirectories(unittest.TestCase):
    @patch("os.path.exists", return_value=False)
    @patch("os.makedirs")
    def test_prepare_directories_creates_folder(self, mock_makedirs, mock_exists):
        # Test that the function creates a directory
        folder_name = prepare_directories("testApp")
        mock_exists.assert_called(os.path.expanduser("~/.local/AppImages/"))
        mock_makedirs.assert_called(os.path.expanduser("~/.local/AppImages/"))
        self.assertTrue(os.path.exists(folder_name))
        self.assertTrue(os.path.isdir(folder_name))

    # @patch("os.path.exists", return_value=True)
    # def test_prepare_directories_folder_exists(self, mock_exists):
    #     # Test that the function doesn't create a folder if it already exists
    #     folder_name = prepare_directories("testApp")
    #     mock_exists.assert_called_once_with(os.path.expanduser("~/.local/AppImages/"))
    #     self.assertTrue(os.path.exists(folder_name))
    #     self.assertTrue(os.path.isdir(folder_name))
    #
    # @patch("os.path.exists", return_value=False)
    # @patch("os.makedirs")
    # def test_prepare_directories_with_extension(self, mock_makedirs, mock_exists):
    #     # Test that the function handles file names with extensions correctly
    #     folder_name = prepare_directories("testApp.AppImage")
    #     mock_exists.assert_called_once_with(os.path.expanduser("~/.local/AppImages/"))
    #     mock_makedirs.assert_called_once_with(os.path.expanduser("~/.local/AppImages/"))
    #     self.assertTrue(os.path.exists(folder_name))
    #     self.assertTrue(os.path.isdir(folder_name))


if __name__ == "__main__":
    unittest.main()
