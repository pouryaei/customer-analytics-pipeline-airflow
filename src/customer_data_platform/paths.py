from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FEATURES_DATA_DIR = DATA_DIR / "features"
MODELS_DIR = DATA_DIR / "models"
REPORTS_DIR = DATA_DIR / "reports"
ARCHIVE_DIR = DATA_DIR / "archive"

# Dataset
ONLINE_RETAIL_DATASET = EXTERNAL_DATA_DIR / "online_retail_II.xlsx"

# Ensure directories exist
for directory in (
    DATA_DIR,
    EXTERNAL_DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FEATURES_DATA_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    ARCHIVE_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)