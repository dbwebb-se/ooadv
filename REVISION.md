Revision history
===================

TODO
-------------------

* Add testcases for module shell.
* Add settings for virtualenv (add support to Makefile).
* Add automatic build/tests with Travis, CircleCI, coveralls.


v1.3.2 (2017-01-31)
-------------------

* Move tests to directory `tests/`
* Adding Makefile to run all tests.
* Adding file `.requirements.txt` for pip installs.
* Makefile for `make install` and `make check`.
* Add coverage and `make coverage`.
* Add pep8 and pylint as test/validation tools.
* Add `make doc` for api-documentation and uml.


v1.3.1 (2017-01-24)
-------------------

* Usage: Added comments for tests.
* Usage: Added unittest for --version, -v and --help, -h.


v1.3.0 (2017-01-24)
-------------------

* Usage: Added unittest for --silent and --verbose.


v1.2.1 (2017-01-24)
-------------------

* Shell: Change behaviour for empty lines.
* Shell: Add ctrl-d as alternative to exit.
* Adding pythonic `.pylintrc`.


v1.2.0 (2017-01-24)
-------------------

* Adding a shell for interactive usage, adding sample commands to make it work.


v1.1.1 (2017-01-24)
-------------------

* Adding default options inside class Usage.
* Main now prints default options and active options.
* Supports `--silent` and `--verbose`.


v1.1.0 (2017-01-24)
-------------------

* Ported getopts and usage to usage.py and made a class of it.
* Supports `-v --version` and `-h --help`.
* Prints out the options (empty) when called without options.
* Adding .gitignore


v1.0.0 (2017-01-24)
-------------------

* Adding `orig/mynameis2py` to rewrite as OO-code.
* Started work in line with course oopython as sample code to use in lectures.
