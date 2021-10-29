from source.dashboard.dashboard_locators import (
    DashboardLocators as DL,
)
from source.dashboard.campaign_page import  CampaignPage
from source.base_page.base_page_task import BasePage


class DashboardPage(BasePage):
    
    def get_profile(self):
        """open profile tab
        """        
        self.click(DL.MODULE_PROFILE)
    
    def get_billing(self):
        """open billing tab
        """        
        self.click(DL.MODULE_BILLINGS)
    
    def get_campaign_page(self):
        """open campaign tab
        """        
        self.click(DL.MODULE_CAMPAIGN)
        return CampaignPage(self.web_driver)