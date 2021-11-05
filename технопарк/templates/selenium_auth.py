import pytest
from selenium import webdriver
import locators

def test_one(login):
    assert True

@pytest.fixture(scope='function', autouse=False)
def browser():
    """
    Fixture automatically login and logout user,
    generates browser(driver) object
    """
    chrome_options = webdriver.ChromeOptions()

    # user is not authed in this mode
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path="./chromedriver",
                               options=chrome_options)
    try:
        browser.get("https://target.my.com")
        # set wait for elemnts load if it is needed
        browser.implicitly_wait(10)
        browser.maximize_window()  # all tabs are on the screen
        yield browser
    finally:
        browser.close()

@pytest.fixture(scope='function', autouse=True)
def login(browser):
    login_btn = browser.find_element(*locators.LOGIN_BTN_LOCATOR)
    login_btn.click()
    email_field = browser.find_element(*locators.EMAIL_FIELD_LOCATOR)
    email_field.send_keys("tttshelby6@gmail.com")
    pass_field = browser.find_element(*locators.PASSWORD_FIELD_LOCATOR)
    pass_field.send_keys("S3leniumpass")
    login_btn = browser.find_element(*locators.LOGIN_FORM_BTN_LOCATOR)
    login_btn.click()
    yield browser