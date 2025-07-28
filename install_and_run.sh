#!/bin/bash

echo "=== MIORITIC INJECTOR SETUP ==="
echo "Installing dependencies..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "mioritic_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv mioritic_env
fi

# Activate virtual environment and install dependencies
echo "Installing Python packages..."
source mioritic_env/bin/activate
pip install -r requirements.txt

# Make the main script executable
chmod +x mioritic_injector.py

echo ""
echo "=== SETUP COMPLETE ==="
echo "Starting Mioritic Injector..."
echo ""

# Run the application
python mioritic_injector.py