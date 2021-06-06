#!/usr/bin/env python
from datetime import date, datetime
from pytz import timezone
import sys


def tz_converter(my_date_time, target_time_zone):
    date_time_str = my_date_time
    date_time_obj = datetime.strptime(
        date_time_str, '%Y-%m-%d %H:%M:%S')
    indian_standard = timezone('Asia/Colombo')
    loc_dt = indian_standard.localize(datetime(date_time_obj.year, date_time_obj.month,
                                               date_time_obj.day, date_time_obj.hour, date_time_obj.minute, date_time_obj.second))
    # print(loc_dt)
    target_tz = timezone(target_time_zone)
    target_dt = loc_dt.astimezone(target_tz)
    print(str(loc_dt)+" ----> "+str(target_dt))


def main(start_date_time, end_date_time, target_time_zone):
    tz_converter(sys.argv[1], sys.argv[3])
    tz_converter(sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
