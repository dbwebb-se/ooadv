#!/usr/bin/env python3

"""
Main program for ooav, to start it all up.

See usage.py for details how to use program.
"""

import sys
from usage import Usage
from shell import Shell


def main():
    """
    Main function where it all starts.
    """
    usage = Usage()
    usage.parseOptions()

    print("Default options:")
    print(usage.default_options)

    print("Active options:")
    print(usage.options)
    print()

    Shell().cmdloop()

    sys.exit()


if __name__ == "__main__":
    main()
