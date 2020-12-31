from selenium.webdriver.common.by import By

from pageObjects.DashBoardPage import DashBoard


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.CSS_SELECTOR, "input[name='firstName']")
    lastname = (By.CSS_SELECTOR, "input[name='lastName']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    cardnum = (By.CSS_SELECTOR, "input[name='cardnumber']")
    ccexp = (By.CSS_SELECTOR, "input[name='exp-date']")
    cvc = (By.CSS_SELECTOR, "input[name='cvc']")
    password = (By.CSS_SELECTOR, "input[title='Password']")
    confirmpassword = (By.CSS_SELECTOR, "input[title='Confirm Password']")
    checkbox = (By.CSS_SELECTOR, "input[class*='form-check-input']")
    accounsubmit = (By.XPATH, "//div[@class='form-group']/button")
    passwordss =(By.CSS_SELECTOR, "input[title='Enter Password']")

    def FirstName(self):
        return self.driver.find_element(*SignUp.firstname)

    def LastName(self):
        return self.driver.find_element(*SignUp.lastname)

    def Email(self):
        return self.driver.find_element(*SignUp.email)

    def CardNumber(self):
        return self.driver.find_element(*SignUp.cardnum)

    def CcExp(self):
        return self.driver.find_element(*SignUp.ccexp)

    def Cvc(self):
        return self.driver.find_element(*SignUp.cvc)

    def Password(self):
        return self.driver.find_element(*SignUp.password)

    def PasswordSS(self):
        return self.driver.find_element(*SignUp.passwordss)

    def ConfirmPassword(self):
        return self.driver.find_element(*SignUp.confirmpassword)

    def CheckBox(self):
        return self.driver.find_element(*SignUp.checkbox)

    def AccountSubmit(self):
        self.driver.find_element(*SignUp.accounsubmit).click()
        dashboard = DashBoard(self.driver)
        return dashboard
