from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//h4[@class='card-title']/a")
    cardFooter = (By.XPATH, "//div[@class='card-footer']/button")
    reCheckout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getReCheckout(self):
        return self.driver.find_element(*CheckoutPage.reCheckout)






    # card.find_element("xpath", "div/button").click()