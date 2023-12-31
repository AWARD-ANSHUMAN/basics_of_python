import datetime

# creating a date
# date = datetime.date(2023, 12, 30)   # passing date in yy-mm-dd format
# print(date)

# creating today date
today = datetime.date.today()
print(today)
# print(today.day)
# print(today.year)
# print(today.month)
# print(today.weekday())

# creating a time delta
time_delta = datetime.timedelta(days=8)
# today=today+time_delta
# print(today)

# date2= date1 + time_delta
# time_delta =date2-date_1

# t= datetime.time()        returns time object
# dt= datetime.datetime(pass ant data,tzinfo=pytz.utc)   returns datetime object (naive:without time zone info)/timezone aware)
# dt.date
# dt.time

# dt_today= datetime.datetime.today()     timezone = none
# utc aware time zone
# dt_utcnow= datetime.datetime.now(tz=pytz.utc)          option to pass timezone/ returns utc time
# local time zone
# dt_local=dt_utcnow.astimezone(putz.timezone())


# pipinstall pytz to get timezone aware datetime
