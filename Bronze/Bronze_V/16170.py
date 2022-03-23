import datetime

time = datetime.datetime.now()
print(time.year)
print('0' + str(time.month)) if len(str(time.month)) == 1 else print(time.day)
print('0' + str(time.day)) if len(str(time.day)) == 1 else print(time.day)
