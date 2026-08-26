# 📊 Data Cleaning & Reporting Automation

> **An automated Python-based data preprocessing, analysis, visualization, and reporting workflow.**

## 👨‍💻 Author

**Sarthak Bhangade**
B.Tech – Artificial Intelligence & Data Science
Sanjivani University | 2024–2028

---

## 📌 Project Overview

**Data Cleaning & Reporting Automation** is an end-to-end Python project developed to automate common data preprocessing and reporting tasks.

The project takes a raw and inconsistent sales dataset, automatically cleans and validates the data, performs business analysis, generates visual summaries, and produces an Excel report and text-based summary report.

The main goal is to reduce manual data preparation and reporting effort while improving data quality, consistency, and reporting efficiency.

---

## 🎯 Objectives

* Automate data cleaning and preprocessing.
* Handle missing values efficiently.
* Detect and remove duplicate records.
* Standardize inconsistent text and categorical data.
* Convert and validate date and numerical fields.
* Perform basic sales analysis.
* Calculate important business KPIs.
* Generate visual summaries automatically.
* Create an automated Excel report.
* Generate an automated text summary.
* Build a reusable end-to-end reporting workflow.

---

## 🛠️ Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Core programming language           |
| Pandas     | Data manipulation and analysis      |
| NumPy      | Numerical operations                |
| Matplotlib | Data visualization                  |
| OpenPyXL   | Excel report generation             |
| CSV        | Raw and cleaned data storage        |
| Excel      | Automated reporting                 |
| VS Code    | Development environment             |
| Git/GitHub | Version control and project hosting |

---

## 🔄 Project Workflow

```text
                    RAW DATA
                       │
                       ▼
              Data Loading
                       │
                       ▼
             Data Quality Check
                       │
                       ▼
             Missing Value Handling
                       │
                       ▼
             Duplicate Removal
                       │
                       ▼
           Data Standardization
                       │
                       ▼
             Data Type Conversion
                       │
                       ▼
              Data Validation
                       │
                       ▼
               KPI Calculation
                       │
                       ▼
              Business Analysis
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Visualizations      Excel Report
             │                   │
             └─────────┬─────────┘
                       ▼
              Automated Summary
```

---

## ✨ Key Features

### 1. Automated Data Loading

The project automatically loads the raw CSV dataset using Pandas.

### 2. Missing Value Handling

Missing values are detected and handled using appropriate replacement strategies.

Examples include:

* Missing dates
* Missing customer names
* Missing quantities
* Missing sales values
* Missing regions
* Missing payment methods

### 3. Duplicate Removal

Duplicate records are automatically detected and removed to improve data accuracy.

### 4. Text Standardization

Inconsistent categorical values are standardized.

For example:

```text
laptop
Laptop
LAPTOP
```

are converted into:

```text
Laptop
```

Similarly, region and payment-method values are standardized.

### 5. Date Standardization

Different date formats are converted into a consistent datetime format.

Example:

```text
2026-01-05
2026/01/10
10-01-2026
```

are processed into a standardized date format.

### 6. Numerical Data Cleaning

Numeric columns are converted into appropriate numeric data types and missing numerical values are handled automatically.

### 7. Data Validation

The cleaned dataset is checked for:

* Remaining missing values
* Remaining duplicates
* Negative sales
* Invalid quantities
* Number of rows
* Number of columns

### 8. KPI Analysis

The project automatically calculates:

* Total Sales
* Total Orders
* Total Quantity Sold
* Average Order Value
* Average Sales

### 9. Automated Visualizations

The system generates:

* Monthly Sales Trend
* Sales by Product
* Sales by Region
* Sales by Payment Method

### 10. Automated Excel Report

A professional Excel report is generated containing multiple worksheets:

```text
Cleaned Data
KPI Summary
Monthly Sales
Product Sales
Region Sales
Payment Analysis
```

### 11. Automated Summary Report

A text-based summary report is also generated containing important business insights.

---

## 📁 Project Structure

```text
Data-Cleaning-Reporting-Automation/
│
├── data/
│   ├── raw/
│   │   └── raw_sales_data.csv
│   │
│   └── cleaned_sales_data.csv
│
├── outputs/
│   ├── charts/
│   │   ├── monthly_sales_trend.png
│   │   ├── sales_by_product.png
│   │   ├── sales_by_region.png
│   │   └── sales_by_payment_method.png
│   │
│   └── reports/
│       ├── automated_sales_report.xlsx
│       └── automated_summary_report.txt
│
├── src/
│   ├── create_dataset.py
│   ├── data_cleaning.py
│   ├── reporting.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 🧩 Python Scripts

### `create_dataset.py`

Creates a sample raw sales dataset containing intentionally introduced data-quality issues such as:

* Missing values
* Duplicate records
* Inconsistent text
* Different date formats

This is used to demonstrate the complete automation workflow.

### `data_cleaning.py`

Responsible for:

* Loading raw data
* Cleaning column names
* Removing duplicates
* Handling missing values
* Standardizing text
* Converting dates
* Cleaning numeric columns
* Validating the final dataset
* Saving cleaned data

### `reporting.py`

Responsible for:

* KPI calculation
* Sales analysis
* Monthly analysis
* Product analysis
* Regional analysis
* Payment-method analysis
* Chart generation
* Excel report generation
* Summary report generation

### `main.py`

Acts as the main automation controller.

It executes the complete workflow automatically:

```text
Dataset Creation
       ↓
Data Cleaning
       ↓
Data Validation
       ↓
Analysis
       ↓
Visualization
       ↓
Excel Report
       ↓
Summary Report
```

---

## ⚙️ Installation

### Step 1: Clone or download the project

Open the project in VS Code.

### Step 2: Install dependencies

Open the terminal and run:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install pandas numpy matplotlib openpyxl
```

---

## ▶️ How to Run

Run the complete automated workflow using:

```bash
python src/main.py
```

The system will automatically:

1. Create/load the raw dataset.
2. Clean the data.
3. Handle missing values.
4. Remove duplicate records.
5. Standardize inconsistent values.
6. Validate the cleaned dataset.
7. Calculate KPIs.
8. Generate charts.
9. Create the Excel report.
10. Create the summary report.

---

## 📤 Generated Outputs

After successful execution, the project generates the following outputs.

### Cleaned Dataset

```text
data/cleaned_sales_data.csv
```

### Excel Report

```text
outputs/reports/automated_sales_report.xlsx
```

### Summary Report

```text
outputs/reports/automated_summary_report.txt
```

### Visualizations

```text
outputs/charts/monthly_sales_trend.png
outputs/charts/sales_by_product.png
outputs/charts/sales_by_region.png
outputs/charts/sales_by_payment_method.png
```

---

## 📊 Generated Visualizations

### Monthly Sales Trend

Shows how sales change over time and helps identify monthly sales patterns.

### Sales by Product

Compares the sales contribution of different products.

### Sales by Region

Shows regional sales performance.

### Sales by Payment Method

Shows the distribution of sales across different payment methods.

---

## 📑 Excel Report

The automated Excel workbook contains:

### Cleaned Data

The complete cleaned dataset.

### KPI Summary

Contains:

```text
Total Sales
Total Orders
Total Quantity Sold
Average Order Value
Average Sales
```

### Monthly Sales

Monthly sales aggregation.

### Product Sales

Sales performance by product.

### Region Sales

Sales performance by region.

### Payment Analysis

Sales performance by payment method.

---

## 🧪 Data Quality Checks

The project performs automated validation after cleaning.

The following checks are performed:

```text
✓ Missing value check
✓ Duplicate record check
✓ Negative sales check
✓ Quantity validation
✓ Row count validation
✓ Column count validation
✓ Date conversion validation
✓ Numeric data validation
```

---

## 🔐 Data Cleaning Rules

| Data Issue                   | Automated Solution                 |
| ---------------------------- | ---------------------------------- |
| Missing text values          | Replaced with `Unknown`            |
| Missing numeric values       | Filled using median                |
| Missing dates                | Filled using median date           |
| Duplicate rows               | Removed                            |
| Inconsistent product names   | Standardized                       |
| Inconsistent categories      | Standardized                       |
| Inconsistent regions         | Standardized                       |
| Inconsistent payment methods | Standardized                       |
| Invalid numeric values       | Converted using numeric validation |
| Different date formats       | Converted to datetime              |

---

## 📈 Business Value

Automating data cleaning and reporting provides several benefits:

* Reduces manual data-processing time.
* Improves data consistency.
* Reduces human errors.
* Makes reports reproducible.
* Provides faster business insights.
* Creates a repeatable reporting workflow.
* Makes the process easier to scale for larger datasets.

---

## 🚀 Future Enhancements

The project can be further improved by adding:

* Excel input support.
* Automatic database connectivity.
* Power BI dashboard integration.
* Interactive dashboards.
* Automated email reporting.
* Scheduled daily/weekly reports.
* Advanced anomaly detection.
* Automated data-quality alerts.
* Machine learning-based forecasting.
* Cloud-based data pipelines.
* Real-time reporting.

---

## 🎓 Internship Task Mapping

This project directly addresses the internship requirements:

| Internship Requirement         | Implementation |
| ------------------------------ | -------------- |
| Use Python, Excel, or Power BI | Python + Excel |
| Handle missing values          | Implemented    |
| Handle duplicates              | Implemented    |
| Handle inconsistent data       | Implemented    |
| Automate cleaning              | Implemented    |
| Generate reports               | Implemented    |
| Generate visual summaries      | Implemented    |
| Understand preprocessing       | Demonstrated   |
| Understand automation          | Demonstrated   |
| Improve reporting efficiency   | Demonstrated   |

---

## 💡 Learning Outcomes

Through this project, I developed practical experience in:

* Data preprocessing
* Data cleaning
* Data validation
* Exploratory data analysis
* KPI generation
* Data visualization
* Excel automation
* Python automation
* Report generation
* Building reusable data workflows

---

## 🏆 Project Outcome

The project successfully demonstrates an automated data-processing pipeline that transforms raw and inconsistent data into a clean, validated, analyzed, and report-ready dataset.

Instead of manually performing each step, the entire workflow can be executed using a single command:

```bash
python src/main.py
```

This makes the solution efficient, repeatable, and suitable for practical data-analysis and reporting workflows.

---

## 📌 Internship Project

**Task:** Data Cleaning & Reporting Automation

**Domain:** Data Analytics / Data Science

**Tools:** Python, Pandas, NumPy, Matplotlib, OpenPyXL, Excel

**Type:** Automation & Reporting Project

**Status:** Completed ✅

---

## 👨‍💻 Author

**Sarthak Bhangade**

B.Tech – Artificial Intelligence & Data Science
Sanjivani University | 2024–2028

**Skills:** Python • Data Analytics • Machine Learning • Data Science • Statistics • SQL • DevOps

---

⭐ *This project was developed as part of an internship task to demonstrate practical skills in data preprocessing, automation, analysis, visualization, and reporting.*
