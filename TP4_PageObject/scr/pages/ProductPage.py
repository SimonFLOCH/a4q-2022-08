import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TP4_PageObject.scr.wrapper.UsefullWrapper import Wrapper



class ProductPage:
    buyButtonSelector = (By.ID, "data-produit-acheter")
    driveButtonSelector = (By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")
    zipCodeTextBarSelector = (By.CSS_SELECTOR, "[data-cs-mask=true]")
    chooseStoreButtonSelector = (By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")
    textStatusSelector = (By.CSS_SELECTOR, "div.ds-body-text--color-inherit")



    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.wrapper = Wrapper(driver)

    def buy(self):
        self.wrapper.clickOnElementAfterWait(self.buyButtonSelector)
        self.wait.until(expected_conditions.element_to_be_clickable(self.driveButtonSelector))


    def chooseDriveMethod(self):
        self.wrapper.clickOnElementAfterWait(self.driveButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.zipCodeTextBarSelector))


    def enterZipCode(self):
        self.wrapper.writeIntoBoxWithEnterAfterWait(self.zipCodeTextBarSelector, 75001)
        self.wait.until(expected_conditions.element_to_be_clickable(self.chooseStoreButtonSelector))


    def selectStore(self, dir):
        self.wrapper.clickOnElementAfterWait(self.chooseStoreButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.textStatusSelector))
        scshEle = self.driver.find_element(By.ID, "modal-relative")
        self.driver.get_screenshot_as_file(dir + "\\unavailableProduct" + time.strftime("%Y%m%d-%H%M%S") + ".png")
        scshEle.screenshot(dir + "\\unavailableProductFrame" + time.strftime("%Y%m%d-%H%M%S") + ".png")

    def getAvailabilityStatus(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.ds-body-text--color-inherit").text


