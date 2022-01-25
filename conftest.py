import pytest
from selenium.webdriver import Firefox


@pytest.fixture()
def browser():
    _driver = Firefox()
    yield _driver
    _driver.quit()
