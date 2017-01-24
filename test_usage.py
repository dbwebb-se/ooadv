#!/usr/bin/env python3

"""
Unittest for the usage module.
"""

import unittest
from usage import Usage


class TestUsageModul(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        """Setup each testcase"""
        self.usage = Usage()

    def test_silent_verbose(self):
        """
        --silent
        --verbose
        --silent --verbose
        """
        options = self.usage.parseOptions("".split())
        self.assertFalse(options["silent"])
        self.assertFalse(options["verbose"])

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

    def test_version(self):
        """
        -v
        --version
        """
        with self.assertRaises(SystemExit):
            self.usage.parseOptions("-v".split())

        with self.assertRaises(SystemExit):
            self.usage.parseOptions("--version".split())

    def test_help(self):
        """
        -h
        --help
        """
        with self.assertRaises(SystemExit):
            self.usage.parseOptions("-h".split())

        with self.assertRaises(SystemExit):
            self.usage.parseOptions("--help".split())


if __name__ == "__main__":
    unittest.main()
