#!/usr/bin/env python3

"""
Main program for ooav, to start it all up.

See usage.py for details how to use program.
"""

import sys
from usage import Usage


def main():
    """
    Main function where it all starts.
    """
    usage = Usage()
    options = usage.parseOptions()
    print(options)

    sys.exit()


if __name__ == "__main__":
    main()
