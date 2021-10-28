import datetime

now = datetime.datetime.now()
start = [
  {"id": 1, "dt": datetime.datetime(2021, 8, 29, 0, 0, 0)},
  {"id": 2, "dt": datetime.datetime(2021, 10, 24, 0, 0, 0)},
  {"id": 3, "dt": datetime.datetime(2021, 10, 28, 11, 0, 0)},
  {"id": 4, "dt": datetime.datetime(2021, 11, 28, 0, 0, 0)}
]

for i in start:
  if i['id'] == 1:
    old = i
    continue
  pa = i['dt'] - old['dt']
  re = i['dt'] - now
  print("{} ~ {} / passed {}".format(old['dt'], i['dt'], pa))
  old = i

print("remain {} ".format(re))

