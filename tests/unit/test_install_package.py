import unittest
import subprocess
from unittest.mock import Mock, patch
from io import StringIO
from sepywiz.sepywiz import (
    install_package,
)


class TestInstallPackage(unittest.TestCase):
    @patch("subprocess.run")
    def test_install_success(self, mock_subprocess_run):
        # Mock subprocess.run to return successfully
        mock_subprocess_run.return_value = Mock(returncode=0, stdout=b"")
        package_name = "example-package"

        # Capture stdout during function execution
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            install_package(package_name)

        # Check if the function printed the success message
        self.assertIn(
            f"{package_name} has been successfully installed.", mock_stdout.getvalue()
        )

        # Verify that subprocess.run was called with the correct arguments
        mock_subprocess_run.assert_called_once_with(
            ["sudo", "apt", "install", "-y", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    @patch("subprocess.run")
    def test_install_failure(self, mock_subprocess_run):
        # Mock subprocess.run to return with an error
        mock_subprocess_run.return_value = Mock(returncode=1, stderr=b"Error message")
        package_name = "non-existent-package"

        # Capture stdout during function execution
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            install_package(package_name)

        # Check if the function printed the error message
        self.assertIn(
            f"Error installing {package_name}. Return code: 1", mock_stdout.getvalue()
        )
        self.assertIn("Error message", mock_stdout.getvalue())

        # Verify that subprocess.run was called with the correct arguments
        mock_subprocess_run.assert_called_once_with(
            ["sudo", "apt", "install", "-y", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


if __name__ == "__main__":
    unittest.main()
