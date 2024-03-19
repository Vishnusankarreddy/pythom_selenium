import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
# dropdown = Select(driver.find_element(By.XPATH,"//select[@id='first']"))
# time.sleep(5)
# dropdown.select_by_visible_text("Google")
driver.find_element(By.XPATH, "//select[@id='first']/option[@value='Google']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//select[@id='animals']/option[text()='Avatar']").click()
time.sleep(5)

#back
#refresh
#forward

driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()
