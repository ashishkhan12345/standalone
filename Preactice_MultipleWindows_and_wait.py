import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
WindowsOpen = driver.window_handles
driver.switch_to.window(WindowsOpen[1])
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='New Window']")))
print(driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']").text)
driver.switch_to.window(WindowsOpen[0])


print(driver.find_element(By.XPATH,"//h3[normalize-space()='Opening a new window']").text)

driver.quit()
# driver.close()

