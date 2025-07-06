import subprocess
import sys
import json

def run_subagent(task_type, input_path):
    if task_type == "retrieve":
        subprocess.run(["./subagents/gemini_retrieve.sh", input_path])
    elif task_type == "debate":
        subprocess.run(["./subagents/gemini_debate.sh", input_path])
    else:
        print("Unknown task type.")

if __name__ == "__main__":
    task = sys.argv[1]
    input_file = sys.argv[2]
    run_subagent(task, input_file)
