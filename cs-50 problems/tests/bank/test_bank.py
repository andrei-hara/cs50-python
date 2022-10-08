from bank import value

def test_good_greeting():
    assert value("hello") == 0

def test_acceptable_greeting():
    assert value("hi") == 20
    assert value("hey") == 20

def test_bad_greeting():
    assert value("Good morning") == 100

def test_numbers():
    assert value("12") == 100

def test_punctuation():
    assert value("!!") == 100

def test_say_nothing():
    assert value("") == 100

def test_upper_case():
    assert value("Hi") == 20
    assert value("Hello") == 0