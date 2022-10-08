from numb3rs import validate

def test_upper_values():
    assert validate("256.1.1.1") == False
    assert validate("1.1.300.1") == False

def test_correct_values():
    assert validate("192.0.255.32") == True
    assert validate("0.192.1.0") == True

def test_incorrect_string():
    assert validate("cat") == False

def  test_negative_values():
    assert validate("-1.192.255.0") == False
    assert validate("0.1-32.234.1") == False
