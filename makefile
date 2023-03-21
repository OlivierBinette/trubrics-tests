## Development utilities for trubrics-tests
##
## Usage:
## 		make <target> [<arg>=<value> ...]
##
## Targets:
## 		help:		Show this help message.
##		env: 		Create or update conda environment "trubrics"
##		run_01:		Run Streamlit app "01-simple-example/streamplit_app.py"
ENV?=trubrics-tests

.PHONY: help env run_01

help: makefile
	@sed -n "s/^##//p" $<

env: environment.yml
	@echo "Updating ${ENV} environment..."; conda env update -f $<

run_01:
	conda run -v --live-stream -n ${ENV} streamlit run 01-simple-example/streamlit_app.py --server.fileWatcherType none