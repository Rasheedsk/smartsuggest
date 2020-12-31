import pytest
from selenium.webdriver.common.keys import Keys

from TestData.SmartSuggestData import SSData
from pageObjects.AccountPage import AccountPage
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestTimeZone(BaseClass):
    def test_timezone(self, getData):
        self.driver.get("https://staging.searchblox.com")
        signin = SignIn(self.driver)
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Account().click()
        account = AccountPage(self.driver)
        account.Edit().click()
        account.Phone().clear()
        account.Phone().send_keys(getData["Phone number"])
        account.TimeZone().click()
        account.TimeBox().send_keys(getData["time"])
        account.TimeBox().send_keys(Keys.ENTER)
        account.Save().click()
        assert "India" in account.Time().text

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param

