from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    StaleElementReferenceException
)
from selenium.webdriver import ActionChains
import logging
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By
from source.base_page.base_locators import BaseLocators

CLICK_RETRY = 3


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



class BasePage(object):

    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.logger = logging.getLogger('test')

    def scroll_to(self, element):
        self.web_driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def click(self,locator, timeout=None, loading = False):
        self.logger.info(f'Clicking on {locator}')
        if loading:
            Wait().wait_invisibility_of_element(
                driver = self.web_driver,
                locator= BaseLocators.SPINNER, 
                timeout = 15
            )
        for i in range(CLICK_RETRY):
            try:
                Wait().wait_until_precence_of_lement(
                    driver=self.web_driver,
                    locator=locator,
                    timeout=30
                )
                elem = Wait().wait_element_to_be_clickable(
                    driver=self.web_driver,
                    locator=locator,
                    timeout=45
                )
                self.scroll_to(elem)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise

    def clear(self, locator: str) -> None:
        link = Wait().wait_until_precence_of_lement(
            driver=self.web_driver,
            locator=locator,
            timeout=30
        )
        link.clear()

    def keys(self, locator: str, text: str) -> None:
        link = Wait().wait_until_precence_of_lement(
            driver=self.web_driver,
            locator=locator,
            timeout=30
        )
        link.send_keys(text)

    def is_enabled(self, locator: str) -> bool:
        link = Wait().wait_until_precence_of_lement(
            driver=self.web_driver,
            locator=locator,
            timeout=40
        )
        return link.is_enabled()

    def get_attr(self, locator: str, attribute: str) -> str:
        link = Wait().wait_until_precence_of_lement(
            driver=self.web_driver,
            locator=locator,
            timeout=30
        )
        text_atr: str = link.get_attribute(attribute)
        return text_atr
