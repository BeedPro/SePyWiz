import config


class TextUI:
    def __init__(self) -> None:
        self.__config = config.Config()
        self.__colors = self.__config.get_colors()

    def get_start_menu_text(self) -> str:
        return (
            f"Welcome to [{self.__colors['orange']}]SePyWiz[/{self.__colors['orange']}]\n"
            "This is the setup wizard for installation, syncing, repairing and also deletion.\n"
            f"  - [bold]([{self.__colors['teal']}]I[/{self.__colors['teal']}])[/bold]nstallation\n"
            f"  - [bold]([{self.__colors['blue']}]F[/{self.__colors['blue']}])[/bold]onts [Install fonts, by default this installs the Jetbrains font]\n"
            f"  - [bold]([{self.__colors['grey']}]S[/{self.__colors['grey']}])[/bold]ync Laptop/Desktop dotfiles and apps\n"
            f"  - [bold]([{self.__colors['black']}]D[/{self.__colors['black']}])[/bold]elete back to fresh [Not implemented]\n"
            f"  - [bold]([{self.__colors['pink']}]Q[/{self.__colors['pink']}])[/bold]uit"
        )

    def get_start_menu_invalid_text(self) -> str:
        return (
            "You have chosen an invalid option. Please enter a valid option\n"
            f"Valid options: [bold]([{self.__colors['teal']}]I[/{self.__colors['teal']}])[/bold]nstall, "
            f"[bold]([{self.__colors['blue']}]F[/{self.__colors['blue']}])[/bold]onts, "
            f"[bold]([{self.__colors['grey']}]S[/{self.__colors['grey']}])[/bold]ync, "
            f"[bold]([{self.__colors['black']}]D[/{self.__colors['black']}])[/bold]elete or "
            f"[bold]([{self.__colors['pink']}]Q[/{self.__colors['pink']}])[/bold]uit"
        )
