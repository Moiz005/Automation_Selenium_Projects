from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys("USER_NAME")
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys("PASSWORD")
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()
        time.sleep(5)
        nav = self.driver.find_elements(By.CSS_SELECTOR, ".x1iyjqo2 a.x1i10hfl")
        nav[0].click()
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH,
                                           '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now.click()

    def find_followers(self):
        nav = self.driver.find_elements(By.CSS_SELECTOR, "a.x1i10hfl")
        nav[2].click()
        time.sleep(2)
        search = self.driver.find_element(By.CSS_SELECTOR, ".xjoudau input")
        search.send_keys("chefsteps")
        time.sleep(3)
        result = self.driver.find_element(By.CSS_SELECTOR, "div.x9f619>a.x1i10hfl")
        result.click()
        time.sleep(3)
        followers_btn = self.driver.find_element(By.CSS_SELECTOR, "ul li.xl565be a")
        followers_btn.click()

    def follow(self):
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        check = True
        while check:
            check = False
            for i in range(len(follow_btn)):
                follow_btn[i].click()
                check = True

    def unfollow(self):
        unfollow_btn = self.driver.find_elements(By.CSS_SELECTOR, "._aano button._acat")
        check = True
        i = 0
        while check:
            check = False
            while i < len(unfollow_btn):
                unfollow_btn[i].click()
                time.sleep(1)
                unfollow_btn_click = self.driver.find_element(By.CSS_SELECTOR, ".x78zum5 button._a9-_")
                unfollow_btn_click.click()
                check = True
                i+=1
            time.sleep(3)

    def exit_insta(self):
        self.driver.close()


bot = InstaFollower()
bot.login()
time.sleep(3)
bot.find_followers()
time.sleep(3)
# bot.follow()
bot.unfollow()
time.sleep(5)
bot.exit_insta()
