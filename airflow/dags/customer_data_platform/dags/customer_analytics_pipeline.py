from datetime import datetime

from airflow.sdk import dag, task

from customer_data_platform.extract import extract_customer_data
from customer_data_platform.transform import transform_customer_data
from customer_data_platform.validate import validate_customer_data
from customer_data_platform.load import load_customer_data
from customer_data_platform.ml.features import prepare_features
from customer_data_platform.ml.train import train_model
import logging

logger = logging.getLogger(__name__)

print("########### VERSION 999 ###########")
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
    def validate_data(processed_file):
        logger.info("validate_data received: %s", processed_file)
        validate_customer_data(processed_file)
        return processed_file

    @task
    def load_data(processed_file):
        load_customer_data(processed_file)

    @task
    def feature_engineering(processed_file):
        logger.info("feature_engineering received: %s", processed_file)
        return prepare_features(processed_file)
    
    @task
    def train_model_task(feature_file):
        return train_model(feature_file)


    raw_file = extract_data()

    processed_file = transform_data(raw_file)

    validated_file = validate_data(processed_file)

    loaded = load_data(validated_file)

    feature_file = feature_engineering(validated_file)

    trained_model = train_model_task(feature_file)

customer_analytics_pipeline()