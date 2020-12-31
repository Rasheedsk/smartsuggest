import pytest

from TestData.SmartSuggestData import SSData
from pageObjects.LoginPage import SignIn
from utilities.BaseClass import BaseClass


class TestPrediction(BaseClass):

    def test_Prediction(self, getData):
        signin = SignIn(self.driver)
        self.driver.get("https://staging.searchblox.com/login")
        self.driver.implicitly_wait(10)
        signin.Email().send_keys(getData["Email"])
        signin.Password().send_keys(getData["Password"])
        dashboard = signin.LoginNow()
        dashboard.RootUrl().send_keys(getData["Root URL"])
        dashboard.Save().click()
        assert dashboard.PredictionMessage().is_displayed()

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.param
