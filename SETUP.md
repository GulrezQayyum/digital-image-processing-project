# SE-504 Digital Image Processing Project - Setup Guide

## Environment Status

✓ **Python Environment**: Configured (Python 3.12.3 with virtual environment)
✓ **Dependencies**: Installed successfully

### Installed Packages:
- **opencv-python** (>=4.8.0) - Computer vision library
- **numpy** (>=1.24.0) - Numerical computing
- **matplotlib** (>=3.8.0) - Visualization and plotting
- **scipy** (>=1.11.0) - Scientific computing
- **pillow** (>=10.0.0) - Image processing
- **scikit-image** (>=0.21.0) - Image processing algorithms

## Project Structure

```
/2023-ag-9948(M1)SE-504/
├── src/                           # Source code directory
│   ├── 01_grayscale.py           # Task 1: Grayscale conversion
│   ├── 02_frequency.py           # Task 2: FFT transformation
│   ├── 03_phase_magnitude.py     # Task 3: Phase/magnitude interchange
│   ├── 04_logical_arithmetic.py  # Task 4: Logical & arithmetic operations
│   └── 05_noise_filtering.py     # Task 5: Noise addition and filtering
├── images/                        # Input images (ADD YOUR IMAGES HERE)
├── results/                       # Output images and results
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── SETUP.md                       # This file
├── setup.sh                       # Automated setup script
├── run_all_tasks.py              # Master script to run all tasks
└── .venv/                         # Virtual environment (created)
```

## Quick Start

### Option 1: Automated Setup (Linux/Mac)

```bash
# Make setup script executable
chmod +x setup.sh

# Run setup script
./setup.sh
```

### Option 2: Manual Setup

#### 1. Activate Virtual Environment

```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Add Images

Place your 2 color images in the `images/` folder:
- Supported formats: `.jpg`, `.png`, `.bmp`, `.jpeg`
- Recommended size: 256x256 or larger
- The scripts will automatically detect and process them

#### 4. Run the Project

**Option A: Run all tasks at once**
```bash
python3 run_all_tasks.py
```

**Option B: Run individual tasks**
```bash
# Task 1: Convert to grayscale
python3 src/01_grayscale.py

# Task 2: Frequency domain transformation
python3 src/02_frequency.py

# Task 3: Phase and magnitude interchange
python3 src/03_phase_magnitude.py

# Task 4: Logical and arithmetic operations
python3 src/04_logical_arithmetic.py

# Task 5: Noise addition and filtering
python3 src/05_noise_filtering.py
```

## Task Details

### Task 1: Grayscale Conversion
- Converts color images to grayscale
- Displays side-by-side comparison
- Saves results to `results/01_*_grayscale.png`

### Task 2: Frequency Domain Transformation
- Applies 2D Fast Fourier Transform (FFT)
- Displays magnitude and phase spectra
- Shows reconstructed images
- Saves magnitude and phase information

### Task 3: Phase & Magnitude Interchange
- Extracts magnitude and phase from both images
- Interchanges magnitude and phase between images
- Creates new images with mixed components
- Demonstrates importance of phase information

### Task 4: Logical & Arithmetic Operations
**Logical Operations:**
- AND: Bitwise AND between images
- OR: Bitwise OR between images
- XOR: Bitwise exclusive OR
- NOT: Bitwise negation

**Arithmetic Operations:**
- Addition: Pixel-wise sum (with saturation)
- Subtraction: Pixel-wise difference
- Multiplication: Element-wise product
- Average: Mean of two images

### Task 5: Noise Addition & Filtering
**Noise Added:** Salt & Pepper (5% of pixels)

**Filters Applied:**
1. **Median Filter** - Best for salt & pepper noise
2. **Bilateral Filter** - Preserves edges while removing noise
3. **Morphological Filter** - Uses structural elements

**Quality Metrics:** PSNR (Peak Signal-to-Noise Ratio) calculated for each filter

## Output Files

The `results/` folder will contain:

### From Task 1
- `01_grayscale_comparison.png` - Side-by-side comparison
- `01_*_grayscale.png` - Individual grayscale images

### From Task 2
- `02_frequency_domain.png` - FFT visualizations
- `02_*_magnitude.png` - Magnitude spectra
- `02_*_phase.png` - Phase information

### From Task 3
- `03_phase_magnitude_interchange.png` - Interchange results
- `03_mag*_phase*.png` - Individual results

### From Task 4
- `04_logical_arithmetic_operations.png` - All operations visualization
- `04_*_logical_*.png` - Individual logical operations
- `04_*_arithmetic_*.png` - Individual arithmetic operations

### From Task 5
- `05_noise_filtering.png` - Noise and filter comparison
- `05_*_noisy.png` - Images with salt & pepper noise
- `05_*_median.png` - Median filter results
- `05_*_bilateral.png` - Bilateral filter results
- `05_*_morphological.png` - Morphological filter results

## Troubleshooting

### No Images Found Error
- Ensure the `images/` folder exists
- Place at least 2 color images in the folder
- Supported formats: jpg, png, bmp, jpeg

### Module Import Errors
```bash
# Reinstall packages
pip install --upgrade -r requirements.txt

# Or reinstall specific package
pip install --upgrade opencv-python
```

### Display Issues (for matplotlib)
On Linux systems without display, images are saved to disk automatically.

### Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove old environment
rm -rf .venv

# Create fresh environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Verification

To verify everything is set up correctly:

```bash
python3 -c "import cv2, numpy, matplotlib, scipy, PIL; print('✓ All packages imported successfully')"
```

## Submission Checklist

- [ ] All 5 task scripts completed and tested
- [ ] 2 color images placed in `images/` folder
- [ ] All output files generated in `results/` folder
- [ ] README.md with project documentation
- [ ] Source code (src/ folder)
- [ ] Requirements.txt with dependencies

## Submission Details

- **File Name Format**: `2023-ag-9948(M1)/SE-504`
- **Deadline**: June 15, 2026 / 4:00 pm
- **Email**: mahsanlatif@uaf.edu.pk
- **Include**: Code + Results (both hard and soft copies)

## Additional Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [SciPy Documentation](https://docs.scipy.org/)

## Notes

- The project uses a Python virtual environment for dependency isolation
- All output images are saved with appropriate naming for easy identification
- PSNR values help evaluate filter effectiveness
- Phase information carries spatial details (edges, textures)
- Magnitude information determines overall contrast and structure

## Contact

For issues or questions:
- Course Email: mahsanlatif@uaf.edu.pk
- Course: SE-504 Digital Image Processing
- University: Department of Computer Science, UAF

---
*Last Updated: June 2026*
