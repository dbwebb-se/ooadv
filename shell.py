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

    # Do not show in help
    __hidden_methods = ('do_EOF',)

    def do_hi(self, _):
        """
        Say hi.
        """
        print("Hi yourself!")

    def do_name(self, arg):
        """
        Say your name.
        """
        print("Hi there {}. How are you today?".format(arg))

    def emptyline(self):
        """
        Ignore when line is empty.
        """
        pass

    def get_names(self):
        """
        Get all names of the class, but not those hidden from help.
        """
        l1 = dir(self.__class__)
        l2 = self.__hidden_methods
        return [x for x in l1 if x not in l2]

    def do_exit(self, _):
        """
        Leave.
        """
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, _):
        """
        Exit when ctrl-d
        """
        print()
        return self.do_exit(_)
