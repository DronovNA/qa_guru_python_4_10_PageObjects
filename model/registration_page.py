import os

from selene.support.shared import browser
from selene import be, have, command


class RegistrationPage:
    def open_registration_form(self):
        browser.open("/automation-practice-form")
        return self

    def page_set_up(self):
        browser.all('[class="ob.widget.items.container"]').perform(command.js.remove)
        browser.all("#RightSide_Advertisement").perform(command.js.remove)
        browser.all("#adplus-anchor").perform(command.js.remove)
        return self

    def type_first_name(self, value):
        browser.element("#firstName").should(be.blank).type(value)
        return self

    def type_last_name(self, value):
        browser.element("#lastName").should(be.blank).type(value)
        return self

    def type_email(self, value):
        browser.element("#userEmail").should(be.blank).type(value)
        return self

    def choose_gender(self):
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        return self

    def type_phone_number(self, value):
        browser.element("#userNumber").should(be.blank).type(value)
        return self

    def input_date_of_birth(self):
        browser.element("#dateOfBirthInput").perform(command.js.scroll_into_view)
        browser.element("#dateOfBirthInput").should(be.clickable).click()
        browser.element('[value="1998"]').should(be.clickable).click()
        browser.element(
            f".react-datepicker__day--020:not(.react-datepicker__day--outside-month)"
        ).should(be.clickable).click()
        return self

    def type_subjects(self, subject):
        browser.element(".subjects-auto-complete__input>input").should(be.blank).type(
            subject
        ).press_enter()
        return self

    def choose_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).perform(
            command.js.click
        )
        return self

    def upload_file(self):
        browser.element("#uploadPicture").type(
            os.getcwd() + r'\test\resources\example.png'
        )
        return self

    def type_address(self, value):
        browser.element("#currentAddress").should(be.blank).type(value)
        browser.element("footer").perform(command.js.remove)
        return self

    def choose_state(self):
        browser.element("#state").should(be.clickable).click()
        browser.element('//div[text()="NCR"]').should(be.clickable).click()
        browser.element("#city").should(be.clickable).click()
        browser.element('//div[text()="Delhi"]').should(be.clickable).click()
        return self

    def choose_city(self):
        browser.element("#city").should(be.clickable).click()
        browser.element('//div[text()="Delhi"]').should(be.clickable).click()
        return self

    def fill_registration_form(self, User):
        self.open_registration_form()
        self.page_set_up()
        self.type_first_name(User.first_name)
        self.type_last_name(User.last_name)
        self.type_email(User.email)
        self.choose_gender()
        self.type_phone_number(User.phone_number)
        self.input_date_of_birth()
        self.type_subjects(User.subject)
        self.choose_hobbies()
        self.upload_file()
        self.type_address(User.current_address)
        self.choose_state()
        self.choose_city()

    def click_submit_button(self):
        browser.element("#submit").submit()
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )
        return self

    def should_registered_user_with(self):
        browser.all(".table-responsive td").by(
            have.exact_texts(
                "Test Testovich"
                "Test@example.com"
                "Female"
                "8999758985"
                "01 March,1998"
                "Computer Science"
                "Reading"
                "example.png"
                "Test test test"
                "NCR Delhi"
            )
        )
        return self
