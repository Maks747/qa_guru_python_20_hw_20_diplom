from selene import browser, have


class TVPage:
    def __init__(self):
        self.button_tv = browser.element('[data-testid="tv_button"]')

    def open_main_page(self):
        browser.open("")

    def click_button_tv(self):
        self.button_tv.click()

    def check_tv_page_title(self):
        (browser.element('.TvSchedule_container__VQpHm').should
         (have.text('ТВ Каналы Онлайн и Программа Передач')))