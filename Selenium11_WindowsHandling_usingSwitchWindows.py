# Parent window
# All window
# Switch to child window
# do action in child window
# close current window


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")

# Parent window
parent = driver.current_window_handle
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()
time.sleep(10)


# All window
windows = driver.window_handles

# Switch to child window
for win in windows:
    if win != parent:
        driver.switch_to.window(win)

# do action in child window
driver.find_element(By.XPATH, "//a[@class='nav-link']").click()
time.sleep(20)
driver.close()


driver.switch_to.window(parent)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

# Close current window
driver.quit()