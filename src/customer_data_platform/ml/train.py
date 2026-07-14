import logging

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from customer_data_platform.paths import MODELS_DIR

logger = logging.getLogger(__name__)


def prepare_training_data(input_file: str):

    df = pd.read_csv(input_file)

    logger.info("Loaded feature dataset with %s customers.", len(df))

    y = df["HighValueCustomer"]

    X = df.drop(
        columns=[
            "Customer ID",
            "HighValueCustomer",
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    logger.info(
        "Training samples: %s | Test samples: %s",
        len(X_train),
        len(X_test),
    )

    return X_train, X_test, y_train, y_test


def save_model(model) -> str:

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    output_file = MODELS_DIR / "customer_classifier.joblib"

    joblib.dump(model, output_file)

    logger.info("Saved trained model to %s", output_file)

    return str(output_file)


def train_model(input_file: str) -> str:

    X_train, X_test, y_train, y_test = prepare_training_data(input_file)

    model = RandomForestClassifier(random_state=42)

    model.fit(X_train, y_train)

    logger.info("Model training completed successfully.")

    model_path = save_model(model)

    return model_path