import datetime

now = datetime.datetime.now()
last = datetime.datetime(2021, 9, 29, 0, 0, 0)
start = datetime.datetime(2021, 8, 29, 0, 0, 0)
pa = now - start
re = last - now
print("passed {} ".format(pa))
print("remain {} ".format(re))

