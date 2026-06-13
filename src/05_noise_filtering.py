"""
Task 5: Noise Addition and Noise Removal Filters
SE-504: Digital Image Processing Project
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import ndimage
from scipy.ndimage import median_filter
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

def add_salt_pepper_noise(img, salt_prob=0.01, pepper_prob=0.01):
    """Add salt and pepper noise to image"""
    noisy = img.copy().astype(np.float32)
    
    # Salt (white) noise
    salt_mask = np.random.rand(*img.shape) < salt_prob
    noisy[salt_mask] = 255
    
    # Pepper (black) noise
    pepper_mask = np.random.rand(*img.shape) < pepper_prob
    noisy[pepper_mask] = 0
    
    return noisy.astype(np.uint8)

def apply_median_filter(img, kernel_size=5):
    """Apply median filter (best for salt & pepper)"""
    return median_filter(img, size=kernel_size).astype(np.uint8)

def apply_bilateral_filter(img, d=9, sigma_color=75, sigma_space=75):
    """Apply bilateral filter (preserves edges)"""
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)

def apply_morphological_filter(img, kernel_size=5):
    """Apply morphological opening (removes small noise)"""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def calculate_mse(img1, img2):
    """Calculate Mean Squared Error"""
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)

def calculate_psnr(img1, img2):
    """Calculate Peak Signal-to-Noise Ratio"""
    mse = calculate_mse(img1, img2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def display_noise_filtering_results(img_name, original, noisy, 
                                    filtered_median, filtered_bilateral, 
                                    filtered_morpho):
    """Display noise filtering results"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Row 1
    axes[0, 0].imshow(original, cmap='gray')
    axes[0, 0].set_title(f"{img_name} - Original")
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(noisy, cmap='gray')
    axes[0, 1].set_title("Noisy Image\n(Salt & Pepper)")
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(filtered_median, cmap='gray')
    mse_m = calculate_mse(original, filtered_median)
    psnr_m = calculate_psnr(original, filtered_median)
    axes[0, 2].set_title(f"Median Filter\nMSE: {mse_m:.2f}, PSNR: {psnr_m:.2f}")
    axes[0, 2].axis('off')
    
    # Row 2
    axes[1, 0].imshow(filtered_bilateral, cmap='gray')
    mse_b = calculate_mse(original, filtered_bilateral)
    psnr_b = calculate_psnr(original, filtered_bilateral)
    axes[1, 0].set_title(f"Bilateral Filter\nMSE: {mse_b:.2f}, PSNR: {psnr_b:.2f}")
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(filtered_morpho, cmap='gray')
    mse_mo = calculate_mse(original, filtered_morpho)
    psnr_mo = calculate_psnr(original, filtered_morpho)
    axes[1, 1].set_title(f"Morphological Filter\nMSE: {mse_mo:.2f}, PSNR: {psnr_mo:.2f}")
    axes[1, 1].axis('off')
    
    # Comparison text
    axes[1, 2].axis('off')
    comparison_text = f"""
    Filter Comparison:
    
    Noisy Image MSE: {calculate_mse(original, noisy):.2f}
    
    Median: Best for salt & pepper
    Bilateral: Preserves edges well
    Morphological: Good for binary noise
    
    PSNR (Higher is Better):
    Median: {psnr_m:.2f} dB
    Bilateral: {psnr_b:.2f} dB
    Morpho: {psnr_mo:.2f} dB
    """
    axes[1, 2].text(0.5, 0.5, comparison_text, ha='center', va='center', fontsize=9,
                   family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    # Only save for the first image (Task 5 will show both images in one PNG)
    plt.savefig('results/Task_05_Noise_Filtering.png', dpi=150, bbox_inches='tight')
    print("Saved: results/Task_05_Noise_Filtering.png")
    plt.show()

def main():
    print("=" * 60)
    print("Task 5: Noise Addition and Noise Removal")
    print("=" * 60)
    
    os.makedirs('results', exist_ok=True)
    
    # Load grayscale images
    images = load_grayscale_images('images')
    if not images:
        print("No images found!")
        return
    
    print(f"Loaded {len(images)} image(s)")
    
    # Process each image and collect results
    all_results = []
    
    for img_dict in images:
        img_name = img_dict['name']
        original = img_dict['grayscale']
        
        print(f"\nProcessing {img_name}...")
        
        # Add salt and pepper noise
        print("  Adding salt & pepper noise...")
        noisy = add_salt_pepper_noise(original, salt_prob=0.025, pepper_prob=0.025)
        
        # Apply filters
        print("  Applying filters...")
        filtered_median = apply_median_filter(noisy, kernel_size=5)
        filtered_bilateral = apply_bilateral_filter(noisy, d=9, sigma_color=75, sigma_space=75)
        filtered_morpho = apply_morphological_filter(noisy, kernel_size=5)
        
        # Store results
        all_results.append({
            'name': img_name,
            'original': original,
            'noisy': noisy,
            'median': filtered_median,
            'bilateral': filtered_bilateral,
            'morpho': filtered_morpho
        })
        
        # Print quality metrics
        print(f"\n  Quality Metrics for {img_name}:")
        print(f"    Noisy Image PSNR: {calculate_psnr(original, noisy):.2f} dB")
        print(f"    Median Filter PSNR: {calculate_psnr(original, filtered_median):.2f} dB")
        print(f"    Bilateral Filter PSNR: {calculate_psnr(original, filtered_bilateral):.2f} dB")
        print(f"    Morphological Filter PSNR: {calculate_psnr(original, filtered_morpho):.2f} dB")
    
    # Create combined visualization with all results
    fig = plt.figure(figsize=(20, 5 * len(all_results)))
    gs = fig.add_gridspec(len(all_results), 6, hspace=0.35, wspace=0.35)
    
    for idx, result in enumerate(all_results):
        # Original
        ax = fig.add_subplot(gs[idx, 0])
        ax.imshow(result['original'], cmap='gray')
        ax.set_title(f"{result['name']}\nOriginal", fontweight='bold')
        ax.axis('off')
        
        # Noisy
        ax = fig.add_subplot(gs[idx, 1])
        ax.imshow(result['noisy'], cmap='gray')
        noisy_psnr = calculate_psnr(result['original'], result['noisy'])
        ax.set_title(f"Noisy\nPSNR: {noisy_psnr:.2f}dB")
        ax.axis('off')
        
        # Median
        ax = fig.add_subplot(gs[idx, 2])
        ax.imshow(result['median'], cmap='gray')
        median_psnr = calculate_psnr(result['original'], result['median'])
        ax.set_title(f"Median Filter\nPSNR: {median_psnr:.2f}dB")
        ax.axis('off')
        
        # Bilateral
        ax = fig.add_subplot(gs[idx, 3])
        ax.imshow(result['bilateral'], cmap='gray')
        bilateral_psnr = calculate_psnr(result['original'], result['bilateral'])
        ax.set_title(f"Bilateral Filter\nPSNR: {bilateral_psnr:.2f}dB")
        ax.axis('off')
        
        # Morphological
        ax = fig.add_subplot(gs[idx, 4])
        ax.imshow(result['morpho'], cmap='gray')
        morpho_psnr = calculate_psnr(result['original'], result['morpho'])
        ax.set_title(f"Morphological\nPSNR: {morpho_psnr:.2f}dB")
        ax.axis('off')
        
        # Info
        ax = fig.add_subplot(gs[idx, 5])
        ax.axis('off')
        info_text = f"Image: {result['name']}\n\nNoise: S&P 5%\n\nBest: Median\n({median_psnr:.1f}dB)\n\nComparison"
        ax.text(0.5, 0.5, info_text, ha='center', va='center', fontsize=11, 
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9),
               family='monospace', fontweight='bold')
    
    plt.suptitle('Task 5: Noise Addition & Filtering', fontsize=16, fontweight='bold', y=0.995)
    plt.savefig('results/Task_05_Noise_Filtering.png', dpi=150, bbox_inches='tight')
    print("\nSaved: results/Task_05_Noise_Filtering.png")
    
    print("\n✓ Task 5 completed successfully!")
    print("  - Salt & pepper noise added")
    print("  - Median, Bilateral, and Morphological filters applied")
    print("  - PSNR quality metrics calculated")

if __name__ == "__main__":
    main()
