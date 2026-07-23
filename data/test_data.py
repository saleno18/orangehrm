

import csv
import os


def load_login_data(csv_path: str = "data/login_data.csv"):

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Login data source not found: {csv_path}")

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]

    if not rows:
        raise ValueError(f"Login data source '{csv_path}' is empty.")

    return rows
