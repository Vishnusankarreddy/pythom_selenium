# Rabio button, and Check box.
from selenium.webdriver.common.by import By
from Selenium2_RadioButton_in import driver



driver.find_element(By.XPATH,"//input[@value='Mle']")

li = driver.find_element(By.XPATH, "//input[@type='checkbox']")

for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Cricket':
        ele.click()