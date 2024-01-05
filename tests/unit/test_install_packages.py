import unittest
from unittest.mock import patch
from io import StringIO
from sepywiz.sepywiz import (
    install_packages,
)


class TestInstallPackages(unittest.TestCase):
    @patch("sepywiz.sepywiz.is_package_installed")
    @patch("sepywiz.sepywiz.install_package")
    def test_install_packages_installed(
        self, mock_install_package, mock_is_package_installed
    ):
        # Mock is_package_installed to return True for all packages
        mock_is_package_installed.return_value = True

        # Call the function
        with patch("sys.stdout", new_callable=StringIO) as _:
            install_packages()

        # Verify that install_package is not called when packages are already installed
        mock_install_package.assert_not_called()

    @patch("sepywiz.sepywiz.is_package_installed")
    @patch("sepywiz.sepywiz.install_package")
    def test_install_packages_not_installed(
        self, mock_install_package, mock_is_package_installed
    ):
        # Mock is_package_installed to return False for all packages
        mock_is_package_installed.return_value = False
        # Call the function
        install_packages()

        # Verify that install_package is called for all packages that are not installed
        mock_install_package.assert_called()


if __name__ == "__main__":
    unittest.main()
