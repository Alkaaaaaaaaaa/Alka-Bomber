#!/bin/bash

sudo cp Launch-Linux.sh /usr/local/bin/AlkaBomber
sudo chmod +x /usr/local/bin/AlkaBomber

PYTHON_EXECUTABLE=/usr/bin/python3

SCRIPT_FILE=Alka-Bomber.py

if [ ! -x "$PYTHON_EXECUTABLE" ]; then
  echo "Error: Python executable not found at $PYTHON_EXECUTABLE"
  exit 1
fi

if [ ! -f "$SCRIPT_FILE" ]; then
  echo "Error: Script file not found at $SCRIPT_FILE"
  exit 1
fi

"$PYTHON_EXECUTABLE" "$SCRIPT_FILE" "$@"
