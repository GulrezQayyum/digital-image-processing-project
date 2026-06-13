#!/bin/bash
# Setup Script for SE-504 Digital Image Processing Project
# This script installs all dependencies and sets up the environment

echo "=================================================="
echo "SE-504 Digital Image Processing - Setup Script"
echo "=================================================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python $python_version detected"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

echo "✓ Virtual environment activated"
echo ""

# Install requirements
echo "Installing Python packages..."
pip install -q -r requirements.txt
echo "✓ All packages installed successfully"
echo ""

# Create necessary directories
echo "Creating project directories..."
mkdir -p images
mkdir -p results
echo "✓ Directories created/verified"
echo ""

echo "=================================================="
echo "Setup Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Place your 2 color images in the 'images' folder"
echo "2. Run: python3 run_all_tasks.py"
echo "   OR run individual tasks:"
echo "      python3 src/01_grayscale.py"
echo "      python3 src/02_frequency.py"
echo "      python3 src/03_phase_magnitude.py"
echo "      python3 src/04_logical_arithmetic.py"
echo "      python3 src/05_noise_filtering.py"
echo ""
echo "Output images will be saved to the 'results' folder"
echo ""
