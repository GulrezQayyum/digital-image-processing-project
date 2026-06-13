"""
Task 2: Frequency Domain Transformation using FFT
SE-504: Digital Image Processing Project
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

def load_grayscale_images(image_dir='images'):
    """Load color images and convert to grayscale"""
    image_dir = Path(image_dir)
    images = []
    
    for ext in ['*.jpg', '*.png', '*.bmp', '*.jpeg']:
        images.extend(list(image_dir.glob(ext)))
    
    grayscale_images = []
    for path in sorted(images)[:2]:  # Get first 2 images
        color_img = cv2.imread(str(path))
        if color_img is not None:
            gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
            grayscale_images.append({
                'name': path.stem,
                'grayscale': gray_img
            })
    
    return grayscale_images

def compute_fft(gray_img):
    """Compute FFT and return spectrum and phase"""
    # Apply FFT
    f_transform = np.fft.fft2(gray_img)
    
    # Shift zero-frequency component to center
    f_shift = np.fft.fftshift(f_transform)
    
    # Compute magnitude and phase
    magnitude = np.abs(f_shift)
    phase = np.angle(f_shift)
    
    # Log scale for better visualization
    magnitude_log = np.log1p(magnitude)
    
    return {
        'fft': f_shift,
        'magnitude': magnitude,
        'magnitude_log': magnitude_log,
        'phase': phase
    }

def display_frequency_domain(images):
    """Display images in frequency domain"""
    fig, axes = plt.subplots(len(images), 4, figsize=(16, 4*len(images)))
    
    if len(images) == 1:
        axes = axes.reshape(1, -1)
    
    for idx, img_dict in enumerate(images):
        gray = img_dict['grayscale']
        fft_data = img_dict['fft_data']
        
        # Original image
        axes[idx, 0].imshow(gray, cmap='gray')
        axes[idx, 0].set_title(f"{img_dict['name']} - Original")
        axes[idx, 0].axis('off')
        
        # Magnitude spectrum
        axes[idx, 1].imshow(fft_data['magnitude_log'], cmap='hot')
        axes[idx, 1].set_title(f"{img_dict['name']} - Magnitude Spectrum")
        axes[idx, 1].axis('off')
        
        # Phase spectrum
        axes[idx, 2].imshow(fft_data['phase'], cmap='hsv')
        axes[idx, 2].set_title(f"{img_dict['name']} - Phase Spectrum")
        axes[idx, 2].axis('off')
        
        # Reconstruction
        f_ishift = np.fft.ifftshift(fft_data['fft'])
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        axes[idx, 3].imshow(img_back, cmap='gray')
        axes[idx, 3].set_title(f"{img_dict['name']} - Reconstructed")
        axes[idx, 3].axis('off')
    
    plt.tight_layout()
    plt.savefig('results/Task_02_Frequency_Domain.png', dpi=150, bbox_inches='tight')
    print("Saved: results/Task_02_Frequency_Domain.png")
    plt.show()

def main():
    print("=" * 60)
    print("Task 2: Frequency Domain Transformation (FFT)")
    print("=" * 60)
    
    os.makedirs('results', exist_ok=True)
    
    # Load grayscale images
    images = load_grayscale_images('images')
    if not images:
        print("No images found! Please add images to the 'images' folder")
        return
    
    print(f"Loaded {len(images)} image(s)")
    
    # Compute FFT for each image
    for img_dict in images:
        print(f"Computing FFT for {img_dict['name']}...")
        img_dict['fft_data'] = compute_fft(img_dict['grayscale'])
    
    # Display results
    display_frequency_domain(images)
    
    print("\n✓ Task 2 completed successfully!")
    print("  - Magnitude spectra computed")
    print("  - Phase information extracted")
    print("  - Images reconstructed from FFT")

if __name__ == "__main__":
    main()
