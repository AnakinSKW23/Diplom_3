from selenium.webdriver.firefox import webdriver
import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()