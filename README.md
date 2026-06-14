# 🖼️ DIPix - Digital Image Processing Suite

**SE-504: Digital Image Processing | Final Exam Project | Spring 2026**

University of Agriculture, Faisalabad | Department of Computer Science

---

## 📋 Project Overview

DIPix is a comprehensive Python-based image processing suite that implements fundamental digital image processing techniques. This project demonstrates core concepts including color space transformations, frequency domain analysis, image filtering, and pixel-level operations.

**Semester Project for:** SE-504 Digital Image Processing  
**Institution:** University of Agriculture, Faisalabad  
**Author:** Gulrez Qayyum  
**Date:** June 2026

---

## ✨ Features

### **Task 1: Grayscale Conversion** 🎨
Convert color images (RGB/BGR) to grayscale using the standard luminosity formula.
- Preserves detail and contrast
- Reduces 3 channels to single channel
- Foundation for frequency domain analysis

### **Task 2: Frequency Domain Transformation** 📡
Transform images from spatial to frequency domain using Fast Fourier Transform (FFT).
- Extract magnitude spectrum (intensity/power distribution)
- Extract phase spectrum (structural information)
- Visualize with log scaling for better frequency representation
- Reconstruct images from frequency components

### **Task 3: Phase & Magnitude Interchange** 🔄
Demonstrate the relative importance of phase vs. magnitude by swapping components between images.
- Combine magnitude from Image 1 with phase from Image 2
- Combine magnitude from Image 2 with phase from Image 1
- **Key Finding:** Phase carries more structural information than magnitude

### **Task 4: Logical & Arithmetic Operations** ⚙️
Apply pixel-level operations between two grayscale images.

**Logical Operations (Bitwise):**
- AND - Common bright pixels
- OR - Any bright pixels
- XOR - Exclusive difference
- NOT - Inversion

**Arithmetic Operations:**
- Addition - Combine brightness (saturates at 255)
- Subtraction - Pixel-by-pixel difference
- Multiplication - Normalized product
- Average - 50/50 blend

### **Task 5: Noise Addition & Filtering** 🔧
Add realistic salt-and-pepper noise and test 3 denoising filters.

**Noise Model:**
- Salt noise (1.5%): Random white (255) pixels
- Pepper noise (1.5%): Random black (0) pixels

**Filter 1: Median Filter (5×5)**
- Replaces each pixel with median of neighborhood
- Excellent for salt & pepper noise
- Preserves edges effectively

**Filter 2: Bilateral Filter (9×9)**
- Edge-preserving smoothing
- Combines spatial and intensity similarity
- Maintains boundaries while smoothing

**Filter 3: Morphological Opening (5×5 Ellipse)**
- Structure-based denoising
- Erosion followed by dilation
- Removes small noise structures

**Performance Metrics:**
- PSNR (Peak Signal-to-Noise Ratio): Higher is better
- MSE (Mean Squared Error): Lower is better

---

## 📁 Project Structure

```
dipix-se504/
├── README.md                              # This file
├── run_all_tasks.py                   # Combined main script
│
├── Task Scripts (Modular Implementation):
├── 01_grayscale.py                        # Grayscale conversion
├── 02_frequency.py                        # Frequency domain
├── 03_phase_magnitude.py                  # Phase/magnitude swap
├── 04_logical_arithmetic.py               # Logical/arithmetic ops
├── 05_noise_filtering.py                  # Noise filtering
│
├── images/                                # Input folder
│   ├── image.jpeg
│   └── image2.jpg
│
├── results/                               # Output folder
│   ├── Task_01_Grayscale.png
│   ├── Task_02_Frequency_Domain.png
│   ├── Task_03_Phase_Magnitude_Interchange.png
│   ├── Task_04_Logical_Arithmetic.png
│   ├── Task_05_Noise_Filtering.png
│   └── [individual processed images...]
│
└── requirements.txt                       # Python dependencies
```

---

## 💻 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Programming language |
| **OpenCV (cv2)** | Image processing operations |
| **NumPy** | Numerical computations & FFT |
| **Matplotlib** | Visualization & result generation |
| **SciPy** | Advanced image filtering (morphological operations) |

---

## 📊 Expected Output

All scripts generate high-quality visualization images in the `results/` folder:

### **Task 1: Grayscale Conversion**
- Side-by-side comparison of original color and grayscale images
- Shows successful color-to-gray transformation

### **Task 2: Frequency Domain**
- Original image in spatial domain
- Magnitude spectrum (log-scaled for visualization)
- Phase spectrum (HSV colormap)
- Reconstructed image from frequency components

### **Task 3: Phase & Magnitude Interchange**
- Original Image 1 and Image 2
- Magnitude spectrum of both
- Phase spectrum of both
- Result: Mag(Img1) + Phase(Img2)
- Result: Mag(Img2) + Phase(Img1)

### **Task 4: Logical & Arithmetic Operations**
- 9 different operations displayed:
  - Bitwise AND, OR, XOR
  - NOT operations for both images
  - Addition, Subtraction, Average

### **Task 5: Noise & Filtering**
- Original images
- Noisy versions (salt & pepper)
- Results from each filter:
  - Median Filter
  - Bilateral Filter
  - Morphological Opening
- Performance comparison chart (PSNR metrics)

---

## 🔍 Key Algorithms & Concepts

### **Fast Fourier Transform (FFT)**
```python
fft = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft)
magnitude = np.abs(fft_shifted)
phase = np.angle(fft_shifted)
```

### **Phase/Magnitude Swapping**
```python
new_fft = magnitude1 * np.exp(1j * phase2)
result = np.fft.ifft2(np.fft.ifftshift(new_fft))
```

### **Median Filtering**
```python
filtered = cv2.medianBlur(noisy_image, 5)
```

### **Bilateral Filtering**
```python
filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
```

### **Morphological Operations**
```python
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
filtered = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
```

---

## 📈 Results & Analysis

### **Grayscale Conversion**
- ✅ Both images successfully converted
- ✅ Detail preservation verified
- ✅ Contrast ranges: 0-255 levels

### **Frequency Domain Analysis**
- ✅ FFT reveals low-frequency (background) components
- ✅ High-frequency (detail) components identified
- ✅ Log scaling helps visualize dynamic range

### **Phase vs. Magnitude**
- ✅ Phase spectrum carries structural information
- ✅ Magnitude alone produces low-contrast results
- ✅ Phase is critical for image recognition

### **Logical Operations**
- ✅ AND produces intersection of bright regions
- ✅ OR produces union of bright regions
- ✅ XOR highlights differences between images

### **Filter Performance**
- ✅ Median filter: Best for salt & pepper noise (PSNR ~25-30 dB)
- ✅ Bilateral filter: Good edge preservation (PSNR ~22-28 dB)
- ✅ Morphological: Structural approach (PSNR varies by content)

---

## 🎯 Learning Outcomes

After completing this project, you'll understand:

1. **Color Space Transformations** - RGB to grayscale conversion
2. **Frequency Domain Analysis** - FFT theory and implementation
3. **Signal Processing** - Filtering, convolution, morphological operations
4. **Noise Models** - Salt & pepper noise characteristics
5. **Filter Design** - Median, bilateral, morphological approaches
6. **Image Enhancement** - Restoration from noise-degraded images
7. **Visualization** - Professional image representation techniques
8. **Python Libraries** - OpenCV, NumPy, Matplotlib workflows

---

## 📝 Code Quality

- ✅ Modular design with separate task files
- ✅ Comprehensive documentation and comments
- ✅ Error handling for missing images
- ✅ Professional visualization outputs
- ✅ PEP 8 style compliance
- ✅ Reusable utility functions

---

## 👤 Author Information

**Name:** Gulrez Qayyum  
**Class/Section:** BSSE-6TH-M1  
**Course Code:** SE-504  
**Email:** [gulrezqayyum@gmail.com]  
**GitHub:** https://github.com/GulrezQayyum

---

## 📄 License

This project is created for educational purposes as part of SE-504 Digital Image Processing course at University of Agriculture, Faisalabad.

---

## 🙏 Acknowledgments

- Dr. Ahsan Latif for course guidance
- University of Agriculture, Faisalabad
- OpenCV and NumPy communities for excellent libraries

---
