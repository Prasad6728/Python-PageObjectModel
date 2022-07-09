
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonSelfFramework.pageObjects.CheckoutPage import CheckoutPage
from PythonSelfFramework.pageObjects.ContinueShopping import ContinueShopping
from PythonSelfFramework.pageObjects.Homepage import HomePage
from PythonSelfFramework.utilities.BaseClass1 import BaseClass1


class TestOne(BaseClass1):

    def test_e2e(self):

        log = self.getLogger()
        homepage = HomePage(self.driver)

        checkoutpage = homepage.shopItems()
        log.info("Getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            productName = card.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.getReCheckout().click()
        continueshopping = ContinueShopping(self.driver)
        continueshopping.getTotalCheckout().click()
        log.info("Entering country name as ind")
        continueshopping.setCountryName("ind")

        # time.sleep(5)
        self.verifyLinkPresence("India")

        continueshopping.tapCountryName().click()
        continueshopping.getCheckBox().click()
        continueshopping.getPurchase().click()

        # textMatch = ContinueShopping.getConformation()
        textMatch = self.driver.find_element("css selector", "[class*='alert-success']").text
        log.info("Text received from application is " + textMatch)

        assert "Success! Thank you!" in textMatch

