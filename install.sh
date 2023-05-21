#!/bin/bash

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Display success message
echo "Virtual environment created and dependencies installed."
