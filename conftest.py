import pytest
#TODO: # Use pickle for setup cookies
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    request.cls.driver = driver
    yield driver
    driver.quit()
