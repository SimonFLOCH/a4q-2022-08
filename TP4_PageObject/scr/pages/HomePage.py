from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TP4_PageObject.scr.wrapper.UsefullWrapper import Wrapper



class HomePage:
    closeCookieButtonSelector = (By.ID, "onetrust-accept-btn-handler")
    hamburgerButtonSelector = (By.ID, "data-rayons")


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wrapper = Wrapper(driver)


    def closeCookie(self):
        self.wrapper.clickOnElementAfterWait(self.closeCookieButtonSelector)
        self.wait.until(expected_conditions.invisibility_of_element_located(self.closeCookieButtonSelector))
