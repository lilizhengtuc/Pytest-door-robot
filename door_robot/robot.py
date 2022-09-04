from datetime import datetime


def admit_guest(guest: dict, time: datetime) -> bool:
    if time.isoweekday() < 6 and time.hour < 16:
        return False

    if time.isoweekday() >= 6 and 3 <= time.hour < 16:
        return False

    if time.isoweekday() == 7 and time.hour > 3:
        return False

    if time.isoweekday() == 5 and time.hour >= 21 and guest["age"] < 18:
        return False

    if time.isoweekday() == 6 and time.hour >= 21 and guest["age"] < 25:
        return False

    if time.isoweekday() < 5 and time.hour >= 23:
        return False

    return True
