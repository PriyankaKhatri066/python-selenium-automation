from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open amazon BestSellers page')
def open_bestseller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are {expected_count} links')
def bestseller_link_count(context, expected_count):
    actual_count = len(context.driver.find_elements(By.CSS_SELECTOR,'#zg_tabs a'))
    assert actual_count == int(expected_count), f'Expected {expected_count} links, but got {actual_count}'