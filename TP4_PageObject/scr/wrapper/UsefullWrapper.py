import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class Wrapper:

    def __init__(self,  driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)
        self.wait2 = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def clickOnElementAfterWait(self, locator):
        ele = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        ele.click()

    def clickOnElement(self, locator):
        ele = self.driver.find_element(locator)
        ele.click()

    def writeIntoBoxWithEnterAfterWait(self, locator, text):
        ele = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        ele.send_keys(text)
        time.sleep(1)
        ele.send_keys(Keys.ENTER)

    def writeIntoBoxWithEnter(self, locator, text):
        ele = self.driver.find_element(locator)
        ele.send_keys(text)
        time.sleep(1)
        ele.send_keys(Keys.ENTER)

    def hoverElementAfterWait(self, locator):
        ele = self.wait2.until(expected_conditions.visibility_of_element_located(locator))
        self.action.move_to_element(ele)
        self.action.perform()

    def writeIntoBox(self, locator, text):
        ele = self.driver.find_element(locator)
        ele.send_keys(text)

    def validateTextBoxWithEnter(self, locator):
        ele = self.driver.find_element(locator)
        ele.send_keys(Keys.ENTER)
