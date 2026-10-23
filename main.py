
import subprocess
import sys

print("===== AUTOMATED DATA CLEANING SYSTEM =====")
print("=" * 45)
print("\n" + "=" * 45)

print("\nStep 1: Dataset Profiling")

try:
    subprocess.run(
        [sys.executable, "-m", "src.profiling"],
        check=True
    )
except subprocess.CalledProcessError as error:
    print("Error: Dataset profiling failed.")
    print("Exit code:", error.returncode)
    sys.exit(1)

print("\n" + "=" * 45)
print("\nStep 2: Data Cleaning")

try:
    subprocess.run(
        [sys.executable, "-m", "src.cleaning"],
        check=True
    )
except subprocess.CalledProcessError as error:
    print("Error: Data cleaning failed.")
    print("Exit code:", error.returncode)
    sys.exit(1)

print("\n" + "=" * 45)
print("\nStep 3: Data Validation")

try:
    subprocess.run(
        [sys.executable, "-m", "src.validation"],
        check=True
    )
except subprocess.CalledProcessError as error:
    print("Error: Data validation failed.")
    print("Exit code:", error.returncode)
    sys.exit(1)

print("\n===== ALL STEPS COMPLETED SUCCESSFULLY =====")
print("\n" + "=" * 45)
print("\n===== PROJECT SUMMARY =====")
print("1. Dataset profiling completed.")
print("2. Data cleaning completed.")
print("3. Data validation completed.")
print("4. Reports saved in the reports folder.")
