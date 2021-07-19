from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon product blouse page')
def open_product_page(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')

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
        # sleep(3)
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    # sleep(1)

@then('Verify user can click through colors')
def verify_click_through_colors(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki', 'Pink', 'White', 'Yellow', 'Light Green']
    color_names = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")
    for i in range(len(color_names)):
        color_names[i].click()
        actual_color = context.driver.find_element(By.CSS_SELECTOR, '#variation_color_name span.selection').text
        assert actual_color == expected_colors[i], f'Error color is {actual_color}, but expected {expected_colors[i]}'
