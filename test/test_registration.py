from model.registration_page import RegistrationPage


def test_fill_and_submit_form(browser_options):
    registration_page = RegistrationPage()

    registration_page.page_open()
    registration_page.page_set_up()
    registration_page.type_first_name('Тест')
    registration_page.type_last_name('Тестович')
    registration_page.type_email('Test@example.com')
    registration_page.choose_gender()
    registration_page.type_phone_number('89997589856')
    registration_page.input_date_of_birth()
    registration_page.type_subjects('sci')
    registration_page.choose_hobbies()
    registration_page.upload_pictire()
    registration_page.type_address('Test test test')
    registration_page.choose_state()
    registration_page.choose_city()

    registration_page.click_submit_button()

    registration_page.should_registered_user_with()