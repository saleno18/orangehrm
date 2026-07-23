"""
Central logging configuration.
Every test-case execution result is logged to both the console and a
rotating log file under reports/, satisfying the project requirement
that "each test case execution must include logging of results."
"""

import logging
import os

LOG_DIR = "reports"
LOG_FILE = os.path.join(LOG_DIR, "execution.log")


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger that writes to console + reports/execution.log."""
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)
    if logger.handlers:  # avoid duplicate handlers on repeated calls
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
