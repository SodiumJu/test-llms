#!/bin/bash
set -e
# ./scripts/minizero-start-container.sh --image yanrudocker/qwen-runner:v1 $@
./scripts/minizero-start-container.sh --image yanrudocker/test-llm $@
