# SE-504 Quick Reference Guide

## One-Minute Setup

```bash
# Navigate to project
cd /home/gulrez/2023-ag-9948*SE-504

# Add your 2 color images to images/ folder
# (Then run:)
python3 run_all_tasks.py
```

## Task Overview

| Task | Script | Purpose | Key Functions |
|------|--------|---------|----------------|
| 1 | `01_grayscale.py` | Color → Grayscale | `convert_to_grayscale()`, `display_results()` |
| 2 | `02_frequency.py` | FFT Analysis | `compute_fft()`, Magnitude/Phase extraction |
| 3 | `03_phase_magnitude.py` | Interchange Mag/Phase | `interchange_magnitude_phase()` |
| 4 | `04_logical_arithmetic.py` | AND/OR/XOR/ADD/SUB | Bitwise + Arithmetic operations |
| 5 | `05_noise_filtering.py` | Denoise | Median, Bilateral, Morphological filters |

## Running Tasks

### All Tasks at Once
```bash
python3 run_all_tasks.py
```

### Individual Tasks
```bash
python3 src/01_grayscale.py
python3 src/02_frequency.py
python3 src/03_phase_magnitude.py
python3 src/04_logical_arithmetic.py
python3 src/05_noise_filtering.py
```

## File Organization

**Input**: `images/` → Add your 2 color images here
**Output**: `results/` → All output images saved here

## Key Output Files

- Task 1: `01_grayscale_comparison.png`
- Task 2: `02_frequency_domain.png`
- Task 3: `03_phase_magnitude_interchange.png`
- Task 4: `04_logical_arithmetic_operations.png`
- Task 5: `05_noise_filtering.png`

## Environment

- **Python**: 3.12.3
- **Virtual Env**: `.venv/` (pre-configured)
- **Libraries**: OpenCV 4.13, NumPy 2.4.6, Matplotlib 3.11, SciPy 1.17.1

## Deadline

**June 15, 2026 / 4:00 pm** → mahsanlatif@uaf.edu.pk

## Common Issues

| Issue | Solution |
|-------|----------|
| "No images found" | Add images to `images/` folder |
| Import errors | Run: `pip install -r requirements.txt` |
| No display | Images auto-saved to `results/` |

---

For detailed information, see `SETUP.md` or `ENVIRONMENT_REPORT.md`
