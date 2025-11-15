#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    if os.geteuid() != 0:
        print("\nPermission denied. Rerun this command with root privilege.\n")
        sys.exit(1)
    try:
        packageCLI().cmdloop()
    except KeyboardInterrupt:
        print("\n\nExiting...")
