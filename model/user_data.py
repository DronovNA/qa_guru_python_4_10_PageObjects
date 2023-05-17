from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    birth_year: str
    birth_month: str
    birth_day: str
    subject: str
    hobby: str
    upload_filename: str
    current_address: str
    state: str
    city: str
