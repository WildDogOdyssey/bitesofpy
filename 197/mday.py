from datetime import date, timedelta


MAY = 5
SUNDAY = 6
ONE_WEEK = 7

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_day = date(year, MAY, 1)
    days_to_sunday = SUNDAY - first_day.weekday()
    return first_day + timedelta(days=(days_to_sunday+ONE_WEEK))