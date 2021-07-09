from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input {search_word} in search field')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    sleep(2)

@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    sleep(2)

@then('Verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    print(f'Actual result: {actual_result}')
    expected_result = '"Table"'

@then('Verify Amazon footer has {link_count} links')
def footer_link_count(context, link_count):
    count = len(context.driver.find_elements(By.CSS_SELECTOR, '.navFooterDescItem a.nav_a'))
    assert count == int(link_count), f'Expected count is {link_count}, but got {count}'

