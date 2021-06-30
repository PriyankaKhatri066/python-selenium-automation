from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\ashok\\Documents\\JobEasy-Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=04SRM7N2HTHX3K9KYCQN&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
# Find icon
# driver.find_element(By.CSS_SELECTOR, "a.a-link-nav-icon i.a-icon").click()
# Create Account - $$('h1.a-spacing-small')
# Your name Box
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name').send_keys('Priyanka Khatri')
# Email
driver.find_element(By.CSS_SELECTOR, 'input#ap_email').send_keys('test@test.com')
# password
driver.find_element(By.CSS_SELECTOR, 'input#ap_password').send_keys('Test')
# password must be at least 6 characters ??
driver.find_element(By.XPATH, "")
# password check
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check').send_keys('Test')
# create account
driver.find_element(By.CSS_SELECTOR, 'input#continue').click()
# conditions of use
# driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_condition_of_use?']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_privacy_notice?']").click()
# sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid']").click()



