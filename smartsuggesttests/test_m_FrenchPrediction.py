

import pytest

from TestData.SmartSuggestData import FrenchPredictionData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestFrenchPrediction(BaseClass):
    @pytest.mark.skip
    def test_frenchprediction(self, getData):
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

        log.info("Entered URL")
        #dashboard.LanguageInput().click()
        #dashboard.LanguageSelect().send_keys(getData["Language"])
        #dashboard.Save().click()
        # assert dashboard.PredictionMessage().is_displayed()

    @pytest.fixture(params=FrenchPredictionData.frenchpredictiondata)
    def getData(self, request):
        return request.param
