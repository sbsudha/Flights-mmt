Feature: Make_My_Trip
  Background: Common code
    Given launch chrome browser
    When open make_my_trip page
    Then click flight module

    Scenario Outline: choose places
      Then click oneway Trip
      And enter the From places "<From>"
      And enter the To places "<To>"
      And click the Departure
          Examples:
           | From              |  To     |
           | Bengaluru          |  Pune   |

      And click the TRAVELLERS & CLASS
      And click on Apply
      And click the Fare type
      And click on search
      Then close browser


