#!/usr/bin/env python3

"""
Keep details for a room.

.
"""

import json
from graphics import Graphics


class Room():
    """Wrap all details of a room.

    Attributes:
        name    Name of the room.
        data    Content of room/name.json.
        graphic Room viewed with graphic details.
    """

    name = None
    data = None
    graphics = None

    def __init__(self, name):
        """Init the room."""
        self.name = name
        self._load_details()
        self._load_graphics()

    def _load_details(self):
        """Load room details from file."""
        path = "room/" + self.name + ".json"
        with open(path) as f:
            self.data = json.load(f)

    def _load_graphics(self):
        """Load room graphics from file."""
        self.graphics = Graphics(self.data["graphics"])

    def __str__(self):
        """Print a view of the room."""
        return str(self.graphics) + "\n" + self.data["description"] + "\n"
