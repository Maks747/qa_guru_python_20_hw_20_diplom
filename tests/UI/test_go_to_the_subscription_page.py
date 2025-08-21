from start.model.pages.subscription_page import SubscriptionPage
import allure

@allure.title("Проверка страницы подписки")
def test_button_for_more_detail(browser_settings):
    browser = (browser_settings)

    with allure.step('Открыть главную страницу'):
        subscription_page = SubscriptionPage()
        subscription_page.open_main_page()

    with allure.step('Нажать кнопку Подробнее'):
        subscription_page.click_for_more_detail_button()

    with allure.step('Проверка страницы подписки'):
        subscription_page.check_subscription_page()