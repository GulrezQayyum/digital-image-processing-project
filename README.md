# SE-504: Digital Image Processing - Final Project

**Course:** Digital Image Processing (SE-504)  
**University:** Department of Computer Science (UAF)  
**Semester:** Spring 2026  
**Deadline:** June 15, 2026 / 4:00 pm  
**Marks:** 10

## Project Objectives

Work with 2 color images and perform the following operations:

1. **Convert to Grayscale** - Convert both color images to grayscale format
2. **Frequency Domain Transformation** - Apply FFT to transform images into frequency domain
3. **Phase & Magnitude Interchange** - Swap phases and magnitudes between images and display results
4. **Logical & Arithmetic Operations** - Demonstrate bitwise operations (AND, OR, XOR) and arithmetic operations on grayscale images
5. **Noise & Filtering** - Add salt & pepper noise and apply 3 different noise removal filters

## Project Structure

```
├── images/                 # Input color images (add your 2 images here)
├── results/               # Output images and results
├── src/
│   ├── 01_grayscale.py   # Task 1: Grayscale conversion
│   ├── 02_frequency.py   # Task 2: Frequency domain transformation
│   ├── 03_phase_magnitude.py  # Task 3: Phase/magnitude interchange
│   ├── 04_logical_arithmetic.py  # Task 4: Operations
│   └── 05_noise_filtering.py  # Task 5: Noise and filtering
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation & Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your Images

Place your 2 color images in the `images/` folder:
- Any standard format: `.jpg`, `.png`, `.bmp`, etc.
- The scripts will automatically detect images in this folder

### 3. Run the Project

Each script can be run independently:

```bash
python src/01_grayscale.py
python src/02_frequency.py
python src/03_phase_magnitude.py
python src/04_logical_arithmetic.py
python src/05_noise_filtering.py
```

Or run the main script (if created) that executes all tasks sequentially.

## Image Processing Libraries Used

- **OpenCV (cv2)**: Image reading, basic operations, filtering
- **NumPy**: Numerical operations and FFT
- **Matplotlib**: Visualization and displaying results
- **SciPy**: Advanced filtering (median, bilateral, etc.)
- **Pillow**: Image format handling

## Output

All results will be saved to the `results/` folder with appropriate naming:
- Grayscale images
- Frequency domain visualizations
- Phase/magnitude swapped results
- Operation demonstrations
- Filtered noisy images

## Submission Requirements

- **File Naming:** `2023-ag-9948(M1)/SE-504`
- **Include:** Source code + Results (images)
- **Format:** Code files + output images
- **Email:** mahsanlatif@uaf.edu.pk

## Deliverables Checklist

- [ ] Both color images converted to grayscale
- [ ] FFT transformation and visualization
- [ ] Phase and magnitude interchanged results displayed
- [ ] Logical operations (AND, OR, XOR) demonstrated
- [ ] Arithmetic operations demonstrated
- [ ] Salt & pepper noise added to images
- [ ] 3 different noise removal filters applied
- [ ] Comparison and results displayed
- [ ] All code properly commented
- [ ] Results saved with clear naming

## Notes

- Ensure images are in the `images/` folder before running scripts
- Results will overwrite previous runs, so save important results separately
- All display windows auto-close after a few seconds (can be modified in code)
- Adjust image paths if needed in each script

## Contact

For questions: mahsanlatif@uaf.edu.pk

---

*Project setup created with Python 3.x environment and required image processing libraries.*
