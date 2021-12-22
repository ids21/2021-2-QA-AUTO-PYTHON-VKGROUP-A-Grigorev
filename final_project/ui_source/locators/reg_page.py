from selenium.webdriver.common.by import By


class RegistrationLocators:
    REG_USERNAME = (By.XPATH, "//input[@id='username' and @required]")
    REG_PASSWORD = (By.XPATH, "//input[@id='password' and @required]")

    REG_EMAIL = (By.XPATH, "//input[@id='email']")
    REG_EMAIL_VALID = (By.XPATH, "//input[@id='email' and @required]")

    REPEAT_PASSWORD = (By.XPATH, "//input[@id='confirm']")
    REPEAT_PASSWORD_VALID = (By.XPATH, "//input[@id='confirm' and @required]")

    ACCEPT_CHECKBOX = (By.XPATH, "//input[@id='term' and @required]")
    REGISTER_BUTTON = (
        By.XPATH, "//input[@name='submit' and @value='Register']")
    GO_TO_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")

    USERNAME_ERROR = (
        By.XPATH, "//div[@id='flash' and text()='Incorrect username length']")
    INVALID_EMAIL_ERROR = (
        By.XPATH, "//div[@id='flash' and text()='Invalid email address']")
    INCORRECT_EMAIL_LENGTH = (
        By.XPATH, "//div[@id='flash' and text()='Incorrect email length']")
    PASSWORD_NOT_MATCH_ERROR = (
        By.XPATH, "//div[@id='flash' and text()='Passwords must match']")
    USER_ALREADY_EXIST = (
        By.XPATH, "//div[@id='flash' and text()='User already exist']")
