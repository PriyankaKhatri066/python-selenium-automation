from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\ashok\\Documents\\JobEasy-Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
search = driver.find_element(By.ID, "helpsearch").send_keys('Cancel order')
driver.implicitly_wait(3)
driver.find_element(By.ID, "helpsearch").submit()
actual_result= driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
print(f'Actual result: {actual_result}')
expected_result= 'Cancel Items or Orders'
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
driver.quit()