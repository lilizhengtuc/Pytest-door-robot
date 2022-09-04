from pytest_bdd import scenario, given, when, then

from door_robot.robot import admit_guest
from .guest_time import *


# 5 happy path scenarios
@scenario("doorrobot.feature", "Let anyone in at standard bistro hours")
def test_door_robot_std_hours():
    pass


@given("A guest of any age", target_fixture="guest")
def given_guest():
    return base_guest


@when("Guest tries to enter bistro on a mon-thurs during opening hours 16-23", target_fixture="admission_mon_thur_std_hours")
def when_guest_enter_std_hours(guest):
    return admit_guest(guest, standard_opening_hour)


@then("Any guest is let in")
def then_guest_in(admission_mon_thur_std_hours):
    assert admission_mon_thur_std_hours is True


@scenario("doorrobot.feature", "Let a 18 year old guest in on a friday night")
def test_18_yo_fri_night():
    pass


@given("A guest of 18 years old", target_fixture="guest_18_yo")
def given_18_yo_guest():
    return base_guest | {"age": 18}


@when("Guest tries to enter bistro on a friday night from 21-03",
      target_fixture="fri_guest_admission")
def when_18_yo_enter_fri_night(guest_18_yo):
    return admit_guest(guest_18_yo, fri_club_hours)


@then("18 years old guest is let in")
def then_let_guest_in(fri_guest_admission):
    assert fri_guest_admission is True


# 3rd scenario
@scenario("doorrobot.feature",
          "Let a 19 year old guest in on a friday-saturday midnight")
def test_19_yo_fri_midnight():
    pass


@given("A guest of 19 years old", target_fixture="guest_19_years_old")
def given_19_yo_guest():
    return base_guest | {"age": 19}


@when("Guest tries to enter bistro on a friday-saturday midnight at 00:00",
      target_fixture="fri_midnight_guest_admission")
def when_19_yo_enter_fri_midnight(guest_19_years_old):
    return admit_guest(guest_19_years_old, fri_midnight)


@then("19 years old guest is let in")
def then_let_guest_in(fri_midnight_guest_admission):
    assert fri_midnight_guest_admission is True


@scenario("doorrobot.feature", "Let a 25 year old guest in on a saturday night")
def test_25_yo_sat_night():
    pass


@given("A guest of 25 years old", target_fixture="guest_25_year_old")
def given_25_yo_guest():
    return base_guest | {"age": 25}


@when("Guest tries to enter bistro on a saturday night from 21-03",
      target_fixture="sat_guest_admission")
def when_25_yo_enter_sat_night(guest_25_year_old):
    return admit_guest(guest_25_year_old, sat_club_hours)


@then("25 years old guest is let in")
def then_let_guest_in(sat_guest_admission):
    assert sat_guest_admission is True


@scenario("doorrobot.feature", "Let a 26 year old guest in on a saturday-sunday midnight")
def test_26_yo_sat_midnight():
    pass


@given("A guest of 26 years old", target_fixture="guest_26_yo")
def given_26_yo_guest():
    return base_guest | {"age": 26}


@when("Guest tries to enter bistro on a saturday-sunday midnight at 00:00",
      target_fixture="sat_midnight_guest_admission")
def when_26_yo_enter_fri_night(guest_26_yo):
    return admit_guest(guest_26_yo, sat_midnight)


@then("26 years old guest is let in")
def then_let_guest_in(sat_midnight_guest_admission):
    assert sat_midnight_guest_admission is True


# 5 sad path scenarios
@scenario("doorrobot.feature", "Deny anyone at standard closing hours on mon-thurs")
def test_deny_anyone_closing_mon_thurs():
    pass


@given("A guest of certain age", target_fixture="guest_27_yo")
def when_guest_27_yo_mon_closing():
    return base_guest | {"age": 27}


@when("Guest tries to enter bistro on a mon-thurs during closing hours 23-16",
      target_fixture="mon_closing_hour_denial")
def when_27_yo_enter_mon_closing(guest_27_yo):
    return admit_guest(guest_27_yo, mon_closing_hours2)


@then("A guest of certain age is denied")
def then_deny_guest(mon_closing_hour_denial):
    assert mon_closing_hour_denial is False


@scenario("doorrobot.feature", "Deny anyone at closing hours on fri-sat")
def test_deny_anyone_closing_fre_sat():
    pass


@given("A random guest of any age", target_fixture="guest_13_yo")
def given_13_yo_guest():
    return base_guest | {"age": 13}


@when("Guest tries to enter bistro on a fri-sat during closing hours 03-16",
      target_fixture="sat_closing_denial")
def when_13_yo_enter_sat_closing(guest_13_yo):
    return admit_guest(guest_13_yo, sat_closing)


@then("A random guest of any age is denied")
def then_guest_denied(sat_closing_denial):
    assert sat_closing_denial is False


@scenario("doorrobot.feature", "Deny anyone at closing hours on sun")
def test_deny_anyone_closing_sun():
    pass


@given("A random guest", target_fixture="guest_32_yo")
def given_32_yo_guest():
    return base_guest | {"age": 32}


@when("Guest tries to enter bistro on a sun during closing hours 03-24",
      target_fixture="sun_closing_denial")
def when_32_yo_enter_sun_closing(guest_32_yo):
    return admit_guest(guest_32_yo, sun_closing)


@then("The random guest is denied")
def then_guest_denied(sun_closing_denial):
    assert sun_closing_denial is False


@scenario("doorrobot.feature", "Deny a 17 year old guest on a friday night")
def test_deny_17_yo_fri_night():
    pass


@given("A guest of 17 years old", target_fixture="guest_17_yo")
def given_17_yo_guest():
    return base_guest | {"age": 17}


@when("17 years old guest tries to enter bistro on a friday night from 21-03",
      target_fixture="denial_17_yo_fri")
def when_17_yo_enter_fri(guest_17_yo):
    return admit_guest(guest_17_yo, fri_club_hours)


@then("17 years old guest is denied")
def then_guest_denied(denial_17_yo_fri):
    assert denial_17_yo_fri is False


@scenario("doorrobot.feature", "Deny a 24 year old guest on a saturday night")
def test_deny_24_yo_sat():
    pass


@given("A guest of 24 years old", target_fixture="guest_24_yo")
def given_guest_24_yo():
    return base_guest | {"age": 24}


@when("24 years old guest tries to enter bistro on a saturday night from 21-03",
      target_fixture="denial_guest_24_yo_sat")
def when_guest_24_yo_enter(guest_24_yo):
    return admit_guest(guest_24_yo, sat_club_hours)


@then("24 years old guest is denied")
def deny_24_yo_sat(denial_guest_24_yo_sat):
    assert denial_guest_24_yo_sat is False
