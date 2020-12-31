import pytest

from TestData.SmartSuggestData import RussiaPredictionData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestRussiaPrediction(BaseClass):
    @pytest.mark.skip
    def test_Russiaprediction(self, getData):
        log = self.getLogger()
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.SSEdit().click()
        self.driver.implicitly_wait(5)
        log.info("eidt button has been clicked")
        dashboard.RootUrl().clear()
        log.info("rooturl cleared")
        dashboard.RootUrl().send_keys(getData["Root URL"])
        dashboard.Save().click()
        assert dashboard.PredictionMessage().is_displayed()

    @pytest.fixture(params=RussiaPredictionData.russiapredictiondata)
    def getData(self, request):
        return request.param