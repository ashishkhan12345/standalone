import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#information alert
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
Alert(driver).accept() # this is accepting alert at driver
print(driver.find_element(By.XPATH,"//p[@id='result']").text)

# confermation alert
driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
# Alert(driver).dismiss() #this is dismiss the alter at driver
# print(driver.find_element(By.XPATH,"//p[@id='result']").text)
print(Alert(driver).text) #this is print to alert massage
alert = Alert(driver)
Alert(driver).accept() #this is accepting alter at driver
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
#altert promt
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert.send_keys("Hello all")
Alert(driver).accept()
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
