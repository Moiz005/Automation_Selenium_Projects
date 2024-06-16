from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_btn.click()
        time.sleep(30)
        down_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data span")
        print(down_speed.text)

bot = InternetSpeedTwitterBot(150, 10)
bot.get_internet_speed()
