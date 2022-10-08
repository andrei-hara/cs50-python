from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_convert_value():
   with pytest.raises(ValueError):
        convert("3/cat")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"


