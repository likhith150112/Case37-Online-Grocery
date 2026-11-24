"""Automated execution, monitoring, and screenshot capture script for FreshCart (Case 37).

Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

import os
import subprocess
import sys
import threading
import time
import urllib.request

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grocery_app.app import app

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_URL = "http://127.0.0.1:5000"
SCREENSHOTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "screenshots"))
LOGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "execution_logs"))

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)


def start_flask_server():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


def wait_for_server():
    for _ in range(30):
        try:
            with urllib.request.urlopen(f"{BASE_URL}/health", timeout=1) as resp:
                if resp.status == 200:
                    print("Flask server is live and responding on port 5000.")
                    return True
        except Exception:
            time.sleep(0.5)
    return False


def capture_screenshot(url, output_path, delay=2):
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1280,900",
        f"--screenshot={output_path}",
        url,
    ]
    try:
        subprocess.run(cmd, check=True, timeout=15)
        print(f"Captured: {os.path.basename(output_path)}")
        return True
    except Exception as exc:
        print(f"Failed to capture {output_path}: {exc}")
        return False


def run_pipeline():
    # 1. Start server in thread
    t = threading.Thread(target=start_flask_server, daemon=True)
    t.start()

    if not wait_for_server():
        print("Failed to start Flask server.")
        return

    # Seed an order if needed for confirmation screen
    client = app.test_client()
    client.post("/cart/add", data={"sku": "MIL-001", "quantity": 2})
    client.post("/order/place", data={
        "customer_name": "Likhith Gowda M S",
        "phone": "9876543210",
        "address": "No. 37, 5th Main, Kumaraswamy Layout, Bengaluru",
        "slot_id": "1",
        "dietary_preference": "Standard"
    })

    # 2. Capture Screenshots
    screenshots = [
        (f"{BASE_URL}/", os.path.join(SCREENSHOTS_DIR, "01_catalog_home.png")),
        (f"{BASE_URL}/demo/cart", os.path.join(SCREENSHOTS_DIR, "02_cart_out_of_stock.png")),
        (f"{BASE_URL}/demo/substitutions", os.path.join(SCREENSHOTS_DIR, "03_substitution_engine.png")),
        (f"{BASE_URL}/demo/checkout", os.path.join(SCREENSHOTS_DIR, "04_checkout_slot_selection.png")),
        (f"{BASE_URL}/demo/confirmation", os.path.join(SCREENSHOTS_DIR, "05_order_confirmation.png")),
        (f"{BASE_URL}/health", os.path.join(SCREENSHOTS_DIR, "06_health_check_json.png")),
    ]

    print("\nCapturing Application Screenshots with Headless Chrome...")
    for url, path in screenshots:
        capture_screenshot(url, path)

    # 3. Run Monitoring Checks
    print("\nExecuting Continuous Health Monitoring Probes (10 Checks)...")
    monitor_log_file = os.path.join(LOGS_DIR, "monitor.log")
    with open(monitor_log_file, "w", encoding="utf-8") as log:
        log.write("# FreshCart Real Monitoring Probe Log\n# Timestamp, Status, Latency(s), Note\n")
        for i in range(1, 11):
            t0 = time.perf_counter()
            with urllib.request.urlopen(f"{BASE_URL}/health", timeout=5) as r:
                code = r.status
            elapsed = time.perf_counter() - t0
            line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')}, status={code}, response={elapsed:.4f}s, NORMAL"
            print(f"Probe {i:02d}/10: {line}")
            log.write(line + "\n")
            time.sleep(0.5)

    print("\nAll monitoring and screenshot captures completed successfully!")


if __name__ == "__main__":
    run_pipeline()

