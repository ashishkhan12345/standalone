import time

from pageobject.Loginpage import loginpage
from pageobject.addemp_page import addemployee
from utilites import XLutils
from utilites.Logger import LogGenerator
from utilites.readproperties import readconfig


class Test_ADD_EMP_DDT:
    log = LogGenerator.loggen()
    url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    path = "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\test_case\\test_data\\emloyeelist.xlsx"

    def test_add_emp_007(self, setup):
        self.log.info("test_add_emp_007 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("opening this url--->" + self.url)
        self.lp = loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.log.info("entering username")
        self.lp.enter_passowrd(self.password)
        self.log.info("entering password")
        self.lp.click_login()
        self.log.info("click login botton")
        self.ad = addemployee(self.driver)
        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        print("no of rows-->", self.rows)
        self.ad.click_pim()
        self.log.info("click on PIM botton")
        self.ad.Click_addEmployee()
        self.log.info("click on AddEmployee Botton")
        status_list = []
        for r in range(2, self.rows + 1):
            self.FirstName = XLutils.readData(self.path, "Sheet1", r, 2)
            self.MiddleName = XLutils.readData(self.path, "Sheet1", r, 3)
            self.LastName = XLutils.readData(self.path, "Sheet1", r, 4)
            self.ad.enter_firstname(self.FirstName)
            self.log.info("Entering FirstName")
            self.ad.enter_middlename(self.MiddleName)
            self.log.info("Entering MiddleName")
            self.ad.enter_lastname(self.LastName)
            self.log.info("Entering LastName")
            self.ad.click_save()
            self.log.info("click on save Botton")
            if self.ad.addemployee_status() == True:
                self.ad.Click_addEmployee()
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\add_emp_test_007_pass.png")
                status_list.append("Pass")
                XLutils.writeData(self.path, "Sheet1", r, 5, "Pass")
            else:
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\add_emp_test_007_fail.png")
                status_list.append("Fail")
                XLutils.writeData(self.path, "Sheet1", r, 5, "Fail")
        print(status_list)
        time.sleep(4)
        self.lp.click_menu_botton()
        self.log.info("click menu Botton")
        self.lp.click_logout_botton()
        self.log.info("click logout botton")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("add_emp_test_007 is passed")
            assert True
        else:
            self.log.info("add_emp_test_007 is failed")
            assert False
        self.log.info("add_emp_test_007 is Completed")
