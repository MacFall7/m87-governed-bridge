# M87 Governed Bridge

A governed agent orchestration bridge connecting Claude with Gemini CLI agents, featuring emotional modulation, safe output delivery, and CLI sub-agent execution.

## Features

- Orchestrator → Gemini handoff
- CLAUDE.md as primary instruction source
- Emotion signal integration
- CLI-safe execution via `run_chain.sh`
- Output validation (SPOT, FORT, PARCEL pattern)

## Quick Start

```bash
pip install -r requirements.txt
bash run_chain.sh prompt.txt
```

Customize `CLAUDE.md` and `emotion_signal.json` as needed.
