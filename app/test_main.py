from main import add, is_secure

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_secure_port():
    assert is_secure(443) == True

def test_secure_port_80():
    assert is_secure(80) == True

def test_dangerous_port_ssh():
    assert is_secure(22) == False

def test_dangerous_port_rdp():
    assert is_secure(3389) == False
















