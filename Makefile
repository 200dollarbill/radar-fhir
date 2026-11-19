# PRATA: run `make` to list commands.
FQBN := m5stack:esp32:m5stack_atoms3r:USBMode=hwcdc,CDCOnBoot=cdc
PORT ?= /dev/ttyACM0
PY   := .venv/bin/python
ENV  := .env/prata.env

.DEFAULT_GOAL := help
.PHONY: help setup server test firmware flash eval

help: ## list commands
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

setup: ## create .venv and install the server
	python3 -m venv .venv
	$(PY) -m pip install -e .

server: ## run the server on http://127.0.0.1:8000 (website at /capture/)
	@test -f $(ENV) || { echo "missing $(ENV): see README.md, Secrets"; exit 1; }
	. ./$(ENV) && $(PY) -m fhir_server serve --port 8000

test: ## run every test suite
	$(PY) -m pytest tests -q
	node --test "website/tests/*.test.js"
	python3 -m pytest tools/scrape/tests -q
	python3 tools/scrape/lint_views.py

firmware: ## compile the board firmware
	arduino-cli compile --fqbn "$(FQBN)" firmware/radar_json

flash: firmware ## compile and upload to the board (PORT=/dev/ttyACM0)
	arduino-cli upload -p $(PORT) --fqbn "$(FQBN)" firmware/radar_json

eval: ## rescore the display methods (rewrites docs/eval/)
	node website/eval/run.mjs
