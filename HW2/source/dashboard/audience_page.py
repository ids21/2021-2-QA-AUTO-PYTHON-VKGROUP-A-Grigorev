from source.dashboard.dashboard_locators import (
    AudienceLocator as AL,
)
from source.base_page.base_page_task import BasePage


class AudiencePage(BasePage):
    
    def delete_segments(self):
        """[summary]
        """        
        while(True):
            if self.len_elements(AL.RECORD_SEGEMTS, retry=True)[0] is not None:
                self.click(AL.FIELD_REMOVE)
                self.click(AL.CONFIRM_DELETE)
                #self.click(AL.REFRESH_TABLE)
                self.web_driver.refresh()
            else:
                break

    def create_segments(self):
        """Create new campaign
        """        
        if self.is_enabled(AL.CREATE_SEGMENT):
            self.click(AL.CREATE_SEGMENT)
        else:
            self.click(AL.CREATE_SEGMENT_BUTTON)
        self.click(AL.CHECK_BOX)
        self.click(AL.BUTTON_ADD)
        self.shot("Creating segment")
        self.click(AL.BUTTON_SUBMIT_CREATE)
        

    def check_segments_added(self):
        """[summary]
        """      
        try:
            assert self.is_enabled(AL.RECORD_SEGEMTS)
        except:
            assert False, "Segment dont created"
        finally:
            self.shot("Our Segment after creating")