from selenium.webdriver.common.by import By

from PythonSelfFramework.pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-dismissible']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def setNameDetails(self, value):
        return self.driver.find_element(*HomePage.name).send_keys(value)

    def setEmailDetails(self, value):
        return self.driver.find_element(*HomePage.email).send_keys(value)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def setPassword(self, value):
        return self.driver.find_element(*HomePage.password).send_keys(value)

    def getGenderDetails(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

