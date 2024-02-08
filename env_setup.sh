#!/bin/bash

# Define the name of the virtual environment
VENV_NAME="hypimg"

# Define the Python version
PYTHON_VERSION="3.8"

# Check if the virtual environment already exists
if ! { conda env list | grep $VENV_NAME; } &> /dev/null; then
    echo "Creating virtual environment..."
    conda create --name $VENV_NAME python=$PYTHON_VERSION -y
fi

echo "Activating conda environment................"
source activate $VENV_NAME || { echo "Failed to activate Conda environment"; exit 1; }

# Update pip
echo "Updating pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Replace Python scripts
echo "Replacing Python scripts..."
cp Misc/spherecluster_correction/spherical_kmeans.py $CONDA_PREFIX/lib/python$PYTHON_VERSION/site-packages/spherecluster/spherical_kmeans.py
cp Misc/spherecluster_correction/von_mises_fisher_mixture.py $CONDA_PREFIX/lib/python$PYTHON_VERSION/site-packages/spherecluster/von_mises_fisher_mixture.py

# Display completion message
echo "Virtual environment setup complete."
