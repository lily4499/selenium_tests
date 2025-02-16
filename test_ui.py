import os
#import time
from selenium import webdriver

def test_homepage():
    # Get Selenium Grid URL from environment variable or default value
    selenium_hub_url = os.getenv("SELENIUM_HUB_URL", "http://a0602369809b44851b05f02c7ed7c9d4-806899473.us-east-1.elb.amazonaws.com/wd/hub")
    app_url = os.getenv("APP_URL", "http://a3cc31262ab454f429c4933a6d0ecbd0-1161205187.us-east-1.elb.amazonaws.com//")  # Use service name in K8s

    # Set up Chrome options for Selenium Grid
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=selenium_hub_url,
        options=chrome_options
    )

    try:
        # Navigate to Online Boutique frontend
        driver.get(app_url)

        # Validate title
        expected_title = "Ecommerce Online Boutique"
        actual_title = driver.title
        print(f"Actual Title: {actual_title}")

        assert expected_title in actual_title, f"Expected title '{expected_title}' not found in '{actual_title}'"

    finally:
        # Ensure the browser session is always closed
        driver.quit()