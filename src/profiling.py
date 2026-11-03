
from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the sample CSV file
file_path = project_folder / "data" / "sample_data.csv"

# Check whether the CSV file exists
if not file_path.exists():
    print("Error: Sample dataset file not found.")
    print("Expected location:", file_path)
    raise SystemExit(1)

# Check whether the CSV file is empty
if file_path.stat().st_size == 0:
    print("Error: Sample dataset file is empty.")
    raise SystemExit(1)

# Read the CSV file
data = pd.read_csv(file_path)
# Check whether the dataset contains any records
if data.empty:
    print("Error: Sample dataset contains no records.")
    raise SystemExit(1)
# Check whether all required columns are available
required_columns = [
    "student_id",
    "name",
    "age",
    "course",
    "marks"
]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    print("Error: Required columns are missing.")
    print("Missing columns:", missing_columns)
    raise SystemExit(1)
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
# Find invalid age values
invalid_age_values = data.loc[
    age_numbers.isna() & data["age"].notna(),
    "age"
].tolist()

print("\nInvalid age values for report:")
print(invalid_age_values)
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
    "column_data_types": {
        column: str(data[column].dtype)
        for column in data.columns
    },

    "unique_values": {
        column: int(data[column].nunique())
        for column in data.columns
},
    "constant_columns": [
        column
        for column in data.columns
        if data[column].nunique() == 1
    ],
    "numerical_statistics": {
        column: {
            "minimum": float(data[column].min()),
            "maximum": float(data[column].max()),
            "mean": float(data[column].mean()),
            "median": float(data[column].median())
        }
        for column in data.select_dtypes(include="number").columns
    },
    "categorical_statistics": {
        column: {
            "most_frequent": str(data[column].mode()[0]),
            "frequency": int(data[column].value_counts().iloc[0])
        }
        for column in data.select_dtypes(include=["object", "str"]).columns
        if not data[column].mode().empty
    },
    "data_types": {
        column: str(data[column].dtype)
        for column in data.columns
    },
    "invalid_age_values": invalid_age_values,
    "missing_values": {
        key: int(value)
        for key, value in missing_values.items()
    },
    "missing_value_percentage": {
        column: round(
            (data[column].isnull().sum() / len(data)) * 100, 2
        )
        for column in data.columns
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
