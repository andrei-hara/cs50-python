from twttr import shorten

def test_vowels():
    assert shorten("hara") == "hr"
    assert shorten("vowels") == "vwls"

def test_upperCase():
    assert shorten("HARA") == "HR"
    assert shorten("VOWELS") == "VWLS"

def test_emptyString():
    assert shorten("") == ""

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("!,.';") == "!,.';"



