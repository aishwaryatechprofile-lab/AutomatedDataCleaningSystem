
import subprocess
import sys

print("===== AUTOMATED DATA CLEANING SYSTEM =====")
print("=" * 45)
print("\n" + "=" * 45)
print("\nStep 1: Dataset Profiling")

subprocess.run(
    [sys.executable, "-m", "src.profiling"],
    check=True
)
print("\n" + "=" * 45)
print("\nStep 2: Data Cleaning")
subprocess.run(
    [sys.executable, "-m", "src.cleaning"],
    check=True
)
print("\n" + "=" * 45)
print("\nStep 3: Data Validation")
subprocess.run(
    [sys.executable, "-m", "src.validation"],
    check=True
)

print("\n===== ALL STEPS COMPLETED SUCCESSFULLY =====")
print("\n" + "=" * 45)
print("\n===== PROJECT SUMMARY =====")
print("1. Dataset profiling completed.")
print("2. Data cleaning completed.")
print("3. Data validation completed.")
print("4. Reports saved in the reports folder.")