"""
LOGGING CONFIG
logging setup in one place, so clean and reusable.
"""

import logging
import os
from app.config.settings import LOG_FILE


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # if already configured, do nothing
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # auto create logs folder
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    console_handler = logging.StreamHandler()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    file_handler.setFormatter(fmt)
    console_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
