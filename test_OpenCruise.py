from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_opencruise():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://opencruise-ok.sogeti-center.cloud")
    username = driver.find_element(By.CSS_SELECTOR, "[formcontrolname=username]")
    username.send_keys("admin@poei.com")
    password = driver.find_element(By.CSS_SELECTOR, "[formcontrolname=password]")
    password.send_keys("Admin123")
    connexion = driver.find_element(By.CSS_SELECTOR, "button")
    connexion.click()
    driver.quit()