from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.XPATH, "//input[@id='username' and @required]")
    PASSWORD = (By.XPATH, "//input[@id='password' and @required]")

    LOGIN_BUTTON = (By.XPATH, "//input[@name='submit']")

    INCORRECT_ERROR_MESSAGE = (
        By.XPATH, "//div[@id='flash' and text()='Incorrect username length']")
    INVALID_ERROR_MESSAGE = (
        By.XPATH, "//div[@id='flash' and text()='Invalid username or password']")
    BLOCK_MESSAGE = (
        By.XPATH, "//div[@id='flash' and text()='Ваша учетная запись заблокирована']")

    REGISTRATION_BUTTON = (By.XPATH, "//a[@href='/reg']")
