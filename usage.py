#!/usr/bin/env python3

"""
Usage and parsing options.

Exit status:
0 EXIT_SUCCESS success
1 EXIT_USAGE   failed parsing cli options
2 EXIT_FAILED  Execution error
"""

import os
import sys
import getopt


#
# Add basics about this program
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Mikael Roos"
EMAIL = "mikael.t.h.roos@gmail.com"
VERSION = "v1.1.1"

MSG_USAGE = """{program} - short description. By {author} ({email}), version {version}.

Usage:
  {program} [options] name

Options:
  -h, --help                         Display this help message.
  -v, --version                      Print version and exit.
""".format(
    program=PROGRAM,
    author=AUTHOR,
    email=EMAIL,
    version=VERSION
)

MSG_VERSION = "{program} version {version}.".format(
    program=PROGRAM,
    version=VERSION
)

MSG_HELP = "Use {program} --help to get usage.".format(program=PROGRAM)


#
# Global default settings affecting behaviour of script in several places
#
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2


class Usage():
    """
    Parse CLI options and return as dict. Deal with usage information.
    """
    default_options = {
        "verbose": False,
        "silent": False,
    }

    options = {}

    def __init__(self):
        """
        Initiate.
        """
        self.options = self.default_options.copy()

    def printUsage(self, exitStatus=0):
        """
        Print usage information about the script and exit.
        """
        print(MSG_USAGE)
        sys.exit(exitStatus)

    def printVersion(self):
        """
        Print version information and exit.
        """
        print(MSG_VERSION)
        sys.exit()

    def parseOptions(self, argv=None):
        """
        Parse all command line options and arguments and
        return them as a dictionary.
        """
        argv = argv if not None else sys.argv[1:]
        try:
            opts, _ = getopt.getopt(argv, "hv", [
                "help",
                "version",
                "silent",
                "verbose"
            ])

            for opt, _ in opts:
                if opt in ("-h", "--help"):
                    self.printUsage()

                elif opt in ("-v", "--version"):
                    self.printVersion()

                elif opt in ("--silent"):
                    self.options["silent"] = True

                elif opt in ("--verbose"):
                    self.options["verbose"] = True

        except getopt.GetoptError as e:
            print(e)
            print(MSG_HELP)
            sys.exit(EXIT_USAGE)

        return self.options
