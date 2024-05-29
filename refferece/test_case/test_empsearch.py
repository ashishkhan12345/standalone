import time

from pageobject.EmployeeSearchPage import EmployeeSearch
from pageobject.Loginpage import loginpage
from pageobject.addemp_page import addemployee
from utilites.Logger import LogGenerator
from utilites.readproperties import readconfig


class Test_Search_Emp:
    url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    log = LogGenerator.loggen()
    def test_search_emp_6(self,setup):
        self.driver = setup
        self.log.info("test case is started")
        self.driver.get(self.url)
        self.log.info("go to this url-->"+self.url)
        self.lp = loginpage(self.driver)
        time.sleep(3)
        self.lp.enter_username(self.username)
        self.log.info("entering this username-->"+self.username)
        self.lp.enter_passowrd(self.password)
        self.log.info("entering this password->"+self.password)
        self.lp.click_login()
        self.log.info("click on login botton")
        self.ae = addemployee(self.driver)
        self.ae.click_pim()
        self.log.info("click on pim botton")
        self.es = EmployeeSearch(self.driver)
        time.sleep(2)
        self.es.Enter_EmpName("David")
        self.log.info("entering emp name")
        time.sleep(2)
        self.es.Click_SearchButton()
        time.sleep(4)
        self.log.info("click on search botton")
        print(self.es.Search_Result())
        if self.es.Search_Result() ==True:
            self.log.info("search found")
            self.log.info("test case is passed")
            self.lp.click_menu_botton()
            self.log.info("click on menu botton")
            self.lp.click_logout_botton()
            self.log.info("click on lougout botton")
            assert True
        else:
            self.log.info("no search found")
            self.log.info("test case is failed")
            assert False
        self.driver.close()

# -------------------------------------------------------------------------------------------------------------
# sir ka banaya hua code----
# -------------------------------------------------------------------------------------------------------------
#
# import time
#
#
#
#
# from tt.EmployeeSearchPage import EmployeeSearch
# from tt.Loginpage import loginpage
# from tt.addemp_page import addemployee
# from Utilites.Logger import LogGenerator
# from Utilites.readproperties import readconfig
#
# class Test_Search_Emp:
#     Url = readconfig.geturl()
#     username = readconfig.getusername()
#     password = readconfig.getpassword()
#     log = LogGenerator.loggen()
#
#     def test_searchEmp_005(self, setup):
#         self.log.info("test_searchEmp_005 is started")
#         self.driver = setup
#         self.log.info("Opening Browser")
#         self.driver.get(self.Url)
#         self.log.info("Going to Url-->" + self.Url)
#         self.lp = loginpage(self.driver)
#         self.lp.enter_username(self.username)
#         self.log.info("Entering UserName-->" + self.username)
#         self.lp.enter_passowrd(self.password)
#         self.log.info("Entering password-->" + self.password)
#         self.lp.click_login()
#         self.log.info("Click On login")
#         self.ae = addemployee(self.driver)
#         self.ae.click_pim()
#         self.log.info("Click On PIM")
#         self.es = EmployeeSearch(self.driver)
#         self.es.Enter_EmpName("Nikki ")
#         self.log.info("Entering Emp Name")
#         time.sleep(2)
#         self.es.Click_SearchButton()
#         self.log.info("Clicking on search Button")
#         time.sleep(2)
#         print(self.es.Search_Result())
#         if self.es.Search_Result() == True:
#             self.log.info("Search Found")
#             self.log.info("test_searchEmp_005 is Passed")
#             self.lp.click_menu_botton()
#             self.log.info("Click on MenuButton")
#             self.lp.click_logout_botton()
#             self.log.info("Click on Logout Button")
#             assert True
#             self.log.info("test_searchEmp_005 is Passed")
#         else:
#             self.log.info("No Search Found")
#             self.lp.click_menu_botton()
#             self.log.info("Click on MenuButton")
#             self.lp.click_logout_botton()
#             self.log.info("Click on Logout Button")
#             self.log.info("test_searchEmp_005 is Failed")
#             assert False
#         self.driver.close()
