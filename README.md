# Automated Data Cleaning & Validation System

## Project Overview

The Automated Data Cleaning & Validation System is a Python-based project that automates dataset profiling, data cleaning, and data validation using Pandas.

It helps identify data quality issues, clean datasets, and generate reports automatically.

## Project Objectives

- Identify missing and invalid values.
- Analyze dataset structure and statistics.
- Detect duplicate and potential duplicate records.
- Clean data using suitable methods.
- Validate the cleaned dataset.
- Generate reports in JSON format.

## Features

### 1. Dataset Profiling
- Displays total rows and columns.
- Identifies column names and data types.
- Calculates unique values and unique value percentages.
- Identifies missing values and missing value percentages.
- Calculates numerical and categorical statistics.
- Identifies the most frequent value in each column.
- Detects duplicate and potential duplicate records.

### 2. Data Cleaning
- Handles missing values.
- Converts invalid age values into appropriate numeric values.
- Fills missing numerical values using the median.
- Saves the cleaned dataset.

### 3. Data Validation
- Checks for missing values.
- Identifies invalid age and marks values.
- Detects duplicate records.
- Generates a validation report.

### 4. Workflow Automation
- Runs profiling, cleaning, and validation through a single Python file.
- Saves reports automatically in the reports folder.

## Technologies Used

- Python
- Pandas
- JSON
- Git
- GitHub

## Project Structure

```text
AutomatedDataCleaningSystem/
|
|-- data/
|   |-- sample_data.csv
|   |-- cleaned_data.csv
|
|-- reports/
|   |-- profiling_report.json
|   |-- cleaning_log.json
|   |-- validation_report.json
|
|-- src/
|   |-- profiling.py
|   |-- cleaning.py
|   |-- validation.py
|
|-- main.py
|-- config.json
|-- README.md
|-- .gitignore
```
## How to Run the Project

1. Install Python.
2. Install Pandas:

```bash
pip install pandas
```

3. Open the project folder in PowerShell or a terminal.
4. Run the following command:

```bash
python main.py
```

## Output

The system generates:

- A dataset profiling report.
- A data cleaning log.
- A data validation report.
- A cleaned CSV dataset.

All reports are saved in the `reports/` folder, and the cleaned dataset is saved in the `data/` folder.

## Project Status

The core development of the Automated Data Cleaning & Validation System is completed, including dataset profiling, data cleaning, data validation, report generation, and workflow automation.

## Author

Developed as a Python data cleaning and validation project.