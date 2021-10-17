from source.main.main_page import MainPage
from source.dashboard.dashboard_page import DashboardPage, ProfilePage

import pytest


class TestMainPage:
    
    @pytest.mark.ui
    def test_TMP001_check_logout(self, web_driver):
        main_page_task = MainPage(web_driver)
        main_page_task.login()
        main_page_task.logout()    
        main_page_task.check_main_page()
    

class TestDashboard:

    @pytest.mark.ui
    def test_TDB001_check_login(self, web_driver):
        main_page_task = MainPage(web_driver)
        dashboard_page_task = DashboardPage(web_driver)
        main_page_task.login()
        dashboard_page_task.check_precense_of_elements()
    
    @pytest.mark.parametrize('modules', list(['billing','profile']))
    @pytest.mark.ui
    def test_TDB002_check_get_pages_to_modules(self, web_driver, modules):
        main_page_task = MainPage(web_driver)
        dashboard_page_task = DashboardPage(web_driver)
        main_page_task.login()
        dashboard_page_task.check_get_pages_to_modules(modules)
    
    @pytest.mark.ui
    def test_TDB003_check_edit_fio(self, web_driver):
        main_page_task = MainPage(web_driver)
        dashboard_page_task = DashboardPage(web_driver)
        profile_page_task = ProfilePage(web_driver)        
        main_page_task.login()
        dashboard_page_task.get_profile()
        profile_page_task.set_orginal_full_name()
        profile_page_task.check_edit_full_name()
        profile_page_task.set_orginal_full_name()