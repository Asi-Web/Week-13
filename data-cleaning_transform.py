## Asiwome Agbleze
## CMSC 111/1
## Asignment 3- Data Cleaninig, Encoding, Normalization, and Group Analysis (Pandas)

# data_cleaning_transform.py
#
# This program demonstrates data cleaning and transformation with pandas:
# 1. Load CSV data into a DataFrame
# 2. Check for missing values
# 3. Fill missing numeric values (median for units_sold, mean for unit_price)
# 4. Remove duplicate rows
# 5. One-hot encode categorical variables (region, product)
# 6. Normalize numeric columns (min-max scaling)
# 7. Group the cleaned (pre-encoded) data by region and compute summary stats

import pandas as pd


# Task 1: Load the dataset and print the first 5 rows
def load_dataset(filename):
    """Load CSV into a DataFrame and show head()."""
    try:
        df = pd.read_csv(filename)
        print("=== Task 1: First 5 rows of sales_data.csv ===")
        print(df.head())
        print()
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Make sure it is in the same folder.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{filename}' is empty.")
    except pd.errors.ParserError as e:
        print(f"Error: Could not parse '{filename}' as CSV.")
        print("Details:", e)
    except Exception as e:
        print("An unexpected error occurred while loading the CSV file.")
        print("Details:", e)

    # Return None if something went wrong so the caller can stop.
    return None


# Task 2: Check for missing values
def check_missing_values(df):
    """Print the number of missing values per column."""
    try:
        print("=== Task 2: Missing values per column ===")
        missing_counts = df.isna().sum()  # or df.isnull().sum()
        print(missing_counts)
        print()
    except Exception as e:
        print("An error occurred while checking for missing values.")
        print("Details:", e)


# Task 3: Handle missing values (median for units_sold, mean for unit_price)
def handle_missing_values(df):
    """Fill missing units_sold with median and unit_price with mean, then print DataFrame."""
    try:
        print("=== Task 3: Handle missing values ===")

        # Convert numeric columns to numeric types, coercing invalid entries to NaN
        df["units_sold"] = pd.to_numeric(df["units_sold"], errors="coerce")
        df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

        # Calculate median for units_sold and mean for unit_price (NaN ignored by default)
        units_median = df["units_sold"].median()
        price_mean = df["unit_price"].mean()

        # Fill missing units_sold and unit_price
        df["units_sold"].fillna(units_median, inplace=True)
        df["unit_price"].fillna(price_mean, inplace=True)

        print("Data after filling missing units_sold (median) and unit_price (mean):")
        print(df)
        print()

        return df
    except KeyError as e:
        print("Error: Missing expected numeric column in the dataset.")
        print("Missing column:", e)
    except Exception as e:
        print("An error occurred while handling missing values.")
        print("Details:", e)

    return df


# Task 4: Remove duplicate rows
def remove_duplicates(df):
    """Remove duplicate rows and show row counts before and after."""
    try:
        print("=== Task 4: Remove duplicate rows ===")
        rows_before = len(df)
        df_no_dupes = df.drop_duplicates()
        rows_after = len(df_no_dupes)

        print(f"Rows before removing duplicates: {rows_before}")
        print(f"Rows after removing duplicates:  {rows_after}")
        print()

        return df_no_dupes
    except Exception as e:
        print("An error occurred while removing duplicate rows.")
        print("Details:", e)

    return df


# Task 5: One-hot encode region and product
def encode_categorical(df):
    """Encode region and product columns using one-hot encoding (get_dummies)."""
    try:
        print("=== Task 5: One-hot encode 'region' and 'product' ===")

        # Use get_dummies to encode selected categorical columns
        df_encoded = pd.get_dummies(df, columns=["region", "product"], dtype=int)

        print("Columns after one-hot encoding:")
        print(df_encoded.columns)
        print()

        return df_encoded
    except KeyError as e:
        print("Error: Could not find one of the categorical columns to encode.")
        print("Missing column:", e)
    except Exception as e:
        print("An error occurred during one-hot encoding.")
        print("Details:", e)

    return df


# Task 6: Normalize numerical values (min-max scaling)
def normalize_numeric(df):
    """Normalize units_sold and unit_price using min-max formula and print DataFrame."""
    try:
        print("=== Task 6: Normalize 'units_sold' and 'unit_price' with min-max scaling ===")

        # Ensure numeric types
        df["units_sold"] = pd.to_numeric(df["units_sold"], errors="coerce")
        df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

        # Min-max normalization: (x - min) / (max - min)
        for col in ["units_sold", "unit_price"]:
            col_min = df[col].min()
            col_max = df[col].max()
            if col_max == col_min:
                # Avoid division by zero if all values are the same
                df[col + "_normalized"] = 0.0
            else:
                df[col + "_normalized"] = (df[col] - col_min) / (col_max - col_min)

        print("Data with normalized numeric columns:")
        print(df)
        print()

        return df
    except KeyError as e:
        print("Error: Missing numeric column for normalization.")
        print("Missing column:", e)
    except Exception as e:
        print("An error occurred while normalizing numeric columns.")
        print("Details:", e)

    return df


# Task 7: Group by region and summarize
def group_and_summarize(df):
    """Group cleaned (pre-encoded) data by region, summing units_sold and averaging unit_price."""
    try:
        print("=== Task 7: Grouped summary by region (sum units_sold, mean unit_price) ===")

        # Group by region and compute sum of units_sold and mean of unit_price
        summary = df.groupby("region").agg(
            total_units_sold=("units_sold", "sum"),
            average_unit_price=("unit_price", "mean")
        )

        print(summary)
        print()
    except KeyError as e:
        print("Error: Could not group by 'region' or missing numeric columns.")
        print("Missing column:", e)
    except Exception as e:
        print("An error occurred while grouping and summarizing the data.")
        print("Details:", e)


# Main function: run all tasks in order
def main():
    """Main driver to run all data cleaning and transformation steps in order."""
    filename = "sales_data.csv"

    # 1) Load dataset
    df = load_dataset(filename)
    if df is None:
        # Stop early if the file could not be loaded
        return

    # 2) Check missing values
    check_missing_values(df)

    # 3) Handle missing values
    df_clean = handle_missing_values(df)

    # 4) Remove duplicate rows (keep first occurrence)
    df_clean = remove_duplicates(df_clean)

    # Keep a copy of the cleaned dataset BEFORE encoding (used in Task 7)
    df_for_grouping = df_clean.copy()

    # 5) One-hot encode categorical columns
    df_encoded = encode_categorical(df_clean)

    # 6) Normalize numeric values (units_sold, unit_price) on the encoded DataFrame
    df_normalized = normalize_numeric(df_encoded)

    # 7) Group original cleaned data by region and compute summary stats
    group_and_summarize(df_for_grouping)


# Standard boilerplate to call main() when the file is executed
if __name__ == "__main__":
    main()