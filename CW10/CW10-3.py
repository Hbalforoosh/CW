from datetime import date
from datetime import datetime
from datetime import timedelta
# today = date.today()
# print(today)
special_date = date(2025, 5, 5)
# print(special_date)
# print(f'Year: {today.year}')
# print(special_date.day)
now = datetime.now()
# print(now)
delta = timedelta(days=4, hours=18, minutes=30)
futurtime = datetime.now() + timedelta(days=5, hours=2)
# print(delta)
# print(futurtime)
string = "2025-08-26 18:57:02"
dt = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
# print(dt)


#####################################################
name = input("please input your name: ")
birthday = input("please input your birthday (YYYY-MM-DD): ")
today = date.today()
birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
if today.day == birthday_date.day and today.month == birthday_date.month:
    print(f'ohh yes! {name} Happy birthday to you......')
