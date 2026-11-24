"""End-to-End Selenium Test Automation for FreshCart Online Grocery (Task D & L4.3).

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
Automates: Catalog browse -> Add out-of-stock item -> Substitution review -> Accept -> Slot selection -> Order confirmation.
"""

import os
import sys
import time

def run_selenium_headless_order_flow(base_url="http://127.0.0.1:5000"):
    """Execute end-to-end browser automation flow using Selenium with Chrome."""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        print(f"[Selenium] Navigating to {base_url}...")
        driver.get(base_url)
        wait.until(EC.visibility_of_element_located((By.ID, "search")))
        print("[Selenium] Home catalog loaded successfully.")

        # Step 1: Search for 'milk'
        search_box = driver.find_element(By.ID, "search")
        search_box.clear()
        search_box.send_keys("milk")
        search_box.submit()
        time.sleep(1)
        print("[Selenium] Search for 'milk' completed.")

        # Step 2: Add out-of-stock item (MIL-002: Amul Taaza)
        add_btn = driver.find_element(By.ID, "add-to-cart-MIL-002")
        add_btn.click()
        time.sleep(1)
        print("[Selenium] Added out-of-stock item MIL-002 to cart.")

        # Step 3: Navigate to Cart
        driver.get(f"{base_url}/cart")
        wait.until(EC.visibility_of_element_located((By.ID, "cart-count")))
        print("[Selenium] Cart page loaded with out-of-stock alert.")

        # Step 4: Click Review Substitutions
        sub_btn = driver.find_element(By.ID, "review-substitutions-btn")
        sub_btn.click()
        time.sleep(1)
        print("[Selenium] Navigated to Substitution Review page.")

        # Step 5: Accept the suggested substitute (MIL-001: Nandini Milk)
        accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "accept-substitute-MIL-002")))
        accept_btn.click()
        time.sleep(1)
        print("[Selenium] Accepted intelligent substitution!")

        # Step 6: Proceed to Checkout
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
        time.sleep(1)
        print("[Selenium] Checkout page reached.")

        # Step 7: Select delivery slot and place order
        slot_radio = driver.find_element(By.ID, "slot-1")
        if not slot_radio.is_selected():
            slot_radio.click()

        confirm_btn = driver.find_element(By.ID, "confirm-order-btn")
        confirm_btn.click()
        time.sleep(1)

        # Step 8: Verify Order Confirmation
        wait.until(EC.visibility_of_element_located((By.ID, "order-confirmation")))
        print("[Selenium] Order successfully confirmed and verified in browser!")
        return True

    finally:
        driver.quit()


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"
    success = run_selenium_headless_order_flow(url)
    print("Selenium Order Flow Result:", "SUCCESS" if success else "FAILED")
