import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD_LOCATOR = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD_LOCATOR = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD_LOCATOR = ("xpath", "//input[@name='lastName']")
    EMPLOYEE_ID_FIELD_LOCATOR = ("xpath", "(//input[contains(@class, 'oxd-input')])[5]")
    SAVE_BUTTON_LOCATOR = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER_LOCATOR = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_value):
        with allure.step(f"Change name on '{new_value}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD_LOCATOR))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_value)
            self.new_value = new_value

    def change_middle_name(self, new_value):
        with allure.step(f"Change middle name on '{new_value}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD_LOCATOR))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.BACKSPACE)
            middle_name_field.send_keys(new_value)
            self.new_value = new_value

    def change_last_name(self, new_value):
        with allure.step(f"Change last name on '{new_value}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD_LOCATOR))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.BACKSPACE)
            middle_name_field.send_keys(new_value)
            self.new_value = new_value

    def change_employee_id(self, new_value):
        with allure.step(f"Change employee id on '{new_value}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_ID_FIELD_LOCATOR))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.BACKSPACE)
            middle_name_field.send_keys(new_value)
            self.new_value = new_value

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)).click()

    @allure.step("Changes has been saved successfully")
    def is_changes_saved(self, field_locator):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER_LOCATOR))
        self.wait.until(EC.visibility_of_element_located(field_locator))
        self.wait.until(EC.text_to_be_present_in_element_value(field_locator, self.new_value))
