#!/bin/bash
# Ralph-style loop: keeps re-launching the agent with a fresh context.
# Stops ONLY when you press Ctrl+C.
mkdir -p loop_logs
i=0
while :; do
  i=$((i+1))
  echo "=== Iteration $i — $(date) ==="
  cat LOOP_PROMPT.md | gemini -p --yolo 2>&1 | tee "loop_logs/iter_${i}.log"
  echo "=== End iteration $i ==="
  sleep 5
done
