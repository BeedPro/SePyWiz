from typing import Any
import unittest
from unittest.mock import patch
from sepywiz.fonts import FontManager
import os


class TestFontManagerDownloadFont(unittest.TestCase):
    def setUp(self):
        self.font_manager = FontManager()
        self.file_name = "font"
        self.download_path = os.path.expanduser(f"~/Downloads/{self.file_name}.zip")

    @patch("sepywiz.fonts.subprocess.run")
    def test_successful_download_with_zip(self, mock_subprocess_run: Any):
        mock_subprocess_run.return_value.returncode = 0

        result = self.font_manager._FontManager__download_font(f"http://example.com/{self.file_name}.zip", f"{self.file_name}.zip")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", self.download_path]
        )
        self.assertTrue(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_failed_download_with_zip(self, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 1

        result = self.font_manager._FontManager__download_font(f"http://example.com/{self.file_name}.zip", f"{self.file_name}.zip")  # type: ignore
        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", self.download_path]
        )

        self.assertFalse(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_successful_download_without_zip(self, mock_subprocess_run: Any):
        mock_subprocess_run.return_value.returncode = 0

        result = self.font_manager._FontManager__download_font(f"http://example.com/{self.file_name}.zip", f"{self.file_name}")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", self.download_path]
        )
        self.assertTrue(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_failed_download_without_zip(self, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 1

        result = self.font_manager._FontManager__download_font(f"http://example.com/{self.file_name}.zip", f"{self.file_name}")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", self.download_path]
        )

        self.assertFalse(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_non_zip_extension_url(self, mock_subprocess_run):
        result = self.font_manager._FontManager__download_font(f"http://example.com/{self.file_name}", f"{self.file_name}")  # type: ignore
        mock_subprocess_run.assert_not_called()

        self.assertFalse(result)
