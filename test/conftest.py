import pytest
from selene.support.shared import browser
import os


@pytest.fixture(scope='function')
def browser_options():
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com')