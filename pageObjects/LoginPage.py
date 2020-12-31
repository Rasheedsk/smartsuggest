from selenium.webdriver.common.by import By

from pageObjects.DashBoardPage import DashBoard
from pageObjects.ForgotPassword import Forgot


class SignIn:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[name='password']")
    loginnow = (By.XPATH, "//div[@class='mt-3 form-group']/button")
    forgot = (By.XPATH, "//div[@class='col-sm-6']/a")


    def Email(self):
        return self.driver.find_element(*SignIn.email)

    def Password(self):
        return self.driver.find_element(*SignIn.password)

    def LoginNow(self):
        self.driver.find_element(*SignIn.loginnow).click()
        dashboard = DashBoard(self.driver)
        return dashboard

    def Forgotpassword(self):
        self.driver.find_element(*SignIn.forgot).click()
        forget = Forgot(self.driver)
        return forget





