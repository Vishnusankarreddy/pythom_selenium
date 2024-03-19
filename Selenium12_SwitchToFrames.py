import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")

# Using the Index
driver.switch_to.frame(0)

#Using the name or id
driver.switch_to.frame("singleframe") #id
driver.switch_to.frame("singleframe") #name


# using the webelement
single_frame = driver.find_element(By.XPATH, "//div[@id='Single']/iframe")
driver.switch_to.frame(single_frame)

text = driver.find_element(By.TAG_NAME, "input")
text.send_keys("This is framework")
time.sleep(5)
driver.quit()