import os
import shutil
import subprocess
from typing import Any


class AppImageManager:
    def __init__(self) -> None:
        pass

    def __prepare_directories(self, file_name: str) -> str:
        if not file_name.lower().endswith(".AppImage"):
            dir_name: str = file_name
            file_name += ".AppImage"
        else:
            dir_name, _ = os.path.splitext(file_name)[0]

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
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["wget", url, "-O", download_path]
        )
        return response

    def __set_permissions(self, file_path: str, file_name: str) -> None:
        if os.path.exists(file_path):
            # Set permissions to 755
            os.chmod(f"{file_path}/{file_name}", 0o755)
            print(f"Permissions for {file_name} set to 755.")
        else:
            print(f"File {file_path} not found.")

    def __extract_appimage(self, path: str, file_name: str) -> bool:
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            [f"{path}/{file_name}", "--appimage-extract"]
        )
        source_directory: str = "squashfs-root"
        shutil.move(source_directory, path)
        return response.returncode == 0

    def __download_appimage(self, url: str, file_name: str) -> bool:
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
        if self.__download_appimage(url, name):
            print(f"Downloaded {name}'s AppImage")
        else:
            print(f"{name} AppImage was not able to be downloaded")
