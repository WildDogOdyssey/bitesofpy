from datetime import date, timedelta


TODAY = date.today()

def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    delta = timedelta(days=num_days)
    period, count = 1, 0
    while True:
        yield start_date + (period)*delta
        count += 1
        if count % num_bites == 0:
            period += 1

# test = gen_bite_planning(2, 1)
# for _ in range(10):
#     print(next(test))