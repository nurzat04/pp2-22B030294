from datetime import datetime, time
def difinsec(a, b):
    timedelta = b - a
    return timedelta.days * 24 * 3600 + timedelta.seconds

a = datetime.strptime('2004-03-10 06:00:00', '%Y-%m-%d %H:%M:%S')
b = datetime.now()
print(difinsec(a, b))

