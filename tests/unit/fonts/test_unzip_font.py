import unittest
from unittest.mock import mock_open, patch
from sepywiz.fonts import FontManager


# TODO: Need to mock os.makedirs, zipfile.ZipFile
# TODO: And write the tests for these
class TestUnzipFont(unittest.TestCase):
    def setUp(self):
        self.font_manager = FontManager()

    def test_successful_extraction(self):
        pass

    def test_empty_zip_file_ending_zip(self):
        pass

    def test_non_zip_extension_ending_zip(self):
        pass

    def test_successful_extraction_not_ending_zip(self):
        pass

    def test_empty_zip_file_not_ending_zip(self):
        pass

    def test_non_zip_extension_not_ending_zip(self):
        pass


if __name__ == "__main__":
    unittest.main()
