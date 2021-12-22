
import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 3


class SecondTabError(Exception):
    pass


class LocatorNotFoundError(Exception):
    pass


class BasePage:
    locators = None

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')

    @allure.step('Клик по локатору {locator}...')
    def click(self, locator, timeout=10):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                self.logger.info(f'Clicking on {locator}')
                element.click()
                
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    @allure.step('Скролл к элементу {element}...')
    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Поиск локатора {locator}...')
    def find(self, locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Отправление сообщения <{message}> в локатор {locator}...')
    def send_message(self, locator, message, timeout=10):
        field = self.wait(timeout).until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(message)

    @allure.step('Переключение на вторую вкладку в браузере...')
    def switch_to_second_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except IndexError:
            raise SecondTabError('Новая вкладка не найдена!')