#!/usr/bin/env python3

from pathlib import Path

import script


def test_load_config_type():
    """Test that it return the expect object type."""

    config = script.load_config()

    assert isinstance(config, dict)


def test_config_api():
    """Test that configuration contains an api section and options."""

    config = script.load_config()

    assert "api" in config
    assert "url" in config["api"]


def test_config_db():
    """Test that configuration contains an db section and options."""

    config = script.load_config()

    assert "db" in config
    assert "driver" in config["db"]
    assert "path" in config["db"]


def test_load_db_csv(tmpdir):
    """Test that database is loadable and return the expect object."""

    db_path = Path(tmpdir, "db.csv")
    db_data = "login;password\ntest;7c4a8d09ca3762af61e59520943dc26494f8941b"
    with open(db_path, "w") as fo:
        fo.write(db_data)

    data = script.load_db(db_path, "csv")

    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    assert data[0]["login"] == "test"
    assert data[0]["password"] == "7c4a8d09ca3762af61e59520943dc26494f8941b"


def test_check_if_pwned(respx_mock):
    """Test that request results are correctly interpreted."""

    api_url = "https://api.pwnedpasswords.com/range"
    passwd = "76e4b28b5527652fd7af9a57e17f6adce5bbba78"
    prefix = passwd[:5]
    suffix = passwd[5:]
    route = respx_mock.get(f"{api_url}/{prefix}").respond(text=f"{suffix}:30\n")

    results = script.check_if_pwned(api_url, passwd)

    assert route.called
    assert results == 30


def test_check_if_pwned_not_found(respx_mock):
    """Test that request results are correctly interpreted if not found."""

    api_url = "https://api.pwnedpasswords.com/range"
    passwd = "76e4b28b5527652fd7af9a57e17f6adce5bbba78"
    prefix = passwd[:5]
    route = respx_mock.get(f"{api_url}/{prefix}").respond(text="")

    results = script.check_if_pwned(api_url, passwd)

    assert route.called
    assert results == 0
