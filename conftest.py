import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def language(request):
    page_language = request.config.getoption("language")
    yield page_language
