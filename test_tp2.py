import time
import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    # search_zone = driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'and@type='text']")
    # search_zone.send_keys("Playstation 5")
    # search_Button = driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'and@type='submit']")
    # search_Button.click()
    # first_item = driver.find_element(By.XPATH, "//img[@data-image-index='1']")
    # first_item.click()
    time.sleep(2)
    close_cookies = driver.find_element(By.XPATH, "//div[@class='banner-actions-container']/button")
    close_cookies.click()
    search_bar = driver.find_element(By.XPATH, "//div[@class='pl-input-text']/input")
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.XPATH, "//button[contains(@class, 'header-search__submit-btn')]")
    search_button.click()
    first_result = driver.find_element(By.XPATH, "//li[@style='order: 1;']//a[@tabindex='-1']")
    first_result.click()
    time.sleep(2)
    buy_button = driver.find_element(By.XPATH, "//button[contains(@class, 'pl-button--primary add-to-cart__plus')]")
    buy_button.click()
    time.sleep(5)
    drive = driver.find_element(By.XPATH, "//div[contains(@class,'push-services--pickers')]/ul/li[1]//div[contains(@class,'ds-body-text')]")
    delivery24 = driver.find_element(By.XPATH,
                                     "//div[contains(@class,'push-services--pickers')]/ul/li[2]//div[contains(@class,'ds-body-text')]")
    delivery1 = driver.find_element(By.XPATH,
                                    "//div[contains(@class,'push-services--pickers')]/ul/li[3]//div[contains(@class,'ds-body-text')]")
    assert drive.text == 'Retrait gratuit en magasin'
    print('Selector "retrait en drive" is present')
    assert delivery24.text == 'Votre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    assert delivery1.text == 'Vos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    # presence des 3 selectors
    # time.sleep(10)
    driver.quit()

def test_css():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    time.sleep(2)
    close_cookies = driver.find_element(By.CSS_SELECTOR, "div.banner-actions-container > button")
    close_cookies.click()
    search_bar = driver.find_element(By.CSS_SELECTOR, "div.pl-input-text > input")
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button.header-search__submit-btn")
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, "li[style='order: 1;'] a[tabindex='-1']")
    first_result.click()
    time.sleep(1)
    buy_button = driver.find_element(By.CSS_SELECTOR, "button.pl-button--primary.add-to-cart__plus")
    buy_button.click()
    time.sleep(2)
    drive = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers  li:nth-child(1) .ds-body-text")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers  li:nth-child(2) .ds-body-text")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers  li:nth-child(3) .ds-body-text")
    assert drive.text == 'Retrait gratuit en magasin'
    print('Selector "retrait en drive" is present')
    assert delivery24.text == 'Votre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    assert delivery1.text == 'Vos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    # presence des 3 selectors
    # time.sleep(2)
    driver.quit()


def test_css_correction_sleep():
    logging.basicConfig(filename="essai.log",level=logging.WARNING)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    time.sleep(2)

    close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")

    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()

    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    time.sleep(1)

    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    time.sleep(2)

    pick_up = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")

    assert pick_up.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in pick_up.text
    print('Selector "retrait en drive" is present')
    logging.debug("Drive OK")
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    logging.warning("Livraison 24h OK")
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    logging.error("Livraison 1h OK")
    # time.sleep(2)

    driver.quit()


def test_css_correction_implicit_wait():
    logging.basicConfig(filename="essai.log",level=logging.WARNING)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")

    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()

    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    pick_up = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")

    assert pick_up.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in pick_up.text
    print('Selector "retrait en drive" is present')
    logging.debug("Drive OK")
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    logging.warning("Livraison 24h OK")
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    logging.error("Livraison 1h OK")

    driver.quit()



def test_css_correction_explicit_wait():
    logging.basicConfig(filename="essai.log",level=logging.WARNING)
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    wait = WebDriverWait(driver, 10)

    close_cookies = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".banner-actions-container > button")))
    close_cookies.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")

    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()

    first_result = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")))
    first_result.click()

    buy_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    pick_up = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")

    assert pick_up.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in pick_up.text
    print('Selector "retrait en drive" is present')
    logging.debug("Drive OK")
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    logging.warning("Livraison 24h OK")
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    logging.error("Livraison 1h OK")

    driver.quit()