import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


INPUT_FILE = "data/cleaned_sales_data.csv"

CHART_DIR = "outputs/charts"

REPORT_DIR = "outputs/reports"

EXCEL_FILE = "outputs/reports/automated_sales_report.xlsx"

TEXT_REPORT = "outputs/reports/automated_summary_report.txt"


def load_clean_data():

    if not os.path.exists(INPUT_FILE):

        raise FileNotFoundError(
            "Cleaned dataset not found. Run data_cleaning.py first."
        )

    df = pd.read_csv(INPUT_FILE)

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"]
    )

    return df


def create_folders():

    os.makedirs(CHART_DIR, exist_ok=True)

    os.makedirs(REPORT_DIR, exist_ok=True)


def calculate_kpis(df):

    total_sales = df["Sales"].sum()

    total_orders = df["Order_ID"].nunique()

    total_quantity = df["Quantity"].sum()

    average_order_value = (
        total_sales / total_orders
        if total_orders > 0
        else 0
    )

    average_sales = df["Sales"].mean()

    kpis = {
        "Total Sales": total_sales,
        "Total Orders": total_orders,
        "Total Quantity Sold": total_quantity,
        "Average Order Value": average_order_value,
        "Average Sales": average_sales
    }

    return kpis


def monthly_sales(df):

    df["Month"] = df["Order_Date"].dt.to_period(
        "M"
    ).astype(str)

    monthly = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    return monthly


def product_sales(df):

    result = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    return result


def region_sales(df):

    result = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    return result


def payment_sales(df):

    result = (
        df.groupby("Payment_Method")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    return result


def create_monthly_chart(monthly):

    plt.figure(figsize=(10, 6))

    plt.plot(
        monthly["Month"],
        monthly["Sales"],
        marker="o"
    )

    plt.title("Monthly Sales Trend")

    plt.xlabel("Month")

    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        f"{CHART_DIR}/monthly_sales_trend.png",
        dpi=300
    )

    plt.close()


def create_product_chart(products):

    plt.figure(figsize=(10, 6))

    plt.bar(
        products["Product"],
        products["Sales"]
    )

    plt.title("Sales by Product")

    plt.xlabel("Product")

    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        f"{CHART_DIR}/sales_by_product.png",
        dpi=300
    )

    plt.close()


def create_region_chart(regions):

    plt.figure(figsize=(8, 6))

    plt.bar(
        regions["Region"],
        regions["Sales"]
    )

    plt.title("Sales by Region")

    plt.xlabel("Region")

    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig(
        f"{CHART_DIR}/sales_by_region.png",
        dpi=300
    )

    plt.close()


def create_payment_chart(payments):

    plt.figure(figsize=(8, 6))

    plt.bar(
        payments["Payment_Method"],
        payments["Sales"]
    )

    plt.title("Sales by Payment Method")

    plt.xlabel("Payment Method")

    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig(
        f"{CHART_DIR}/sales_by_payment_method.png",
        dpi=300
    )

    plt.close()


def create_excel_report(
    df,
    kpis,
    monthly,
    products,
    regions,
    payments
):

    with pd.ExcelWriter(
        EXCEL_FILE,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Cleaned Data",
            index=False
        )

        pd.DataFrame(
            list(kpis.items()),
            columns=["KPI", "Value"]
        ).to_excel(
            writer,
            sheet_name="KPI Summary",
            index=False
        )

        monthly.to_excel(
            writer,
            sheet_name="Monthly Sales",
            index=False
        )

        products.to_excel(
            writer,
            sheet_name="Product Sales",
            index=False
        )

        regions.to_excel(
            writer,
            sheet_name="Region Sales",
            index=False
        )

        payments.to_excel(
            writer,
            sheet_name="Payment Analysis",
            index=False
        )

    print(
        f"Excel report created: {EXCEL_FILE}"
    )


def create_text_report(
    df,
    kpis,
    monthly,
    products,
    regions
):

    with open(
        TEXT_REPORT,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "DATA CLEANING & REPORTING AUTOMATION\n"
        )

        file.write("=" * 60 + "\n\n")

        file.write(
            "EXECUTIVE SUMMARY\n"
        )

        file.write("-" * 60 + "\n")

        file.write(
            f"Total Sales: ₹{kpis['Total Sales']:,.2f}\n"
        )

        file.write(
            f"Total Orders: {kpis['Total Orders']}\n"
        )

        file.write(
            f"Total Quantity Sold: "
            f"{kpis['Total Quantity Sold']:,.0f}\n"
        )

        file.write(
            f"Average Order Value: "
            f"₹{kpis['Average Order Value']:,.2f}\n"
        )

        file.write(
            f"Average Sales: "
            f"₹{kpis['Average Sales']:,.2f}\n\n"
        )

        file.write(
            "TOP PRODUCTS\n"
        )

        file.write("-" * 60 + "\n")

        for _, row in products.head(5).iterrows():

            file.write(
                f"{row['Product']}: "
                f"₹{row['Sales']:,.2f}\n"
            )

        file.write("\n")

        file.write(
            "REGIONAL PERFORMANCE\n"
        )

        file.write("-" * 60 + "\n")

        for _, row in regions.iterrows():

            file.write(
                f"{row['Region']}: "
                f"₹{row['Sales']:,.2f}\n"
            )

        file.write("\n")

        file.write(
            "MONTHLY SALES\n"
        )

        file.write("-" * 60 + "\n")

        for _, row in monthly.iterrows():

            file.write(
                f"{row['Month']}: "
                f"₹{row['Sales']:,.2f}\n"
            )

        file.write("\n")

        file.write(
            "REPORT GENERATED AUTOMATICALLY USING PYTHON.\n"
        )

    print(
        f"Text report created: {TEXT_REPORT}"
    )


def main():

    print("=" * 70)
    print("AUTOMATED REPORT GENERATION")
    print("=" * 70)

    create_folders()

    df = load_clean_data()

    print(
        f"Cleaned dataset loaded: {len(df)} rows"
    )

    # KPI calculations
    kpis = calculate_kpis(df)

    # Analysis
    monthly = monthly_sales(df)

    products = product_sales(df)

    regions = region_sales(df)

    payments = payment_sales(df)

    # Charts
    create_monthly_chart(monthly)

    create_product_chart(products)

    create_region_chart(regions)

    create_payment_chart(payments)

    # Excel
    create_excel_report(
        df,
        kpis,
        monthly,
        products,
        regions,
        payments
    )

    # Text report
    create_text_report(
        df,
        kpis,
        monthly,
        products,
        regions
    )

    print("\n" + "=" * 70)
    print("REPORTING COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated files:")

    print(
        "- outputs/reports/automated_sales_report.xlsx"
    )

    print(
        "- outputs/reports/automated_summary_report.txt"
    )

    print(
        "- outputs/charts/monthly_sales_trend.png"
    )

    print(
        "- outputs/charts/sales_by_product.png"
    )

    print(
        "- outputs/charts/sales_by_region.png"
    )

    print(
        "- outputs/charts/sales_by_payment_method.png"
    )


if __name__ == "__main__":
    main()
