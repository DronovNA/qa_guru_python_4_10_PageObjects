from model.registration_page import RegistrationPage
from model.user_data import User


def test_fill_and_submit_form(browser_options):
    testovich = User(
        first_name="Тест",
        last_name="Тестович",
        email="Test@example.com",
        gender="Female",
        phone_number="89997589856",
        birth_year="March",
        birth_month="1998",
        birth_day="01",
        subject="sci",
        hobby="Computer Science",
        upload_picture="example.png",
        current_address="Test test test",
        state="NCR",
        city="Delhi",
    )

    registration_page = RegistrationPage()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(testovich)

    registration_page.click_submit_button()

    registration_page.should_registered_user_with()
