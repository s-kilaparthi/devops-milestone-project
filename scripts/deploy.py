import subprocess
import datetime
import json
import os
import sys

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def check_environment():
    log("Checking environment variables...")
    required_vars = ["APP_ENV", "APP_PORT"]
    missing = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing.append(var)
    
    if missing:
        log(f"WARNING: Missing environment variables: {missing}")
        log("Stopping deployment — fix config before retrying.")
        sys.exit(1)  # hard stop, don't continue

    
    log("Environment check passed ✅")
    return True

def run_tests():
    log("Running automated tests...")
    result = subprocess.run(
        ["python3", "-m", "pytest", "app/test_main.py", "-v"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        log("All tests passed ✅")
        return True
    else:
        log("Tests FAILED ❌")
        log(result.stdout)
        return False

def generate_report(env_ok, tests_ok):
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "environment_check": "PASSED" if env_ok else "FAILED",
        "test_results": "PASSED" if tests_ok else "FAILED",
        "deployment_status": "SUCCESS" if (env_ok and tests_ok) else "BLOCKED"
    }
    
    with open("deployment_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    
    log(f"Deployment report saved → deployment_report.json")
    return report

def deploy():
    log("=== Starting Deployment Pipeline ===")
    
    env_ok = check_environment()
    tests_ok = run_tests()
    report = generate_report(env_ok, tests_ok)
    
    if report["deployment_status"] == "SUCCESS":
        log("=== Deployment SUCCESS ✅ ===")
    else:
        log("=== Deployment BLOCKED ❌ — fix issues before deploying ===")

if __name__ == "__main__":
    deploy()
