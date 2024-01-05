import unittest
import subprocess
from unittest.mock import Mock, patch
from sepywiz.sepywiz import (
    is_package_installed,
)


class TestIsPackageInstalled(unittest.TestCase):
    @patch("subprocess.run")
    def test_package_installed(self, mock_subprocess_run):
        # Mock subprocess.run to return successfully
        mock_subprocess_run.return_value = Mock(returncode=0, stdout=b"")
        package_name = "example-package"

        # Check if the function returns True when the package is installed
        self.assertTrue(is_package_installed(package_name))

        # Verify that subprocess.run was called with the correct arguments
        mock_subprocess_run.assert_called_once_with(
            ["dpkg", "-l", package_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    @patch("subprocess.run")
    def test_package_not_installed(self, mock_subprocess_run):
        # Mock subprocess.run to raise a CalledProcessError
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "dpkg")
        package_name = "non-existent-package"

        # Check if the function returns False when the package is not installed
        self.assertFalse(is_package_installed(package_name))

        # Verify that subprocess.run was called with the correct arguments
        mock_subprocess_run.assert_called_once_with(
            ["dpkg", "-l", package_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


if __name__ == "__main__":
    unittest.main()
