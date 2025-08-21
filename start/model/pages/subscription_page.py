from selene import browser, have


class SubscriptionPage:
    def open_main_page(self):
            browser.open("")

    def click_for_more_detail_button(self):
            browser.element('.Button_text__CEKtw')

    def check_subscription_page(self):
        browser.element('.Button_text__CEKtw').should(have.text('Попробовать 30 дней бесплатно'))
