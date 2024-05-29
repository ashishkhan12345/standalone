import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://phptravels.net")
driver.find_element(By.LINK_TEXT, "ACCOUNT").click()
driver.find_element(By.LINK_TEXT, "Login").click()
# driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
Wait = WebDriverWait(driver, 10, poll_frequency=0.5)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("admin@phptravels.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("demoadmin")
driver.find_element(By.XPATH,"//button[@id='submitBTN']").click()
# WebDriverWait(driver, 10, poll_frequency=0.5)
# try:

#     # Wait = WebDriverWait(driver, 10, poll_frequency=0.5)
#     # time.sleep(10)
#     driver.title == "Dashboard"
#     # print("tes pass")
# except NoSuchElementException:
#     print("test fail")
if driver.title == "Dashboard":
    assert True
    print("test pass")
else:
    assert False


