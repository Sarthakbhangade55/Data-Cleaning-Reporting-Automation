import pandas as pd
import numpy as np
import os

RAW_FILE = "data/raw/raw_sales_data.csv"
CLEAN_FILE = "data/cleaned_sales_data.csv"


def load_data():
    """Load raw dataset."""

    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_FILE}"
        )

    df = pd.read_csv(RAW_FILE)

    print(f"Raw dataset loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df


def clean_column_names(df):
    """Standardize column names."""

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df


def remove_duplicates(df):
    """Remove duplicate records."""

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    removed = before - after

    print(f"Duplicate rows removed: {removed}")

    return df, removed


def clean_dates(df):
    """Convert Order_Date into standard datetime format."""

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce",
        dayfirst=True
    )

    # Fill missing dates with median date
    if df["Order_Date"].isnull().sum() > 0:

        median_date = df["Order_Date"].dropna().sort_values().iloc[
            len(df["Order_Date"].dropna()) // 2
        ]

        df["Order_Date"] = df["Order_Date"].fillna(median_date)

    return df


def clean_text_columns(df):
    """Standardize text columns."""

    text_columns = [
        "Customer",
        "Product",
        "Category",
        "Region",
        "Payment_Method"
    ]

    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
            )

    # Standardize product names
    if "Product" in df.columns:

        df["Product"] = df["Product"].str.title()

    # Standardize category
    if "Category" in df.columns:

        df["Category"] = df["Category"].str.title()

    # Standardize region
    if "Region" in df.columns:

        df["Region"] = df["Region"].str.title()

    # Standardize payment method
    if "Payment_Method" in df.columns:

        df["Payment_Method"] = df["Payment_Method"].str.title()

    return df


def clean_numeric_columns(df):
    """Convert numeric columns and handle missing values."""

    numeric_columns = [
        "Quantity",
        "Unit_Price",
        "Sales"
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            # Fill missing numeric values with median
            median_value = df[column].median()

            df[column] = df[column].fillna(median_value)

    return df


def validate_data(df):
    """Perform final data validation."""

    validation = {}

    validation["Total_Rows"] = len(df)

    validation["Total_Columns"] = len(df.columns)

    validation["Missing_Values"] = int(
        df.isnull().sum().sum()
    )

    validation["Duplicate_Rows"] = int(
        df.duplicated().sum()
    )

    validation["Negative_Sales"] = int(
        (df["Sales"] < 0).sum()
    )

    validation["Zero_Quantity"] = int(
        (df["Quantity"] <= 0).sum()
    )

    return validation


def save_cleaned_data(df):

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        CLEAN_FILE,
        index=False
    )

    print(f"\nCleaned dataset saved to:")
    print(CLEAN_FILE)


def main():

    print("=" * 70)
    print("AUTOMATED DATA CLEANING")
    print("=" * 70)

    df = load_data()

    print("\nMissing values BEFORE cleaning:")
    print(df.isnull().sum())

    original_rows = len(df)

    # Cleaning
    df = clean_column_names(df)

    df, duplicates_removed = remove_duplicates(df)

    df = clean_dates(df)

    df = clean_text_columns(df)

    df = clean_numeric_columns(df)

    # Calculate sales if required
    if "Sales" in df.columns:

        calculated_sales = (
            df["Quantity"] *
            df["Unit_Price"]
        )

        # Replace missing/invalid sales
        df["Sales"] = df["Sales"].fillna(
            calculated_sales
        )

    # Sort data
    if "Order_Date" in df.columns:

        df = df.sort_values(
            "Order_Date"
        )

    # Reset index
    df = df.reset_index(drop=True)

    # Validation
    validation = validate_data(df)

    save_cleaned_data(df)

    print("\n" + "=" * 70)
    print("CLEANING SUMMARY")
    print("=" * 70)

    print(f"Original rows       : {original_rows}")
    print(f"Final rows          : {len(df)}")
    print(f"Duplicates removed  : {duplicates_removed}")
    print(
        f"Missing values left : {validation['Missing_Values']}"
    )
    print(
        f"Duplicate rows left : {validation['Duplicate_Rows']}"
    )
    print(
        f"Negative sales      : {validation['Negative_Sales']}"
    )
    print(
        f"Invalid quantities  : {validation['Zero_Quantity']}"
    )

    print("\nMissing values AFTER cleaning:")
    print(df.isnull().sum())

    print("\nData cleaning completed successfully.")


if __name__ == "__main__":
    main()