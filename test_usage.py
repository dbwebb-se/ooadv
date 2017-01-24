#!/usr/bin/env python3

"""
Unittest for the usage module.
"""

import unittest
from usage import Usage

# pylint: disable=C0111


class TestUsageModul(unittest.TestCase):

    def setUp(self):
        self.usage = Usage()

    def test_silent_verbose(self):
        self.usage.__init__()
        options = self.usage.parseOptions("--silent".split())
        self.assertTrue(options["silent"])
        self.assertFalse(options["verbose"])

        self.usage.__init__()
        options = self.usage.parseOptions("--verbose".split())
        self.assertFalse(options["silent"])
        self.assertTrue(options["verbose"])

        self.usage.__init__()
        options = self.usage.parseOptions("--verbose --silent".split())
        self.assertTrue(options["silent"])
        self.assertTrue(options["verbose"])


if __name__ == "__main__":
    unittest.main()
