from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
phone_number=os.getenv("PHONE_NUMBER")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get( "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0")

time.sleep(2)
driver.find_element(By.LINK_TEXT,"Sign in").click()
time.sleep(5)
my_email=driver.find_element(By.ID, "username")
my_email.send_keys(email)
my_password=driver.find_element(By.ID, "password")
my_password.send_keys(password)
submit=driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
submit.click()
input("Press Enter when you have solved the Captcha")
easy_pply= driver.find_elements(By.CLASS_NAME,"artdeco-button__text")
time.sleep(5)
for i in easy_pply:
    if i.text=="Easy Apply":
        i.click()
        time.sleep(5)
    try:
         phone=driver.find_element(By.CLASS_NAME,"fb-dash-form-element__error-field artdeco-text-input--input")
         if phone.text=="":
             phone.send_keys(phone_number)
             time.sleep(5)
         next=driver.find_element(By.CLASS_NAME,"artdeco-button__text")
         next.click()
    except NoSuchElementException:
         print("No application, button,skipped")
