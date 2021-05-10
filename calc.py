import datetime

now = datetime.datetime.now()
last = datetime.datetime(2021, 6, 7, 0, 0, 0)
start = datetime.datetime(2021, 5, 7, 0, 0, 0)
pa = now - start
re = last - now
print("passed {} ".format(pa))
print("remain {} ".format(re))

