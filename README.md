# 🏆 CloudGuard AI 
### *Intelligent Runtime Cost & Security Circuit Breaker for AWS Cloud Beginners*

CloudGuard AI is an automated, proactive cloud governance system built for freshers and student developers. It acts as an autonomous sandbox guardian that scans execution patterns and enforces **real-time runtime halting** to prevent runaway cloud bills and critical credential exposures before they impact production environments.

---

## 🎯 The Core Problem & Innovation Space
Current enterprise cloud optimization architectures suffer from a critical operational flaw:
* **Delayed Budget Telemetry:** AWS Budgets alerts take **4 to 8 hours** to process billing logs. For an infinite execution loop triggered by a fresher, a multi-thousand-dollar bill is generated before the notification email arrives.
* **Static Scanning Deficiencies:** Existing IDE linters flag hardcoded strings but lack runtime execution context, failing to evaluate dynamic loops or deep structural token inflation.

**Our Solution:** CloudGuard AI bridges this gap by introducing an **Intelligent AI Circuit Breaker** that bridges static context evaluation with active, millisecond-level runtime threshold enforcement.

---

## 🚀 Core Features Matrix

### 🔐 1. Layer-1: Proactive AI Security Gatekeeper
* **Credential Protection:** Scans live deployment payloads for hardcoded cloud credentials (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) using simulated Amazon Bedrock/Nova reasoning layers.
* **Instant Risk Flagging:** Immediately blocks execution pipelines if insecure authorization tokens are present, protecting repositories from immediate bot scrapers.

### 📉 2. Layer-2: Live Compute Metric Tracking Engine
* **Predictive Pricing Telemetry:** Continuously evaluates the incoming code structure to simulate active resource consumption footprints on AWS Lambda.
* **Dynamic Visualization:** Pipes real-time cost accumulations down to a centralized developer dashboard, showing the active cost processing path instantly.

### 🛑 3. Layer-3: Autonomous Circuit Breaker Intervention
* **Hard Threshold Halting:** Monitors the execution runtime against strict pre-configured budget constraints (e.g., Max threshold limit of ₹100).
* **System Interception:** If a toxic loop causes costs to spike, it simulates an automated AWS Lambda pause routine, freezing the microservice state safely without destroying persistent application parameters.

---

## 🌐 Technical Architecture Flow
```text
[ USER CONSOLE UI ] 
       │
       ▼ (Passes Code Payload via HTTP POST)
[ FastAPI Unified Backend Platform ]
       │
       ├───► [ Layer 1: Amazon Bedrock Security Scanner ] ➔ Flags Leaks & Logic Traps
       │
       └───► [ Layer 2: Telemetry Simulation Engine ]     ➔ Computes Live Cost Increments
               │
               ▼ (Automated Execution Check: Cost > Threshold)
[ AWS Lambda Runtime Circuit Breaker Intercept ] ➔ Freezes Microservice Script Globally
       │
       ▼ (Pipes Analytics Matrix)
[ LIVE METRICS DASHBOARD VIEW ] ➔ Renders Final State & Financial Protection Logs
```

---

## 💻 Tech Stack Configuration
* **Backend Framework:** FastAPI (Asynchronous Python Web Server Architecture)
* **AI Engine Framework:** Automated Mock Pipeline mapping Amazon Bedrock / AWS Nova interfaces
* **Execution Environment:** Mock AWS Lambda Event Processing loop
* **Frontend Controller:** Asynchronous JavaScript Fetch API with Semantic CSS3 Component views

---

## ⚡ Deployment & Verification Steps

### 1. Initialize Root Environment Setup
Ensure Python 3.10+ is actively installed on your local host system. Clone the workspace files and run dependency synchronization:
```bash
python -m pip install fastapi uvicorn jinja2 pydantic boto3
```

### 2. Launch Local Server Instantiation
Execute the localized asynchronous web server pipeline interface:
```bash
python -m uvicorn main:app --reload
```

### 3. Verify Operational Functionality
Navigate your web client browser to `http://127.0.0.1:8000` to execute verification loops:
* **Scenario A (Token Protection):** Input `AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"` and trigger execution to view immediate security blocks.
* **Scenario B (Financial Guard):** Input `while True: print("Run")` to observe real-time cost throttling and circuit breaker isolation.
