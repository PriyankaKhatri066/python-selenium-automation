from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify "{expected_text}" text is displayed')
def empty_cart(context, expected_text):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    assert actual_text == expected_text, f"Expected {expected_text} instead got {actual_text}"

