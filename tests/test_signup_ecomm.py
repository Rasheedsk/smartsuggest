import pytest

from TestData.SmartSuggestData import SignUpData
from pageObjects.SignUpPage import SignUp
from utilities.BaseClass import BaseClass


class TestSignup(BaseClass):

    def test_createaccount(self,getData):
        log = self.getLogger()
        signup = SignUp(self.driver)
        self.driver.get("https://staging.searchblox.com/signup?ecomm=true")
        self.driver.implicitly_wait(10)
        log.info("First Name is "+ getData["FisrtName"])
        signup.FirstName().send_keys(getData["FisrtName"])
        signup.LastName().send_keys(getData["LastName"])
        signup.Email().send_keys(getData["Email"])
        log.info("Email used to create account is " + getData["Email"])
        self.driver.switch_to.frame("__privateStripeFrame5")
        signup.CardNumber().send_keys(getData["card"])
        signup.CcExp().send_keys(getData["expdate"])
        signup.Cvc().send_keys(getData["cvc"])
        self.driver.switch_to.default_content()
        signup.Password().send_keys(getData["password"])
        signup.ConfirmPassword().send_keys(getData["confirmpassword"])
        signup.CheckBox().click()
        dashboard =  signup.AccountSubmit()
        assert dashboard.ColInfo().is_displayed()

    @pytest.fixture(params=SignUpData.signupdata)
    def getData(self, request):
        return request.param






