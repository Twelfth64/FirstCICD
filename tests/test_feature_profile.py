import random
import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile functionality")
class TestProfileFeature(BaseTest):

    # @pytest.mark.skip(reason="no way of currently testing this")
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoketest
    def test_change_profile_name(self):
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
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_employee_id(f"{random.randint(0, 1_000_000_000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.EMPLOYEE_ID_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")

    @allure.title("Change profile other id")
    @allure.severity("High")
    @pytest.mark.smoketest
    def test_change_profile_employee_other_id(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_employee_other_id(f"{random.randint(1, 1_000_000_000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.OTHER_ID_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")

    @allure.title("Change profile driver license")
    @allure.severity("High")
    @pytest.mark.smoketest
    def test_change_profile_employee_driver_license(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_employee_driver_license(f"{random.randint(1, 1_000_000_000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(self.personal_page.DRIVER_LICENSE_FIELD_LOCATOR)
        self.personal_page.make_screenshot("Success")
