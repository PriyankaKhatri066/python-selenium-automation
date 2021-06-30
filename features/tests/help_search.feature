# Created by priyanka at 6/30/2021
Feature: Amazon Help Search
  # Enter feature description here

  Scenario: User can Search for solutions of Cancelling an order on Amazon
    # Enter steps here
    Given Open Amazon Help page
    When Use “Search Help Library” field and search for Cancel order
    And Emulate hitting keyboard ENTER, send_keys command
    Then  Verify that Cancel Items or Orders text is present


