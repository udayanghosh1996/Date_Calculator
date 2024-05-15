from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def add_time_to_date(years, months, weeks, days, hours, minutes, seconds):
    # Get the current date and time
    current_date = datetime.now()
    print("Current date and time:", current_date)

    # Create a relativedelta object for years and months
    date_offset = relativedelta(years=years, months=months)

    # Create a timedelta object for weeks, days, hours, minutes, and seconds
    time_offset = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)

    # Calculate the new date and time
    new_date = current_date + date_offset + time_offset
    return current_date, new_date
