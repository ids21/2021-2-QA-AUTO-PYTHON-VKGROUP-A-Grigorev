from source.base_page.data import Credentials
from source.main.main_page_locators import Locators
from source.dashboard.dashboard_locators import DashboardLocators as CL
from source.base_page.base_page_task import BasePage


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
    
    def check_non_filled_field(self):
        """Check authorization if login and password didn't filled
        """        
        self.click(Locators.BUTTON_LOGIN)
        self.clear(Locators.INPUT_EMAIL)
        self.clear(Locators.INPUT_PASSWORD)
        try:
            assert 'disabled' in self.get_attr(Locators.BUTTON_AUTH, 'class')
        except:
            assert False, "Auth button should be disabled "
        finally:
            self.shot(description="Login attempt without data.Auth button should be disabled")

    def check_incorrect_credentials(self, credential):
        """Check authorization if credential incorrect
        """        
        self.click(Locators.BUTTON_LOGIN)
        if credential=='login':
            self.clear(Locators.INPUT_EMAIL)
            self.keys(Locators.INPUT_EMAIL, 'testtest@gmail.com')
            self.clear(Locators.INPUT_PASSWORD)
            self.keys(Locators.INPUT_PASSWORD, Credentials.PASSWORD)
        elif credential=='password':
            self.clear(Locators.INPUT_EMAIL)
            self.keys(Locators.INPUT_EMAIL, Credentials.USERNAME)
            self.clear(Locators.INPUT_PASSWORD)
            self.keys(Locators.INPUT_PASSWORD, 'testest')
        else:
            raise AttributeError(f"This credential type {credential} don't exist")

        self.click(Locators.BUTTON_AUTH)
        try:
            assert self.is_enabled(Locators.RETRY_AUTH_FORM)
        except:
            assert False, "Should be retry auth form there"
        finally:
            self.shot(description="Retrying the login")