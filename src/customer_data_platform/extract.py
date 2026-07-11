import pandas as pd
import logging
from customer_data_platform.paths import ONLINE_RETAIL_DATASET, RAW_DATA_DIR

logger = logging.getLogger(__name__)

def extract_customer_data():

    output_file = RAW_DATA_DIR / "customer_raw.csv"

    df = pd.read_excel(ONLINE_RETAIL_DATASET)

    df.to_csv(output_file, index=False)

    logger.info("Extracted %s rows", len(df))

    return str(output_file)