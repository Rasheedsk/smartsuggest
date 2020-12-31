from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class Testforgot(BaseClass):

    def test_passwordForgot(self):
        forgot = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        forget = forgot.Forgotpassword()
        forget.Email().send_keys("rasheeds@searchblox.com")
        forget.Submit().click()
        assert forget.Message().is_displayed()
