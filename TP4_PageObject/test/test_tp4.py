import time
from selenium import webdriver
from TP4_PageObject.scr.pages.HomePage import HomePage
from TP4_PageObject.scr.pages.ProductCategoryPage import ProductCategoryPage
from TP4_PageObject.scr.pages.ProductPage import ProductPage
import os
from datetime import datetime


def testPageObject():
    # création d'un dossier horodaté pour stocker mes screenshots
    run_dir = "C:\\Users\\ib\\PycharmProjects\\A4Q\\TP4_PageObject\\screenshots\\screenshots" + datetime.now().strftime(
        "%Y%m%d-%H%M%S")
    os.mkdir(run_dir)

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
    # appel d'une fonction possedant un screenshot avec le paramètre run_dir défini précédement
    home.openPatesCategoryPage(run_dir)


    productCat.openProductsPage(3, run_dir)


    product.buy()
    product.chooseDriveMethod()
    product.enterZipCode()
    product.selectStore(run_dir)
    #product.getAvailabilityStatus()

    assert product.getAvailabilityStatus() == "1 produit indisponible dans ce magasin."

    driver.quit()
