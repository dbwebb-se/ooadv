#!/usr/bin/env python3

"""Unittest for the usage module."""

import unittest
from usage import Usage


class TestUsageModule(unittest.TestCase):
    """Test cases."""

    def setUp(self):
        """Setup each testcase."""
        self.usage = Usage()

    def test_silent_verbose(self):
        """Check options for silent and verbose.

        --silent
        --verbose
        --silent --verbose
        """
        options = self.usage.parse_options("".split())
        self.assertFalse(options["silent"])
        self.assertFalse(options["verbose"])

        self.usage.__init__()
        options = self.usage.parse_options("--silent".split())
        self.assertTrue(options["silent"])
        self.assertFalse(options["verbose"])

        self.usage.__init__()
        options = self.usage.parse_options("--verbose".split())
        self.assertFalse(options["silent"])
        self.assertTrue(options["verbose"])

        self.usage.__init__()
        options = self.usage.parse_options("--verbose --silent".split())
        self.assertTrue(options["silent"])
        self.assertTrue(options["verbose"])

    def test_version(self):
        """Check options for version.

        -v
        --version
        """
        with self.assertRaises(SystemExit):
            self.usage.parse_options("-v".split())

        with self.assertRaises(SystemExit):
            self.usage.parse_options("--version".split())

    def test_help(self):
        """Check options for help.

        -h
        --help
        """
        with self.assertRaises(SystemExit):
            self.usage.parse_options("-h".split())

        with self.assertRaises(SystemExit):
            self.usage.parse_options("--help".split())


if __name__ == "__main__":
    unittest.main()
