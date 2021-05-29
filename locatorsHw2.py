from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\ashok\\Documents\\JobEasy-Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Amazon logo
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").click()

# Email field
# driver.find_element(By.ID, "ap_email").send_keys("abc@gmail.com")

# Continue button
# driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

# Need help
driver.find_element(By.CLASS_NAME, "a-expander-prompt").click()

# forgot your password
# driver.find_element(By.ID, "auth-fpp-link-bottom").click()

# other issue with sign-in
# driver.find_element(By.ID, "ap-other-signin-issues-link").click()

# create your account
# driver.find_element(By.ID, "createAccountSubmit").click()

# driver.find_element(By.XPATH, "//a[text()='Conditions of Use']").click()

driver.find_element(By.XPATH, "//a[text()='Privacy Notice']").click()

