from fastapi import FastAPI
import uvicorn

app = FastAPI()

def add(a, b):
    return a + b

def is_secure(port):
    dangerous_ports = [22, 3389, 0]
    return port not in dangerous_ports

@app.get("/")
def home():
    return {"status": "running", "message": "DevOps Milestone Project"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/check-port/{port}")
def check_port(port: int):
    secure = is_secure(port)
    return {
        "port": port,
        "secure": secure,
        "message": "Port is safe" if secure else "DANGER: Port is exposed"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
