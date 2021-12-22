from ui_source.locators.main_page import MainLocators as Locators
from ui_source.pages.base_page import BasePage
import allure


class MainPage(BasePage):
    locators = Locators()

    @allure.step('Открыть выпадающее меню')
    def open_dropdow_menu(self, locator):
        self.click(locator)
        assert self.driver.current_url == 'http://myapp_proxy:8070/welcome/'

    @allure.step('Open redirect page')
    def open_redirect_page(self, expected_result):
        self.click(self.locators.LINUX_BUTTON)
        self.click(self.locators.DOWNLOAD_CENTOS_BUTTON_LOCATOR)

        tabs = []
        for handle in self.driver.window_handles:
            tabs.append(handle)
        assert len(tabs) == 2
        self.driver.switch_to.window(tabs[1])
        assert expected_result in self.driver.page_source
        self.driver.switch_to.window(tabs[0])
        assert self.driver.current_url == 'http://myapp_proxy:8070/welcome/'
