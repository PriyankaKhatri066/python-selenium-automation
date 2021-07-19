# Created by priyanka at 6/6/2021
Feature: Tests for sigh in page
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    # Enter steps here
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario: Sign in page can be opened from sign in popup
    Given Open Amazon page
    When Click sign in from popup
    Then Verify Sign in page opened