import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook
import logging

logger = logging.getLogger(__name__)

def load_customer_data(input_file: str):

    hook = PostgresHook(postgres_conn_id="postgres_customer_analytics")
    df = pd.read_csv(input_file)

    engine = hook.get_sqlalchemy_engine()

    df.to_sql(
    name="customers_raw",
    con=engine,
    if_exists="replace",
    index=False,
    )

    logger.info("Loaded %s rows into PostgreSQL.", len(df))