from working import convert
import pytest

def test_correct_val():
    assert convert("5 PM to 7 AM") == "17:00 to 07:00"
    assert convert("7:32 AM to 8:32 PM") == "07:32 to 20:32"
    assert convert("12:01 AM to 11:30 PM") == "00:01 to 23:30"

def test_incorrect_str():
    with pytest.raises(ValueError):
        convert("cat")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("12:02 AM - 1:35 PM")
    with pytest.raises(ValueError):
        convert("13.03 AM to 18.30 PM")

def test_incorrect_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("12 PM to 0 AM")
    with pytest.raises(ValueError):
        convert("13 PM to 17 AM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 8:60 PM")