from source.base_page.data import Credentials
from source.dashboard.dashboard_locators import (
    CampaignLocator as CL,
)
from source.base_page.base_page_task import BasePage
from time import sleep
import os 


class CampaignPage(BasePage):

    def create_campaign(self):
        """Create new campaign
        """        
        if self.is_enabled(CL.BUTTON_CREATE_CAMPAIGN):
            self.click(CL.BUTTON_CREATE_CAMPAIGN)
        else:
            self.click(CL.BUTTON_CREATE)
        self.click(CL.REACH_BUTTON)
        self.keys(CL.INPUT_LINK, Credentials.CAMPAIGN_LINK)
        self.move_to(CL.BUDGET_BLOCK)
        self.keys(CL.BUDGET_PER_DAY, '100')
        self.keys(CL.BUDGET_TOTAL,'1000')
        self.click(CL.FIELD_BANNER)
        directory = os.getcwd()
        scr = os.path.join(directory, "test.jpeg")
        self.move_to(CL.FIELD_UPLOAD_IMAGE)
        self.keys(CL.INPUT_IMAGE, scr)
        sleep(1.5)
        self.shot("Adding campaign")
        self.click(CL.BUTTON_CREATE)

    def check_campaign_added(self):
        """[summary]
        """      
        try:
            assert self.is_enabled(CL.RECORD_CAMPAIGN)
        except:
            assert False, "Campaign dont created"
        finally:
            self.shot("Our campaign after creating")

    def delete_campaign(self):
        """[summary]
        """        
        while(True):
            if self.len_elements(CL.RECORD_CAMPAIGN, retry=True)[0] is not None:
                self.click(CL.SELECT_RECORD)
                self.click(CL.DROP_ACTIONS)
                self.click(CL.DELETE_RECORD)
                #self.click(CL.REFRESH_TABLE)
                self.web_driver.refresh()
            else:
                break



