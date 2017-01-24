#!/usr/bin/env python3

"""
Using module cmd to create a shell for the interactive program.
"""

import cmd


class Shell(cmd.Cmd):
    """
    Interactive shell to carry out commands within main loop.
    """
    intro = "Welcome to the XXX shell. Type help or ? to list commands.\n"
    prompt = "(XXX) "

    def do_hi(self):
        """
        Say hi.
        """
        print("Hi yourself!")

    def do_name(self, arg):
        """
        Say your name.
        """
        print("Hi there {}. How are you today?".format(arg))

    def do_exit(self):
        """
        Leave.
        """
        print("Bye bye - see ya soon again")
        return True

    def emptyline(self):
        pass
