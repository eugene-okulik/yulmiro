from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--force-device-scale-factor=0.7")
    chrome_driver = webdriver.Chrome(chrome_options)
    chrome_driver.maximize_window()
    return chrome_driver


def test_buy_mobile(driver):
    driver.implicitly_wait(5)
    driver.get('https://www.demoblaze.com/index.html')
    mobile_link = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    ActionChains(driver).key_down(Keys.CONTROL).click(mobile_link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.CLASS_NAME, 'btn-success').click()
    alert = Alert(driver)
    WebDriverWait(driver,5).until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH,'//*[text()="Samsung galaxy s6"]'),
            'Samsung galaxy s6'
        )
    )


def test_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    driver.refresh()
    card = driver.find_element(By.CSS_SELECTOR,'[alt="Push It Messenger Bag"]')
    compare_list = driver.find_elements(By.CSS_SELECTOR, 'a.action.tocompare')
    compare = compare_list[0]
    ActionChains(driver).move_to_element(card).click(compare).perform()
    titles = driver.find_elements(By.CSS_SELECTOR, 'a.product-item-link')
    assert titles[0].text == titles[12].text
