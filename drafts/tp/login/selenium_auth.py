import pytest

# from selenium import webdriver
from seleniumwire import webdriver

import locators
from webdriver_manager.chrome import ChromeDriverManager

def test_one(login):
    driver = login
    for request in driver.requests:
        if request.response:
            if request.url.count("auth?lang") > 0:
                print("")
                print(
                    dir(request)
                )
                print("")
                print("Body: " + str(request.body))
                print("Cert: " + str(request.cert))
                print("Params: " + str(request.params))
                print("QueryStr: " + str(request.querystring))
                print("\n ================ \n")
                print(request.response.headers)

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
    browser = webdriver.Chrome(ChromeDriverManager().install())
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