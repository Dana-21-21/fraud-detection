import pandas as pd


def load_data(filepath):
    """
    Load a CSV file safely.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded: {filepath}")
        return df

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None


def clean_fraud_data(df):
    """
    Clean fraud dataset.
    """

    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert datetime columns
    df["signup_time"] = pd.to_datetime(
        df["signup_time"],
        errors="coerce"
    )

    df["purchase_time"] = pd.to_datetime(
        df["purchase_time"],
        errors="coerce"
    )

    return df


def clean_creditcard_data(df):
    """
    Clean credit card dataset.
    """

    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    return df