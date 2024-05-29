import time

from pageobject.Loginpage import loginpage
from pageobject.addemp_page import addemployee
from utilites.readproperties import readconfig
from utilites.Logger import LogGenerator

class Test_add_employee:
    url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    log = LogGenerator.loggen()
    def test_add_employee(self,setup):
        self.log.info("test case is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("go to this url-->"+ self.url)

        self.lp = loginpage(self.driver)
        time.sleep(3)
        self.lp.enter_username(self.username)
        self.lp.enter_passowrd(self.password)
        self.lp.click_login()
        self.ae = addemployee(self.driver)
        self.ae.click_pim()
        self.ae.click_add()
        self.ae.enter_firstname("adi")
        time.sleep(3)

        self.ae.enter_middlename("rao")
        time.sleep(3)
        # self.driver.save_screenshot("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\"
                                    # "until_middle_name_pass.png")

        self.ae.enter_lastname("jadhav")
        time.sleep(3)



        self.ae.click_save()
        if self.ae.addemployee_status() == True:
            self.driver.implicitly_wait(10)

            # self.driver.save_screenshot("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\"
            #                             "test_addemp_page_pass.png")

            assert True

        else:
            assert False

        self.driver.close()



