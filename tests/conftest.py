import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")





@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("D:/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("D:/geckodriver-v0.31.0-win64/geckodriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "IE":
        s = Service("D:/IEDriverServer_x64_4.2.0/IEDriverServer.exe")
        driver = webdriver.Chrome(service=s)


    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()




