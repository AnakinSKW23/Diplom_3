from pages.base_page import BasePage
from src.locators import StartPageLocators, OrderFeedLocators, PersonalAccountLocators
import allure

class OrderFeedPage(BasePage):

    @allure.step('Кликаем на заказ в «Ленте заказов»')
    def click_first_order(self):
        self.click_element_with_wait(OrderFeedLocators.FIRST_ORDER)

    @allure.step('Находим текст элемента')
    def find_compound_text(self):
        return self.find_element_with_wait(OrderFeedLocators.COMPOUND_ORDER)

    @allure.step('Получаем номер заказа')
    def get_order_numbers(self):
        return self.find_element_with_wait(OrderFeedLocators.ORDER_NUMBERS).text

    @allure.step('Получаем номер заказа в «Истории заказов»')
    def get_last_order_number(self):
        return self.find_element_with_wait(PersonalAccountLocators.LAST_ORDER_NUMBER).text

    @allure.step('Кликаем на «Ленту заказов»')
    def click_history_button(self):
        self.click_element(StartPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Получаем количество заказов за все время')
    def get_all_time_numbers_of_orders(self):
        return self.get_text(OrderFeedLocators.ORDERS_COUNTER_ALL_TIME)

    @allure.step('Получаем количество заказов за сегодня')
    def get_today_numbers_of_orders(self):
        return self.get_text(OrderFeedLocators.ORDERS_COUNTER_TODAY)

    @allure.step('Кликаем с ожиданием на «Ленту заказов»')
    def click_history_button_with_wait(self):
        self.click_element_with_wait(StartPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Получаем номер заказа после обновления информации')
    def get_order_number_with_template(self):
        self.wait_for_element_located(OrderFeedLocators.ORDER_NUMBER)
        self.wait_for_new_text(OrderFeedLocators.ORDER_NUMBER, "9999")
        return self.get_text(OrderFeedLocators.ORDER_NUMBER)

    @allure.step('Получаем номер заказа «В работе» после обновления информации')
    def get_order_numer_in_work_with_template(self):
        self.wait_for_element_located(OrderFeedLocators.ORDER_NUMBER_IN_WORK)
        self.wait_for_new_text(OrderFeedLocators.ORDER_NUMBER_IN_WORK, "Все текущие заказы готовы!")
        return self.get_text(OrderFeedLocators.ORDER_NUMBER_IN_WORK)

