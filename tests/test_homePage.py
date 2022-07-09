import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from PythonSelfFramework.Test_Data.TestData import TestData
from PythonSelfFramework.pageObjects.Homepage import HomePage
from PythonSelfFramework.utilities.BaseClass1 import BaseClass1


class Test_HomePage(BaseClass1):
    def test_formSubmission(self, getData):

        homepage1 = HomePage(self.driver)
        homepage1.setNameDetails(getData["name"])
        homepage1.setEmailDetails(getData["email"])
        homepage1.setPassword(getData["password"])
        homepage1.clickCheckBox().click()
        self.selectOptionByText(homepage1.getGenderDetails(), "Male")
        homepage1.getSubmitButton().click()

        message = homepage1.getSuccessMessage().text
        assert "Success! The Form" in message

        self.driver.refresh()

    @pytest.fixture(params=TestData.dictionary_values)
    def getData(self, request):
        return request.param


    # @pytest.fixture(params=TestData.dictionary_values)
    # @pytest.fixture(params=[{"firstname" : "prasad", "lastname" : "prasad@123", "passwords" : "abc123"}, {"firstname" : "vijaya", "lastname" : "viji@123", "passwords" : "xyz345"}])
    # @pytest.fixture(params=[("prasad", "rocky@gmail", "abc123"), ("vijaya", "scooby@123", "xyz234")])
    # getData[0]
    # getData[1]
    # getData[2]


