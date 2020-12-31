import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class Testforgot(BaseClass):

    def test_passwordForgot(self,getData):
        forgot = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        forget = forgot.Forgotpassword()
        forget.Email().send_keys(getData["Email"])
        forget.Submit().click()
        assert forget.Message().is_displayed()

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
