import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ProductCategoryPage:
    selectProductSelector = (By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
    loadProductPageSelector = (By.ID, "data-produit-acheter")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def openProductsPage(self, index, dir):
        # Function to open product by list
        if index >= 0 and index < 60:
            selectProduct = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.selectProductSelector))
            selectProduct[index].click()
            self.wait.until(expected_conditions.visibility_of_element_located(self.loadProductPageSelector))
            self.driver.get_screenshot_as_file(dir + "\\productPage" + time.strftime("%Y%m%d-%H%M%S") + ".png")
        else:
            print("Index value is out of range. Should be between 0 and 59")