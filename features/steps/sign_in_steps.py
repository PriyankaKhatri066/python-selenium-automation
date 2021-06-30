from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.driver.find_element(By.ID, 'ap_email')
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'wrong url {context}'