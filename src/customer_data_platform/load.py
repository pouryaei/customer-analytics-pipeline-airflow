import pandas as pd
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

def load_customer_data(input_file: str):

    df = pd.read_csv(input_file)

    engine = create_engine(
        "postgresql+psycopg://postgres:postgres@localhost:5432/customer_analytics"
    )

    df.to_sql(
        name="customers_raw",
        con=engine,
        if_exists="replace",
        index=False,
    )

    logger.info("Loaded %s rows into PostgreSQL.", len(df))