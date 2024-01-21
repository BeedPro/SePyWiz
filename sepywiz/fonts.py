import subprocess
from typing import List, Tuple
import os
import shutil
import zipfile


class FontManager:
    """
    FontManager is a class for managing font downloads, extraction, installation, and updates.

    Attributes:
        None

    Methods:
        install_font
    """

    def __init__(self) -> None:
        """
        FontManager is a class for managing font downloads, extraction, installation, and updates.

        Attributes:
            None

        Methods:
            install_font
        """
        pass

    def __download_font(self, url: str, file_name: str) -> bool:
        """
        Download a font file from a given URL and save it with a specified file name.

        Args:
            url (str): The URL of the font file to download.
            file_name (str): The name of the font file to save.

        Returns:
            bool: True if the download is successful, False otherwise.
        """
        if not url.lower().endswith(".zip"):
            print("File in the url being downloaded is not a zip file")
            return False

        elif not file_name.lower().endswith(".zip"):
            file_name += ".zip"
        download_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
        response: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["wget", url, "-O", download_path]
        )
        return response.returncode == 0

    def __get_filename_and_extension(self, file_name: str) -> Tuple[str, str]:
        """
        Extract the filename and its corresponding extension from a given filename.

        Args:
            file_name (str): The input filename, which may or may not include the ".zip" extension.

        Returns:
            Tuple[str, str]: A tuple containing two strings:
                1. The filename without the ".zip" extension.
                2. The original filename with the ".zip" extension (if not present, it is added).

        Example:
            filename, filename_with_extension = self.__get_filename_and_extension("my_font")
            # Result: filename = "my_font", filename_with_extension = "my_font.zip"

            filename, filename_with_extension = self.__get_filename_and_extension("another_font.zip")
            # Result: filename = "another_font", filename_with_extension = "another_font.zip"
        """
        if file_name.lower().endswith(".zip"):
            file_name_with_extension: str = file_name
            file_name = file_name.replace(".zip", "")
        else:
            file_name_with_extension: str = f"{file_name}.zip"

        return (file_name, file_name_with_extension)

    # WARNING: Make this method testable since we cannot test failed extractions. Method crashes
    # FIX: Should not extract to folder ending in .zip
    # FIX: Should not throw error zip not found
    def __unzip_font(self, name: str) -> List[str]:
        """
        Unzip a font file and return a list of extracted files.

        Args:
            file_name (str): The name of the font file to unzip.

        Returns:
            List[str]: A list of file names that were extracted from the zip file.
        """
        file_name, file_name_with_extension = self.__get_filename_and_extension(name)

        zip_file_path: str = os.path.expanduser(
            f"~/Downloads/{file_name_with_extension}"
        )

        if not os.path.exists(zip_file_path):
            # HACK: Should raise an error or not be shown here
            print("The zip file does not exist")
            return []
        extracted_file_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
        os.makedirs(extracted_file_path, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(extracted_file_path)
        return os.listdir(extracted_file_path)

    def __move_font_to_directory(
        self, file_name: str, extracted_file_path: str, font_dir: str
    ):
        """
        Move font files from the extraction directory to the specified font directory.

        Args:
            file_name (str): The name of the font file.
            extracted_file_path (str): The path to the directory containing extracted font files.
            font_dir (str): The target directory to move the font files to.
        """
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
        """
        Install the fonts and update the font cache.

        Args:
            file_name (str): The name of the font to install.
        """
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
        """
        Install a font from a URL.

        Args:
            url (str): The URL of the font file to download and install.
            file_name (str): The name of the font file.

        Example:
            font_manager = FontManager()
            font_manager.install_font("https://example.com/font.zip", "font_name")
        """
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
