from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By


class BasePage:
    
    def __init__(self, web_driver) -> None:
        """Set driver and url for tests
         Args:
         - web_driver (object): selenium.webdriver browser
        """
        self.web_driver = web_driver

    def click(self, locator: str, loading = False) -> None:
        if loading:
            WebDriverWait(self.web_driver, 15).until(
                ExpCond.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'spinner')]")
                )
            )
        try:
            link = WebDriverWait(self.web_driver, 15).until(
                ExpCond.presence_of_element_located((By.XPATH, locator))
            )
            link.click()
        except ElementClickInterceptedException:
            link = WebDriverWait(self.web_driver, 5).until(
                ExpCond.element_to_be_clickable((By.XPATH, locator))
            )
            link.click()
    
    def clear(self, locator: str) -> None:
        link = WebDriverWait(self.web_driver, 15).until(
                ExpCond.presence_of_element_located((By.XPATH, locator))
            )
        link.clear()
    
    def keys(self, locator: str, text: str) -> None:
        link = WebDriverWait(self.web_driver, 15).until(
            ExpCond.presence_of_element_located((By.XPATH, locator))
        )
        link.send_keys(text)
    
    def is_enabled(self, locator: str) -> bool:
        link = WebDriverWait(self.web_driver, 15).until(
            ExpCond.presence_of_element_located((By.XPATH, locator))
        )
        return link.is_enabled()

    def get_attr(self, locator:str, attribute:str)-> str:
        link = WebDriverWait(self.web_driver, 15).until(
            ExpCond.presence_of_element_located((By.XPATH, locator))
        )
        text_atr: str = link.get_attribute(attribute)
        return text_atr