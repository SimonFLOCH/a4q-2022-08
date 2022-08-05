import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains




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
        self.action = ActionChains(driver)


    def closeCookie(self):
        closeCookiesButton = self.wait.until(expected_conditions.element_to_be_clickable(
            self.closeCookieButtonSelector))
        closeCookiesButton.click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.closeCookieButtonSelector))


    def openMenu(self):
        hamburgerButton = self.wait.until(expected_conditions.element_to_be_clickable(self.hamburgerButtonSelector))
        hamburgerButton.click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.mainMenuSelector))


    def openEpicerieSalee(self):
        epicerieSalee = self.wait.until(expected_conditions.visibility_of_element_located(
            self.epicerieSaleeSelector))
        self.action.move_to_element(epicerieSalee)
        self.action.perform()
        self.wait.until(expected_conditions.visibility_of_element_located(self.sideMenuSelector))


    def openPatesRizFeculents(self):
        feculent = self.wait.until(expected_conditions.visibility_of_element_located(
            self.patesRizFeculentsSelector))
        self.action.move_to_element(feculent)
        self.action.perform()
        self.wait.until(expected_conditions.visibility_of_element_located(self.lastMenuSelector))


    def openPatesCategoryPage(self):
        pates = self.wait.until(expected_conditions.element_to_be_clickable(self.patesSelector))
        pates.click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.loadPageSelector))
