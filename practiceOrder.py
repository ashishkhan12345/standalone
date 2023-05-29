# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common import NoSuchElementException
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Firefox()
# driver.get("https://automation.credence.in/")
# driver.find_element(By.LINK_TEXT, "Login").click()
# # Enter EMAIL ID
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
# # Enter password using CSS_SELECTOR
# driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
#
# # Click on login button
# driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# # Click on product-->Apple Macbook Pro
# driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple Macbook Pro']").click()
#
# # Add To Cart
# driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# # Click of Proceed to Checkout
# driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
# time.sleep(3)
#
# # Check Out Page
# # Enter First Name
# driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
#
# # Enter Last Name
# driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("IT")
#
# # Enter Phone
# driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
#
# # Enter address
# driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankwadi, Pune, Maharashtra, India")
#
# # Enter zip code
# driver.find_element(By.CSS_SELECTOR, "#zip").send_keys("411043")
#
# # Select state
# Select(driver.find_element(By.XPATH, "//select[@id='state']")).select_by_index(2)
#
# # Enter Owner Name
# driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
# # Enter Card CVV
# driver.find_element(By.CSS_SELECTOR, "#cvv").send_keys("257")
#
# # Enter Card Number
# # 4716 1089 9971 6531
# driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4716")
# driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
# driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
# driver.find_element(By.CSS_SELECTOR, "input[id='cardNumber']").send_keys("6531")
# # Select Card Exp Year
# Select(driver.find_element(By.XPATH, "//select[@id='exp_year']")).select_by_visible_text("2025")
#
# # Select Month
# Select(driver.find_element(By.XPATH, "//select[@id='exp_month']")).select_by_index(2)
#
# # Click Sumit
# driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/")
driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@credence.in")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
# enter email address
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("credance")
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("IT")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(9091929355)
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("dhankawadi, pune, maharashtra")
driver.find_element(By.XPATH, "//input[@id='zip']").send_keys(411043)
Select(driver.find_element(By.XPATH, "//select[@id='state']")).select_by_index(1)
driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Ashish")
driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("257")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4716")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6531")
Select(driver.find_element(By.XPATH, "//select[@id='exp_year']")).select_by_index(3)
Select(driver.find_element(By.XPATH, "//select[@id='exp_month']")).select_by_visible_text("February")
driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
time.sleep(4)

try:
    driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']")
    print("test case has been pass")
    driver.save_screenshot("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screenshots\\orderplaced.png")
except NoSuchElementException:
    print("login test case is failed")


# try:
#     driver.find_element(By.XPATH, "//p[normalize-space()='Your order has been placed successfully.']")
#     print("Login Test Case is Passed")
#     driver.save_screenshot("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screenshots\\OrderPlaced2.png")
# except NoSuchElementException:
#     print("Login Test Case is Failed")

# driver.close()
# driver.close() vs driver.quit()
# how to handle alters