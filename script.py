#!/usr/bin/env python3

from pathlib import Path

import requests


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict object with values."""

    config_dict = {}

    return config_dict


def load_db(db_path: Path) -> list:
    """Parse database and return content as a list of dict."""

    data = []

    return data


def check_if_pwned(api_url: str, passwd: str) -> int:
    """Check password hash again HIBP API and return result."""

    pwned = 0

    return pwned


def main():
    """Check each user password against HIBP API."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))
    users = load_db(config["db"]["path"])
    for user in users:
        count = check_if_pwned(config["api"]["url"], user["password"])


if __name__ == "__main__":
    main()
