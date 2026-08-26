import subprocess
import sys


def run_script(script):

    print("\n")
    print("=" * 70)
    print(f"RUNNING: {script}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:

        print(
            f"\nERROR: {script} failed."
        )

        sys.exit(1)


def main():

    print("=" * 70)
    print("DATA CLEANING & REPORTING AUTOMATION")
    print("=" * 70)

    print(
        "\nStarting complete automated workflow..."
    )

    # Step 1
    run_script(
        "src/create_dataset.py"
    )

    # Step 2
    run_script(
        "src/data_cleaning.py"
    )

    # Step 3
    run_script(
        "src/reporting.py"
    )

    print("\n")
    print("=" * 70)
    print("AUTOMATION COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nYour outputs are available in:")

    print(
        "\nCleaned Data:"
        "\ndata/cleaned_sales_data.csv"
    )

    print(
        "\nReports:"
        "\noutputs/reports/"
    )

    print(
        "\nCharts:"
        "\noutputs/charts/"
    )


if __name__ == "__main__":
    main()