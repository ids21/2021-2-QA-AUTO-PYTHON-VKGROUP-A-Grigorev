from selenium.webdriver.common.by import By


class MainLocators:
    TM_BUTTON = (By.XPATH, "//a[contains(@class, 'uk-navbar-brand')]")
    HOME_BUTTON = (By.XPATH, "//a[text()='HOME']")

    PYTHON_BUTTON = (By.XPATH, "//a[text()='Python']")
    PYTHON_HISTORY = (By.XPATH, "//a[text()='Python history']")
    ABOUT_FLASK = (By.XPATH, "//a[text()='About Flask']")

    LINUX_BUTTON = (By.XPATH, "//a[text()='Linux']")

    NETWORK_BUTTON = (By.XPATH, "//a[text()='Network']")
    WIRESHARK_NEWS = (By.XPATH, "//a[text()='News']")
    DOWNLOAD_WIRESHARK = (By.XPATH, "//a[text()='Download']")
    TCPDUMP_EXAMPLES = (By.XPATH, "//a[text()='Examples ']")

    LOGGED_AS = (By.XPATH, "//li[contains(text(), 'Logged as')]")
    VK_ID = "//li[text()='VK ID: {}']"
    VK_ID_NONE = (By.XPATH, "//div[@id='login-name']/ul/li[2][text()='']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    API_BUTTON = (By.XPATH, "//img[@src='/static/images/laptop.png']")
    FUTURE_OF_INTERNET = (By.XPATH, "//img[@src='/static/images/loupe.png']")
    SMTP = (By.XPATH, "//img[@src='/static/images/analytics.png']")

    PYTHON_ZEN_QUOTE = (
        By.XPATH, "//div[contains(@class, 'uk-text-center')]/p[2]")
