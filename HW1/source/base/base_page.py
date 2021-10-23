from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
)
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By

from source.base.base_locators import BaseLocators

class Wait:

    @staticmethod
    def wait_until_precence_of_lement(driver, locator, timeout):
        """waiting for the xpath element to appear on the page
        """
        return WebDriverWait(driver, timeout).until(
            ExpCond.presence_of_element_located((By.XPATH, locator))
            )
        
    @staticmethod
    def wait_invisibility_of_element(driver, locator, timeout):
        """
        """        
        return WebDriverWait(driver, timeout).until(
                ExpCond.invisibility_of_element_located(
                    (By.XPATH, locator)
                )
            )
    
    @staticmethod
    def wait_element_to_be_clickable(driver, locator, timeout):
        """
        """        
        return WebDriverWait(driver, timeout).until(
            ExpCond.element_to_be_clickable((By.XPATH, locator))
            )
    

class BasePage:
    
    def __init__(self, web_driver) -> None:
        """Set driver and url for tests
         Args:
         - web_driver (object): selenium.webdriver browser
        """
        self.web_driver = web_driver

    def click(self, locator: str, loading = False) -> None:
        if loading:
            Wait().wait_invisibility_of_element(
                driver = self.web_driver,
                locator= BaseLocators.SPINNER, 
                timeout = 15
            )
        try:
            link = Wait().wait_until_precence_of_lement(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 15
            )
            link.click()
        except ElementClickInterceptedException:
            link = Wait().wait_element_to_be_clickable(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 5
            )
            link.click()
    
    def clear(self, locator: str) -> None:
        link = Wait().wait_until_precence_of_lement(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 15
            )
        link.clear()
    
    def keys(self, locator: str, text: str) -> None:
        link = Wait().wait_until_precence_of_lement(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 15
            )
        link.send_keys(text)
    
    def is_enabled(self, locator: str) -> bool:
        link = Wait().wait_until_precence_of_lement(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 15
            )
        return link.is_enabled()

    def get_attr(self, locator:str, attribute:str)-> str:
        link = Wait().wait_until_precence_of_lement(
                driver = self.web_driver, 
                locator = locator, 
                timeout = 15
            )
        text_atr: str = link.get_attribute(attribute)
        return text_atr