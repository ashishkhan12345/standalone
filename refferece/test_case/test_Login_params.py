import time


from pytest_practice_part_1_del.Page_object.logonpage import logonpage
from pytest_practice_part_1_del.Utilites.Readproperties import readconfig
# from utilites.readproperties import readconfig
from utilites.Logger import LogGenerator


class Test_Login_Params:
    url = readconfig.geturl()
    # log = LogGenerator.loggen()

    def test_login_params_004(self, setup, getDataforlogin):
        self.driver = setup
        # self.log.info("test_login_params_004 is started")
        self.driver.get(self.url)
        # self.log.info("go to this url-->"+self.url)
        self.lp = logonpage(self.driver)
        self.lp.enter_username(getDataforlogin[0])
        # self.log.info("entering this username-->"+getDataforlogin[0])
        self.lp.enter_password(getDataforlogin[1])
        # self.log.info("entering this password-->"+getDataforlogin[1])
        self.lp.click_login_botton()
        # self.log.info("click on login botton")
        if self.lp.login_status() == True:
            if getDataforlogin[2] == "Pass":
                self.lp.click_menu_botton()
                # self.log.info("click on menu botton")
                self.lp.click_logout_botton()
                # self.log.info("click on lougout botton")
                # self.log.info("test_login_params_004 is Passed")
                assert True
            else:
                # self.log.info("test_login_params_004 is Failed")
                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                # self.log.info("test_login_params_004 is Failed")
                assert False

        self.driver.close()
        # self.log.info("test_login_params_004 is complited")
