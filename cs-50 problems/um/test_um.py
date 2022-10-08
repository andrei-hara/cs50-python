from um import count

def test_case_insensitivity():
    assert count("Um, um") == 2

def test_substrings():
    assert count("Um, hello, dummy") == 1
    assert count("Um, thanks for the album") == 1

def test_begin_um():
    assert count("um um ummy") == 2

def test_end_um():
    assert count("um, dum") == 1