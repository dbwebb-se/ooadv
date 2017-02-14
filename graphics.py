#!/usr/bin/env python3

"""Load graphic parts and map on to each other."""


class Graphics():
    """Load, merge and print several asciiart."""

    parts = []
    canvas = []

    def __init__(self, parts):
        """"Setup and load all parts."""
        self.parts = parts
        self.load_and_merge_parts()

    def load_and_merge_parts(self):
        """Load graphics from file and merge into one."""
        for part in self.parts:
            content = self._load_part(part)
            self._merge_part(part, content)

    def _load_part(self, part):
        """Load one graphic from file."""
        path = "graphics/" + part["graphic"]
        with open(path) as f:
            content = f.readlines()
            content = [line.strip("\n") for line in content]
            return content

    def _merge_part(self, part, content):
        """Merge part onto canvas."""
        if not self.canvas:
            self.canvas = content
            return

        p_len = len(content)
        py = part["posY"]
        px = part["posX"]

        for i in range(p_len):
            c_len = len(content[i])
            part_a = self.canvas[i + py][0:px]
            part_b = content[i][:]
            part_c = self.canvas[i + py][px + c_len:]
            self.canvas[i + py] = part_a + part_b + part_c

    def __str__(self):
        """Print a view of the room."""
        str1 = ""
        for row in self.canvas:
            str1 += "".join(row) + "\n"

        return str1


def test():
    print("hej")
    
    g = Graphics([
        {
            "graphic": "base.txt",
            "posX": 0,
            "posY": 0
        },
        {
            "graphic": "tree.txt",
            "posX": 1,
            "posY": 1
        },
        {
            "graphic": "cat1.txt",
            "posX": 20,
            "posY": 8
        },
        {
            "graphic": "alien.txt",
            "posX": 50,
            "posY": 5
        }
    ])

    print(g)


if __name__ == "__main__":
    test()
