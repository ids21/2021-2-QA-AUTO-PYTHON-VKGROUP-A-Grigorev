from source.base.data import Credentials
from source.main.main_page_locators import Locators
from source.dashboard.dashboard_locators import DashboardLocators as CL
from source.base.base_page import BasePage


class MainPage(BasePage):

    def login(self):
        """Login in the system
        """
        self.click(Locators.BUTTON_LOGIN)
        self.keys(Locators.INPUT_EMAIL, Credentials.USERNAME)
        self.keys(Locators.INPUT_PASSWORD, Credentials.PASSWORD)
        self.click(Locators.BUTTON_AUTH)
    
    def logout(self):
        """Logout from the system
        """
        self.click(CL.USER_PROFILE, loading=True)
        self.click(CL.FIELD_LOG_OFF, loading=True)
    
    def check_main_page(self):
        """Check content and footer of main page
        """        
        try:
            assert self.is_enabled(Locators.CONTENT_MAIN_PAGE)
            assert self.is_enabled(Locators.FOOTER_MAIN_PAGE)
        except:
            assert False, "No content and footer of main page"
