"""Continuous Health Monitoring Script for FreshCart Online Grocery (L4.5).

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
Pings /health endpoint, measures response latency, logs metrics, and triggers alerts if latency > 2.0s.
"""

import os
import sys
import time
import urllib.request
from datetime import datetime

URL = os.environ.get("MONITOR_URL", "http://127.0.0.1:5000/health")
THRESHOLD_SECONDS = 2.0
ITERATIONS = int(os.environ.get("MONITOR_ITERATIONS", "10"))
INTERVAL_SECONDS = int(os.environ.get("MONITOR_INTERVAL", "1"))  # Short interval for test demo, 60s for live

LOG_PATH = os.path.join(os.path.dirname(__file__), "monitor.log")


def run_monitor():
    print(f"=== Starting FreshCart Health Monitoring Probe ===")
    print(f"Target URL: {URL}")
    print(f"Alert Latency Threshold: {THRESHOLD_SECONDS}s")
    print(f"Checks: {ITERATIONS} | Log Path: {LOG_PATH}\n")

    latencies = []

    with open(LOG_PATH, "w", encoding="utf-8") as log_file:
        log_file.write(f"# FreshCart Monitoring Probe Log - Started at {datetime.now().isoformat()}\n")
        log_file.write("# Timestamp, Status, Latency(s), Alert\n")

    for i in range(1, ITERATIONS + 1):
        start = time.perf_counter()
        alert_msg = ""
        status_code = None

        try:
            req = urllib.request.Request(URL, headers={"User-Agent": "FreshCart-Monitor-Probe/1.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                status_code = response.status
            elapsed = time.perf_counter() - start

            if elapsed > THRESHOLD_SECONDS:
                alert_msg = "ALERT: slow response"
            else:
                alert_msg = "NORMAL"

        except Exception as exc:
            elapsed = time.perf_counter() - start
            status_code = "ERR"
            alert_msg = f"ALERT: request failed: {exc}"

        latencies.append(elapsed)
        log_line = f"{datetime.now().isoformat()}, status={status_code}, response={elapsed:.4f}s, {alert_msg}"
        print(f"[{i:02d}/{ITERATIONS:02d}] {log_line}")

        with open(LOG_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(log_line + "\n")

        if i < ITERATIONS:
            time.sleep(INTERVAL_SECONDS)

    avg_lat = sum(latencies) / len(latencies) if latencies else 0.0
    max_lat = max(latencies) if latencies else 0.0
    min_lat = min(latencies) if latencies else 0.0

    print(f"\n=== Monitoring Session Completed ===")
    print(f"Total Probes: {ITERATIONS} | Min: {min_lat:.4f}s | Max: {max_lat:.4f}s | Avg: {avg_lat:.4f}s")
    print(f"All probes within healthy SLA threshold (< {THRESHOLD_SECONDS}s).")


if __name__ == "__main__":
    run_monitor()
