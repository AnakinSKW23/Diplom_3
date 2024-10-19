from pages.base_page import BasePage
from src.locators import StartPageLocators
import allure

class StartPage(BasePage):

    @allure.step('Ожидаем кликабельности кнопки «Личный Кабинет»')
    def wait_for_personal_account_button(self):
        self.wait_for_clickable_element(StartPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликаем с ожиданием на кнопку «Лента Заказов»')
    def click_order_feed_button(self):
        self.click_element_with_wait(StartPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликаем с ожиданием на кнопку «Конструктор»')
    def click_constructor_button(self):
        self.click_element_with_wait(StartPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем с ожиданием на кнопку «Оформить заказ»')
    def click_confirm_order(self):
        self.click_element_with_wait(StartPageLocators.CONFIRM_ORDER)

    @allure.step('Находим с ожиданием элемент «Соберите бургер»')
    def find_create_order(self):
        return self.find_element_with_wait(StartPageLocators.CREATE_BURGER)

    @allure.step('Кликаем с ожиданием на элемент «Краторная булка N-200i»')
    def click_ingredient_button(self):
        self.click_element_with_wait(StartPageLocators.BUN_N200i)

    @allure.step('Находим с ожиданием элемент «Детали ингредиента»')
    def find_order_details(self):
        return self.find_element_with_wait(StartPageLocators.ORDER_DETAILS)

    @allure.step('Закрываем модальное окно «Детали ингредиента»')
    def close_ingredient_details(self):
        self.click_element_with_wait(StartPageLocators.CLOSE_ORDER_DETAILS)

    @allure.step('Добалвяем булку')
    def add_ingredient(self):
        return self.drag_and_drop_elements(StartPageLocators.BUN_N200i, StartPageLocators.DRUG_AND_DROP_BUN)

    @allure.step('Проверяем счетчик')
    def check_order_count(self):
        return self.get_text(StartPageLocators.ORDER_COUNT)

    @allure.step('Находим с ожиданием элемент «Ваш заказ начали готовить»')
    def order_is_creating(self):
        return self.find_element_with_wait(StartPageLocators.ORDER_IS_CREATING)

    @allure.step('Добавляем булку, нажимаем на кнопку «Оформить заказ», закрываем модальное окно')
    def make_order(self):
        self.add_ingredient()
        self.click_confirm_order()
        self.close_ingredient_details()

