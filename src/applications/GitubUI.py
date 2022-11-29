import time

from src.config.config import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time



class GitHubUI:
    def __init__(self) -> None:
        service_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_obj)
       

    def open_base_page(self):
        self.driver.get(config.BASE_URL_UI)
        pass

    def goto_login_page(self):
        self.driver.get(config.BASE_URL_UI + '/login')
        time.sleep(55)
        

    def login(self, username, password):
        pass
    
    def logout(self):
        pass
    
    def check_title(self):
        pass