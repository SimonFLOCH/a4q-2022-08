import time
from selenium import webdriver
from TP4_PageObject.scr.pages.HomePage import HomePage
from TP4_PageObject.scr.pages.ProductCategoryPage import ProductCategoryPage
from TP4_PageObject.scr.pages.ProductPage import ProductPage


def testPageObject():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    home = HomePage(driver)
    productCat = ProductCategoryPage(driver)
    product = ProductPage(driver)

    home.closeCookie()
    home.openMenu()
    home.openEpicerieSalee()
    home.openPatesRizFeculents()
    home.openPatesCategoryPage()
    driver.get_screenshot_as_file(
        "C:\\Users\\ib\\PycharmProjects\\A4Q\\TP4_PageObject\\screenshots\\productCategaoryPage" + time.strftime(
            "%Y%m%d-%H%M%S") + ".png")

    productCat.openProductsPage(3)
    driver.get_screenshot_as_file(
        "C:\\Users\\ib\\PycharmProjects\\A4Q\\TP4_PageObject\\screenshots\\productPage" + time.strftime(
            "%Y%m%d-%H%M%S") + ".png")

    product.buy()
    product.chooseDriveMethod()
    product.enterZipCode()
    product.selectStore()
    product.getAvailabilityStatus()

    assert product.getAvailabilityStatus() == "1 produit indisponible dans ce magasin."

    driver.get_screenshot_as_file(
        "C:\\Users\\ib\\PycharmProjects\\A4Q\\TP4_PageObject\\screenshots\\unavailableProduct" + time.strftime(
                    "%Y%m%d-%H%M%S") + ".png")

    driver.quit()
