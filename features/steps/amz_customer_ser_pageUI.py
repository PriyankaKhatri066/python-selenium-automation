from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazom customer service page')
def open_customer_ser_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@then("Verify that {Expected} text is present on Customer service page")
def verify_text(context, Expected):
    actual= context.driver.find_element(By.CSS_SELECTOR, 'div.ss-landing-container h1').text
    assert Expected == actual, f'Expected text is {Expected}, but got {actual}'

@then('Verify that some things you can go box is persent')
def box_some_things(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.a-section.a-spacing-large.ss-landing-container-wide')

@then('Verify that help search is present')
def customer_help_search(context):
    context.driver.find_element(By.ID, 'helpsearch')

@then('Verify that browse help topic container is present')
def help_topic_container(context):
    context.driver.find_element(By.CSS_SELECTOR, '.csg-hover-box-categories')

@then('Verify that cagetory image is present')
def category_image(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div#help-gateway-category-0 img.csg-hb-promo')
