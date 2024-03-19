import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)
More = driver.find_element(By.XPATH, "//a[text()='More']")
action = ActionChains(driver)
action.move_to_element(More).perform()
time.sleep(2)
Mode = driver.find_element(By.XPATH, "//a[text()='Modals']")
action.click(Mode).perform()
time.sleep(2)
driver.quit()
