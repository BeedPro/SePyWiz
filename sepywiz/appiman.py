import os
import shutil
import subprocess
from typing import Any


class AppImageManager:
    """
    AppImageManager is a class for managing AppImage downloads, installations, and extractions.

    Attributes:
        None

    Methods:
        install_appimage
    """

    def __init__(self) -> None:
        """
        AppImageManager is a class for managing AppImage downloads, installations, and extractions.

        Attributes:
            None

        Methods:
            install_appimage
        """
        pass

    def __prepare_directories(self, file_name: str) -> str:
        """
        Prepare directories for AppImage download and extraction.

        Args:
            file_name (str): The name of the AppImage file.

        Returns:
            str: The path to the directory where the AppImage will be downloaded and extracted.

        Example:
            download_path = self.__prepare_directories("my_app")
            # Result: download_path = "~/.local/AppImages/my_app"
        """
        if not file_name:
            raise ValueError("File name given is empty")

        if not file_name.lower().endswith(".appimage"):
            dir_name: str = file_name
            file_name += ".AppImage"
        else:
            dir_name: str = os.path.splitext(file_name)[0]

        app_images_folder: str = os.path.expanduser("~/.local/AppImages/")
        if not os.path.exists(app_images_folder):
            os.makedirs(app_images_folder)
            print(f"Directory {app_images_folder} has been created.")
        else:
            print(f"Directory {app_images_folder} already exists.")

        app_image_folder: str = os.path.expanduser(f"~/.local/AppImages/{dir_name}/")
        os.makedirs(app_image_folder)

        return os.path.expanduser(f"~/.local/AppImages/{dir_name}")

    def __download_file(
        self, url: str, download_path: str
    ) -> subprocess.CompletedProcess:
        """
        Download a file from a given URL and save it to a specified path.

        Args:
            url (str): The URL of the file to download.
            download_path (str): The path where the file will be saved.

        Returns:
            subprocess.CompletedProcess: The result of the download process.
        """
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["wget", url, "-O", download_path]
        )
        return response

    def __set_permissions(self, file_path: str, file_name: str) -> None:
        """
        Set file permissions to 755.

        Args:
            file_path (str): The path to the file.
            file_name (str): The name of the file.
        """
        if os.path.exists(file_path):
            # Set permissions to 755
            os.chmod(f"{file_path}/{file_name}", 0o755)
            print(f"Permissions for {file_name} set to 755.")
        else:
            print(f"File {file_path} not found.")

    def __extract_appimage(self, path: str, file_name: str) -> bool:
        """
        Extract an AppImage file.

        Args:
            path (str): The path to the directory where the AppImage is located.
            file_name (str): The name of the AppImage file.

        Returns:
            bool: True if extraction is successful, False otherwise.
        """
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            [f"{path}/{file_name}", "--appimage-extract"]
        )
        source_directory: str = "squashfs-root"
        shutil.move(source_directory, path)
        return response.returncode == 0

    def __download_appimage(self, url: str, file_name: str) -> bool:
        """
        Download, set permissions, and extract an AppImage.

        Args:
            url (str): The URL of the AppImage file.
            file_name (str): The name of the AppImage file.

        Returns:
            bool: True if the AppImage is downloaded, permissions are set, and extraction is successful, False otherwise.
        """
        download_path: str = self.__prepare_directories(file_name)

        response: subprocess.CompletedProcess[Any] = self.__download_file(
            url, f"{download_path}/{file_name}"
        )
        self.__set_permissions(download_path, file_name)
        if self.__extract_appimage(download_path, file_name):
            print("Extracted AppImage")
        else:
            print("AppImage failed to extract")
        return response.returncode == 0

    def install_appimage(self, url: str, name: str):
        """
        Install an AppImage by downloading, setting permissions, and extracting it.

        Args:
            url (str): The URL of the AppImage file.
            name (str): The name of the AppImage.

        Example:
            app_image_manager = AppImageManager()
            app_image_manager.install_appimage("https://example.com/my_app.AppImage", "my_app")
        """
        if self.__download_appimage(url, name):
            print(f"Downloaded {name}'s AppImage")
        else:
            print(f"{name} AppImage was not able to be downloaded")
