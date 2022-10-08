from seasons import validate_format, convert_minutes
import pytest


def test_correct_dates():
    assert validate_format("2005-12-31") == True
    assert validate_format("1999-06-01") == True

def test_bisect_years():
    assert validate_format("1968-02-29") == True

def test_invalid_days():
    with pytest.raises(SystemExit):
        validate_format("2005-12-32")
        validate_format("1999-06-31")

def test_invalid_months():
    with pytest.raises(SystemExit):
        validate_format("2005-13-30")
        validate_format("1999-25-12")

def test_invalid_years():
    with pytest.raises(SystemExit):
        convert_minutes("2025-12-10")