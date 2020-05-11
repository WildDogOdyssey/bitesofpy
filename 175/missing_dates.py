from datetime import timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """

    # find range and min from dates
    min_date = min(dates)
    num_days = (max(dates) - min_date).days

    # build full range of dates with range and min
    full_dates = [min_date + timedelta(days=i) for i in range(num_days)]

    # return difference between full range set and dates set
    return set(full_dates) - set(dates)