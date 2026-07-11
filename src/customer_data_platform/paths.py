from pathlib import Path

#project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = DATA_DIR / "reports"
ARCHIVE_DIR = DATA_DIR / "archive"

# Dataset
ONLINE_RETAIL_DATASET = EXTERNAL_DATA_DIR / "online_retail_II.xlsx"