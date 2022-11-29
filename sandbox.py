from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com")
# driver.find_element(By.Name, "q").send_keys("GlobalLogic")
time.sleep(55)
