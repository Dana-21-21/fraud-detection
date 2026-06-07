import pandas as pd
import numpy as np


def create_time_features(df):

    df = df.copy()

    df["time_since_signup"] = (
        df["purchase_time"]
        - df["signup_time"]
    ).dt.total_seconds()

    df["hour_of_day"] = (
        df["purchase_time"].dt.hour
    )

    df["day_of_week"] = (
        df["purchase_time"].dt.dayofweek
    )

    return df


def create_user_transaction_count(df):

    df = df.copy()

    user_count = (
        df.groupby("user_id")
        .size()
    )

    df["user_transaction_count"] = (
        df["user_id"]
        .map(user_count)
    )

    return df


def create_device_transaction_count(df):

    df = df.copy()

    device_count = (
        df.groupby("device_id")
        .size()
    )

    df["device_transaction_count"] = (
        df["device_id"]
        .map(device_count)
    )

    return df


def map_country(fraud_df, ip_df):

    fraud_df = fraud_df.copy()

    fraud_df["ip_address"] = (
        fraud_df["ip_address"]
        .astype(np.int64)
    )

    ip_df["lower_bound_ip_address"] = (
        ip_df["lower_bound_ip_address"]
        .astype(np.int64)
    )

    ip_df["upper_bound_ip_address"] = (
        ip_df["upper_bound_ip_address"]
        .astype(np.int64)
    )

    fraud_df = fraud_df.sort_values(
        "ip_address"
    )

    ip_df = ip_df.sort_values(
        "lower_bound_ip_address"
    )

    merged = pd.merge_asof(
        fraud_df,
        ip_df,
        left_on="ip_address",
        right_on="lower_bound_ip_address",
        direction="backward"
    )

    merged = merged[
        merged["ip_address"]
        <= merged["upper_bound_ip_address"]
    ]

    return merged