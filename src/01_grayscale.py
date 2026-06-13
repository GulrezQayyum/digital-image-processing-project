"""
Task 1: Convert Color Images to Grayscale
SE-504: Digital Image Processing Project
"""

import cv2
import os
import matplotlib.pyplot as plt
from pathlib import Path

def load_images(image_dir='images'):
    """Load color images from the images directory"""
    image_dir = Path(image_dir)
    if not image_dir.exists():
        print(f"Error: {image_dir} directory not found!")
        return []
    
    images = []
    for ext in ['*.jpg', '*.png', '*.bmp', '*.jpeg']:
        images.extend(list(image_dir.glob(ext)))
    
    return sorted(images)[:2]  # Get first 2 images

def convert_to_grayscale(image_paths):
    """Convert color images to grayscale"""
    grayscale_images = []
    
    for path in image_paths:
        print(f"Processing: {path.name}")
        
        # Read color image
        color_img = cv2.imread(str(path))
        if color_img is None:
            print(f"Error reading {path}")
            continue
        
        # Convert BGR to Grayscale
        gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
        grayscale_images.append({
            'name': path.stem,
            'original': color_img,
            'grayscale': gray_img
        })
        print(f"Processing: {path.name}")
    
    return grayscale_images

def display_results(images):
    """Display color and grayscale versions side by side"""
    fig, axes = plt.subplots(len(images), 2, figsize=(12, 5*len(images)))
    
    if len(images) == 1:
        axes = axes.reshape(1, -1)
    
    for idx, img_dict in enumerate(images):
        # Convert BGR to RGB for display
        original_rgb = cv2.cvtColor(img_dict['original'], cv2.COLOR_BGR2RGB)
        
        axes[idx, 0].imshow(original_rgb)
        axes[idx, 0].set_title(f"{img_dict['name']} - Color")
        axes[idx, 0].axis('off')
        
        axes[idx, 1].imshow(img_dict['grayscale'], cmap='gray')
        axes[idx, 1].set_title(f"{img_dict['name']} - Grayscale")
        axes[idx, 1].axis('off')
    
    plt.tight_layout()
    plt.savefig('results/Task_01_Grayscale.png', dpi=150, bbox_inches='tight')
    print("Saved: results/Task_01_Grayscale.png")
    plt.show()

def main():
    print("=" * 60)
    print("Task 1: Color to Grayscale Conversion")
    print("=" * 60)
    
    # Create results directory if not exists
    os.makedirs('results', exist_ok=True)
    
    # Load images
    image_paths = load_images('images')
    if not image_paths:
        print("No images found in 'images' folder!")
        print("Please add 2 color images to the 'images' folder")
        return
    
    print(f"Found {len(image_paths)} image(s)")
    
    # Convert to grayscale
    grayscale_images = convert_to_grayscale(image_paths)
    
    if grayscale_images:
        # Display results
        display_results(grayscale_images)
        print("\n✓ Task 1 completed successfully!")
    else:
        print("No images were processed")

if __name__ == "__main__":
    main()
