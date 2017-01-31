#!/usr/bin/make -f

# Detect OS
OS = $(shell uname -s)

# Defaults
ECHO = echo

# Make adjustments based on OS
# http://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux/27776822#27776822
ifneq (, $(findstring CYGWIN, $(OS)))
	ECHO = /bin/echo -e
endif

# Colors and helptext
NO_COLOR	= \033[0m
ACTION		= \033[32;01m
OK_COLOR	= \033[32;01m
INFO_COLOR	= \033[34;01m
ERROR_COLOR	= \033[31;01m
WARN_COLOR	= \033[33;01m

# Which makefile am I in?
WHERE-AM-I = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call WHERE-AM-I)

# Echo some nice helptext based on the target comment
HELPTEXT = $(ECHO) "$(ACTION)--->" `egrep "^\# target: $(1) " $(THIS_MAKEFILE) | sed "s/\# target: $(1)[ ]*-[ ]* / /g"` "$(NO_COLOR)"

# Set path to environ coverage file
ENV = export COVERAGE_FILE="build/coverage"



# target: help                - Displays help.
.PHONY:  help
help:
	@$(call HELPTEXT,$@)
	@$(ECHO) "Usage:"
	@$(ECHO) " make [target] ..."
	@$(ECHO) "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# target: clean               - Clean all generated files.
.PHONY: clean
clean:
	@$(call HELPTEXT,$@)
	find -type d -name __pycache__ -exec rm -rf {} \;
	find -type f -name '*.pyc' -exec rm -f {} \;
	rm -rf build



# target: test                - Run all tests.
.PHONY: test
test: pylint pep8 unittest doctest coverage
	@$(call HELPTEXT,$@)



# target: unittest            - Run all unittests.
.PHONY: unittest
unittest:
	@$(call HELPTEXT,$@)
	python3 -m unittest discover -b -s tests



# target: doctest             - Run all doctests.
.PHONY: doctest
doctest:
	@$(call HELPTEXT,$@)
	python3 -m doctest *.py



# target: coverage            - Run code coverage of all unittests.
.PHONY: coverage
coverage:
	@$(call HELPTEXT,$@)
	@install -d build/coverage-html
	$(ENV) && coverage run --source=. -m unittest discover -b -s tests
	$(ENV) && coverage html --directory=build/coverage-html
	$(ENV) && coverage report -m



# target: pep8                - Run pep8 validation.
.PHONY: pep8
pep8:
	@$(call HELPTEXT,$@)
	@install -d build/pep8
	-pep8 --exclude=orig --count --statistics . | tee build/pep8/log.txt



# target: pylint              - Run pylint validation.
.PHONY: pylint
pylint:
	@$(call HELPTEXT,$@)
	@install -d build/pylint
	-pylint --reports=no *.py
	-@pylint *.py > build/pylint/output.txt



# target: doc                 - Create documentation.
.PHONY: doc
doc: doc-api doc-uml
	@$(call HELPTEXT,$@)



# target: doc-api             - Create api-documentation as HTML.
.PHONY: doc-api
doc-api:
	@$(call HELPTEXT,$@)
	@#python3 -m pydoc -w `find . -name '*.py'`
	python3 -m pydoc -w ./
	mv *.html doc/api



# target: doc-uml             - Create uml-documentation as images.
.PHONY: doc-uml
doc-uml:
	@$(call HELPTEXT,$@)
	#pyreverse -S -A -b -o png  -p ooadv *.py
	pyreverse -o png  -p ooadv *.py
	mv *.png doc/uml



# target: version             - Check version number consistency.
.PHONY: version
version:
	@$(call HELPTEXT,$@)
	grep -m 1 '^v.*)' REVISION.md
	./main.py --version 



# target: tag                 - Prepare to tag new version.
.PHONY: tag
tag: version doc test
	@$(call HELPTEXT,$@)



# target: install-tools       - Install needed devtools.
.PHONY: install-tools
install-tools:
	@$(call HELPTEXT,$@)
	python3 -m pip install --requirement .requirements.txt 



# target: upgrade-tools       - Upgrade needed devtools.
.PHONY: upgrade-tools
upgrade-tools:
	@$(call HELPTEXT,$@)
	python3 -m pip install --upgrade --requirement .requirements.txt 



# target: check               - Check versions of installed devtools.
.PHONY: check
check:
	@$(call HELPTEXT,$@)
	@$(ECHO) "$(INFO_COLOR)python:$(NO_COLOR)" && which python3 && python3 --version
	@$(ECHO) "\n$(INFO_COLOR)pip:$(NO_COLOR)" && python3 -m pip --version
	@$(ECHO) "\n$(INFO_COLOR)pylint:$(NO_COLOR)" && which pylint && pylint --version
	@$(ECHO) "\n$(INFO_COLOR)coverage:$(NO_COLOR)" && which coverage && coverage --version
	@$(ECHO) "\n$(INFO_COLOR)pep8:$(NO_COLOR)" && which pep8 && pep8 --version
