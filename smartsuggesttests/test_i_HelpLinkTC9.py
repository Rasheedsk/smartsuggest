import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestHelpLink(BaseClass):
    def test_helplink(self, getData):
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Help().click()
        childwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childwindow)
        assert "SmartSuggest" in self.driver.title

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
