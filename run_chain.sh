#!/bin/bash

echo "[M87] Starting governed orchestration chain..."
python3 orchestrator.py retrieve $1
python3 orchestrator.py debate $1
echo "[M87] Chain complete."
