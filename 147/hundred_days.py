from datetime import date


from dateutil.rrule import rrule, DAILY


TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    return [day.date() for day in rrule(DAILY,
                                        count=100,
                                        dtstart=start_date,
                                        byweekday=[0, 1, 2, 3, 4])]