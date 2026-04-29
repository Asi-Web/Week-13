##Asiwome Agbleze
## CMSC 111/1
## Asignment 4: Sales Visualization with Pands Matplotlib

# ==========================================
# Import pandas for working with data
# Import matplotlib.pyplot for making charts
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# Use a try-except block so the program
# does not crash if there is a file problem
# ==========================================
try:

    # ==========================================
    # Load the CSV file into a pandas DataFrame
    # ==========================================
    df = pd.read_csv("sales_data.csv")

    # ==========================================
    # Convert the date column to datetime format
    # ==========================================
    df["date"] = pd.to_datetime(df["date"])

    # ==========================================
    # Convert the sales column to numbers
    # ==========================================
    df["sales"] = pd.to_numeric(df["sales"])

    # ==========================================
    # Print the DataFrame to make sure it loaded
    # correctly
    # ==========================================
    print("Sales Data:")
    print(df)
    print()

    # ==========================================
    # Group the data by date and add total sales
    # for each day
    # ==========================================
    sales_by_date = df.groupby("date")["sales"].sum()

    # ==========================================
    # Create a line chart for sales trends over time
    # ==========================================
    plt.figure(figsize=(8, 5))
    plt.plot(sales_by_date.index, sales_by_date.values, marker="o")
    plt.title("Sales Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # ==========================================
    # Group the data by product and add total sales
    # for each product
    # ==========================================
    sales_by_product = df.groupby("product")["sales"].sum()

    # ==========================================
    # Create a bar chart for total sales by product
    # ==========================================
    plt.figure(figsize=(8, 5))
    plt.bar(sales_by_product.index, sales_by_product.values, color="skyblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

    # ==========================================
    # Create a histogram to show the distribution
    # of sales values
    # ==========================================
    plt.figure(figsize=(8, 5))
    plt.hist(df["sales"], bins=5, color="orange", edgecolor="black")
    plt.title("Distribution of Sales Values")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ==========================================
# Handle the error if the file is missing
# ==========================================
except FileNotFoundError:
    print("Error: sales_data.csv was not found.")

# ==========================================
# Handle other possible errors
# ==========================================
except Exception as e:
    print("An error occurred:", e)