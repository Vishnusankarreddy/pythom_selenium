import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.ID,'OKTab').click()
time.sleep(5)

#ok - accept
driver.switch_to.alert.accept()

#confrimation
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
time.sleep(2)
driver.find_element(By.ID,"CancelTab").click()
time.sleep(5)
#cancel - dismiss
driver.switch_to.alert.dismiss()

#text
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
time.sleep(2)
driver.find_element(By.ID, "Textbox").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Test")
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(5)
driver.quit()
