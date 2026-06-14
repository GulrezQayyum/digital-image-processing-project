import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

def load_grayscale_images(image_dir='images'):
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
    f_transform = np.fft.fft2(gray_img)
    f_shift = np.fft.fftshift(f_transform)
    magnitude = np.abs(f_shift)
    phase = np.angle(f_shift)
    magnitude_log = np.log1p(magnitude)
    
    return {
        'fft': f_shift,
        'magnitude': magnitude,
        'magnitude_log': magnitude_log,
        'phase': phase
    }

def display_frequency_domain(images):
    fig, axes = plt.subplots(len(images), 4, figsize=(16, 4*len(images)))
    
    if len(images) == 1:
        axes = axes.reshape(1, -1)
    
    for idx, img_dict in enumerate(images):
        gray = img_dict['grayscale']
        fft_data = img_dict['fft_data']
        axes[idx, 0].imshow(gray, cmap='gray')
        axes[idx, 0].set_title(f"{img_dict['name']} - Original")
        axes[idx, 0].axis('off')
        axes[idx, 1].imshow(fft_data['magnitude_log'], cmap='hot')
        axes[idx, 1].set_title(f"{img_dict['name']} - Magnitude Spectrum")
        axes[idx, 1].axis('off')
        axes[idx, 2].imshow(fft_data['phase'], cmap='hsv')
        axes[idx, 2].set_title(f"{img_dict['name']} - Phase Spectrum")
        axes[idx, 2].axis('off')
        f_ishift = np.fft.ifftshift(fft_data['fft'])
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        axes[idx, 3].imshow(img_back, cmap='gray')
        axes[idx, 3].set_title(f"{img_dict['name']} - Reconstructed")
        axes[idx, 3].axis('off')
    
    plt.tight_layout()
    plt.savefig('results/Task_02_Frequency_Domain.png', dpi=150, bbox_inches='tight')

def main():
    os.makedirs('results', exist_ok=True)
    images = load_grayscale_images('images')
    if not images:
        return
    for img_dict in images:
        img_dict['fft_data'] = compute_fft(img_dict['grayscale'])
    display_frequency_domain(images)

if __name__ == "__main__":
    main()
