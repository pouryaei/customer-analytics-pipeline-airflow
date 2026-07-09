import logging

logger = logging.getLogger(__name__)


def extract_customers() -> list[dict]:
    """
    Extract customer records.

    Returns:
        A list of customer records.
    """

    logger.info("Starting customer extraction.")

    customers = [
        {
            "customer_id": "C001",
        },
        {
            "customer_id": "C002",
        },
    ]

    logger.info("Customer extraction completed.")

    return customers