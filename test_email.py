def is_valid_email(email):
    return "@" in email and "." in email and len(email) >= 5

def test_valid_email():
    assert is_valid_email("ivan@gmail.com") == True

def test_invalid_email():
    assert is_valid_email("ivan") == False

def test_email_without_at():
    assert is_valid_email("ivan.gmail.com") == False

def test_email_without_dot():
    assert is_valid_email("ivan@gmailcom") == False

def test_email_too_short():
    assert is_valid_email("a@b.") == False