from source.dashboard.dashboard_locators import (
    DashboardLocators as DL,
    BillingLocator as BL,
    ProfileLocators as PL,
)
from source.base_page.base_page_task import BasePage
from source.base_page.data import Credentials


class DashboardPage(BasePage):
    
    def check_precense_of_elements(self):
        """Method for checking the presence of 
           basic elements on the "/dashboard" page
        """
        try:
            assert self.is_enabled(DL.MODULE_SEGMENTS)
            assert self.is_enabled(DL.MODULE_BILLINGS)
            assert self.is_enabled(DL.MODULE_STATISTICS)
        except:
             assert False, "no such element"
    
    def get_profile(self):
        """open profile tab
        """        
        self.click(DL.MODULE_PROFILE)
    
    def get_billing(self):
        """open billing tab
        """        
        self.click(DL.MODULE_BILLINGS)
    
    def check_get_pages_to_modules(self, modules):
        """
        """
        if modules == 'billing':
            self.get_billing()
            assert self.is_enabled(BL.TABLE_DEPOSIT), "Error to open billing tab"
        if modules == 'profile':
            self.get_profile()
            assert self.is_enabled(PL.INPUT_FIO), "Error to open profile tab"

class ProfilePage(BasePage):
    
    def check_edit_full_name(self):
        """Check edit contact information
        """        
        fio_text_before = self.get_attr(PL.INPUT_FIO,'value')
        self.edit_fio()
        fio_text_after = self.get_attr(PL.INPUT_FIO,'value')
        assert fio_text_after != fio_text_before, (
            f"error change name:before {fio_text_before} and after {fio_text_after}"
        )

    def edit_fio(self):
        """Edit fio on profile page
        """      
        self.clear(PL.INPUT_FIO)
        self.keys(PL.INPUT_FIO, "Отредактированный")
        self.click(PL.BUTTON_SAVE)  
    
    def set_orginal_full_name(self):
        """Set original full name. It's precondition for test 
           and posttest cleaning method
        """        
        self.clear(PL.INPUT_FIO)
        self.keys(PL.INPUT_FIO, Credentials.FIO)
        self.click(PL.BUTTON_SAVE)