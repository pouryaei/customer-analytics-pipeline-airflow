import logging

logger = logging.getLogger(__name__)


def validate_customers(customers: list[dict]) -> list[dict]:
    """
    Validate extracted customer records.

    Args:
        customers: Customer records.

    Returns:
        Validated customer records.
    """

    logger.info("Starting customer validation.")

    if not customers:
        raise ValueError("No customer records found.")

    logger.info("Customer validation completed.")

    return customers