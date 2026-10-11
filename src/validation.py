import json
from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the cleaned CSV file
file_path = project_folder / "data" / "cleaned_data.csv"

# Read the cleaned data
data = pd.read_csv(file_path)

# Display the cleaned data
print("Cleaned Data:")
print(data)

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Check whether ages are within a reasonable range
invalid_ages = data[
    (data["age"] < 0) | (data["age"] > 120)
]

print("\nInvalid Ages:")
print(invalid_ages)

# Check whether marks are between 0 and 100
invalid_marks = data[
    (data["marks"] < 0) | (data["marks"] > 100)
]

print("\nInvalid Marks:")
print(invalid_marks)

# Check for duplicate student records
duplicate_records = data.duplicated(
    subset=["name", "age", "course", "marks"]
)

print("\nDuplicate Records:")
print(data[duplicate_records])

print("\nNumber of Duplicate Records:")
print(int(duplicate_records.sum()))

# Prepare the validation report
validation_report = {
    "total_rows": int(len(data)),
    "total_columns": int(len(data.columns)),
    "missing_values": int(data.isnull().sum().sum()),
    "invalid_age_records": int(len(invalid_ages)),
    "invalid_marks_records": int(len(invalid_marks)),
    "duplicate_records": int(duplicate_records.sum())
}

# Create the reports folder
reports_folder = project_folder / "reports"
reports_folder.mkdir(exist_ok=True)

# Save the validation report
report_path = reports_folder / "validation_report.json"

with open(report_path, "w", encoding="utf-8") as file:
    json.dump(validation_report, file, indent=4)

print("\nValidation report saved to:")
print(report_path)
