from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def check_elements():
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    submit = driver.find_element(By.ID, "login-button")
    if username and password and submit:
        print("Элементы найдены")
    driver.quit()
check_elements()