from selenium import webdriver


def test_essai():
    driver = webdriver.Chrome()
    driver.get("https://python.org")
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://perl.org")
    driver.switch_to.window(driver.window_handles[0])