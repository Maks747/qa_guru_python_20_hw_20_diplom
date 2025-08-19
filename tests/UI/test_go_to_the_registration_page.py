from start.model.pages.registration_page import RegistrationPage
import allure

@allure.title("Проверка страницы регистрации")
def test_button_for_free(browser_settings):
    browser = (browser_settings)

    with allure.step('Открыть главную страницу'):
        registration_page = RegistrationPage()
        registration_page.open_registration_page()

    with allure.step('Нажать кнопку бесплатного периода'):
        registration_page.click_for_free_button()

    with allure.step('Проверка страницы регистрации'):
        registration_page.check_registration_page()