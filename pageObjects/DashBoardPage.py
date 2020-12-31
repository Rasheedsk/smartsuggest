from selenium.webdriver.common.by import By


class DashBoard():

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//p[text()='test']")
    collectioninfo = (By.LINK_TEXT, "Add Collection")
    upgrade = (By.XPATH, "//li[@class='nav-item']/a")
    smartsuggestinfo = (By.XPATH, "//h4[text()='SmartSuggest ']")
    ssedit = (By.XPATH, "//div[@class='text-left']/button")
    rooturl = (By.CSS_SELECTOR, "input[name='rootUrls']")
    dashboard = (By.CSS_SELECTOR, "div#sidebar div a:nth-of-type(1) img")
    widget = (By.CSS_SELECTOR, "div#sidebar div a:nth-of-type(2) img")
    account = (By.CSS_SELECTOR, "div#sidebar div a:nth-of-type(3) img")
    help = (By.CSS_SELECTOR, "div#sidebar div a:nth-of-type(4) img")
    save = (By.XPATH, "//button[text()='Save']")
    predictionmessage = (By.XPATH, "//p[text()='Our AI engine is generating the predictions. Normally, it takes 5 to "
                                   "10 minutes based on the number of predictions']")
    popupyes = (By.XPATH, "//button[text()='Yes']")
    popupno = (By.XPATH, "//button[text()='No']")
    languageinput = (By.CSS_SELECTOR, "div[class*='select__value-container']")
    languageselect = (By.CSS_SELECTOR, "//div[@class='react-select__input']/input")

    def ColInfo(self):
        return self.driver.find_element(*DashBoard.collectioninfo)

    def Upgrade(self):
        return self.driver.find_element(*DashBoard.upgrade)

    def SmartInfo(self):
        return self.driver.find_element(*DashBoard.smartsuggestinfo)

    def SSEdit(self):
        return self.driver.find_element(*DashBoard.ssedit)

    def RootUrl(self):
        return self.driver.find_element(*DashBoard.rooturl)

    def Dashboard(self):
        return self.driver.find_element(*DashBoard.dashboard)

    def Widget(self):
        return self.driver.find_element(*DashBoard.widget)

    def Account(self):
        return self.driver.find_element(*DashBoard.account)

    def Help(self):
        return self.driver.find_element(*DashBoard.help)

    def Save(self):
        return self.driver.find_element(*DashBoard.save)

    def PredictionMessage(self):
        return self.driver.find_element(*DashBoard.predictionmessage)

    def PopupYes(self):
        return self.driver.find_element(*DashBoard.popupyes)

    def PopupNo(self):
        return self.driver.find_element(*DashBoard.popupno)

    def LanguageInput(self):
        return self.driver.find_element(*DashBoard.languageinput)

    def LanguageSelect(self):
        return self.driver.find_element(*DashBoard.languageselect)
