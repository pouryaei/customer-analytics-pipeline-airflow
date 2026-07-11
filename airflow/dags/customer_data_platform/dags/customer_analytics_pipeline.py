from datetime import datetime

from airflow.sdk import dag, task

from customer_data_platform.extract import extract_customer_data
from customer_data_platform.transform import transform_customer_data
from customer_data_platform.validate import validate_customer_data
from customer_data_platform.load import load_customer_data


@dag(
    dag_id="customer_analytics_pipeline",
    start_date=datetime(2026, 7, 10),
    schedule=None,
    catchup=False,
    tags=["customer", "analytics", "production"],
)
def customer_analytics_pipeline():

    @task
    def extract_data():
        return extract_customer_data()

    @task
    def transform_data(csv_path):
        return transform_customer_data(csv_path)

    @task
    def validate_data(df):
        validate_customer_data(df)
        return df

    @task
    def load_data(df):
        load_customer_data(df)

    raw_file = extract_data()

    processed_file = transform_data(raw_file)

    validated_file = validate_data(processed_file)

    load_data(validated_file)


customer_analytics_pipeline()