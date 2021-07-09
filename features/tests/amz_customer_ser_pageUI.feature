# Created by priyanka at 7/9/2021
Feature: Tests for Amazon Customer Service’s page UI elements

  Scenario:  Customer Service’s page UI elements are present
    Given Open Amazom customer service page
    Then Verify that Hello. What can we help you with? text is present on Customer service page
    Then Verify that some things you can go box is persent
    Then Verify that help search is present
    Then Verify that browse help topic container is present
    Then Verify that cagetory image is present