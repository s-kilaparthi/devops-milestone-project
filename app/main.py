

def add(a,b):
    return a + b

def is_secure(port):
    dangerous_ports = [22, 3389, 0]
    return port not in dangerous_ports

if __name__ == "__main__":
    print ("App running")
    print (f"port 22 secure : { is_secure(22)}")
    print (f"port 443 secure : {is_secure(443)}")
