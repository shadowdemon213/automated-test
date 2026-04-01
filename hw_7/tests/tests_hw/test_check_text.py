from selenium import webdriver
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
import time

def test_check_footer_text():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    footer = BaseComponent(driver, (By.CSS_SELECTOR, "footer"))

    assert footer.get_text() == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    driver.quit()

def test_check_elements_text():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0, 300);")
    driver.find_element(By.XPATH, "//h5[text()='Elements']").click()
    time.sleep(2)
    text = driver.find_element(
        By.XPATH,
        "//div[contains(text(), 'Please select an item')]"
    ).text
    assert text == "Please select an item from left to start practice."

    driver.quit()

