from selenium.webdriver.common.by import By


class UpgradePage():
    def __init__(self, driver):
        self.driver = driver

    monthlygrowth = (By.CSS_SELECTOR, "ul[class*='growth monthly'] li button")
    growthprediction = (By.XPATH, "//span[text()='10,000']")
    popupyes = (By.XPATH, "//button[text()='Yes']")
    popupno = (By.XPATH, "//button[text()='No']")
    ccnumber = (By.CSS_SELECTOR, "input[autocomplete='cc-number']")
    ccexpiry = (By.CSS_SELECTOR, "input[autocomplete='cc-exp']")
    cvc = (By.CSS_SELECTOR, "input[autocomplete='cc-csc']")
    pay = (By.XPATH, "//button[text()='Pay']")
    monthlypro = (By.XPATH, "//ul[@class='plansList pro monthly']/li/button")
    proprediction = (By.XPATH, "//span[text()='25,000']")
    switch = (By.CSS_SELECTOR, "span[class='bootstrap-switch-label']")
    proyearly = (By.CSS_SELECTOR, "ul[class='plansList pro yearly'] li button")
    yearlyremainingdays = (By.XPATH, "//span[text()='365']")

    def MonthlyGrowth(self):
        return self.driver.find_element(*UpgradePage.monthlygrowth)

    def GrowthPrediction(self):
        return self.driver.find_element(*UpgradePage.growthprediction)

    def ProPrediction(self):
        return self.driver.find_element(*UpgradePage.proprediction)

    def PopupYes(self):
        return self.driver.find_element(*UpgradePage.popupyes)

    def PopupNo(self):
        return self.driver.find_element(*UpgradePage.popupno)

    def CCNumber(self):
        return self.driver.find_element(*UpgradePage.ccnumber)

    def CCExpiry(self):
        return self.driver.find_element(*UpgradePage.ccexpiry)

    def CVC(self):
        return self.driver.find_element(*UpgradePage.cvc)

    def Pay(self):
        return self.driver.find_element(*UpgradePage.pay)

    def MonthlyPro(self):
        return self.driver.find_element(*UpgradePage.monthlypro)

    def Switch(self):
        return self.driver.find_element(*UpgradePage.switch)

    def ProYearly(self):
        return self.driver.find_element(*UpgradePage.proyearly)

    def YearlyRemainingDays(self):
        return self.driver.find_element(*UpgradePage.yearlyremainingdays)
