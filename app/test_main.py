
from main import add, is_secure

def test_add():
    assert add(2, 3) == 5

def test_secure_port():
    assert is_secure(443) == True

def test_secure_port():
    assert is_secure(22) == False




















