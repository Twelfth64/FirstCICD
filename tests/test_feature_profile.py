import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoketest
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.FIRST_NAME_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")

    @allure.title("Change profile middle name")
    @allure.severity("Critical")
    @pytest.mark.smoketest
    def test_change_profile_middle_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_middle_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.MIDDLE_NAME_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")

    @allure.title("Change profile last name")
    @allure.severity("Critical")
    @pytest.mark.smoketest
    def test_change_profile_last_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_last_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.LAST_NAME_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")

    @allure.title("Change profile employee id")
    @allure.severity("High")
    @pytest.mark.smoketest
    def test_change_profile_employee_id(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_employee_id(f"{random.randint(1, 1_000_000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.EMPLOYEE_ID_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")
