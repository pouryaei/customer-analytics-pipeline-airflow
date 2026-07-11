import pandas as pd
import logging
from customer_data_platform.paths import PROCESSED_DATA_DIR

logger = logging.getLogger(__name__)

def transform_customer_data(input_file: str):

    df = pd.read_csv(input_file)

    logger.info("Rows before transform: %s", len(df))

    df = df.drop_duplicates()

    logger.info("Rows after transform: %s", len(df))

    output_file = PROCESSED_DATA_DIR / "customer_processed.csv"

    df.to_csv(output_file, index=False)

    return str(output_file)