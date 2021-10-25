import datetime

now = datetime.datetime.now()
start = [
  {"id": 1, "dt": datetime.datetime(2021, 8, 29, 0, 0, 0)},
  {"id": 2, "dt": datetime.datetime(2021, 10, 24, 0, 0, 0)},
  {"id": 3, "dt": datetime.datetime(2021, 11, 24, 0, 0, 0)}
]

for i in start:
  if i['id'] == 1:
    old = i
    continue
  pa = i['dt'] - old['dt']
  re = i['dt'] - now
  print("{} ~ {} / passed {} / remain {} ".format(old['dt'], i['dt'], pa, re))
  old = i

