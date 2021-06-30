# Created by ashok at 6/6/2021
Feature: Tests for sigh in page
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    # Enter steps here
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened
