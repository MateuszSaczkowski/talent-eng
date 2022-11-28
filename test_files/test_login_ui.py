
from src.applications.GitubUI import GitHubUI
# from src.config.config import config
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time

def test_first_login_test(github_ui_app):
    github_ui_app.goto_login_page()
    # github_ui_app.goto_login_page()
    # github_ui_app.login('username','password')
    # assert github_ui_app.check_title() == 'some title'
    
    # service_obj = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service_obj)
    # driver.maximize_window()
    # driver.get(config.BASE_URL_UI)
    # assert driver.title == "GitHub: Let’s build from here · GitHub"
    # driver.find_element(By.Name, "q").send_keys("GlobalLogic")
