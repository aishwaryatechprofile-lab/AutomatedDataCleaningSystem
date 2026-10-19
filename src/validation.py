import json
from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent
# Find the configuration file
config_path = project_folder / "config.json"

# Read the configuration
with open(config_path, "r") as file:
    config = json.load(file)

rules = config["validation_rules"]
min_age = rules["min_age"]
max_age = rules["max_age"]
min_marks = rules["min_marks"]
max_marks = rules["max_marks"]
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
    (data["age"] < min_age) | (data["age"] > max_age)
]


print("\nInvalid Ages:")
print(invalid_ages)

# Check whether marks are within the configured range
invalid_marks = data[
    (data["marks"] < min_marks) | (data["marks"] > max_marks)
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
    "duplicate_records": int(duplicate_records.sum()),
    "validation_status": "PASSED WITH WARNINGS" if len(invalid_ages) == 0 and len(invalid_marks) == 0 and data.isnull().sum().sum() == 0 and duplicate_records.sum() > 0 else "PASSED" if len(invalid_ages) == 0 and len(invalid_marks) == 0 and data.isnull().sum().sum() == 0 else "FAILED"
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
print("\nValidation Status:", validation_report["validation_status"])