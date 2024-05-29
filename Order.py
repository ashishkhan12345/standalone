import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
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
# Click of Proceed to Checkout
driver.find_element(By.LINK_TEXT, "Proceed to Checkout").click()
# Check Out Page
# Enter First Name
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
# Enter Last Name
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("IT")
# Enter Phone
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
# Enter address
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankwadi, Pune, Maharashtra, India")
# Enter zip code
driver.find_element(By.CSS_SELECTOR, "#zip").send_keys("411043")
# Select state
Select(driver.find_element(By.XPATH, "//select[@id='state']")).select_by_index(2)
# Enter Owner Name
driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
# Enter Card CVV
driver.find_element(By.CSS_SELECTOR, "#cvv").send_keys("257")
# Enter Card Number
# 4716 1089 9971 6531
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4716")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
driver.find_element(By.CSS_SELECTOR, "input[id='cardNumber']").send_keys("6531")
# Select Card Exp Year
Select(driver.find_element(By.XPATH, "//select[@id='exp_year']")).select_by_visible_text("2025")
# Select Month
Select(driver.find_element(By.XPATH, "//select[@id='exp_month']")).select_by_index(2)
# Click Sumit
driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
time.sleep(4)

try:
    driver.find_element(By.XPATH, "//p[normalize-space()='Your order has been placed successfully.']")
    print("Login TestCase is Passed")
    driver.save_screenshot(".\\Screenshots\\OrderPlaced2.png")
except NoSuchElementException:
    print("Login TestCase is Failed")

# driver.close()
# driver.close() vs driver.quit()
# how to handle alters