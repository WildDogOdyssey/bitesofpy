from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')

MILLER_TO_EARTH = 1 / (7 * 365 * 24)
SEC_TO_HR = 1 / (60**2)

def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    d = (PY2_DEATH_DT - start_date).total_seconds()
    return round(d * SEC_TO_HR, 2)

def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    d = (PY2_DEATH_DT - start_date).days
    return round(d * MILLER_TO_EARTH * 24 * 60, 2)
