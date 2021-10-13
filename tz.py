import datetime
import pytz
from dateutil import tz

# pst = tz.gettz('PT')
pst = datetime.timezone(datetime.timedelta(hours=-8))
jst = datetime.timezone(datetime.timedelta(hours=9))

date1 = datetime.datetime(2021, 10, 13, 9, 0, 0, tzinfo=pst)
print(date1)

date2 = date1.astimezone(pytz.timezone('Asia/Tokyo'))

print(date2)

