import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ProductPage:
    buyButtonSelector = (By.ID, "data-produit-acheter")
    driveButtonSelector = (By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")
    zipCodeTextBarSelector = (By.CSS_SELECTOR, "[data-cs-mask=true]")
    chooseStoreButtonSelector = (By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")
    textStatusSelector = (By.CSS_SELECTOR, "div.ds-body-text--color-inherit")


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def buy(self):
        buyButton = self.driver.find_element(By.ID, "data-produit-acheter")
        buyButton.click()
        self.wait.until(expected_conditions.element_to_be_clickable(self.driveButtonSelector))


    def chooseDriveMethod(self):
        pickUp = self.driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")
        pickUp.click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.zipCodeTextBarSelector))


    def enterZipCode(self):
        zipCode = self.driver.find_element(By.CSS_SELECTOR, "[data-cs-mask=true]")
        zipCode.send_keys("75001")
        time.sleep(1)
        zipCode.send_keys(Keys.ENTER)
        self.wait.until(expected_conditions.element_to_be_clickable(self.chooseStoreButtonSelector))


    def selectStore(self, dir):
        firstStore = self.driver.find_element(By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")
        firstStore.click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.textStatusSelector))
        scshEle = self.driver.find_element(By.ID, "modal-relative")
        self.driver.get_screenshot_as_file(dir + "\\unavailableProduct" + time.strftime("%Y%m%d-%H%M%S") + ".png")
        scshEle.screenshot(dir + "\\unavailableProductFrame" + time.strftime("%Y%m%d-%H%M%S") + ".png")

    def getAvailabilityStatus(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.ds-body-text--color-inherit").text


