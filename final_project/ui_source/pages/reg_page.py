import allure
from selenium.common.exceptions import TimeoutException
from utils.builder import Builder
from ui_source.pages.base_page import BasePage
from ui_source.pages.main_page import MainPage

from ui_source.locators.reg_page import RegistrationLocators


class ValidationError(Exception):
    pass


class RegistrationPage(BasePage):
    locators = RegistrationLocators()

    @allure.step('Проверка валидации полей при регистрации...')
    def check_fields_validation(self):
        try:
            self.find(self.locators.REG_USERNAME, 2)
            self.find(self.locators.REG_EMAIL_VALID, 2)
            self.find(self.locators.REG_PASSWORD, 2)
            self.find(self.locators.REPEAT_PASSWORD_VALID, 2)
            self.find(self.locators.ACCEPT_CHECKBOX, 2)
        except TimeoutException:
            raise ValidationError('Валидация не пройдена!')

    @allure.step('Регистрация.')
    def register(self):
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email
        self.click(self.locators.REG_USERNAME)
        self.send_message(self.locators.REG_USERNAME, username)
        self.click(self.locators.REG_EMAIL)
        self.send_message(self.locators.REG_EMAIL, email)
        self.click(self.locators.REG_PASSWORD)
        self.send_message(self.locators.REG_PASSWORD, password)
        self.click(self.locators.REPEAT_PASSWORD)
        self.send_message(self.locators.REPEAT_PASSWORD, password)
        self.click(self.locators.ACCEPT_CHECKBOX)
        self.click(self.locators.REGISTER_BUTTON)

        if self.driver.current_url == 'http://myapp:9999/welcome/':
            with allure.step('Регистрация прошла успешно! Выполнен переход на главную страницу.'):
                return MainPage(self.driver)
        else:
            with allure.step('Регистрация не удалась...'):
                pass