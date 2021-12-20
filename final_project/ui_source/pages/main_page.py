from ui_source.locators.main_page import MainLocators as Locators
from ui_source.pages.base_page import BasePage
import allure

class MainPage(BasePage):
    locators = Locators()
    
    @allure.step('Открыть выпадающее меню')
    def open_dropdow_menu(self, locator):
        self.click(locator)
        assert self.driver.current_url == 'http://myapp/welcome/'