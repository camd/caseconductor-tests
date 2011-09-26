Feature: Login Authentication

Scenario: Test logging in when logged out
  Given user "admin" is not logged in
  When user "admin" logs in
  Then user "admin" is logged in