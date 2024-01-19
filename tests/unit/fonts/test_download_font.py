from typing import Any
import unittest
from unittest.mock import patch
from sepywiz.fonts import FontManager
import os


class TestFontManagerDownloadFont(unittest.TestCase):
    @patch("sepywiz.fonts.subprocess.run")
    def test_successful_download_with_zip(self, mock_subprocess_run: Any):
        font_manager = FontManager()
        file_name: str = "font"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}.zip")
        mock_subprocess_run.return_value.returncode = 0

        result = font_manager._FontManager__download_font(f"http://example.com/{file_name}.zip", f"{file_name}.zip")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", download_path]
        )
        self.assertTrue(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_failed_download_with_zip(self, mock_subprocess_run):
        font_manager = FontManager()
        file_name: str = "font"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}.zip")
        mock_subprocess_run.return_value.returncode = 1

        result = font_manager._FontManager__download_font(f"http://example.com/{file_name}.zip", f"{file_name}.zip")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", download_path]
        )

        self.assertFalse(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_successful_download_without_zip(self, mock_subprocess_run: Any):
        font_manager = FontManager()
        file_name: str = "font"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}.zip")
        mock_subprocess_run.return_value.returncode = 0

        result = font_manager._FontManager__download_font(f"http://example.com/{file_name}.zip", f"{file_name}")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", download_path]
        )
        self.assertTrue(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_failed_download_without_zip(self, mock_subprocess_run):
        font_manager = FontManager()
        file_name: str = "font"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}.zip")
        mock_subprocess_run.return_value.returncode = 1

        result = font_manager._FontManager__download_font(f"http://example.com/{file_name}.zip", f"{file_name}")  # type: ignore

        mock_subprocess_run.assert_called_with(
            ["wget", "http://example.com/font.zip", "-O", download_path]
        )

        self.assertFalse(result)

    @patch("sepywiz.fonts.subprocess.run")
    def test_non_zip_extension_url(self, mock_subprocess_run):
        font_manager = FontManager()
        file_name: str = "font"

        result = font_manager._FontManager__download_font(f"http://example.com/{file_name}", f"{file_name}")  # type: ignore

        mock_subprocess_run.assert_not_called()

        self.assertFalse(result)
