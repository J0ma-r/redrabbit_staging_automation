import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_new_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service('C:\Program Files (x86)\chromedriver.exe')
    return webdriver.Chrome(options=options, service=service)


class Browser:
    def __init__(self):
        self.driver = get_new_driver()

    def get_new_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        service = Service('C:\Program Files (x86)\chromedriver.exe')
        return webdriver.Chrome(options=options, service=service)

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    def find_by_xpath(self, xpath):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(By.XPATH, xpath)

    def fill_by_id(self, text, i):
        self.driver.find_element(By.ID, i).send_keys(text)

    def close(self):
        self.driver.quit()

    def open_tab(self, url):
        # driver.execute_script(f"window.open('{url}');")
        self.driver.switch_to.new_window('tab')
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def close_tab(self):
        self.driver.quit()

    def clear(self, xpath):
        self.find_by_xpath(xpath).clear()

    def click(self, xpath):
        self.find_by_xpath(xpath).click()

    def fill(self, text, xpath):
        self.find_by_xpath(xpath).send_keys(text)

    def upload(self, xpath, photo_location):
        self.find_by_xpath(xpath).send_keys(os.getcwd()+photo_location)