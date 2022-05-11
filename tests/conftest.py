import json

from pytest import fixture
from config import Config

from selenium import webdriver

data_path = "tests/test_data.json"


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(scope="session")
# @fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    # return browser
    yield browser

    #     Teardown code below
    print("\nI'm tearing down this browser")


# we need webdriver for each browser
# @fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Opera], scope="session")
@fixture(params=[webdriver.Chrome], scope="session")
# @fixture(scope="function")
def browser(request):
    driver = request.param
    drvr = driver()
    # browser = webdriver.Firefox()
    # return browser
    yield drvr
    drvr.quit()
    #     Teardown code below
    print("\nI'm tearing down this browser")


@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        # default="dev"
        help="Envs to run tests against."
    )


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg
