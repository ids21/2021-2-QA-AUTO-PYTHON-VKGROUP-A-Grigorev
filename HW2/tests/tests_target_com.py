from source.main.main_page import MainPage
from source.dashboard.dashboard_page import DashboardPage, ProfilePage
from base import BaseCase

import allure
import pytest

@allure.epic("Dasboard Page")
class TestDashboard(BaseCase):

    authorize = False
    