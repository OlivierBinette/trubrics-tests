## Development utilities for trubrics-tests
##
## Usage:
## 		make <target> [<arg>=<value> ...]
##
## Targets:
## 		help:		Show this help message.
##		env: 		Create or update conda environment "trubrics"
ENV?=trubrics

.PHONY: help env

help: makefile
	@sed -n "s/^##//p" $<

env: environment.yml
	@echo "Updating ${ENV} environment..."; conda env update -f $<