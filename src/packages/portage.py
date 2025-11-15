#!/usr/bin/env python3

import os
import sys
import cmd
import subprocess
import shlex

# TODO: Write the comments and docs cause I won't be remembering this afterwards.
class packageCLI(cmd.Cmd):

    # Set package manager name
    PKG_MGR_NAME = "emerge"

    # Command alias list
    # TODO: To make a real, --pretend less version, replace --pretend with --ask
    CMD_HELP = "emerge --help"
    CMD_MANUAL = "man emerge"
    CMD_SEARCH = "emerge --search"
    CMD_INFO = "emerge --info"
    CMD_INSTALL = "emerge"
    CMD_REMOVE = "emerge --unmerge"
    CMD_UPDATE = "emerge --update"
    CMD_CLEAN = "emerge --clean"
    CMD_DEPS_CLEAN = "emerge  --depclean"
    CMD_MAKE_CONFIG = "$EDITOR /etc/portage/make.conf"
    CMD_SYNC_DEPS = "emerge --sync"

    # Shell environment setup
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.intro = f'Welcome to CLI shell of {self.PKG_MGR_NAME}. Type help for command list. Press Ctrl+C or type \'exit\' to exit.\n'
        self.prompt = f'{self.PKG_MGR_NAME} > '

    # Search function
    def do_search(self, arg):
        parts = arg.split()
        if not parts:
            try:
                package_name = input("Input the package to search: ").strip()
            except EOFError:
                print("\nCancelled by user. Returning...")
                return
            if not package_name:
                print("No package names received. Returning...")
                return
            parts = package_name.split()
        package_name = parts[0]
        if len(parts) > 1:
             print(f"\nNote: Only one package may be searched at a time. The subsequent arguments will be ignored.\n")
        full_command = f"{self.CMD_SEARCH} {package_name}"
        self.execute_system_command(full_command)

    # Information function
    def do_info(self, arg):
        parts = arg.split()
        if not parts:
            try:
                package_name = input("Input the package to check information: ").strip()
            except EOFError:
                print("\nCancelled by user. Returning...")
                return
            if not package_name:
                print("No package name received. Returning...")
                return
            parts = package_name.split()
        package_name = parts[0]
        if len(parts) > 1:
             print(f"\nNote: Only one package may be checked at a time. The subsequent arguments will be ignored.\n")
        full_command = f"{self.CMD_INFO} {package_name}"
        self.execute_system_command(full_command)

    # Install function
    def do_install(self, arg):
        parts = arg.split()
        if parts:
                package_name = parts[0]
        else:
            try:
                package_name = input("Input the package to attempt installation: ").strip()
            except EOFError:
                print("\nCancelled by user. Returning...")
                return
            if not package_name:
                print("No package name received. Returning...")
                return
        try:
            options_line = input
            parts = package_name.split()
        package_name = parts[0]
        full_command = f"{self.CMD_INSTALL} {package_name}"
        self.execute_system_command(full_command)

    # Configure make.conf
    def do_configure(self, arg):
        full_command = f"{self.CMD_MAKE_CONFIG}"
        self.execute_system_command(full_command)

    # Exiting environment
    def do_exit(self, arg):
        print("\nExiting...")
        return True

    # Execution
    def execute_system_command(self, full_command):
        try:
            subprocess.run(shlex.split(full_command), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}.")
        except FileNotFoundError:
            print("\nError: Portage (emerge) was not found. Make sure you are on Gentoo Linux system.")
            print("If you are currently on Gentoo Linux, check if emerge is behaving correctly without this shell.")
            print("If Portage is not working correctly, you may check the wiki on how to troubleshoot")
            print("(https://wiki.gentoo.org/wiki/Portage/Help) or how to restore broken Portage")
            print("(https://wiki.gentoo.org/wiki/Project:Portage/Fixing_broken_portage)\n")

# Shell environment

if __name__ == '__main__':
    if os.geteuid() != 0:
        print("\nPermission denied. Rerun this command with root privilege.\n")
        sys.exit(1)
    try:
        packageCLI().cmdloop()
    except KeyboardInterrupt:
        print("\n\nExiting...")
