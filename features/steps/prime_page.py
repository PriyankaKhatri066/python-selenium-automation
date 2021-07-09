from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given ('Open Amazon Prime page')
def open_prime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then ('Verify that {box_count} benefit boxes are displayed')
def prime_benefit_boxes(context, box_count):
    boxes = context.driver.find_elements(By.CSS_SELECTOR, 'div.benefit-box')
    print(boxes)
    assert len(boxes) == int(box_count) , f'Expected {box_count} boxes but got {len(boxes)}'
