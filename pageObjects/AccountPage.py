from selenium.webdriver.common.by import By


class AccountPage():

    def __init__(self, driver):
        self.driver = driver

    changepassword = (By.XPATH, "//button[text()='Change Password']")
    currentpassword = (By.CSS_SELECTOR, "input[placeholder='Current Password']
    newpassword = (By.CSS_SELECTOR, "input[placeholder='New Password']")
    confirmpassowrd = (By.CSS_SELECTOR, "input[placeholder='Confirm Password']")
    update = (By.XPATH, "//button[text()='Update']")
    edit = (By.XPATH, "//button[text()='Edit']")
    phone = (By.CSS_SELECTOR, "input[name='phone']")
    timezone = (By.CSS_SELECTOR, "div[class*='css-1hwfws3 react-select__value-container']")
    timebox = (By.XPATH, "//div[@class='react-select__input']/input")
    save = (By.XPATH, "//button[text()='Save']")
    time = (By.XPATH, "//p[text()='(GMT+05:30) India Standard Time']")
    editcard = (By.XPATH, "//button[@class='btn btn-primary btn-sm']/i")
    cardnumber = (By.CSS_SELECTOR, "input[autocomplete='cc-number']")
    expiry = (By.CSS_SELECTOR, "input[autocomplete='cc-exp']")
    cvc = (By.CSS_SELECTOR, "input[autocomplete='cc-csc']")
    cardupdate = (By.XPATH, "//button[text()='Update']")

    def ChangePassword(self):
        return self.driver.find_element(*AccountPage.changepassword)

    def NewPassword(self):
        return self.driver.find_element(*AccountPage.newpassword)

    def CurrentPassword(self):
        return self.driver.find_element(*AccountPage.currentpassword)

    def ConfirmPassword(self):
        return self.driver.find_element(*AccountPage.confirmpassowrd)

    def Update(self):
        return self.driver.find_element(*AccountPage.update)

    def Edit(self):
        return self.driver.find_element(*AccountPage.edit)

    def Phone(self):
        return self.driver.find_element(*AccountPage.phone)

    def TimeZone(self):
        return self.driver.find_element(*AccountPage.timezone)

    def TimeBox(self):
        return self.driver.find_element(*AccountPage.timebox)

    def Save(self):
        return self.driver.find_element(*AccountPage.save)

    def Time(self):
        return self.driver.find_element(*AccountPage.time)

    def EditCard(self):
        return self.driver.find_element(*AccountPage.editcard)

    def CardNumber(self):
        return self.driver.find_element(*AccountPage.cardnumber)

    def Expiry(self):
        return self.driver.find_element(*AccountPage.expiry)

    def CVC(self):
        return self.driver.find_element(*AccountPage.cvc)

    def CardUpdate(self):
        return self.driver.find_element(*AccountPage.cardupdate)
