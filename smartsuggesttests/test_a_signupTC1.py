import pytest


from TestData.SmartSuggestData import SSData
from pageObjects.SignUpPage import SignUp
from utilities.BaseClass import BaseClass


class TestSignupSS(BaseClass):

    def test_createaccountss(self, getData):
        log = self.getLogger()
        signupss = SignUp(self.driver)
        self.driver.get("https://staging.searchblox.com/smartsuggest/signup")
        self.driver.implicitly_wait(10)
        log.info("First Name is " + getData["FisrtName"])
        signupss.FirstName().send_keys(getData["FisrtName"])
        signupss.LastName().send_keys(getData["LastName"])
        signupss.Email().send_keys(getData["Email"])
        log.info("Email used to create account is " + getData["Email"])
        signupss.PasswordSS().send_keys(getData["password"])
        signupss.ConfirmPassword().send_keys(getData["confirmpassword"])
        signupss.CheckBox().click()
        dashboard = signupss.AccountSubmit()
        assert dashboard.SmartInfo().is_displayed()

    @pytest.fixture(params=SSData.smartsuggestdata)
    def getData(self, request):
        return request.params
