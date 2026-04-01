from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon()

def test_check_username(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_username()

def test_check_password(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password()