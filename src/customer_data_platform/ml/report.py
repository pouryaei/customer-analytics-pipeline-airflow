import logging

from customer_data_platform.paths import REPORTS_DIR

logger = logging.getLogger(__name__)


def save_classification_report(report: str) -> str:
    output_file = REPORTS_DIR / "classification_report.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    logger.info("Saved classification report to %s", output_file)

    return str(output_file)