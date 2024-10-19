from pages.base_page import BasePage
from src.helpers import TestData
from src.locators import StartPageLocators, LogInLocators, PersonalAccountLocators
import allure

class PersonalAccountPage(BasePage):

    @allure.step('Кликаем с ожиданием на кнопку «Личный кабинет»')
    def click_personal_account(self):
        self.click_element_with_wait(StartPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Вводим почту')
    def set_email(self):
        self.set_text(LogInLocators.NAME_FIELD, TestData.test_email)

    @allure.step('Вводим пароль')
    def set_password(self):
        self.set_text(LogInLocators.PASSWORD_FIELD, TestData.test_password)

    @allure.step('Кликаем с ожиданием на кнопку «Войти»')
    def click_log_in_button(self):
        self.click_element_with_wait(LogInLocators.LOG_IN_BUTTON)

    @allure.step('Ожидаем кликабельности кнопки «Оформить заказ»')
    def wait_make_order(self):
        self.wait_for_clickable_element(StartPageLocators.CONFIRM_ORDER)

    @allure.step('Находим с ожиданием кнопку «Личный кабинет»')
    def find_profile_button(self):
        return self.find_element_with_wait(PersonalAccountLocators.PROFILE_BUTTON)

    @allure.step('Кликаем с ожиданием на кнопку «Лента заказов»')
    def click_history_order_button(self):
        self.click_element_with_wait(PersonalAccountLocators.HISTORY_BUTTON)

    @allure.step('Кликаем с ожиданием на кнопку «Выход»')
    def click_exit_button(self):
        self.click_element_with_wait(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Находим с ожиданием кнопку «Войти»')
    def find_enter_button(self):
        return self.find_element_with_wait(LogInLocators.LOG_IN_BUTTON)

    @allure.step('Логинимся на сайте')
    def log_in(self):
        self.click_personal_account()
        self.set_email()
        self.set_password()
        self.click_log_in_button()

