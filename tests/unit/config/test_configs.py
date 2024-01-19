import unittest
from unittest.mock import mock_open, patch
from sepywiz.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    @patch("sepywiz.config.os.path.exists", return_value=False)
    def test_load_data_non_exist(self, _):
        self.config._Config__app_install_path = "test_config.json"  # type: ignore

        data = self.config._Config__load_data()  # type: ignore

        expected_data = {}
        self.assertEqual(data, expected_data)

    @patch("sepywiz.config.os.path.exists", return_value=True)
    @patch(
        "sepywiz.config.open",
        new_callable=mock_open,
        read_data='{"apt_packages": ["package1", "package2"]}',
    )
    @patch(
        "sepywiz.config.json.load",
        return_value={"apt_packages": ["package1", "package2"]},
    )
    def test_load_data_exist(self, *_):
        self.config._Config__app_install_path = "dummy_path"  # type: ignore

        data = self.config._Config__load_data()  # type: ignore

        expected_data = {"apt_packages": ["package1", "package2"]}
        self.assertEqual(data, expected_data)

    def test_get_packages_to_install(self):
        sample_data = {"apt_packages": ["package1", "package2"]}

        self.config._Config__data = sample_data  # type: ignore

        packages = self.config.get_packages_to_install()
        expected_packages = ["package1", "package2"]
        self.assertEqual(packages, expected_packages)

    def test_get_colors(self):
        colors = self.config.get_colors()
        expected_colors = {
            "orange": "#FFC170",
            "black": "#696363",
            "teal": "#84DCCF",
            "blue": "#A6D9F7",
            "grey": "#BCCCE0",
            "pink": "#BF98A0",
        }
        self.assertEqual(colors, expected_colors)

    def test_get_valid_menu_options(self):
        menu_options = self.config.get_valid_menu_options()
        expected_options = [
            "i",
            "f",
            "s",
            "d",
            "q",
            "install",
            "fonts",
            "sync",
            "delete",
            "quit",
        ]
        self.assertEqual(menu_options, expected_options)

    def test_get_valid_install_options(self):
        install_options = self.config.get_valid_install_options()
        expected_options = ["p", "a"]
        self.assertEqual(install_options, expected_options)


if __name__ == "__main__":
    unittest.main()
