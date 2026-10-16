
from pathlib import Path
import pandas as pd
import json

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the sample CSV file
file_path = project_folder / "data" / "sample_data.csv"

# Read the CSV file
data = pd.read_csv(file_path)

# Count missing values before cleaning
missing_before = data.isnull().sum()

# Count invalid age values BEFORE converting age
invalid_age_count = (
    data["age"].notna()
    & pd.to_numeric(data["age"], errors="coerce").isna()
).sum()

print("Invalid age values:", invalid_age_count)

# Display the original data
print("Original Data:")
print(data)

# Check missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(data.isnull().sum())

# Convert age values to numbers
data["age"] = pd.to_numeric(data["age"], errors="coerce")

# Check missing values after age conversion
print("\nMissing Values After Age Conversion:")
print(data.isnull().sum())

# Find the median age
median_age = data["age"].median()

print("\nMedian Age:")
print(median_age)

# Fill missing and invalid ages with the median
data["age"] = data["age"].fillna(median_age)

# Check missing ages after cleaning
print("\nMissing Ages After Cleaning:")
print(data["age"].isnull().sum())

# Find the median marks
median_marks = data["marks"].median()

print("\nMedian Marks:")
print(median_marks)

# Fill missing marks with the median
data["marks"] = data["marks"].fillna(median_marks)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

# Create the output file path
output_path = project_folder / "data" / "cleaned_data.csv"

# Save the cleaned data
data.to_csv(output_path, index=False)

print("\nCleaned data saved to:")
print(output_path)

# Check for potential duplicate student records
duplicate_records = data.duplicated(
    subset=["name", "age", "course", "marks"]
)

print("\nPotential Duplicate Records:")
print(data[duplicate_records])

# Create the cleaning log

cleaning_log = {
    "missing_ages_filled": int(
        missing_before["age"] + invalid_age_count
    ),
    "missing_marks_filled": int(missing_before["marks"]),
    "potential_duplicates_detected": int(duplicate_records.sum()),
    "total_rows_after_cleaning": int(len(data))
}


# Create the reports folder
reports_folder = project_folder / "reports"
reports_folder.mkdir(exist_ok=True)

# Save the cleaning log
log_path = reports_folder / "cleaning_log.json"

with open(log_path, "w", encoding="utf-8") as file:
    json.dump(cleaning_log, file, indent=4)

print("\nCleaning log saved to:")
print(log_path)
