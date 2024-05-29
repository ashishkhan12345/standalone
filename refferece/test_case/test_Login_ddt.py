from pageobject.Loginpage import loginpage
from utilites import XLutils
from utilites.Logger import LogGenerator
from utilites.readproperties import readconfig


class Test_Login_DDT:
    url = readconfig.geturl()
    log = LogGenerator.loggen()

    path = "C:\\Users\DEP\\PycharmProjects\\pythonProject\\test_case\\test_data\\LoginData.xlsx"

    def test_login_ddt_006(self, setup):
        self.log.info("test_login_ddt_006 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("opening this url--->" + self.url)
        self.lp = loginpage(self.driver)
        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        print("no of rows---->" , self.rows)
        login_status = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, "Sheet1", r, 2)
            self.password = XLutils.readData(self.path, "Sheet1", r, 3)
            self.lp.enter_username(self.username)
            self.log.info("Entering username--->" + self.username)
            self.lp.enter_passowrd(self.password)
            self.log.info("Entering password--->" + self.password)
            self.lp.click_login()
            self.log.info("click on login")
            if self.lp.login_status() == True:
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\" + self.username + self.password + "test_login_ddt_006-pass.png")
                self.lp.click_menu_botton()
                self.log.info("ckick menu botton")
                self.lp.click_logout_botton()
                self.log.info("ckick logout botton")
                login_status.append("pass")
                XLutils.writeData(self.path, "Sheet1", r, 4, "pass")
            else:
                login_status.append("fail")
                XLutils.writeData(self.path, "Sheet1", r, 4, "fail")
                self.driver.save_screenshot(
                    "C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\" + self.username + self.password + "test_login_ddt_006-fail.png")
        print(login_status)
        if self.lp.login_status() == True:
            if "fail" not in login_status:
                self.log.info("test_login_ddt_006 is Passed")
                assert True
            else:
                self.log.info("test_login_ddt_006 is Failed")
                assert False
        else:
            if "fail" in login_status:
                assert True
            else:
                self.log.info("test_login_ddt_006 is Failed")
                assert False
        self.driver.close()
        self.log.info("test_login_ddt_006 is Completed")




