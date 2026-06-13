# SE-504 Digital Image Processing Project - Complete Setup Report

## ✓ SETUP COMPLETE - ENVIRONMENT READY

**Date**: June 13, 2026  
**Project**: 2023-ag-9948(M1) / SE-504  
**University**: Department of Computer Science (UAF)

---

## Environment Status

### Python Configuration
- **Python Version**: 3.12.3
- **Environment Type**: Virtual Environment (.venv)
- **Location**: `/home/gulrez/2023-ag-9948(M1)SE-504/.venv`
- **Status**: ✓ **ACTIVE AND READY**

### Installed Dependencies
| Package | Version | Status |
|---------|---------|--------|
| OpenCV (cv2) | 4.13.0 | ✓ Installed |
| NumPy | 2.4.6 | ✓ Installed |
| Matplotlib | 3.11.0 | ✓ Installed |
| SciPy | 1.17.1 | ✓ Installed |
| Pillow (PIL) | 12.2.0 | ✓ Installed |
| scikit-image | 0.21.0+ | ✓ Installed |

---

## Project Structure

```
/2023-ag-9948(M1)SE-504/
├── .venv/                         ✓ Virtual environment (configured)
├── .github/
│   └── copilot-instructions.md
├── src/
│   ├── 01_grayscale.py           ✓ Task 1 (104 lines)
│   ├── 02_frequency.py           ✓ Task 2 (123 lines)
│   ├── 03_phase_magnitude.py     ✓ Task 3 (190 lines)
│   ├── 04_logical_arithmetic.py  ✓ Task 4 (169 lines)
│   └── 05_noise_filtering.py     ✓ Task 5 (219 lines)
├── images/                        ← Add your 2 color images here
├── results/                       ← Output will be saved here
├── README.md                      ✓ Project documentation
├── SETUP.md                       ✓ Detailed setup guide
├── setup.sh                       ✓ Automated setup script
├── run_all_tasks.py              ✓ Master execution script
└── requirements.txt               ✓ Dependencies list
```

**Total Code**: 805 lines across 5 task scripts

---

## Task Implementation Summary

### ✓ Task 1: Grayscale Conversion (01_grayscale.py)
**Status**: Complete and Ready

**Features**:
- Load color images from `images/` directory
- Convert BGR to grayscale using OpenCV
- Display side-by-side comparison visualization
- Save individual grayscale images
- Save comparison plot

**Output Files**:
- `01_{name}_grayscale.png` - Grayscale images
- `01_grayscale_comparison.png` - Side-by-side comparison

---

### ✓ Task 2: Frequency Domain Transformation (02_frequency.py)
**Status**: Complete and Ready

**Features**:
- Apply 2D Fast Fourier Transform (FFT)
- Compute magnitude and phase spectra
- Logarithmic scaling for visualization
- Image reconstruction from FFT
- Display all intermediate steps

**Output Files**:
- `02_frequency_domain.png` - FFT visualization
- `02_{name}_magnitude.png` - Magnitude spectrum
- `02_{name}_phase.png` - Phase information

---

### ✓ Task 3: Phase & Magnitude Interchange (03_phase_magnitude.py)
**Status**: Complete and Ready

**Features**:
- Extract magnitude and phase from both images
- Interchange magnitude and phase between images
- Create hybrid images (Mag1+Phase2, Mag2+Phase1)
- Demonstrate importance of phase information
- Size matching for different dimension images

**Output Files**:
- `03_phase_magnitude_interchange.png` - Results comparison
- `03_mag1_phase2.png` - First hybrid
- `03_mag2_phase1.png` - Second hybrid

---

### ✓ Task 4: Logical & Arithmetic Operations (04_logical_arithmetic.py)
**Status**: Complete and Ready

**Logical Operations**:
- AND: Bitwise logical AND
- OR: Bitwise logical OR
- XOR: Bitwise exclusive OR
- NOT: Bitwise negation

**Arithmetic Operations**:
- Addition: Pixel-wise sum (saturated)
- Subtraction: Absolute difference
- Multiplication: Element-wise product
- Average: (Img1 + Img2) / 2

**Output Files**:
- `04_logical_arithmetic_operations.png` - All results
- `04_*_logical_*.png` - Individual operations
- `04_*_arithmetic_*.png` - Individual operations

---

### ✓ Task 5: Noise Addition & Filtering (05_noise_filtering.py)
**Status**: Complete and Ready

**Noise Processing**:
- Add salt & pepper noise (5% ratio)
- Apply 3 different filters:
  1. **Median Filter** (5x5) - Best for salt & pepper
  2. **Bilateral Filter** - Edge-preserving
  3. **Morphological Filter** - Structural approach

**Quality Metrics**:
- PSNR (Peak Signal-to-Noise Ratio) calculation
- MSE (Mean Squared Error) calculation
- Comparative analysis of filter effectiveness

**Output Files**:
- `05_noise_filtering.png` - Complete analysis
- `05_{name}_noisy.png` - Noisy image
- `05_{name}_median.png` - Median filtered
- `05_{name}_bilateral.png` - Bilateral filtered
- `05_{name}_morphological.png` - Morphological filtered

---

## How to Run

### Quick Start
```bash
# Activate environment (already done, but for reference)
source .venv/bin/activate

# Run all tasks at once
python3 run_all_tasks.py
```

### Individual Tasks
```bash
# Task 1: Grayscale conversion
python3 src/01_grayscale.py

# Task 2: Frequency domain
python3 src/02_frequency.py

# Task 3: Phase/magnitude interchange
python3 src/03_phase_magnitude.py

# Task 4: Logical/arithmetic operations
python3 src/04_logical_arithmetic.py

# Task 5: Noise and filtering
python3 src/05_noise_filtering.py
```

---

## Data Preparation

### Before Running - IMPORTANT
1. **Add Images**:
   - Place 2 color images in the `images/` folder
   - Supported formats: `.jpg`, `.png`, `.bmp`, `.jpeg`
   - Images will be auto-detected (sorted alphabetically)
   - Recommendation: At least 256x256 pixels

2. **Expected Directory Structure After Adding Images**:
   ```
   images/
   ├── image1.jpg
   └── image2.png
   ```

---

## Output Organization

After running, the `results/` folder will contain:

```
results/
├── 01_grayscale_comparison.png
├── 01_image1_grayscale.png
├── 01_image2_grayscale.png
├── 02_frequency_domain.png
├── 02_image1_magnitude.png
├── 02_image1_phase.png
├── 02_image2_magnitude.png
├── 02_image2_phase.png
├── 03_phase_magnitude_interchange.png
├── 03_mag1_phase2.png
├── 03_mag2_phase1.png
├── 04_logical_arithmetic_operations.png
├── 04_*_logical_*.png (5 files)
├── 04_*_arithmetic_*.png (5 files)
├── 05_noise_filtering.png
├── 05_*_noisy.png (2 files)
├── 05_*_median.png (2 files)
├── 05_*_bilateral.png (2 files)
└── 05_*_morphological.png (2 files)
```

---

## Verification Checklist

- ✓ Python environment configured
- ✓ All dependencies installed and verified
- ✓ All 5 task scripts completed (805 lines total)
- ✓ Virtual environment active and ready
- ✓ Project directories created
- ✓ Run scripts prepared
- ✓ Documentation complete

**Next Step**: Add 2 color images to `images/` folder and run `python3 run_all_tasks.py`

---

## Technical Specifications

### Computational Requirements
- **Python**: 3.12.3
- **Memory**: ~500MB for typical 512x512 images
- **Disk Space**: ~50-100MB for results
- **CPU**: Any modern processor (no GPU required)

### Algorithm Details

**FFT Operations**:
- 2D Forward FFT using NumPy (O(n² log n))
- Frequency shifting (DC component to center)
- Magnitude: sqrt(real² + imaginary²)
- Phase: atan2(imaginary, real)

**Filters**:
- Median: Sorts 5×5 neighborhood
- Bilateral: Considers spatial and intensity similarity
- Morphological: Opening (erosion → dilation)

**Quality Metrics**:
- PSNR = 20 × log₁₀(MAX / √MSE) in dB
- Higher PSNR = Better quality

---

## Troubleshooting Guide

### Issue: "No images found"
**Solution**: 
- Create `images/` folder if missing
- Add at least 2 color images
- Check supported formats (.jpg, .png, .bmp)

### Issue: Module import errors
**Solution**:
```bash
# Reinstall packages
pip install --upgrade -r requirements.txt
```

### Issue: Display/GUI errors on remote system
**Solution**:
- Images are automatically saved to disk
- No display required - all results available in `results/`

### Issue: Memory errors with large images
**Solution**:
- Resize images to ≤1024×1024 pixels
- Increase available RAM/swap space

---

## Project Deadline

- **Submission Date**: June 15, 2026 / 4:00 pm
- **Submission Email**: mahsanlatif@uaf.edu.pk
- **Format**: Code + Results (hard copy + soft copy)
- **File Name**: `2023-ag-9948(M1)/SE-504`

---

## What to Submit

Create a folder named `2023-ag-9948(M1)/SE-504` containing:

1. **Source Code** (`src/` folder)
   - All 5 task Python scripts
   - Total: 805 lines of code

2. **Results** (`results/` folder)
   - All output images from running tasks
   - Total: ~30-40 image files

3. **Original Images** (`images/` folder)
   - Your 2 color input images

4. **Documentation**
   - README.md
   - SETUP.md
   - This report

5. **Configuration Files**
   - requirements.txt
   - run_all_tasks.py

---

## Support & Resources

- **Course Instructor**: Mahsan Latif
- **Email**: mahsanlatif@uaf.edu.pk
- **University**: Department of Computer Science, UAF
- **Course**: SE-504 Digital Image Processing
- **Semester**: Spring 2026

---

## Summary

✓ **SYSTEM STATUS**: FULLY CONFIGURED AND READY

Your SE-504 Digital Image Processing project environment is completely set up with:
- All 5 task implementations ready
- Complete Python environment with all dependencies
- Comprehensive documentation and guides
- Master execution script for all tasks
- Individual task scripts for flexibility

**Next Action**: Add your 2 color images to the `images/` folder and run:
```bash
python3 run_all_tasks.py
```

Good luck with your project!

---

*Generated: June 13, 2026 - SE-504 Project Environment Report*
