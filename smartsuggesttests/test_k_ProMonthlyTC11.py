import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from pageObjects.Upgradepage import UpgradePage
from utilities.BaseClass import BaseClass


class TestProMonthly(BaseClass):
    def test_promonthly(self, getData):
        self.driver.get("https://staging.searchblox.com")
        self.driver.implicitly_wait(10)
        signin = SignIn(self.driver)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Upgrade().click()
        upgrade = UpgradePage(self.driver)
        upgrade.MonthlyPro().click()
        upgrade.PopupYes().click()
        assert "25,000" in upgrade.ProPrediction().text

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
