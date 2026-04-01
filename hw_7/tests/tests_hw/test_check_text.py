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

    elements_button = BaseComponent(driver, ("xpath", "//h5[text()='Elements']"))
    elements_button.find_element().click()

    import time
    time.sleep(2)

    text_block = BaseComponent(
        driver,
        ("xpath", "//*[contains(text(), 'Please select an item')]")
    )

    assert 'Please select an item from left to start practice.' in text_block.get_text()

    driver.quit()