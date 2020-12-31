import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from pageObjects.Upgradepage import UpgradePage
from utilities.BaseClass import BaseClass


class TestProYearly(BaseClass):
    def test_proyearly(self, getData):
        self.driver.get("https://staging.searchblox.com")
        self.driver.implicitly_wait(10)
        signin = SignIn(self.driver)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Upgrade().click()
        upgrade = UpgradePage(self.driver)
        upgrade.Switch().click()
        upgrade.ProYearly().click()
        upgrade.PopupYes().click()
        assert "365" in upgrade.YearlyRemainingDays().text


    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
