from selene import browser, have, command


class RegistrationPage:
    def open_main_page(self):
            browser.open("")

    def click_for_free_button(self):
            browser.element('[data-testid="try_free_button_text"]').perform(command.js.click)

    def check_registration_page(self):
            browser.element('.Sign_sign__form-title__USFwT').should(
                have.text('Зарегистрируйтесь и смотрите START 7 дней бесплатно'))
