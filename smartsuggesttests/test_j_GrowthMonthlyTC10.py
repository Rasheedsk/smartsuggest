import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from pageObjects.Upgradepage import UpgradePage
from utilities.BaseClass import BaseClass


class TestGrowthMonthly(BaseClass):
    def test_growthmonthly(self, getData):
        self.driver.get("https://staging.searchblox.com")
        self.driver.implicitly_wait(10)
        signin = SignIn(self.driver)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.Upgrade().click()
        upgrade = UpgradePage(self.driver)
        upgrade.MonthlyGrowth().click()
        upgrade.PopupYes().click()
        self.driver.switch_to.frame("__privateStripeFrame5")
        upgrade.CCNumber().send_keys(getData["CC-Number"])
        upgrade.CCExpiry().send_keys(getData["expiry"])
        upgrade.CVC().send_keys(getData["CVC"])
        self.driver.switch_to.default_content()
        upgrade.Pay().click()

        assert "10,000" in upgrade.GrowthPrediction().text

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
