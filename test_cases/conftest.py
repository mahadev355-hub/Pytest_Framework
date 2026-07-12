"""conftest.py is a special file in pytest that acts like a shared configuration and utility hub for your tests.
conftest.py keeps things centralized and reusable.

You don’t import it manually—pytest automatically discovers and uses it."""

"""In pytest, a fixture is a way to set up and tear down things your tests need—so you don’t repeat the same setup code in every test."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""In pytest, parser.addoption() is used to add custom command-line arguments when running tests.
It lets you pass extra information into your test run from the terminal."""

"""In pytest, we pass parser because it is the object that manages command-line arguments for the test run.
parser is an instance of pytest’s internal command-line parser"""
"""request is a special pytest object that represents:
Information about the currently running test and its environment"""

"""this is a hook function "pytest_addoption" we are defining below. this is a hook because pytest automatically calls it during the command-line parsing stage."""
"""A predefined point where pytest allows your code to run."""

"""Parallel testing is running multiple tests at the same time instead of one after another.

In pytest, this is used to reduce total test execution time by using multiple CPU cores or processes.
use pytest-xdist and when executing in terminal just add -n 3 or 4 to the pytest -s -v command line so that it creates 3 or 4 workers to run
parallelly. but there should not be any dependencies between test cases to avoid conflict"""

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify the browser: chrome or safari")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup():
    global driver
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    """below code can be enabled if we want to run the code by opening browser"""
    """if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Unknown browser %s" % browser)"""
    return driver

