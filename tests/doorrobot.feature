# Created by lilizheng at 2022-05-25
Feature: Door robot can let in people of the right age at right time
  As a bistro manager
  I want the door robot to let in people of the right age at the right time
  So that 1) nobody can enter the bistro at wrong time; 2) right people can enter at right time

# Happy path test cases
  Scenario: Let anyone in at standard bistro hours
    Given A guest of any age
    When Guest tries to enter bistro on a mon-thurs during opening hours 16-23
    Then Any guest is let in

  Scenario: Let a 18 year old guest in on a friday night
    Given A guest of 18 years old
    When Guest tries to enter bistro on a friday night from 21-03
    Then 18 years old guest is let in

  Scenario: Let a 19 year old guest in on a friday-saturday midnight
    Given A guest of 19 years old
    When Guest tries to enter bistro on a friday-saturday midnight at 00:00
    Then 19 years old guest is let in

  Scenario: Let a 25 year old guest in on a saturday night
    Given A guest of 25 years old
    When Guest tries to enter bistro on a saturday night from 21-03
    Then 25 years old guest is let in

  Scenario: Let a 26 year old guest in on a saturday-sunday midnight
    Given A guest of 26 years old
    When Guest tries to enter bistro on a saturday-sunday midnight at 00:00
    Then 26 years old guest is let in


# Sad path test cases
  Scenario: Deny anyone at standard closing hours on mon-thurs
    Given A guest of certain age
    When Guest tries to enter bistro on a mon-thurs during closing hours 23-16
    Then A guest of certain age is denied

  Scenario: Deny anyone at closing hours on fri-sat
    Given A random guest of any age
    When Guest tries to enter bistro on a fri-sat during closing hours 03-16
    Then A random guest of any age is denied

  Scenario: Deny anyone at closing hours on sun
    Given A random guest
    When Guest tries to enter bistro on a sun during closing hours 03-24
    Then The random guest is denied

  Scenario: Deny a 17 year old guest on a friday night
    Given A guest of 17 years old
    When 17 years old guest tries to enter bistro on a friday night from 21-03
    Then 17 years old guest is denied

  Scenario: Deny a 24 year old guest on a saturday night
    Given A guest of 24 years old
    When 24 years old guest tries to enter bistro on a saturday night from 21-03
    Then 24 years old guest is denied




