#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

import sys

from pkg_resources import DistributionNotFound, VersionConflict

from lib.core.data import options
from lib.core.exceptions import FailedDependenciesInstallation
from lib.core.installation import check_dependencies, install_dependencies

if sys.version_info < (3, 10, 5):
    sys.stdout.write("Sorry, insect requires Python 3.10 or higher\n")
    sys.exit(1)

try:
    check_dependencies()
except (DistributionNotFound, VersionConflict):
    option = input("Missing required dependencies to run.\n"
                   "Do you want insect to automatically install them? [Y/n] ")

    if option.lower() == 'y':
        print("Installing required dependencies...")

        try:
            install_dependencies()
        except FailedDependenciesInstallation:
            print("Failed to install dirsearch dependencies, try doing it manually.")
            exit(1)


def main():
    from lib.core.options import parse_options

    options.update(parse_options())

    from lib.controller.controller import Controller

    Controller()


if __name__ == "__main__":
    main()
