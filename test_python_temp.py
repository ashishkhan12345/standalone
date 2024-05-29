import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chromoptions = webdriver.ChromeOptions()
chromoptions.add_argument("--headless")


class Test_login_001:

  # def test_mul_001(self):
  #   a=2
  #   b=4
  #   sum = a*b
  #   if sum == 8:
  #       print ("test_mul_001 is passed")
  #       assert True
  #   else:
  #       print("test_mul_001 is failed")
  #       assert False

  # def test_google_001(self):
  #     driver = webdriver.Chrome()
  #     driver.get("https://www.google.co.in/")
  #     logo = driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
  #     if logo == True:
  #     # if driver.title == "Google": #--second approach to find logo or title
  #         print("logo")
  #         driver.close()
  #         assert True
  #     else:
  #         assert False
  ##-----agar script me print(driver.title) likhenge to page ka title print hoga------
  #
  #
  # def test_oranghrm(self):
  #     driver = webdriver.Chrome()
  #     driver.get("https://opensource-demo.orangehrmlive.com/")
  #     wait = WebDriverWait(driver,6,poll_frequency=0.5)
  #     wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder='Username']")))
  #     # driver.implicitly_wait(4)
  #     driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  #     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
  #     wait.until(ec.presence_of_element_located((By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")))
  #     driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
  #     driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
  #     # time.sleep(4)
  #     wait.until(ec.presence_of_element_located((By.XPATH,"//img[@acllt='company-branding']")))
  #     logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
  #     if logo == True:
  #       assert True
  #       print("test case of orangeHRM has been pass")
  #
  #     else :
  #        print("fail")
  #        assert False

  #
  #     #ye bhi conditonal statment run hoti hai--
  #     # if driver.title=="OrangeHRM":
  #     #   print("test case of orangeHRM has been pass")
  #     #   driver.quit()
  #     #   assert True
  #     # else:
  #     #   print("test case of orangeHRM has been fail")
  #     #   driver.quit()
  #     #   assert False
  #
      #if use try except block then ----
      # try:
      #   driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']")
      #   print("test case of orangeHRM has been pass")
      #   return True
      # except NoSuchElementException:
      #   print("fail")
      #   return False

  # agar orangeHRM ki is test case me conditional statment and try except block dono ek sath use karna ho to
  # kese karege kahi kuch notes ye example mila to use karke dekho






  #
  # def test_infosys_page(self):
  #   driver = webdriver.Chrome()
  #   driver.get(" https://career.infosys.com/")
  #   driver.maximize_window()
  #   wait = WebDriverWait(driver,4,poll_frequency=0.5)
  #   wait.until(ec.presence_of_element_located((By.XPATH,"//a[normalize-space()='Sign In']")))
  #   driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
  #   time.sleep(4)
  #   driver.find_element(By.XPATH, "//input[@id='username']").send_keys("ashishkhanmulla11@gmail.com")
  #   driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Ashish@123")
  #   driver.find_element(By.XPATH,"//button[@id='btnSubmit']").click()
  #   driver.implicitly_wait(4)
  #   lop = driver.find_element(By.XPATH,"//div[@class='marT80 customcardThree ng-star-inserted']//div[@name='Welcome'][normalize-space()='Welcome, Ashishkhan']").is_displayed()
  #   time.sleep(4)
  #   if lop == True:
  #     assert True
  #   else:
  #     assert False
  #
  # def test_credance(self):
  #   driver = webdriver.Chrome()
  #   driver.get("https://credence.in/")
  #   offer = driver.find_element(By.XPATH,"//span[@class='text-white b label']").text
  #   print(offer)
  #   print(("title is =")+driver.title)
  #   if driver.title == "Credence":
  #     print("test pass")
  #     driver.close()
  #     assert True
  #   else:
  #     print("test fail")
  #     driver.close()
  #     assert False

  #    // img[ @ src = '/website/images/enquiry.png']
  # // div[@class ='quickfinder-description gem-text-output'] // p // a[2]


  def test_credance_mob_no(self):
    driver = webdriver.Chrome()
    driver.get("https://credence.in/")
    driver.find_element(By.XPATH,"// img[ @ src = '/website/images/enquiry.png']").click()
    wait=WebDriverWait(driver,6,poll_frequency=0.5)
    wait.until(ec.presence_of_element_located((By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a")))
    l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
    contact_list = []
    for r in range(1,l+1):
      contact = driver.find_element(By.XPATH,"// div[@class ='quickfinder-description gem-text-output'] // p // a["+str(r)+"]").text
      # print(contact)
      v = (contact[0:])
      contact_list.append(v)
    # print(contact_list)
    # #first approach--
    # if "+91 9091929355" in contact_list:
    #   print("test pass")
    #   assert True
    # else:
    #   print("test fail")
    #   assert False
    # Second approach --
    if contact_list[4]=="+91 9091929355":
      print(contact_list[4])
      print("test is pass")
      # print(contact_list)
      assert True
    else:
      print("test fail")
      assert False
















