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

def perform_operations(img1, img2):
    h1, w1 = img1.shape
    h2, w2 = img2.shape
    if (h1, w1) != (h2, w2):
        min_h, min_w = min(h1, h2), min(w1, w2)
        img1, img2 = img1[:min_h, :min_w], img2[:min_h, :min_w]
    results = {}
    results['AND'] = cv2.bitwise_and(img1, img2)
    results['OR'] = cv2.bitwise_or(img1, img2)
    results['XOR'] = cv2.bitwise_xor(img1, img2)
    results['NOT1'] = cv2.bitwise_not(img1)
    results['NOT2'] = cv2.bitwise_not(img2)
    results['Addition'] = cv2.add(img1, img2)
    results['Subtraction'] = cv2.absdiff(img1, img2)
    results['Multiplication'] = cv2.multiply(img1.astype(np.float32) / 255, 
                                            img2.astype(np.float32) / 255)
    results['Multiplication'] = (results['Multiplication'] * 255).astype(np.uint8)
    results['Average'] = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    
    return results

def display_operations(img1_name, img1, img2_name, img2, results):
    fig, axes = plt.subplots(4, 3, figsize=(15, 16))
    axes[0, 0].imshow(img1, cmap='gray')
    axes[0, 0].set_title(f"{img1_name} - Original")
    axes[0, 0].axis('off')
    axes[0, 1].imshow(img2, cmap='gray')
    axes[0, 1].set_title(f"{img2_name} - Original")
    axes[0, 1].axis('off')
    axes[0, 2].axis('off')
    axes[1, 0].imshow(results['AND'], cmap='gray')
    axes[1, 0].set_title("AND")
    axes[1, 0].axis('off')
    axes[1, 1].imshow(results['OR'], cmap='gray')
    axes[1, 1].set_title("OR")
    axes[1, 1].axis('off')
    axes[1, 2].imshow(results['XOR'], cmap='gray')
    axes[1, 2].set_title("XOR")
    axes[1, 2].axis('off')
    axes[2, 0].imshow(results['NOT1'], cmap='gray')
    axes[2, 0].set_title(f"NOT {img1_name}")
    axes[2, 0].axis('off')
    axes[2, 1].imshow(results['NOT2'], cmap='gray')
    axes[2, 1].set_title(f"NOT {img2_name}")
    axes[2, 1].axis('off')
    axes[2, 2].axis('off')
    axes[3, 0].imshow(results['Addition'], cmap='gray')
    axes[3, 0].set_title("Addition")
    axes[3, 0].axis('off')
    axes[3, 1].imshow(results['Subtraction'], cmap='gray')
    axes[3, 1].set_title("Subtraction")
    axes[3, 1].axis('off')
    axes[3, 2].imshow(results['Average'], cmap='gray')
    axes[3, 2].set_title("Average")
    axes[3, 2].axis('off')
    
    plt.tight_layout()
    plt.savefig('results/Task_04_Logical_Arithmetic.png', dpi=150, bbox_inches='tight')

def main():
    os.makedirs('results', exist_ok=True)
    images = load_grayscale_images('images')
    if len(images) < 2:
        return
    img1 = images[0]['grayscale']
    img2 = images[1]['grayscale']
    results = perform_operations(img1, img2)
    display_operations(images[0]['name'], img1, images[1]['name'], img2, results)

if __name__ == "__main__":
    main()
