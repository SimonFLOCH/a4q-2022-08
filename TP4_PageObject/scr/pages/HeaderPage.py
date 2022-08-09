import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TP4_PageObject.scr.wrapper.UsefullWrapper import Wrapper
from selenium.webdriver.common.action_chains import ActionChains




class HeaderComponent:
    headerFoodSelector = (By.ID, "header-tab-food")
    validationHeaderFoodSelector = (By.CSS_SELECTOR, "#header-tab-food[checked]")
    mainMenuSelector = (By.ID, "data-menu-level-0")
    epicerieSaleeSelector = (By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    sideMenuSelector = (By.ID, "data-menu-level-1_R13")
    patesRizFeculentsSelector = (By.CSS_SELECTOR, "#data-menu-level-1_R13 > li:nth-child(7)")
    lastMenuSelector = (By.ID, "data-menu-level-2_R13F05")
    patesSelector = (By.CSS_SELECTOR, "#data-menu-level-2_R13F05 > li:nth-child(3)")
    loadPageSelector = (By.CSS_SELECTOR, "div.facet-toolbar__sort-button")
    headerNonFoodSelector = (By.ID, "header-tab-non-food")
    validationHeaderNonFoodSelector = (By.CSS_SELECTOR, "#header-tab-non-food[checked]")
    hamburgerButtonSelector = (By.ID, "data-rayons")
    mainMenuListSelector = (By.CSS_SELECTOR, "#data-menu-level-0 > li")
    subMenuListSelector = (By.CSS_SELECTOR, "")
    promotionButtonSelector = (By.ID, "data-promotions")
    catalogueButtonSelector = (By.ID, "data-catalogues")
    momentButtonSelector = (By.ID, "data-moment")
    pagePromotionSelector = (By.CSS_SELECTOR, ".ds-title.ds-title--l")
    pageCatalogueSelector = (By.CSS_SELECTOR, ".catalogues-list-filter")
    dropdownMomentVisibilitySelector = (By.ID, "headerNewsPanel")
    dropdownMomentElementsListSelector = (By.CSS_SELECTOR, "#headerNewsPanel li")
    searchBarSelector = (By.CSS_SELECTOR, "input[required]")
    clearTextButtonSelector = (By.CSS_SELECTOR, ".pl-input-text__clear-btn")
    searchButtonSelector = (By.CSS_SELECTOR, "button[type=submit]")
    titleAfterSearchSelector = (By.CSS_SELECTOR, ".page-title")
    myAccountButtonSelector = (By.ID, "data-account")
    connexionDropdownSelector = (By.ID, "headerAccountPanel")
    connectMeButtonSelector = (By.CSS_SELECTOR, "ds-body-text.ds-body-text--weight-bold.ds-body-text--size-s-fix")
    logInPageSelector = (By.ID, "login-base")
    createAccountSelector = (By.CSS_SELECTOR, ".ds-body-text.ds-body-text--size-s-fix:not(.ds-body-text--weight-bold)")
    logOnPageSelector = (By.ID, "registration-page")
    myProductsSelector = (By.ID, "data-mes-listes")
    helpAndContactSelector = (By.ID, "data-help")
    helpPageSelector = (By.CLASS_NAME, "help-desk-page")


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wrapper = Wrapper(driver)
        self.action = ActionChains(driver)

    def foodHandleSelection(self):
        self.wrapper.clickOnElementAfterWait(self.headerFoodSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.validationHeaderFoodSelector))

    def nonFoodHandleSelection(self):
        self.wrapper.clickOnElementAfterWait(self.headerNonFoodSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.validationHeaderNonFoodSelector))

    def openMenu(self):
        self.wrapper.clickOnElementAfterWait(self.hamburgerButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.mainMenuListSelector))

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

    # def navigationMainMenu(self, index):
    #     if index>=0 and index<24:
    #         mainMenuList = self.driver.find_elements(By.CSS_SELECTOR, "#data-menu-level-0 > li")
    #         self.action.move_to_element(mainMenuList[index])
    #         self.action.perform()
    #         index += 1
    #     else:
    #         print("index hors limites")
    #     self.wait.until(expected_conditions.visibility_of_element_located((
    #         By.CSS_SELECTOR, "#data-menu-level-0 > li:nth-child("+ index +") > ul")))
    #
    #
    # def navigationSubMenu(self, index):
    #     count = self.wait.
    #     nbrMax = len(count)
    #     if index>=0 and index<nbrMax:

    def openPromotionPage(self):
        self.wrapper.clickOnElement(self.promotionButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.pagePromotionSelector))

    def openCataloguePage(self):
        self.wrapper.clickOnElement(self.catalogueButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.pageCatalogueSelector))

    def openMomentPage(self, index):
        self.wrapper.clickOnElement(self.momentButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.dropdownMomentVisibilitySelector))
        momentList = self.driver.find_elements(By.CSS_SELECTOR, "#headerNewsPanel li")
        count = len(momentList)
        if index>=0 and index<count:
            momentList[index].click()
        else:
            print("index is out of limits")

    def searchByText(self, search):
        self.wrapper.writeIntoBoxWithEnter(self.searchBarSelector, search)
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-title"), search))

    def clickOnClearButton(self):
        self.wrapper.clickOnElement(self.clearTextButtonSelector)
        self.wait.until(expected_conditions.invisibility_of_element_located(self.clearTextButtonSelector))

    def clickOnSearchButton(self):
        self.wrapper.clickOnElement(self.searchButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.titleAfterSearchSelector))

    def clickOnMyAccount(self):
        self.wrapper.clickOnElement(self.myAccountButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.connexionDropdownSelector))

    def clickOnConnectMyself(self):
        self.wrapper.clickOnElement(self.connectMeButtonSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.logInPageSelector))

    def clickOnCreateAccount(self):
        self.wrapper.clickOnElement(self.createAccountSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.logOnPageSelector))

    def clickOnMyProduct(self):
        self.wrapper.clickOnElement(self.myProductsSelector)
        # self.wait.until(expected_conditions.visibility_of_element_located(self.))

    def clickOnHelpAndContact(self):
        self.wrapper.clickOnElement(self.helpAndContactSelector)
        self.wait.until(expected_conditions.visibility_of_element_located(self.helpPageSelector))