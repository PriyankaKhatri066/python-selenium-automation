from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\ashok\\Documents\\JobEasy-Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()

# implicit wait
# checks every 100 ms for web element 1/10 sec
driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('dress')

# wait for 4 sec
# sleep(4)

# Explicit wait
# checks every 500 ms for condition 0.5 sec
driver.wait = WebDriverWait(driver, 10)
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message = 'Error, search button not clickable')

# click search
e.click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
