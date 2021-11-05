from source.dashboard.dashboard_locators import (
    AudienceLocator as AL,
)
from source.base_page.base_page_task import BasePage

from time import time 

NAME = 'Test'+ str(time())[:10]


class AudiencePage(BasePage):
    
    def delete_segments(self):   
        if self.is_enabled(AL.RECORD_SEGEMTS.format(NAME), loading=True):
            self.click(AL.FIELD_REMOVE)
            self.click(AL.CONFIRM_DELETE)
            self.web_driver.refresh()


    def create_segments(self):
        """Create new campaign
        """        
        if self.is_enabled(AL.CREATE_SEGMENT):
            self.click(AL.CREATE_SEGMENT)
        else:
            self.click(AL.CREATE_SEGMENT_BUTTON)
        self.click(AL.CHECK_BOX)
        self.click(AL.BUTTON_ADD)
        self.clear(AL.FIELD_INPUT_NAME)
        self.keys(AL.FIELD_INPUT_NAME, NAME)
        self.shot("Creating segment")
        self.click(AL.BUTTON_SUBMIT_CREATE)
        

    def check_segments_added(self): 
        try:
            assert self.is_enabled(AL.RECORD_SEGEMTS.format(NAME))
        except:
            assert False, "Segment dont created"

    def check_segments_deleted(self):
        try:
            num = self.len_elements(AL.RECORD_SEGEMTS.format(NAME), retry=True)
            assert num == None
        except:
            assert False, "Segments dont deleted"