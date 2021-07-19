from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@when('Click on the Cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()

@when('Click sign in from popup')
def click_signIn_button(context):
    sign_in_button = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
    sign_in_button.click()

@then('Verify cart has {expected_count} item')
def cart_count(context, expected_count):
    actual_count = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected_count ==actual_count, f'Expected {expected_count}, but got {actual_count}'

@then('Verify Amazon Hamburger Menu icon is present')
def ham_menu_visible(context):
    print('\n Using find_element')
    element= context.driver.find_element(By.ID, 'nav-hamburger-menu')
    print(element)

    print('\n Using find_elementsss')
    elements = context.driver.find_elements(By.ID, 'nav-hamburger-menu')
    print(elements)