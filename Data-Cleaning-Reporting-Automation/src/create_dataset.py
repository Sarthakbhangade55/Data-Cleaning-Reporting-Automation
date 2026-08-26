import pandas as pd
import numpy as np
import os

# Create folders
os.makedirs("data/raw", exist_ok=True)

# Sample messy sales dataset
data = {
    "Order_ID": [
        "ORD001", "ORD002", "ORD003", "ORD004", "ORD005",
        "ORD006", "ORD007", "ORD008", "ORD009", "ORD010",
        "ORD011", "ORD012", "ORD013", "ORD014", "ORD015",
        "ORD005"
    ],

    "Order_Date": [
        "2026-01-05", "2026-01-07", "2026/01/10", "10-01-2026",
        "2026-01-15", "2026-01-18", None, "2026-01-22",
        "2026-01-25", "2026-01-27", "2026-02-01", None,
        "2026-02-05", "2026-02-08", "2026-02-10", "2026-01-15"
    ],

    "Customer": [
        "Rahul", "Priya", "Amit", "Sneha", "Rohan",
        "Neha", "Akash", "Pooja", "Vikas", None,
        "Anjali", "Kiran", "Sameer", "Meena", "Ravi", "Rohan"
    ],

    "Product": [
        "Laptop", "Mobile", "laptop", "MOBILE", "Tablet",
        "Headphones", "Laptop", "tablet", "Mobile", "Laptop",
        "Headphones", "Mobile", "Laptop", "Tablet", "Mobile", "Tablet"
    ],

    "Category": [
        "Electronics", "Electronics", "electronics", " Electronics ",
        "Electronics", "Accessories", "Electronics", "electronics",
        "Electronics", "Electronics", "Accessories", "Electronics",
        "Electronics", "Electronics", "Electronics", "Electronics"
    ],

    "Region": [
        "North", "South", "WEST", "West", "East",
        "north", "South", "East", "WEST", "North",
        "South", "East", "North", "West", None, "East"
    ],

    "Quantity": [
        2, 1, 3, None, 2,
        4, 1, 2, 3, 2,
        5, 1, None, 2, 3, 2
    ],

    "Unit_Price": [
        55000, 25000, 55000, 25000, 30000,
        3000, 55000, 30000, 25000, 55000,
        3000, 25000, 55000, 30000, 25000, 30000
    ],

    "Sales": [
        110000, 25000, 165000, None, 60000,
        12000, 55000, 60000, 75000, 110000,
        15000, 25000, None, 60000, 75000, 60000
    ],

    "Payment_Method": [
        "UPI", "Card", "upi", "Cash", "CARD",
        "UPI", "Cash", "card", "UPI", "Cash",
        "Card", "UPI", None, "Cash", "card", "Cash"
    ]
}

df = pd.DataFrame(data)

# Add intentional duplicate row
df = pd.concat([df, df.iloc[[2]]], ignore_index=True)

file_path = "data/raw/raw_sales_data.csv"

df.to_csv(file_path, index=False)

print("=" * 70)
print("RAW DATASET CREATED SUCCESSFULLY")
print("=" * 70)
print(f"File: {file_path}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDataset preview:")
print(df.head())