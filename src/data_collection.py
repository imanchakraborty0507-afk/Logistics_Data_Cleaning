import pandas as pd

# Load the logistics orders dataset
orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

# Display first five records
print("First five records:")
print(orders.head())

# Display dataset information
print("\nDataset Information:")
print(orders.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(orders.shape)

# Display column names
print("\nColumn Names:")
print(orders.columns)

# Display missing values
print("\nMissing Values:")
print(orders.isnull().sum())
