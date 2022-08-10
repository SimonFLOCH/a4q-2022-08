from selenium import webdriver
from TP4_PageObject.scr.pages.HomePage import HomePage
from TP4_PageObject.scr.pages.ProductCategoryPage import ProductCategoryPage
from TP4_PageObject.scr.pages.ProductPage import ProductPage
from TP4_PageObject.scr.pages.HeaderPage import HeaderComponent
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
    header = HeaderComponent(driver)

    home.closeCookie()
    header.openMenu()
    header.navigationToProductCategory(11, 6, 2, run_dir)

    productCat.openProductsPage(3, run_dir)


    product.buy()
    product.chooseDriveMethod()
    product.enterZipCode()
    product.selectStore(run_dir)

    assert product.getAvailabilityStatus() == "1 produit indisponible dans ce magasin."

    driver.quit()
