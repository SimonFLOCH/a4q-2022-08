import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TP4_PageObject.scr.wrapper.UsefullWrapper import Wrapper



class HomePage:
    closeCookieButtonSelector = (By.ID, "onetrust-accept-btn-handler")
    hamburgerButtonSelector = (By.ID, "data-rayons")
    mainMenuSelector = (By.ID, "data-menu-level-0")
    epicerieSaleeSelector = (By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    sideMenuSelector = (By.ID, "data-menu-level-1_R13")
    patesRizFeculentsSelector = (By.CSS_SELECTOR, "#data-menu-level-1_R13 > li:nth-child(7)")
    lastMenuSelector = (By.ID, "data-menu-level-2_R13F05")
    patesSelector = (By.CSS_SELECTOR, "#data-menu-level-2_R13F05 > li:nth-child(3)")
    loadPageSelector = (By.CSS_SELECTOR, "div.facet-toolbar__sort-button")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wrapper = Wrapper(driver)


    def closeCookie(self):
        self.wrapper.clickOnElementAfterWait(self.closeCookieButtonSelector)
        self.wait.until(expected_conditions.invisibility_of_element_located(self.closeCookieButtonSelector))


    def openMenu(self):
        self.wrapper.clickOnElementAfterWait(self.hamburgerButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.mainMenuSelector))


    def openEpicerieSalee(self):
        self.wrapper.hoverElementAfterWait(self.epicerieSaleeSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.sideMenuSelector))


    def openPatesRizFeculents(self):
        self.wrapper.hoverElementAfterWait(self.patesRizFeculentsSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.lastMenuSelector))


    def openPatesCategoryPage(self, dir):
        self.wrapper.clickOnElementAfterWait(self.patesSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.loadPageSelector))
        self.driver.get_screenshot_as_file(dir + "\\productCategoryPage" + time.strftime("%Y%m%d-%H%M%S") + ".png")