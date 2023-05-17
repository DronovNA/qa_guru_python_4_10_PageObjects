from model.registration_page import RegistrationPage
from model.user_data import User


def test_fill_and_submit_form(browser_options):
    Testovich = User(
        firstname="Тест",
        lastname="Тестович",
        email="Test@example.com",
        phone="89997589856",
        subjects=("sci"),
        address="Test test test",
    )
    registration_page = RegistrationPage()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(Testovich)

    registration_page.click_submit_button()

    registration_page.should_registered_user_with()
