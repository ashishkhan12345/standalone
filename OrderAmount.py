import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://automation.credence.in/")
driver.find_element(By.LINK_TEXT, "Login").click()
# Enter EMAIL ID
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
# Enter password using CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
# Click on login button
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# Click on product-->Apple Macbook Pro
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple Macbook Pro']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click countinue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
#Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple iPad Retina']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click countinue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
#Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Headphones']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

l = len(driver.find_elements(By.CSS_SELECTOR,"tbody tr"))
print(l)

for r in range(1, l-2):
    Product_Price = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child("+str(r)+") td:nth-child(4)").text
    print(Product_Price)

