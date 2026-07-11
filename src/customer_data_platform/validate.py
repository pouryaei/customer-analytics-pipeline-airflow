import logging
import pandas as pd

logger = logging.getLogger(__name__)


def validate_customer_data(input_file: str):

    df = pd.read_csv(input_file)
    logger.info("Rows: %s", len(df))

    logger.info("Columns: %s", len(df.columns))

    logger.info("Missing Values:\n%s", df.isnull().sum())

    logger.info("Data Types:\n%s", df.dtypes)

    logger.info("Validation completed.")

    return input_file