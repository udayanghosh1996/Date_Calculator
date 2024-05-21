from datetime import datetime, timedelta


def add_time(ini_date, ini_month, ini_year, ini_hour, ini_min, ini_sec, years=0, months=0, weeks=0, days=0, hours=0,
             minutes=0, seconds=0):
    # Current date and time
    if ini_date == ini_month == ini_year == ini_hour == ini_min == ini_sec == 0:
        current_datetime = datetime.now()
    else:
        current_datetime = datetime(ini_year, ini_month, ini_date, ini_hour, ini_min, ini_sec)

    # Adding years and months manually due to variability in month lengths and leap years
    new_month = current_datetime.month + months
    new_year = current_datetime.year + years + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1

    # Handle the day to ensure it's valid (e.g., February 30 doesn't exist)
    max_day = 28
    if new_month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif new_month in (4, 6, 9, 11):
        max_day = 30
    elif new_month == 2:
        if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
            max_day = 29
        else:
            max_day = 28

    # Ensure that day does not exceed the max day of the month
    new_day = min(current_datetime.day, max_day)

    # Creating a new datetime object for the modified year, month, and day
    result_date = datetime(new_year, new_month, new_day, current_datetime.hour, current_datetime.minute,
                           current_datetime.second)

    # Adding weeks, days, hours, minutes, and seconds using timedelta
    result_date += timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)

    return current_datetime, result_date
