#!/usr/bin/env python
# encoding: utf-8
'''
@time: 2023/8/18 上午 11:02
@author: Sherwin (sherwin@retailingdata.com.tw)
@file: create_year_calendar.py
@type: 
@project: 
@desc: 
'''

import datetime
import calendar
import pandas as pd
from utils import connect_DB

# 定义节日列表，这里只是一个示例，实际情况中可以根据需要添加更多的节日
holidays = {
    (1, 1): "元旦連假",
    (1, 2): "元旦連假",

    (1, 20): "春節連假",
    (1, 21): "春節連假",
    (1, 22): "春節連假",
    (1, 23): "春節連假",
    (1, 24): "春節連假",
    (1, 25): "春節連假",
    (1, 26): "春節連假",
    (1, 27): "春節連假",
    (1, 28): "春節連假",
    (1, 29): "春節連假",

    (2, 25): "228連假",
    (2, 26): "228連假",
    (2, 27): "228連假",
    (2, 28): "228連假",

    (4, 1): "清明連假",
    (4, 2): "清明連假",
    (4, 3): "清明連假",
    (4, 4): "清明連假",
    (4, 5): "清明連假",

    (4, 29): "勞動連假",
    (4, 30): "勞動連假",
    (5, 1): "勞動連假",

    (6, 22): "端午連假",
    (6, 23): "端午連假",
    (6, 24): "端午連假",
    (6, 25): "端午連假",

    (9, 29): "中秋連假",
    (9, 30): "中秋連假",
    (10, 1): "中秋連假",

    (10, 7): "國慶連假",
    (10, 8): "國慶連假",
    (10, 9): "國慶連假",
    (10, 10): "國慶連假",

    (12, 30): "元旦連假",
    (12, 31): "元旦連假",
}
makeupdays = {
    (1, 7): "補班日",
    (2, 4): "補班日",
    (2, 18): "補班日",
    (3, 25): "補班日",
    (6, 17): "補班日",
    (9, 23): "補班日",
}

def generate_year_calendar(year):
    year_calendar = []
    for month in range(1, 13):
        num_days = calendar.monthrange(year, month)[1]

        for day in range(1, num_days + 1):
            date = datetime.date(year, month, day)
            weekday = date.weekday()  # 0-6 表示星期一到星期日
            is_workday = weekday < 5  # 周一到周五为工作日

            holiday_name = holidays.get((month, day))
            makeupdays_name = makeupdays.get((month, day))

            if holiday_name:
                day_info = {"date": datetime.datetime(year, month, day), "weekday": weekday, "is_workday": False,
                            "holiday": holiday_name}
            elif makeupdays_name:
                day_info = {"date": datetime.datetime(year, month, day), "weekday": weekday, "is_workday": True,
                            "holiday": makeupdays_name}
            else:
                day_info = {"date": datetime.datetime(year, month, day), "weekday": weekday, "is_workday": is_workday,
                            "holiday": None}

            year_calendar.append(day_info)

    return year_calendar

if __name__ == '__main__':
    year = int(input("請輸入年份："))
    d = pd.DataFrame(generate_year_calendar(year))
    engine, con = connect_DB()
    d.to_sql(name="c_schedule", con=con, schema="employee", index=False, if_exists="append")
    con.close()
    engine.dispose()