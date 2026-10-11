
from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the sample CSV file
file_path = project_folder / "data" / "sample_data.csv"

# Read the CSV file
data = pd.read_csv(file_path)

# Display the data
print("Sample Data:")
print(data)

# Display basic information
print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns.tolist())

# Count missing values in each column
print("\nMissing Values:")
print(data.isnull().sum())


# Count duplicate rows
print("\nDuplicate Rows:")
print(data.duplicated().sum())

print("\nChecking duplicate rows:")
print(data[data["name"] == "Asha"])

print("\nAre rows duplicated?")
print(data.duplicated())

# Check duplicate records while ignoring student_id
print("\nDuplicate student details:")
print(data.duplicated(subset=["name", "age", "course", "marks"]).sum())

# Check which age values are not numeric
age_numbers = pd.to_numeric(data["age"], errors="coerce")

print("\nInvalid age values:")
print(data.loc[age_numbers.isna() & data["age"].notna(), "age"])

import json

# Count missing values in each column
missing_values = data.isnull().sum().to_dict()

# Count potential duplicate records
duplicate_count = int(
    data.duplicated(
        subset=["name", "age", "course", "marks"]
    ).sum()
)

# Prepare the profiling report
report = {
    "total_rows": int(data.shape[0]),
    "total_columns": int(data.shape[1]),
    "column_names": data.columns.tolist(),
    "missing_values": {
        key: int(value)
        for key, value in missing_values.items()
    },
    "potential_duplicates": duplicate_count
}

# Create the reports folder if needed
reports_folder = project_folder / "reports"
reports_folder.mkdir(exist_ok=True)

# Save the report as a JSON file
report_path = reports_folder / "profiling_report.json"

with open(report_path, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("\nProfiling report saved to:")
print(report_path)
