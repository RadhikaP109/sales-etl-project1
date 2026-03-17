import pandas as pd

def transform_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Calculate total amount
    df["total_amount"] = df["quantity"] * df["price"]

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    return df