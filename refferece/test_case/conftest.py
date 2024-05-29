import pytest
from selenium import webdriver

from selenium.webdriver.chrome import webdriver
from selenium import webdriver




@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # driver.get("https://opensource-demo.orangehrmlive.com/")
    return driver



# -----------code for cross browser testing----

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     # elif browser == "edge":
#     #     driver == webdriver.Edge()
#     else:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#
#         driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver




# -----------------------------------------------------------------------------------------------------------
# # while generate html Reprot we can menupulate there report and add or remove variables with help of these codes:-
# def pytest_metadata(metadata):
#     # To add
#     metadata["Environment"] = "Test"
#     metadata['Project Name'] = "OrengeHRM"
#     metadata['Module Name'] = 'Employee'
#     metadata['Tester'] = 'Credence'
#     # To remove
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)





@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1231", "Fail"),
    ("Admin1", "admin1231", "Fail")
])
def getDataforlogin(request):
    return request.param





