from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-size-base-plus a-color-base a-text-normal']]").click()

@when('Click on Add to cart button')
def add_to_cart(context):
    if len(context.driver.find_elements(By.ID, 'dropdown_selected_size_name')) == 1:
        # click size dropdown
        context.driver.find_element(By.ID, 'dropdown_selected_size_name').click()
        # click selected size
        context.driver.find_element(By.ID, 'size_name_3').click()
        sleep(3)
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    sleep(1)
