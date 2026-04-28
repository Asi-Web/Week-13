##Asiwome Agbleze
## CMSC 111/1
## Asignment 2 - Data Cleaning and Analysis

# data_analysis.py
#
# This program loads employee data from a CSV file using pandas
# and performs several common data analysis tasks:
#   1. Load CSV into a DataFrame and show the first 5 rows
#   2. Check for missing values
#   3. Handle missing values (fill missing salary with average salary)
#   4. Filter employees (IT department AND salary > 65000)
#   5. Sort the filtered results by salary in descending order
#   6. Calculate the average salary after cleaning the data
#
# The code includes basic error handling so that problems such as
# a missing file or wrong column names do not crash the program.

import pandas as pd


def load_dataset(filename):
    """Task 1: Load the CSV file into a DataFrame and print the first 5 rows."""
    try:
        df = pd.read_csv(filename)
        print("=== Task 1: First 5 rows of the dataset ===")
        print(df.head())  # show the first 5 rows
        print()
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filename}' is empty.")
    except pd.errors.ParserError as e:
        print(f"Error: Could not parse '{filename}' as CSV.")
        print("Details:", e)
    except Exception as e:
        print("An unexpected error occurred while loading the dataset.")
        print("Details:", e)

    # If there was an error, return None so the caller can stop.
    return None


def check_missing_values(df):
    """Task 2: Display the count of missing values per column."""
    try:
        print("=== Task 2: Missing values per column ===")
        missing_counts = df.isna().sum()  # or df.isnull().sum()
        print(missing_counts)
        print()
    except Exception as e:
        print("An error occurred while checking missing values.")
        print("Details:", e)


def handle_missing_values(df):
    """
    Task 3: Handle missing values.

    We are using Option A (Recommended):
    - Fill missing salary values with the average salary.
    """
    try:
        print("=== Task 3: Handle missing values (fill salary NaN with average) ===")

        # Convert salary to numeric, forcing errors to NaN
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

        # Compute the average salary, ignoring NaN values
        average_salary = df["salary"].mean()

        # Fill only the missing salary values with the average
        df["salary"].fillna(average_salary, inplace=True)

        print("DataFrame after handling missing salary values:")
        print(df)
        print()
        return df, average_salary
    except KeyError:
        print("Error: The 'salary' column is missing from the dataset.")
    except Exception as e:
        print("An error occurred while handling missing values.")
        print("Details:", e)

    return df, None


def filter_data(df):
    """Task 4: Filter to IT employees with salary > 65000 and print the result."""
    try:
        print("=== Task 4: Filtered results (IT department and salary > 65000) ===")

        # Ensure salary is numeric in case it was changed earlier
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

        filtered = df[(df["department"] == "IT") & (df["salary"] > 65000)]
        print(filtered)
        print()
        return filtered
    except KeyError as e:
        print("Error: A required column is missing from the dataset.")
        print("Missing column:", e)
    except Exception as e:
        print("An error occurred while filtering the data.")
        print("Details:", e)

    return df.iloc[0:0]  # return an empty DataFrame on error


def sort_data(filtered_df):
    """Task 5: Sort the filtered data by salary in descending order and print it."""
    try:
        print("=== Task 5: Sorted filtered results by salary (descending) ===")
        sorted_df = filtered_df.sort_values(by="salary", ascending=False)
        print(sorted_df)
        print()
        return sorted_df
    except KeyError:
        print("Error: The 'salary' column is missing from the filtered data.")
    except Exception as e:
        print("An error occurred while sorting the data.")
        print("Details:", e)

    return filtered_df


def calculate_average_salary(df):
    """Task 6: Calculate and print the average salary after cleaning the data."""
    try:
        print("=== Task 6: Average salary after handling missing values ===")

        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
        avg_salary = df["salary"].mean()

        print(f"Average salary: {avg_salary:.2f}")
        print()
    except KeyError:
        print("Error: The 'salary' column is missing from the dataset.")
    except Exception as e:
        print("An error occurred while calculating the average salary.")
        print("Details:", e)


def main():
    """Main function to run all tasks in order."""
    filename = "employees.csv"

    # 1) Load dataset
    df = load_dataset(filename)
    if df is None:
        # If loading failed, stop the program early.
        return

    # 2) Check missing values
    check_missing_values(df)

    # 3) Handle missing values (Option A: fill salary NaN with mean)
    df_clean, _ = handle_missing_values(df)

    # 4) Filter data based on condition
    filtered_df = filter_data(df_clean)

    # 5) Sort filtered results
    sorted_df = sort_data(filtered_df)

    # 6) Calculate average salary on the cleaned dataset
    calculate_average_salary(df_clean)


if __name__ == "__main__":
    main()