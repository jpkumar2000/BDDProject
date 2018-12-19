Feature: The user can login into outsystem

 Scenario: The user can enter username and password to login to outsystems
  Given the user is on the login page
   When the user enters the username
    And the user enters the password
    And clicks on the Log In button
    Then request page will be loaded