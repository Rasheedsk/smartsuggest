import pytest

from TestData.SmartSuggestData import ChangePassowrd
from pageObjects.AccountPage import AccountPage
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestChangePassword(BaseClass):
    def test_changepassword(self, getData):
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Account().click()
        account = AccountPage(self.driver)
        account.ChangePassword().click()
        account.CurrentPassword().send_keys(getData["Current Password"])
        account.NewPassword().send_keys(getData["New Password"])
        account.ConfirmPassword().send_keys(getData["Confirm Password"])
        account.Update().click()


    @pytest.fixture(params=ChangePassowrd.changepassowrd)
    def getData(self, request):
        return request.param
