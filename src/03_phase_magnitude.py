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

def compute_fft_components(gray_img):
    f_transform = np.fft.fft2(gray_img)
    f_shift = np.fft.fftshift(f_transform)
    
    magnitude = np.abs(f_shift)
    phase = np.angle(f_shift)
    
    return magnitude, phase, f_shift

def interchange_magnitude_phase(img1, img2):
    mag1, phase1, fft1 = compute_fft_components(img1)
    mag2, phase2, fft2 = compute_fft_components(img2)
    combined1 = mag1 * np.exp(1j * phase2)
    combined2 = mag2 * np.exp(1j * phase1)
    f_ishift1 = np.fft.ifftshift(combined1)
    f_ishift2 = np.fft.ifftshift(combined2)
    
    result1 = np.fft.ifft2(f_ishift1)
    result2 = np.fft.ifft2(f_ishift2)
    
    result1 = np.clip(np.abs(result1), 0, 255).astype(np.uint8)
    result2 = np.clip(np.abs(result2), 0, 255).astype(np.uint8)
    
    return result1, result2, (mag1, mag2, phase1, phase2)

def display_interchange_results(img1_name, img1_orig, img1_result, 
                                img2_name, img2_orig, img2_result,
                                magnitudes, phases):
    mag1, mag2 = magnitudes
    phase1, phase2 = phases
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    ax = fig.add_subplot(gs[0, 0])
    ax.imshow(img1_orig, cmap='gray')
    ax.set_title(f"{img1_name} - Original")
    ax.axis('off')
    ax = fig.add_subplot(gs[0, 1])
    ax.imshow(np.log1p(mag1), cmap='hot')
    ax.set_title(f"{img1_name} - Magnitude")
    ax.axis('off')
    ax = fig.add_subplot(gs[0, 2])
    ax.imshow(phase1, cmap='hsv')
    ax.set_title(f"{img1_name} - Phase")
    ax.axis('off')
    ax = fig.add_subplot(gs[0, 3])
    ax.imshow(img1_result, cmap='gray')
    ax.set_title(f"{img1_name} + {img2_name} Phase")
    ax.axis('off')
    ax = fig.add_subplot(gs[1, 0])
    ax.imshow(img2_orig, cmap='gray')
    ax.set_title(f"{img2_name} - Original")
    ax.axis('off')
    ax = fig.add_subplot(gs[1, 1])
    ax.imshow(np.log1p(mag2), cmap='hot')
    ax.set_title(f"{img2_name} - Magnitude")
    ax.axis('off')
    ax = fig.add_subplot(gs[1, 2])
    ax.imshow(phase2, cmap='hsv')
    ax.set_title(f"{img2_name} - Phase")
    ax.axis('off')
    ax = fig.add_subplot(gs[1, 3])
    ax.imshow(img2_result, cmap='gray')
    ax.set_title(f"{img2_name} + {img1_name} Phase")
    ax.axis('off')
    ax = fig.add_subplot(gs[2, :])
    ax.axis('off')
    ax.text(0.5, 0.5, f"Phase & Magnitude Interchange\n{img1_name} + {img2_name} components swapped",
            ha='center', va='center', fontsize=10, family='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.savefig('results/Task_03_Phase_Magnitude_Interchange.png', dpi=150, bbox_inches='tight')

def main():
    os.makedirs('results', exist_ok=True)
    images = load_grayscale_images('images')
    if len(images) < 2:
        return
    img1 = images[0]['grayscale']
    img2 = images[1]['grayscale']
    h1, w1, h2, w2 = img1.shape[0], img1.shape[1], img2.shape[0], img2.shape[1]
    if (h1, w1) != (h2, w2):
        min_h, min_w = min(h1, h2), min(w1, w2)
        img1, img2 = img1[:min_h, :min_w], img2[:min_h, :min_w]
    result1, result2, fft_components = interchange_magnitude_phase(img1, img2)
    display_interchange_results(
        images[0]['name'], img1, result1,
        images[1]['name'], img2, result2,
        fft_components[:2], fft_components[2:]
    )

if __name__ == "__main__":
    main()
