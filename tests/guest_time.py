from datetime import datetime

base_guest = {
    "name": "Alex Xu",
    "age": 45,
}

standard_opening_hour = datetime(2022, 6, 15, 16, 00, 00)
fri_club_hours = datetime(2022, 5, 27, 23, 00, 00)
fri_midnight = datetime(2022, 5, 28, 00, 00, 00)
sat_club_hours = datetime(2022, 5, 28, 23, 00, 00)
sat_midnight = datetime(2022, 5, 29, 00, 00, 00)
mon_closing_hours1 = datetime(2022, 5, 30, 15, 00, 00)
mon_closing_hours2 = datetime(2022, 5, 30, 23, 00, 1)
sat_closing = datetime(2022, 5, 28, 4, 00, 00)
sun_closing = datetime(2022, 5, 29, 9, 00, 00)
fri_bistro_time = datetime(2022, 5, 27, 16, 1, 00)
sat_bistro_time = datetime(2022, 5, 28, 16, 1, 00)
sat_sun_21 = datetime(2022, 5, 28, 21, 00, 00)
fri_sat_last_call = datetime(2022, 5, 28, 2, 59, 00)
sat_sun_last_call = datetime(2022, 5, 29, 2, 59, 00)