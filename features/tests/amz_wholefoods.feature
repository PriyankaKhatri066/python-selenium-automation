# Created by priyanka at 7/16/2021
Feature: Test for Amazon Wholefoods

  Scenario: Every product on the Wholefoodsdeals page has a text ‘Regular’ and a product name
    Given Open Amazon Wholefoodsdeals page
    Then Verify that Wholefoods products have product name and regular price