from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TEXT = (By.XPATH, "//div[@class='help-content']//h1")

@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Use “Search Help Library” field and search for Cancel order')
def search_cancel_order(context):
    context.driver.find_element(By.ID, "helpsearch").send_keys('Cancel order')
    sleep(3)

@when('Emulate hitting keyboard ENTER, send_keys command')
def hit_enter(context):
    context.driver.find_element(By.ID, "helpsearch").submit()

@then('Verify that {search_word} text is present')
def cancel_text_present(context, search_word):
    assert search_word in context.driver.find_element(*TEXT).text, f'Expected text not in {context.driver.find_element(*TEXT).text}.'

