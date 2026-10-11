
import subprocess
import sys

print("===== AUTOMATED DATA CLEANING SYSTEM =====")

print("\nStep 1: Dataset Profiling")
subprocess.run(
    [sys.executable, "-m", "src.profiling"],
    check=True
)

print("\nStep 2: Data Cleaning")
subprocess.run(
    [sys.executable, "-m", "src.cleaning"],
    check=True
)

print("\nStep 3: Data Validation")
subprocess.run(
    [sys.executable, "-m", "src.validation"],
    check=True
)

print("\n===== ALL STEPS COMPLETED SUCCESSFULLY =====")
