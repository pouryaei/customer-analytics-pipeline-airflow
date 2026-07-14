import logging
import mlflow
import mlflow.sklearn

logger = logging.getLogger(__name__)


def setup_experiment():
    mlflow.set_experiment("customer_analytics_pipeline")

    logger.info("MLflow experiment configured successfully.")


def log_experiment(model, metrics: dict, report_file: str):
    with mlflow.start_run():
        logger.info("Started MLflow run.")

        mlflow.log_param("algorithm", "RandomForest")
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.20)

        logger.info("Logged MLflow parameters.")

        mlflow.log_metric("accuracy", metrics["accuracy"])
        mlflow.log_metric("precision", metrics["precision"])
        mlflow.log_metric("recall", metrics["recall"])
        mlflow.log_metric("f1_score", metrics["f1_score"])

        logger.info("Logged evaluation metrics.")

        mlflow.sklearn.log_model(sk_model=model, name="customer_classifier")

        logger.info("Logged trained model.")

        mlflow.log_artifact(report_file)

        logger.info("Logged classification report.")

