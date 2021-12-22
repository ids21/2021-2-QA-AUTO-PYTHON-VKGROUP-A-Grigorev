import allure
import pytest

from utils.builder import Builder


@allure.epic('Тесты API')
class TestAPI:

    @pytest.mark.API
    def test_add_user(self, login_api, mysql_builder):
        """
        Тест проверяет добавление пользователя через API.
        Через ORM осуществляется проверка, что пользователь добавлен в БД.
        Ожидаемый результат: username при отправлении запроса совпадает с username в БД.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email
        login_api.post_add_user(
            username=username, 
            password=password,
            email=email
        )
        assert mysql_builder.select_by_username(username).username == username

    @pytest.mark.API
    def test_add_existent_user(self, login_api, fake_data):
        """
        Тест проверяет добавление существующего пользователя через API.
        Ожидаемый результат: код ответа 304 (сущность существует/не изменилась).
        """
        login_api.post_add_user(
            username=fake_data['username'], 
            password=fake_data['password'],
            email=fake_data['email'], expected_status=304
        )


    @pytest.mark.API
    def test_delete_user(self, login_api, mysql_builder, mysql_client):
        """
        Тест проверяет удаление пользователя через API.
        Через ORM происходит добавление пользователя в БД и проверка, что пользователь успешно удален.
        Ожидаемый результат: после удаления username в БД не найден.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email
        mysql_builder.add_user(
            username=username, 
            password=password,
            email= email
        )
        login_api.get_delete_user(username=username)
        assert mysql_client.select_by_username(username) is None

    @pytest.mark.API
    def test_delete_not_existent_user(self, login_api):
        """
        Тест проверяет удаление несуществующего пользователя через API.
        Ожидаемый результат: код ответа 404 (сущности не существует).
        """
        login_api.get_delete_user(username='testusername', expected_status=404)

    @pytest.mark.API
    def test_block_user(self, login_api, mysql_builder, mysql_client):
        """
        Тест проверяет блокировку пользователя через API.
        Через ORM осуществляется добавление пользователя в БД, затем проверка поля access.
        Ожидаемый результат: поле access = 0.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email
        mysql_builder.add_user(
            username=username, 
            password=password,
            email= email
        )
        login_api.get_block_user(username)
        assert mysql_client.select_by_username(username).access == 0

    @pytest.mark.API
    def test_block_not_existent_user(self, login_api):
        """
        Тест проверяет блокировку несуществующего пользователя через API.
        Ожидаемый результат: код ответа 404 (сущности не существует).
        """
        user = Builder.create_user()
        username = user.username
        login_api.get_block_user(username=username, expected_status=404)

    @pytest.mark.API
    def test_unblock_user(self, login_api, mysql_builder, mysql_client):
        """
        Тест проверяет разблокировку пользователя через API.
        Через ORM осуществляется добавление пользователя в БД с полем access=0.
        Затем проверка, что поле access изменилось.
        Ожидаемый результат: поле access стало равно 1.
        """
        user = Builder.create_user()
        username, password, email = user.username, user.password, user.email
        mysql_builder.add_user(username=username, password=password,
                               email=email, access=0)
        login_api.get_unblock_user(username=username)
        assert mysql_client.select_by_username(username).access == 1

    @pytest.mark.API
    def test_unblock_not_existent_user(self, login_api):
        """
        Тест проверяет разблокировку несуществующего пользователя через API.
        Ожидаемый результат: код ответа 404 (сущности не существует).
        """
        user = Builder.create_user()
        username = user.username
        login_api.get_unblock_user(username=username, expected_status=404)


    @pytest.mark.API
    def test_login_not_existent_user(self, api_client):
        """
        Тест проверяет авторизацию несуществующего пользователя через API.
        Ожидаемый результат: код ответа 401 (пользователь не авторизован).
        """
        api_client.post_login(username='lollololo', password='lollol', expected_status=401)

    @pytest.mark.API
    def test_login_without_password(self, api_client):
        """
        Тест проверяет авторизацию пользователя через API без передачи пароля.
        Ожидаемый результат: код ответа 400 (плохой запрос).
        """
        user = Builder.create_user()
        username = user.username
        api_client.post_login(username=username, password=None, expected_status=400)