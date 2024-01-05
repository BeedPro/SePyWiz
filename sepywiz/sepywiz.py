#!/bin/python3
"""
This script depends that gh, git, and nala are installed on the system.

TODO: Need to have test coverage
USEFUL functions: os.readlink()
"""
from rich import print
from rich.console import Console
from typing import Any, List
import os
import zipfile
import subprocess
import shutil
import json

console = Console(color_system="truecolor")

COLORS = {
    "orange": "#FFC170",
    "black": "#696363",
    "teal": "#84DCCF",
    "blue": "#A6D9F7",
    "grey": "#BCCCE0",
    "pink": "#BF98A0",
}

APPLICATION_INSTALL_JSON_PATH = "data/applications_to_install.json"
if os.path.exists(APPLICATION_INSTALL_JSON_PATH):
    with open(APPLICATION_INSTALL_JSON_PATH, "r") as json_file:
        DATA: Any = json.load(json_file)
        PACKAGES_TO_INSTALL: Any = DATA.get("apt_packages", [])
else:
    DATA: Any = {}
    PACKAGES_TO_INSTALL: Any = []

VALID_MENU_OPTIONS: List[str] = [
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

VALID_INSTALLATION_OPTIONS: List[str] = ["p", "a"]


def is_package_installed(name: str) -> bool:
    try:
        subprocess.run(
            ["dpkg", "-l", name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def install_package(name: str) -> bool:
    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["sudo", "apt", "install", "-y", name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode == 0:
        print(f"{name} has been successfully installed.")
        return True
    else:
        print(f"Error installing {name}. Return code: {result.returncode}")
        print(result.stderr.decode("utf-8"))
        return False


def install_packages():
    for package in PACKAGES_TO_INSTALL:
        if is_package_installed(package):
            print(f"Package {package} has already been installed")
        else:
            install_package(package)


def prepare_directories(file_name: str) -> str:
    if not file_name.lower().endswith(".AppImage"):
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


def download_file(url: str, download_path: str) -> subprocess.CompletedProcess:
    response: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["wget", url, "-O", download_path]
    )
    return response


def set_permissions(file_path: str, file_name: str) -> None:
    if os.path.exists(file_path):
        # Set permissions to 755
        os.chmod(f"{file_path}/{file_name}", 0o755)
        print(f"Permissions for {file_name} set to 755.")
    else:
        print(f"File {file_path} not found.")


def extract_appimage(path: str, file_name: str) -> bool:
    response: subprocess.CompletedProcess[bytes] = subprocess.run(
        [f"{path}/{file_name}", "--appimage-extract"]
    )
    source_directory: str = "squashfs-root"
    shutil.move(source_directory, path)
    return response.returncode == 0


def download_appimage(url: str, file_name: str) -> bool:
    download_path: str = prepare_directories(file_name)
    response: subprocess.CompletedProcess[Any] = download_file(
        url, f"{download_path}/{file_name}"
    )
    set_permissions(download_path, file_name)
    if extract_appimage(download_path, file_name):
        print("Extracted AppImage")
    else:
        print("AppImage failed to extract")
    return response.returncode == 0


def install_appimage(url: str, name: str):
    if download_appimage(url, name):
        print(f"Downloaded {name}'s AppImage")
    else:
        print(f"{name} AppImage was not able to be downloaded")


def install_apps():
    print("You have choosen Installation")
    print("(P)ackages, (A)ppImages, (Q)uit")
    choice: str = input(">>> ").lower()[0]
    while choice not in VALID_INSTALLATION_OPTIONS:
        print("Not a valid input")
        choice = input(">>> ")
    match choice:
        case "p":
            install_packages()
        case "a":
            url: str = input("Enter the url of the AppImage to install\n>>> ")
            name: str = input("Enter the application name you want it as\n>>> ")
            install_appimage(url, name)
        case _:
            print("Error in selection")


def setup_dots():
    pass


def install_scripts():
    pass


def download_font(url: str, file_name: str) -> bool:
    if not file_name.lower().endswith(".zip"):
        file_name += ".zip"
    download_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
    response: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["wget", url, "-O", download_path]
    )
    return response.returncode == 0


def unzip_font(file_name: str) -> List[str]:
    if not file_name.lower().endswith(".zip"):
        file_name += ".zip"
    zip_file_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
    extracted_file_path: str = os.path.expanduser(f"~/Downloads/{file_name}")
    os.makedirs(extracted_file_path, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extracted_file_path)
    return os.listdir(extracted_file_path)


def move_font_to_directory(file_name: str, extracted_file_path: str, font_dir: str):
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


def install_fonts(file_name: str):
    result: subprocess.CompletedProcess[bytes] = subprocess.run(["fc-cache", "-fv"])
    if result.returncode == 0:
        print(
            f"Font {file_name} has been installed, and font cache has been updated successfully"
        )
        print("Check if the font has been installed by running:")
        print('`fc-list | grep "FONT_NAME"`')
    else:
        print(f"Error installing {file_name}. Error return code: {result.returncode}")


def install_font(url: str, file_name: str):
    if download_font(url, file_name):
        print(f"{file_name} has been downloaded")
        extracted_files: List[str] = unzip_font(file_name)
        if extracted_files:
            print(f"{file_name} has been extracted in the Downloads directory")
            font_dir: str = "~/.local/share/fonts"
            move_font_to_directory(file_name, f"~/Downloads/{file_name}", font_dir)
            install_fonts(file_name)
        else:
            print("Extraction has failed or the zip file is empty")
    else:
        print(f"{file_name} was not able to be downloaded.")


def wizard_sync():
    print("The sync mode has been choosen")


def wizard_delete():
    print("The delete mode has been choosen")


def wizard_quit():
    print("You have choosen to quit the wizard")
    print("Quitting...")
    print("Quiting completed")


def get_mode() -> str:
    os.system("clear")
    print(f"Welcome to [{COLORS['orange']}]SePyWiz[{COLORS['orange']}]")
    print(
        "This is the setup wizard for installation, syncing, repairing and also deletion."
    )
    print(f"  - [bold]([{COLORS['teal']}]I[/{COLORS['teal']}])[/bold]nstallation")
    print(
        f"  - [bold]([{COLORS['blue']}]F[/{COLORS['blue']}])[/bold]onts [Install fonts, by default this installs the Jetbrains font]"
    )
    print(
        f"  - [bold]([{COLORS['grey']}]S[/{COLORS['grey']}])[/bold]ync Laptop/Desktop dotfiles and apps"
    )
    print(
        f"  - [bold]([{COLORS['black']}]D[/{COLORS['black']}])[/bold]elete back to fresh [Not implemented]"
    )
    print(f"  - [bold]([{COLORS['pink']}]Q[/{COLORS['pink']}])[/bold]uit")
    mode: str = input(">>> ")
    while mode.lower() not in VALID_MENU_OPTIONS:
        print("You have choosen an invalid option please enter a valid option")
        print(
            f"Valid options: [bold]([{COLORS['teal']}]I[/{COLORS['teal']}])[/bold]nstall, [bold]([{COLORS['blue']}]F[/{COLORS['blue']}])[/bold]onts, [bold]([{COLORS['grey']}]S[/{COLORS['grey']}])[/bold]ync, [bold]([{COLORS['black']}]D[/{COLORS['black']}])[/bold]elete or [bold]([{COLORS['pink']}]Q[/{COLORS['pink']}])[/bold]uit"
        )
        mode: str = input(">>> ")
    if len(mode) > 1:
        return mode[0].lower()
    return mode.lower()


def main():
    mode: str = get_mode()
    match mode:
        case "i":
            install_apps()
        case "f":
            url: str = input(
                "Enter the download url for the font you wish to install\n>>> "
            )
            font_name: str = input(
                "Enter the filename you wish it to be downloaded to be named\n>>> "
            )
            install_font(url, font_name)
        case "s":
            wizard_sync()
        case "d":
            wizard_delete()
        case "q":
            wizard_quit()
        case _:
            print("Invalid mode has been selected, please rerun the script")


if __name__ == "__main__":
    main()
