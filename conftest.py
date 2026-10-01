import pytest
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# ========== Custom Options ========== #
def pytest_addoption(parser):
    parser.addoption(
        "--timeout", action="store", type=int, default=15,
        help="Default explicit wait seconds"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


# ========== Fixtures ========== #
@pytest.fixture
def driver(request, pytestconfig):
    # Set lokasi cache biar gak selalu download ulang
    os.environ["WDM_LOCAL"] = "1"  # aktifkan cache lokal
    os.environ["WDM_CACHE"] = str(Path.home() / ".wdm")

    service = FirefoxService(GeckoDriverManager().install())
    d = webdriver.Firefox(service=service)
    d.maximize_window()
    
    yield d 

    # Screenshot otomatis jika test PASS
    if request.node.rep_call.passed:
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = os.path.join(screenshot_dir, f"{request.node.name}.png")
        d.save_screenshot(file_name)
        print(f"\n✅ Screenshot PASS disimpan: {file_name}")
    d.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://bldevwapp11/Insubsyt2/Account/Login?ReturnUrl=%2fInsubsyt2%2fAccount%2fLogOff"


@pytest.fixture(scope="session")
def default_timeout(pytestconfig):
    return pytestconfig.getoption("--timeout")


@pytest.fixture
def wait(driver, default_timeout):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(driver, default_timeout)


