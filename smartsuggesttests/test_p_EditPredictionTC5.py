import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestEditPrediction(BaseClass):

    def test_editprediction(self, getData):
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
        dashboard.RootUrl().send_keys(getData["RootURL"])
        dashboard.Save().click()
        assert dashboard.PredictionMessage().is_displayed()

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
