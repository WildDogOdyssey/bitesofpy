from datetime import date, timedelta


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_day = date(year, 5, 1)
    days_to_sunday = 6 - first_day.weekday()
    return first_day + timedelta(days=(days_to_sunday+7))