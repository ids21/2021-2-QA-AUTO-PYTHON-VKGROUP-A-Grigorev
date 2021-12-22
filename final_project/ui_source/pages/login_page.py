from ui_source.locators.login_page import LoginLocators as Locators
from ui_source.pages.base_page import BasePage
from ui_source.pages.main_page import MainPage
from ui_source.pages.reg_page import RegistrationPage
from api_source.exceptions import ValidationError

from selenium.common.exceptions import TimeoutException
import allure


class LoginPage(BasePage):

    locators = Locators()

    @allure.step('Авторизация')
    def login(self, username, password):
        self.click(self.locators.USERNAME)
        self.send_message(self.locators.USERNAME, username)
        self.click(self.locators.PASSWORD)
        self.send_message(self.locators.PASSWORD, password)
        self.click(self.locators.LOGIN_BUTTON)

        if self.driver.current_url == 'http://myapp_proxy:8070/welcome/':
            with allure.step(
                'Авторизация прошла успешно! Выполнен переход на главную страницу.'
            ):
                return MainPage(self.driver)
        else:
            with allure.step('Авторизация не удалась...'):
                pass

    @allure.step('Проверка валидации полей при авторизации...')
    def check_fields_validation(self):
        try:
            self.find(self.locators.USERNAME, timeout=2)
            self.find(self.locators.PASSWORD, timeout=2)
        except TimeoutException:
            raise ValidationError('Валидация не пройдена!')

    @allure.step('Переход со страницы авторизации на страницу регистрации...')
    def go_to_registration_page(self):
        self.click(self.locators.REGISTRATION_BUTTON)
        if self.driver.current_url == 'http://myapp_proxy:8070/reg':
            return RegistrationPage(self.driver)
