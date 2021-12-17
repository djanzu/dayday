from datetime import datetime
from pytz import timezone
import pytz

# cst = timezone('US/Central')
cst = timezone('Asia/Shanghai')
jst = timezone('Asia/Tokyo')

a = datetime(2021, 3, 15, 11, 0, 0, 0, tzinfo=cst)

js = a.astimezone(jst)

print(js)

