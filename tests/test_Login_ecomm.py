
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class Testlogin(BaseClass):

    def test_login(self):
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys("rasheedsk@searchblox.com")
        signin.Password().send_keys("admin")
        dashboard = signin.LoginNow()

        assert dashboard.Upgrade().is_displayed()





