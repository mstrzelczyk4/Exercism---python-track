import datetime
import calendar


def meetup(year, month, week, day_of_week):
    if month == 12:
        last_days = 25
    else:
        last_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days - 6
    day = {"Monday": 0,
           "Tuesday": 1,
           "Wednesday": 2,
           "Thursday": 3,
           "Friday": 4,
           "Saturday": 5,
           "Sunday": 6,
           "teenth": 13,
           "1st": 1,
           "2nd": 8,
           "3rd": 15,
           "4th": 22,
           "5th": 29,
           "last": last_days}
    try:
        re = calendar.weekday(year, month, day[week])
    except ValueError:
        raise MeetupDayException("Invalid value")
    tur = day[day_of_week]
    if re > tur:
        tur += 7
    return datetime.date(year, month, day[week] - re + tur)


class MeetupDayException(Exception):
    pass
