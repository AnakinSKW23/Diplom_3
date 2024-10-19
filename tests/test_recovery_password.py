from pages.recovery_password_page import RecoveryPasswordPage
from data import Urls
import allure

@allure.suite('Тестируем восстановление пароля')
class TestRecoveryPassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_recovery_page(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        assert driver.current_url == Urls.RECOVERY_PAGE

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        assert driver.current_url == Urls.RESET_PAGE

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_visibility_password(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        recovery_password_page.set_password()
        recovery_password_page.click_show_password()
        assert recovery_password_page.check_password()
