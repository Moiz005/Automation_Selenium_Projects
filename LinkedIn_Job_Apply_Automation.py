from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

time.sleep(3)
driver.get("https://www.linkedin.com")
time.sleep(3)
# driver.refresh()
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
# job = driver.find_element(By.CSS_SELECTOR, ".jobs-search__results-list li a")
# job.click()
time.sleep(3)
email = driver.find_element(By.NAME, "session_key")
email.send_keys("USER-NAME")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("ENTER-YOUR-PASSWORD")
submit_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")
submit_btn.click()
time.sleep(3)
Jobs = driver.find_element(By.LINK_TEXT, "Jobs")
Jobs.click()
time.sleep(3)
searchbar = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
searchbar.send_keys("python developer", Keys.ENTER)
time.sleep(3)
Job_link = driver.find_element(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li .job-card-list__title")
Job_link.click()
time.sleep(2)
job_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
job_apply.click()
time.sleep(2)
phone_num = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--input")
phone_num.send_keys("12345678910")
next_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-button")
next_btn.click()
time.sleep(2)
save_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
save_button.click()

# artdeco-button artdeco-button--2
# artdeco-button--primary ember-view artdeco-modal__confirm-dialog-btn
