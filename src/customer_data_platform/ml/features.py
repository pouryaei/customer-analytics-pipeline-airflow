import logging
import pandas as pd
from customer_data_platform.paths import FEATURES_DATA_DIR

logger = logging.getLogger(__name__)

def prepare_features(input_file: str):
    logger.info("Loading processed dataset...")

    df = pd.read_csv(input_file)

    logger.info("Dataset contains %s rows.", len(df))

    df = df.dropna(subset=["Customer ID"])
    df["TotalPrice"] = df["Quantity"] * df["Price"]

    customer_df = df.groupby("Customer ID").agg(
        TotalSpend=("TotalPrice", "sum"),
        TotalOrders=("Invoice", "nunique"),
        TotalItems=("Quantity", "sum")).reset_index()
    
    customer_df["AvgOrderValue"] = customer_df["TotalSpend"] / customer_df["TotalOrders"]

    threshold = customer_df["TotalSpend"].quantile(0.75)
    customer_df["HighValueCustomer"] = (customer_df["TotalSpend"] >= threshold).astype(int)
    
    logger.info("High value customer threshold: %.2f", threshold)
    
    logger.info("Created TotalPrice feature for %s records.", len(df))

    logger.info("Created customer-level dataset with %s customers.", len(customer_df))

    
    output_file = FEATURES_DATA_DIR / "customer_features.csv"
    customer_df.to_csv(output_file, index=False)

    logger.info("Saved feature dataset to %s", output_file)

    return str(output_file)