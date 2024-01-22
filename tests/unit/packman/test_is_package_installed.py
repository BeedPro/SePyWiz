import unittest
from subprocess import PIPE, CalledProcessError
from unittest.mock import patch
from sepywiz.packman import PackageManager


class TestIsPackageInstalled(unittest.TestCase):
    def setUp(self) -> None:
        self.is_package_installed = PackageManager()._PackageManager__is_package_installed  # type: ignore

    @patch("sepywiz.packman.subprocess.run")
    def test_package_already_installed(self, mock_subprocess_run):
        package_name = "valid_package"
        result = self.is_package_installed(package_name)
        mock_subprocess_run.assert_called_with(
            ["dpkg", "-l", package_name],
            check=True,
            stdout=PIPE,
            stderr=PIPE,
        )
        self.assertTrue(result)

    @patch("sepywiz.packman.subprocess.run")
    def test_package_not_installed(self, mock_subprocess_run):
        package_name = "valid_package"
        mock_subprocess_run.side_effect = CalledProcessError(
            1, f"dpkg -l {package_name}"
        )
        result = self.is_package_installed(package_name)
        mock_subprocess_run.assert_called_with(
            ["dpkg", "-l", package_name],
            check=True,
            stdout=PIPE,
            stderr=PIPE,
        )
        self.assertFalse(result)

    def test_empty_name(self):
        empty_name = ""
        with self.assertRaises(ValueError) as context:
            self.is_package_installed(empty_name)
        self.assertEqual("Name is an empty string", str(context.exception))


if __name__ == "__main__":
    unittest.main()
