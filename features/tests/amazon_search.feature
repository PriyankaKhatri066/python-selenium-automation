# Created by priyanka at 5/23/2021
Feature: Test Amazon Search
  # Enter feature description here

  Scenario: User can search for a product
    # Enter steps here
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked

   Scenario: Amazon footer has correct count of links
    Given Open Amazon page
    Then Verify Amazon footer has 40 links