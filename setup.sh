#!/bin/bash
# This script sets up a virtual environment and installs the required package.

# Check if the virtual environment directory exists.
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment.
# For macOS/Linux:
source venv/bin/activate

# Upgrade pip and install the atlassian-python-api package.
pip install --upgrade pip
pip install atlassian-python-api black

echo "Setup complete. You can now run the demo with: python demo.py"
