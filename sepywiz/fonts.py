import subprocess
from typing import List
import os
import shutil
import zipfile


class FontManager:
    def __init__(self) -> None:
        pass

    def __download_font(self, url: str, file_name: str) -> bool:
        if not file_name.lower().endswith(".zip"):
            file_name += ".zip"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["wget", url, "-O", download_path]
        )
        return response.returncode == 0

    def __unzip_font(self, file_name: str) -> List[str]:
        if not file_name.lower().endswith(".zip"):
            file_name += ".zip"
        zip_file_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
        extracted_file_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
        os.makedirs(extracted_file_path, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(extracted_file_path)
        return os.listdir(extracted_file_path)

    def __move_font_to_directory(
        self, file_name: str, extracted_file_path: str, font_dir: str
    ):
        os.makedirs(font_dir, exist_ok=True)
        ttf_files: List[str] = [
            file
            for file in os.listdir(extracted_file_path)
            if file.lower().endswith(".ttf")
        ]
        for ttf_file in ttf_files:
            source_path: str = f"{extracted_file_path}/{ttf_file}"
            destination_path: str = f"{font_dir}/{ttf_file}"
            shutil.move(source_path, destination_path)
            print(f"{ttf_file} moved to {font_dir}")
        print(f"All the {file_name} fonts have been moved to {font_dir}")

    def __install_fonts(self, file_name: str):
        result: subprocess.CompletedProcess[bytes] = subprocess.run(["fc-cache", "-fv"])
        if result.returncode == 0:
            print(
                f"Font {file_name} has been installed, and font cache has been updated successfully"
            )
            print("Check if the font has been installed by running:")
            print('`fc-list | grep "FONT_NAME"`')
        else:
            print(
                f"Error installing {file_name}. Error return code: {result.returncode}"
            )

    def install_font(self, url: str, file_name: str):
        if self.__download_font(url, file_name):
            print(f"{file_name} has been downloaded")
            extracted_files: List[str] = self.__unzip_font(file_name)
            if extracted_files:
                print(f"{file_name} has been extracted in the Downloads directory")
                font_dir: str = "~/.local/share/fonts"
                self.__move_font_to_directory(
                    file_name, f"~/Downloads/{file_name}", font_dir
                )
                self.__install_fonts(file_name)
            else:
                print("Extraction has failed or the zip file is empty")
        else:
            print(f"{file_name} was not able to be downloaded.")
