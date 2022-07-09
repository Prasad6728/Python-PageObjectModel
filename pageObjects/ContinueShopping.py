from selenium.webdriver.common.by import By


class ContinueShopping:
    def __init__(self, driver):
        self.driver = driver

    totalCheckout = (By.XPATH, "//button[@class='btn btn-success']")
    addCountry = (By.ID, "country")
    tapCountry = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")

    conform = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getTotalCheckout(self):
        return self.driver.find_element(*ContinueShopping.totalCheckout)

    def setCountryName(self, value):
        return self.driver.find_element(*ContinueShopping.addCountry).send_keys(value)

    def tapCountryName(self):
        return self.driver.find_element(*ContinueShopping.tapCountry)

    def getCheckBox(self):
        return self.driver.find_element(*ContinueShopping.checkBox)

    def getPurchase(self):
        return self.driver.find_element(*ContinueShopping.purchase)

    def getConformation(self):
        return self.driver.find_element(*ContinueShopping.conform).text