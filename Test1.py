import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(browser):
    browser.get("https://www.facebook.com/")
    username_input = browser.find_element(By.XPATH, "//input[@id='email']")
    password_input = browser.find_element(By.XPATH, "//input[@id='pass']")
    username_input.send_keys("8106620472")
    password_input.send_keys("nivya reddy")
    login =browser.find_element(By.XPATH, "//button[text()='Log in']")

    assert browser.current_url == "https://www.facebook.com/"


def test_failed_login(browser):

    browser.get("https://www.facebook.com/")
    username_input = browser.find_element(By.XPATH, "//input[@id='email']")
    password_input = browser.find_element(By.XPATH, "//input[@id='pass']")
    username_input.send_keys("7032424667")
    password_input.send_keys("guru reddy")
    login = browser.find_element(By.XPATH, "//button[text()='Log in']")

    assert browser.current_url == "https://www.facebook.com/"
