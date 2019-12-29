from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument("--disable-local-storage")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://x1erangel.blogspot.com/")

driver.find_element_by_link_text("First Post").click()
time.sleep(5)
driver.find_element_by_link_text("link").click()
time.sleep(260)

driver.quit()

print("Done !")
