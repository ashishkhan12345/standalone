import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automation.credence.in/")
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@credence.in")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("test@123")
#click on login
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#clicl on AppleMacbook Pro product
driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
#click on add to cart
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
#click on continue shoping
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.btn-lg").click()
#click on Apple ipad Ratina product
driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
#click on add to cart
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
#click to continue shoping
driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
#click to Headphones product
driver.find_element(By.XPATH,"//h3[normalize-space()='Headphones']").click()
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
#click on proceed to cheakout
driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-lg']").click()
#enter first name
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Ashishkhan")
#enter last name
driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("Mulla")
#enter phon number
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9991929355")
#enter address
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("A/P-dhankawdi,pune")
# enter state
Select(driver.find_element(By.XPATH,"//select[@id='state']")).select_by_index(1)
# enter zip code
driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("411043")
# enter owner name
driver.find_element(By.XPATH,"//input[@id='owner']").send_keys("Ashish")
# enter CVV
driver.find_element(By.XPATH,"//input[@id='cvv']").send_keys("257")
# enter card number
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("4716")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("1089")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("9971")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("6531")
# enter expiring date(year)
Select(driver.find_element(By.XPATH,"//select[@id='exp_year']")).select_by_index(3)
# enter expiring date(month)
Select(driver.find_element(By.XPATH,"//select[@id='exp_month']")).select_by_visible_text("February")
# click on countinue to cheakout
driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()
try:
    driver.find_element(By.XPATH,"//p[@class='lead w-lg-50 mx-auto']").is_displayed()
    print("test is pass")
except NoSuchElementException:
    print("test is fail")

