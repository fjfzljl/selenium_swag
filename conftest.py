import sys
import logging
import pytest
from py.xml import html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# logger = logging.getLogger("unit test")


def pytest_configure(config):
    config._metadata["test software version"] = "0.1"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Description"))
    cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except AttributeError as error:
        logging.info("AttributeError trying to pytest_html_results_table_row - start")
        logging.error(error)
        logging.info("AttributeError trying to pytest_html_results_table_row - end")
    except Exception as e:
        logging.error(
            f"Unknown Exception trying to pytest_html_results_table_row : {e}"
        )
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


@pytest.fixture(scope="module")
def suite_setupteardown():
    logging.info("suite_setupteardown fixture start...")

    logging.info("software install ...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield driver

    logging.info("software uninstall...")

    driver.quit()

    logging.info("suite_setupteardown fixture end...")


@pytest.fixture
def eachtest_setupteardown():
    logging.info("eachtest_setupteardown fixture start...")

    logging.info("change system configuration...")

    yield

    logging.info("recover system configuration...")

    logging.info("eachtest_setupteardown fixture end...")
