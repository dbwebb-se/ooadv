#!/usr/bin/env python3

"""
Using module cmd to create a shell for the interactive program.

Some methods hidden from menu.
"""

import cmd
from game import Game
from room import Room


class Shell(cmd.Cmd):
    """Interactive shell to carry out commands within main loop."""

    intro = "Welcome to the XXX shell. Type help or ? to list commands.\n"
    prompt = "(XXX) "

    game = None

    # Do not show in help
    _hidden_methods = ('do_EOF',)

    # pylint: disable=R0201

    def inject(self, game):
        """The game to work with."""
        self.game = game

    def do_init(self, _):
        """Init the game."""
        pass

    def do_start(self, _):
        """Start the game by moving into the first room."""
        room = Room("start")
        print(room)

    def do_hi(self, _):
        """Say hi.

        >>> Shell().do_hi(None)
        Hi yourself!
        """
        print("Hi yourself!")

    def do_name(self, arg):
        """Say your name."""
        print("Hi there {}. How are you today?".format(arg))

    def emptyline(self):
        """Ignore when line is empty."""
        pass

    def get_names(self):
        """Get all names of the class, but not those hidden from help."""
        list1 = dir(self.__class__)
        list2 = self._hidden_methods
        return [x for x in list1 if x not in list2]

    def do_exit(self, _):
        """Leave."""
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, _):
        """Exit when ctrl-d."""
        print()
        return self.do_exit(_)
