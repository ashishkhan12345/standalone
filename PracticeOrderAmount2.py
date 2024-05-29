import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("--headless")

# ----------------------------------my script start-------------------------------------------------------------

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
l = len(driver.find_elements(By.XPATH,"//tbody/tr/td[4]"))
price_list = []
for r in range(1,l-2):
    var = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child("+str(r)+") td:nth-child(4)").text
    product_price=(var[1:])
    price_list.append(float(product_price))
var2 = sum(price_list)
# print(var2)
Exp_sub_total = round(var2,2)
Exp_tax = round((Exp_sub_total*0.13),2)
Exp_total = Exp_sub_total+Exp_tax
Amount_list = []
for r in range(l-2,l+1):
    var = driver.find_element(By.XPATH,"//tbody/tr["+str(r)+"]/td[4]").text
    var2 = (var[1:])
    # print(var2)

    Amount = var2.replace(",","")
    Amount_list.append(float(Amount))
Act_sub_total = Amount_list[0]
Act_tax = Amount_list[1]
Act_total = Amount_list[2]
if Exp_sub_total == Act_sub_total:
    print("sub_total is match")
    assert True
else:
    print("test fail")
    assert False
if Exp_tax == Act_tax:
    print("Tax is match")
else:
    print("test fail")
    assert False
if Exp_total == Act_total:
    print("total is match")
    assert True
else:
    print("test fail")
    assert False
driver.close()

# -------------------------------------***********------------------------------------------------
# ----------this script save for select dropdown on line no.-97---------------------------------

# driver = webdriver.Chrome(options=chromeoptions)
# driver.maximize_window()
# driver.get("https://automation.credence.in/")
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@credence.in")
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("test@123")
# #click on login
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# #clicl on AppleMacbook Pro product
# driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
# #click on add to cart
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# #click on continue shoping
# driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.btn-lg").click()
# #click on Apple ipad Ratina product
# driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
# #click on add to cart
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# #click to continue shoping
# driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
# #click to Headphones product
# driver.find_element(By.XPATH,"//h3[normalize-space()='Headphones']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# Select(driver.find_element(By.XPATH,"//tbody/tr[3]/td[3]/select[1]")).select_by_index(2)
# time.sleep(4)
# l = len(driver.find_elements(By.XPATH,"//tbody/tr/td[4]"))
# price_list = []
# for r in range(1,l-2):
#     var = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child("+str(r)+") td:nth-child(4)").text #when use .text
#     product_price=(var[1:])
#     price_list.append(float(product_price))
# var2 = sum(price_list)
# # print(var2)
# Exp_sub_total = round(var2,2)
# Exp_tax = round((Exp_sub_total*0.13),2)
# Exp_total =round((Exp_sub_total+Exp_tax),2)
# Amount_list = []
# for r in range(l-2,l+1):
#     var = driver.find_element(By.XPATH,"//tbody/tr["+str(r)+"]/td[4]").text
#     var2 = (var[1:])
#     # print(var2)
#     Amount = var2.replace(",","")
#     Amount_list.append(float(Amount))
# Act_sub_total = Amount_list[0]
# Act_tax = Amount_list[1]
# Act_total = Amount_list[2]
# # print(Act_total)#----------------------
# if Exp_sub_total == Act_sub_total:
#     print("sub_total is match")
#     assert True
# else:
#     print("test fail")
#     assert False
# if Exp_tax == Act_tax:
#     print("Tax is match")
# else:
#     print("test fail")
#     assert False
# if Exp_total == Act_total:
#     print("total is match")
#     assert True
# else:
#     print("test fail")
#     assert False