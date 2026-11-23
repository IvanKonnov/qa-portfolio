def is_strong_password(password):
    return len(password) >= 8

def test_good_password():
    assert is_strong_password("12345678") == True

def test_short_password():
    assert is_strong_password("123") == False