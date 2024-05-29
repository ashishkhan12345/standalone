from pageobject.Loginpage import loginpage
from utilites.readproperties import readconfig
from utilites.Logger import LogGenerator


class Test_login:
    url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    # log = LogGenerator.loggen()  "*"-->this sign for lin of code to generate log file
    def test_homepage(self,setup):
        self.driver = setup
        # self.log.info("test_homepage is started")  ---"*"
        # self.log.info("opening browser")  ---"*"
        self.driver.get(self.url)
        # self.log.info("go to this url-->"+self.url)   ---"*"

        if self.driver.title == "OrangeHRM":
            # self.log.info("test_homepage is passed")  ---"*"
            # self.log.info("page titile is -->" + self.driver.title)  ---"*"
            assert True

        else:
            # self.log.info("test_homepage is failed")  ---"*"
            assert False
        self.driver.close()
        # self.log.info("test_homepage is completed")  ---"*"

    def test_login(self,setup):
        self.driver = setup
        # self.log.info("test_login is started")   "*"-->this sign for lin of code to generate log file
        # self.log.info("opening browser")    ---"*"
        self.driver.get(self.url)
        # self.log.info("go to this url-->"+self.url)   ---"*"
        # loginpage(self.driver).enter_username("Admin")
        loginpage(self.driver).enter_username(self.username)
        # self.log.info("entering user name-->"+self.username)   ---"*"
        # loginpage(self.driver).enter_passowrd("admin123")
        loginpage(self.driver).enter_passowrd(self.password)
        # self.log.info("entering password-->"+self.password)   ---"*"
        loginpage(self.driver).click_login()
        # self.log.info("click on login botton")   ---"*"
        if loginpage(self.driver).login_status() == True:
            loginpage(self.driver).click_menu_botton()
            loginpage(self.driver).click_logout_botton()
            # self.driver.save_screenshot("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Screanshots\\login_test_case_"
            #                             "Pass.png")
            # self.log.info("this test case is passed")   ---"*"

            assert True
        else:
            # self.log.info("this test case is failed")   ---"*"

            assert False
        self.driver.close()
        # self.log.info("this test case is complited")   ---"*"






