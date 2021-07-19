from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__regular-price')
DEAL_ITEMS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class,'prime-price')]]/div")

@given('Open Amazon Wholefoodsdeals page')
def open_wfsdeals_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify that Wholefoods products have product name and regular price')
def verify_name_price(context):
    deal_items = context.driver.find_elements(*DEAL_ITEMS)
    for p in deal_items:
        assert 'Regular' in p.text, f'Expected Regular price not found in {p.text}'
        product_name = p.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Product name is missing'