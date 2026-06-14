import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.ndimage import median_filter
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

def add_salt_pepper_noise(img, salt_prob=0.01, pepper_prob=0.01):
    noisy = img.copy().astype(np.float32)
    salt_mask = np.random.rand(*img.shape) < salt_prob
    noisy[salt_mask] = 255
    pepper_mask = np.random.rand(*img.shape) < pepper_prob
    noisy[pepper_mask] = 0
    
    return noisy.astype(np.uint8)

def apply_median_filter(img, kernel_size=5):
    return median_filter(img, size=kernel_size).astype(np.uint8)

def apply_bilateral_filter(img, d=9, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)

def apply_morphological_filter(img, kernel_size=5):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def calculate_mse(img1, img2):
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)

def calculate_psnr(img1, img2):
    mse = calculate_mse(img1, img2)
    if mse == 0: return float('inf')
    return 20 * np.log10(255.0 / np.sqrt(mse))

def display_noise_filtering_results(img_name, original, noisy, 
                                    filtered_median, filtered_bilateral, 
                                    filtered_morpho):
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes[0, 0].imshow(original, cmap='gray')
    axes[0, 0].set_title(f"{img_name} - Original")
    axes[0, 0].axis('off')
    axes[0, 1].imshow(noisy, cmap='gray')
    axes[0, 1].set_title("Noisy (S&P)")
    axes[0, 1].axis('off')
    axes[0, 2].imshow(filtered_median, cmap='gray')
    psnr_m = calculate_psnr(original, filtered_median)
    axes[0, 2].set_title(f"Median\nPSNR: {psnr_m:.2f}")
    axes[0, 2].axis('off')
    axes[1, 0].imshow(filtered_bilateral, cmap='gray')
    psnr_b = calculate_psnr(original, filtered_bilateral)
    axes[1, 0].set_title(f"Bilateral\nPSNR: {psnr_b:.2f}")
    axes[1, 0].axis('off')
    axes[1, 1].imshow(filtered_morpho, cmap='gray')
    psnr_mo = calculate_psnr(original, filtered_morpho)
    axes[1, 1].set_title(f"Morpho\nPSNR: {psnr_mo:.2f}")
    axes[1, 1].axis('off')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    plt.savefig('results/Task_05_Noise_Filtering.png', dpi=150, bbox_inches='tight')
    plt.show()

def main():
    os.makedirs('results', exist_ok=True)
    images = load_grayscale_images('images')
    if not images:
        return
    all_results = []
    for img_dict in images:
        original = img_dict['grayscale']
        noisy = add_salt_pepper_noise(original, salt_prob=0.025, pepper_prob=0.025)
        all_results.append({
            'name': img_dict['name'],
            'original': original,
            'noisy': noisy,
            'median': apply_median_filter(noisy, kernel_size=5),
            'bilateral': apply_bilateral_filter(noisy, d=9, sigma_color=75, sigma_space=75),
            'morpho': apply_morphological_filter(noisy, kernel_size=5)
        })
    fig = plt.figure(figsize=(20, 5 * len(all_results)))
    gs = fig.add_gridspec(len(all_results), 6, hspace=0.35, wspace=0.35)
    for idx, result in enumerate(all_results):
        ax = fig.add_subplot(gs[idx, 0])
        ax.imshow(result['original'], cmap='gray')
        ax.set_title(f"{result['name']} Original")
        ax.axis('off')
        ax = fig.add_subplot(gs[idx, 1])
        ax.imshow(result['noisy'], cmap='gray')
        noisy_psnr = calculate_psnr(result['original'], result['noisy'])
        ax.set_title(f"Noisy {noisy_psnr:.2f}dB")
        ax.axis('off')
        ax = fig.add_subplot(gs[idx, 2])
        ax.imshow(result['median'], cmap='gray')
        median_psnr = calculate_psnr(result['original'], result['median'])
        ax.set_title(f"Median {median_psnr:.2f}dB")
        ax.axis('off')
        ax = fig.add_subplot(gs[idx, 3])
        ax.imshow(result['bilateral'], cmap='gray')
        bilateral_psnr = calculate_psnr(result['original'], result['bilateral'])
        ax.set_title(f"Bilateral {bilateral_psnr:.2f}dB")
        ax.axis('off')
        ax = fig.add_subplot(gs[idx, 4])
        ax.imshow(result['morpho'], cmap='gray')
        morpho_psnr = calculate_psnr(result['original'], result['morpho'])
        ax.set_title(f"Morpho {morpho_psnr:.2f}dB")
        ax.axis('off')
        ax = fig.add_subplot(gs[idx, 5])
        ax.axis('off')
    plt.savefig('results/Task_05_Noise_Filtering.png', dpi=150, bbox_inches='tight')

if __name__ == "__main__":
    main()
