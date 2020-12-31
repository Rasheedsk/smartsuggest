from selenium.webdriver.common.by import By


class Forgot:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "input[name='email']")
    submit = (By.XPATH, "//div[@class='mt-4 form-group']/button")
    message = (By.XPATH, "//p[text()='Please Check Email to Reset your Password']")


    def Email(self):
        return self.driver.find_element(*Forgot.email)

    def Submit(self):
        return self.driver.find_element(*Forgot.submit)

    def Message(self):
        return self.driver.find_element(*Forgot.message)