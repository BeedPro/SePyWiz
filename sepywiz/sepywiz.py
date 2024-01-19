#!/bin/python3
"""
This script depends that gh, git, and nala are installed on the system.

TODO: Need to have test coverage
USEFUL functions: os.readlink()
"""
from wizard import Wizard


if __name__ == "__main__":
    wizard: Wizard = Wizard()
    wizard.main()
