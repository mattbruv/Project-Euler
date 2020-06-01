import datetime

def problem19():
    date = datetime.datetime(1901, 1, 1)
    end = datetime.datetime(2000, 12, 31)
    days = 0
    total = 0
    while date != end:
        days += 1
        date += datetime.timedelta(1)
        if date.weekday() == 6 and date.day == 1:
            total += 1
    print(total)

# 171