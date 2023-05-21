#!/bin/bash

# Check if virtual environment exists
if [ ! -d "myenv" ]; then
  # Create the virtual environment
  echo "Creating virtual environment..."
  python3 -m venv myenv
fi

# Install dependencies
echo "Installing dependencies..."
myenv/bin/pip install -r requirements.txt

echo "All set! Your virtual environment is ready and the necessary dependencies have been installed. To activate it, use the following command:"
echo "source myenv/bin/activate"
