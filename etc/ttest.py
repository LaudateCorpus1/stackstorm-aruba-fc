import datetime

my_time=1514764800004
my_time = int(my_time / 10)

# 1571005498

datetime_time = datetime.datetime.fromtimestamp(my_time)

print(datetime_time)
