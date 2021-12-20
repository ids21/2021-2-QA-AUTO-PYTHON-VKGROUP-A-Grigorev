from ui_source.locators.main_page import MainLocators
import pytest
import allure
from utils.builder import Builder
from tests.tests_ui.base import BaseCase


@allure.epic('Тесты на UI')
@allure.feature('Тесты на авторизацию')
class TestLoginPage(BaseCase):

    registration = False

    @pytest.mark.UI
    def test_fields_validation(self, ui_report):
        """
        Тест валидации полей в форме авторизации.
        Проверяет наличие атрибута required у полей.
        Ожидаемый результат: у полей присутствует валидация.
        """
        self.login_page.check_fields_validation()

    @pytest.mark.UI
    def test_invalid_username(self, ui_report):
        """
        Негативный тест на авторизацию.
        Проверяет реакцию приложения на невалидные данные (слишком короткий username).
        Ожидаемый результат: сообщение об ошибке 'Incorrect username length'.
        """
        user = Builder.create_user()
        username, password = user.username, user.password
        self.login_page.login(
            username=username[:3], password=password
        )
        self.login_page.find(
            self.login_page.locators.INCORRECT_ERROR_MESSAGE, 2)

    @pytest.mark.UI
    def test_valid_credentials(self, mysql_builder, ui_report):
        """
        Позитивный тест на авторизацию.
        При помощи ORM пользователь добавляется в БД. Затем происходит попытка авторизации.
        Ожидаемый результат: найдена строка 'Logged as' на главной странице.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email

        mysql_builder.add_user(username, password, email)
        self.login_page.login(
            username=username, password=password
        )
        self.main_page.find(self.main_page.locators.LOGGED_AS, 2)

    @pytest.mark.UI
    def test_block_user_authorization(self, mysql_builder, ui_report):
        """
        Негативный тест на авторизацию.
        При помощи ORM пользователь добавляется в БД со значением атрибута access=0. Далее попытка авторизации.
        Ожидаемый результат: сообщение об ошибке 'Ваша учетная запись заблокирована'.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email

        mysql_builder.add_user(username, password, email, access=0)
        self.login_page.login(
            username=username, password=password
        )
        self.login_page.find(
            self.login_page.locators.BLOCK_MESSAGE, 2
        )

    @pytest.mark.UI
    def test_go_to_registration_page(self, ui_report):
        """
        Тест перехода со страницы авторизации на страницу регистрации.
        Проверяет наличие строки 'Registration' в исходном коде страницы.
        Ожидаемый результат: строка присутствует.
        """
        self.login_page.go_to_registration_page()
        assert 'Registration' in self.registration_page.driver.page_source


@allure.feature('Тесты Главного меню')
class TestMainPage(BaseCase):

    locators = MainLocators()

    @pytest.mark.parametrize(
        'locator, expected_results',
        [
            (locators.PYTHON_BUTTON, ('Python history', 'About Flask')),
            (locators.LINUX_BUTTON, ('Download Centos7')),
            (locators.NETWORK_BUTTON, ('Wireshark',
             'News', 'Download', 'Tcpdump', 'Examples'))
        ],
        ids=['dropdown_python', 'dropdown_linux', 'dropdown_network']
    )
    @pytest.mark.UI
    @allure.description('Проверка открытия всех выпадающих списков на панели навигации')
    def test_ui_check_dropdown(self, locator, expected_results, ui_report):
        self.main_page.open_dropdow_menu(locator)
        for result in expected_results:
            assert result in self.web_driver.page_source

    @pytest.mark.UI
    @allure.description('Проверка открытия ссылки Download Centos7')
    def test_ui_open_links(self, ui_report):
        expected_result = 'Download Centos7'
        self.main_page.open_redirect_page(expected_result)


@allure.feature('Тесты регистрации')
class TestRegistrationPage(BaseCase):

    registration = False

    @pytest.mark.UI
    def test_fields_validation(self, ui_report):
        """
        Тест валидации полей в форме регистрации.
        Проверяет наличие атрибута required у полей.
        Ожидаемый результат: у полей присутствует валидация.
        """
        self.login_page.go_to_registration_page()
        self.registration_page.check_fields_validation()
