from plates import is_valid

def test_length():
    assert is_valid("s") == False
    assert is_valid("sdartyh") == False
    assert is_valid("sdfg") == True

def test_first_letters():
    assert is_valid("f2ds") == False
    assert is_valid("2xd") == False

def test_first_number():
    assert is_valid("asd04") == False

def test_last_numbers():
    assert is_valid("fd532") == True
    assert is_valid("fd53e") == False

def test_empty_plate():
    assert is_valid("") == False

def test_punctuation_marks():
    assert is_valid("asd!2") == False



