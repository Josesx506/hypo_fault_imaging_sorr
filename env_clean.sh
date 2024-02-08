#!/bin/bash

# Define the name of the virtual environment
VENV_NAME="hypimg"

# Check if the virtual environment exists
if { conda env list | grep $VENV_NAME; } >/dev/null; then
    echo "Cleaning up virtual environment..."

    # Remove the virtual environment
    conda remove --name $VENV_NAME --all -y
    echo "Virtual environment '$VENV_NAME' deleted."
else
    echo "Virtual environment '$VENV_NAME' does not exist."
fi