import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.AccountPage import AccountPage
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestChangeCard(BaseClass):
    def test_changecard(self, getData):
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Account().click()
        account= AccountPage(self.driver)
        account.EditCard().click()
        self.driver.switch_to.frame("__privateStripeFrame5")
        account.CardNumber().send_keys(getData["CCNumber"])
        account.Expiry().send_keys(getData["Expiry"])
        account.CVC().send_keys(getData["cvc"])
        self.driver.switch_to.default_content()
        account.CardUpdate().click()

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
