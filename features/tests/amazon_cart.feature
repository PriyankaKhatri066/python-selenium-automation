# Created by priyanka at 6/30/2021
Feature: Test Amazon Cart

  Scenario: User can see empty shopping cart
    Given Open Amazon page
    When Click on the Cart icon
    Then Verify "Your Amazon Cart is empty" text is displayed

  Scenario: User can add product in cart
    Given Open Amazon page
    When Input Women shoes in search field
    And Click on Amazon search icon
    And Click on first product
    And Click on Add to cart button
    Then Verify cart has 1 item