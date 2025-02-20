
from chinese_calendar import is_workday, is_holiday
import datetime


current_date = datetime.datetime.now().date()
print(current_date)

date = datetime.datetime(2025, 2, 9)
print(is_holiday(date))
