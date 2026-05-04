#!/usr/bin/env python3
import sys

def classify_failure(log_text):
    log = log_text.lower()
    
    if "timeout" in log or "connection refused" in log:
        return "NETWORK_ERROR", "RETRY"
    elif "flake" in log or "random" in log:
        return "FLAKY_TEST", "RETRY"
    elif "syntax error" in log or "compilation failed" in log:
        return "CODE_ERROR", "ALERT_ONLY"
    elif "cannot connect to docker" in log:
        return "DOCKER_ERROR", "RETRY"
    elif "exit code 137" in log:
        return "OOM_ERROR", "RETRY_WITH_MORE_MEMORY"
    else:
        return "UNKNOWN", "ALERT_ONLY"

if __name__ == "__main__":
    log = sys.stdin.read()
    failure_type, action = classify_failure(log)
    print(f"{failure_type}|{action}")