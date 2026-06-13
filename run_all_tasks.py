"""
Master Script to Run All SE-504 Digital Image Processing Tasks
Executes all 5 tasks sequentially
"""

import subprocess
import sys
import os

def run_task(task_number):
    """Run a single task script"""
    script = f"src/{task_number:02d}_*.py"
    
    # Find the actual script file
    import glob
    scripts = glob.glob(script)
    if not scripts:
        print(f"Error: Could not find task {task_number} script!")
        return False
    
    script_path = scripts[0]
    script_name = os.path.basename(script_path)
    
    print(f"\n{'='*60}")
    print(f"Running Task {task_number}: {script_name}")
    print(f"{'='*60}\n")
    
    try:
        result = subprocess.run([sys.executable, script_path], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("SE-504 Digital Image Processing - Complete Project")
    print("="*60)
    print("\nThis script will run all 5 tasks sequentially:")
    print("  1. Grayscale Conversion")
    print("  2. Frequency Domain Transformation (FFT)")
    print("  3. Phase & Magnitude Interchange")
    print("  4. Logical & Arithmetic Operations")
    print("  5. Noise Addition & Filtering")
    print("\n" + "="*60 + "\n")
    
    # Check if images exist
    import pathlib
    image_dir = pathlib.Path('images')
    if not image_dir.exists():
        print("Warning: 'images' directory not found!")
        print("Please create 'images' folder and add your 2 color images there.")
        sys.exit(1)
    
    images = list(image_dir.glob('*.jpg')) + list(image_dir.glob('*.png')) + list(image_dir.glob('*.bmp'))
    if not images:
        print("Warning: No images found in 'images' folder!")
        print("Please add at least 2 color images to continue.")
        sys.exit(1)
    
    print(f"Found {len(images)} image(s) in 'images' folder")
    for img in images[:5]:  # Show first 5 images
        print(f"  - {img.name}")
    if len(images) > 5:
        print(f"  ... and {len(images) - 5} more")
    
    # Create results directory
    os.makedirs('results', exist_ok=True)
    print(f"\nResults will be saved to 'results' folder\n")
    
    # Run each task
    tasks_completed = 0
    for task_num in range(1, 6):
        try:
            if run_task(task_num):
                tasks_completed += 1
            else:
                print(f"Task {task_num} failed!")
        except Exception as e:
            print(f"Error running Task {task_num}: {e}")
    
    # Summary
    print("\n" + "="*60)
    print(f"Summary: {tasks_completed}/5 tasks completed successfully")
    print("="*60)
    
    if tasks_completed == 5:
        print("\n✓ All tasks completed successfully!")
        print(f"\nCheck the 'results' folder for output images and comparisons.")
    else:
        print(f"\n✗ {5 - tasks_completed} task(s) failed. Please check the output above.")
    
    print("\nProject submission should include:")
    print("  - Source code (src/ folder)")
    print("  - Result images (results/ folder)")
    print("  - Original images (images/ folder)")
    print("  - This README file")
    print(f"\nDeadline: June 15, 2026 / 4:00 pm")
    print(f"Submit to: mahsanlatif@uaf.edu.pk")

if __name__ == "__main__":
    main()
