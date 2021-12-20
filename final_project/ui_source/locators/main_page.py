from selenium.webdriver.common.by import By


class MainLocators:

    PYTHON_BUTTON = (By.XPATH, "//a[text()='Python']")
    DOWNLOAD_CENTOS_BUTTON_LOCATOR = (By.XPATH, './/a[text()="Download Centos7"]')

    LINUX_BUTTON = (By.XPATH, "//a[text()='Linux']")

    NETWORK_BUTTON = (By.XPATH, "//a[text()='Network']")

    LOGGED_AS = (By.XPATH, "//li[contains(text(), 'Logged as')]")   
    VK_ID = "//li[text()='VK ID: {}']"
    VK_ID_NONE = (By.XPATH, "//div[@id='login-name']/ul/li[2][text()='']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
