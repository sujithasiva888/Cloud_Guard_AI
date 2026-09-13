import os
import random
import time
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="CloudGuard AI - Enterprise")

class UserLogin(BaseModel):
    username: str
    password: str

class CodeSubmission(BaseModel):
    code: str
    server_type: str

# IAM User Accounts Mapping Database
VALID_CREDENTIALS = {
    "dev_user": {"password": "devpassword", "role": "developer"},
    "test_user": {"password": "testpassword", "role": "tester"}
}

SERVER_RATES = {
    "t2.micro (Low-Cost Sandbox)": 1.25,
    "m5.large (Standard Compute)": 12.50,
    "g4dn.xlarge (Heavy AI Cluster)": 48.00
}

@app.get("/", response_class=HTMLResponse)
async def serve_portal():
    # Fixed absolute path routing to look inside your templates folder automatically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "templates", "index.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/login")
async def process_auth_routing(user: UserLogin):
    if user.username in VALID_CREDENTIALS and VALID_CREDENTIALS[user.username]["password"] == user.password:
        return {
            "status": "authenticated",
            "role": VALID_CREDENTIALS[user.username]["role"],
            "token": f"mock_secure_token_{random.randint(1000,9999)}"
        }
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid IAM Credentials")

@app.post("/api/scan")
async def scan_and_execute(submission: CodeSubmission):
    user_code = submission.code
    spec = submission.server_type
    
    routing_path = ["Pipeline Ingested", "Amazon Bedrock Static Analysis Active"]
    
    has_leak = "AWS_ACCESS_KEY" in user_code or "secret" in user_code.lower()
    has_loop = "while True" in user_code or "while(true)" in user_code or "Loop" in user_code
    
    security_alert = "SAFE"
    if has_leak:
        security_alert = "CRITICAL BLOCK: Hardcoded Infrastructure Key Leak Detected!"
    elif has_loop:
        security_alert = "WARNING FLAG: Destructive Infinite Processing Pattern Caught."

    routing_path.append("AWS Lambda Metrics Compilation Injected")
    base_modifier = SERVER_RATES.get(spec, 1.0)
    simulated_cost = 0.0
    circuit_breaker_triggered = False
    
    for step in range(1, 6):
        if circuit_breaker_triggered:
            break
        time.sleep(0.02)
        if has_loop:
            simulated_cost += (random.uniform(25.0, 38.0) * base_modifier * 0.5)
        else:
            simulated_cost += (random.uniform(0.5, 1.8) * base_modifier * 0.1)
            
        if simulated_cost >= 100.0:
            circuit_breaker_triggered = True
            routing_path.append("Autonomous Guard Circuit Breaker Intervention Engaged")

    status = "HALTED_BY_GOVERNANCE" if circuit_breaker_triggered else "STABLE_DEPLOYMENT"
    routing_path.append(f"State Finalized: {status}")

    return {
        "security_alert": security_alert,
        "estimated_cost": round(simulated_cost, 2),
        "circuit_breaker": circuit_breaker_triggered,
        "routing_path": " ➔ ".join(routing_path),
        "status": status
    }
