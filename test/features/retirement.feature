
Feature: Retirement Age
  As a worker,
  I would like to know my retirement age,
  This will be based on my birthday year and month.

  Scenario Outline: Calculate full retirement age
    Given I was born in <initial>
    When I input my birthday month as <some>
    Then I will retire the year <total>

    Examples: years
      | initial | some | total |
      | 1985    | 12   | 2052  |
      | 1987    | 11   | 2054  |
      | 1999    | 06   | 2066  |

