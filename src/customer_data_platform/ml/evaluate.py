import logging
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score

logger = logging.getLogger(__name__)

def evaluate_model(model, X_test, y_test) -> dict:
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    logger.info("Accuracy : %.4f", accuracy)
    logger.info("Precision: %.4f", precision)
    logger.info("Recall   : %.4f", recall)
    logger.info("F1 Score : %.4f", f1)
    logger.info("\n%s", report)

    return {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1,
    "classification_report": report}