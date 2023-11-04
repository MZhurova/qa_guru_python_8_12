import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def browser_config():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 3

    yield

    browser.quit()


