
import pandas as pd
import os

# Load original dataset
df = pd.read_csv("data/raw/olist_orders_dataset.csv")

print("Original Dataset Shape:", df.shape)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. Convert date columns into datetime format
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(
        df[col], errors="coerce"
    )

# 3. Normalize text values
df["order_status"] = (
    df["order_status"]
    .astype("string")
    .str.strip()
    .str.lower()
)

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Check duplicate order IDs
print("\nDuplicate Order IDs:",
      df["order_id"].duplicated().sum())

# 6. Identify invalid delivery dates
invalid_dates = df[
    df["order_delivered_customer_date"].notna()
    & df["order_purchase_timestamp"].notna()
    & (
        df["order_delivered_customer_date"]
        < df["order_purchase_timestamp"]
    )
]

print("\nInvalid Delivery Records:", len(invalid_dates))

# 7. Create cleaned data folder
os.makedirs("data/cleaned", exist_ok=True)

# 8. Save cleaned dataset
df.to_csv(
    "data/cleaned/cleaned_orders.csv",
    index=False
)

# 9. Save data quality report
quality_report = pd.DataFrame({
    "Column": df.columns,
    "Missing_Values": df.isnull().sum().values
})

quality_report.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print("\nCleaning Completed Successfully!")
print("Cleaned Dataset Shape:", df.shape)
