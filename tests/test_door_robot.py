import pytest

from door_robot.robot import admit_guest
from .guest_time import *


@pytest.mark.parametrize(
    ("guest", "time", "expected"),
    (
            (base_guest, mon_closing_hours1, False),
            (base_guest, sat_closing, False),
            (base_guest, mon_closing_hours2, False),
            (base_guest, sun_closing, False),
            (base_guest, fri_midnight, True),
            (base_guest | {"age": 10}, fri_bistro_time, True),
            (base_guest | {"age": 10}, sat_bistro_time, True),
            (base_guest | {"age": 24}, sat_sun_21, False),
            (base_guest | {"age": 18}, fri_sat_last_call, True),
            (base_guest | {"age": 25}, sat_sun_last_call, True),

    )

)
def test_door_robot(guest, time, expected):
    assert admit_guest(guest, time) is expected
