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

    def test_version(self):
        with self.assertRaises(SystemExit):
            self.usage.parseOptions("-v".split())

        with self.assertRaises(SystemExit):
            self.usage.parseOptions("--version".split())

    def test_help(self):
        with self.assertRaises(SystemExit):
            self.usage.parseOptions("-h".split())

        with self.assertRaises(SystemExit):
            self.usage.parseOptions("--help".split())


if __name__ == "__main__":
    unittest.main()
