import time
from pageobject.addemp_page import addemployee
from pageobject.Loginpage import loginpage
from utilites.readproperties import readconfig
from utilites import XLutilssss, XLutils
from utilites.Logger import LogGenerator


class Test_Add_Emp_DDT:
    Url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\test_case\\test_data\\emloyeelist.xlsx"

    def test_addEmp_ddt_005(self, setup):
        self.log.info("test_addEmp_ddt_005 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to Url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.log.info("Entering UserName-->" + self.username)
        self.lp.enter_passowrd(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.click_login()
        self.log.info("Click On login")
        self.ae = addemployee(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        self.ae.click_pim()
        self.log.info("Click On PIM")
        self.ae.click_add()
        self.log.info("Click On Add")
        status_list = []
        for r in range(2, self.rows + 1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)
            # time.sleep(2)
            self.ae.enter_firstname(self.FirstName)
            self.log.info("Entering FirstName-->" + self.FirstName)
            self.ae.enter_middlename(self.MiddleName)
            self.log.info("Entering MiddleName-->" + self.MiddleName)
            self.ae.enter_lastname(self.LastName)
            self.log.info("Entering LastName--> " + self.LastName)
            # time.sleep(2)
            self.ae.click_save()
            self.log.info("Click on Save")
            if self.ae.addemployee_status() == True:
                self.ae.Click_addEmployee()
                # time.sleep(2)
                status_list.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")
                # time.sleep(4)
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\test_addEmp_003-pass.png")
            else:
                status_list.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
                # time.sleep(4)
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\test_addEmp_003-fail.png")

        print(status_list)

        time.sleep(2)
        self.lp.click_menu_botton()
        self.log.info("Click on MenuButton")
        self.lp.click_logout_botton()
        self.log.info("Click on Logout Button")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("test_addEmp_ddt_005 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_ddt_005 is Failed")
            assert False
        self.log.info("test_addEmp_ddt_005 is Completed")
