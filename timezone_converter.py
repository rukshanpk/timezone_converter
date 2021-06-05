from datetime import date, datetime
from pytz import timezone
import sys


def main(my_date, my_time, target_time_zone):
    #my_date = raw_input("Date :")
    #my_time = raw_input("Time :")
    #target_time_zone = raw_input("Target Time Zone :")
    date_time_str = my_date+" "+my_time
    date_time_obj = datetime.strptime(
        date_time_str, '%Y-%m-%d %H:%M:%S')
    indian_standard = timezone('Asia/Colombo')
    loc_dt = indian_standard.localize(datetime(date_time_obj.year, date_time_obj.month,
                                               date_time_obj.day, date_time_obj.hour, date_time_obj.minute, date_time_obj.second))
    print(loc_dt)
    au_tz = timezone(target_time_zone)
    print(loc_dt.astimezone(au_tz))

    #fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    ##my_date = raw_input("Date :")
    ##my_time = raw_input("Time :")
    #my_date = "2021-10-25"
    #my_time = "22:25:00"
    #date_time_str = my_date+" "+my_time
    # date_time_obj = datetime.datetime.strptime(
    #    date_time_str, '%Y-%m-%d %H:%M:%S')
    ##dt = date_time_obj.time(timezone('UTC'))
    #dt = date_time_obj
    # print('Date:', dt.)
    #fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    #my_zone = "+0530+0530"
    #my_date = raw_input("Date :")
    #my_time = raw_input("Date :")
    # fmt_time = datetme.datetime.strptime(
    #    my_date+" "+my_time, "%Y-%m-%d %H:%M:%S")
    # print(fmt_time)
    # Current time in UTC
    # print(datetime.now(timezone('Asia/Colombo')).strftime(fmt))
    #now_utc = datetime.now(timezone('UTC'))
    # print now_utc.strftime(fmt)
#
    # Convert to US/Pacific time zone
    #now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    # print now_pacific.strftime(fmt)
#
    # Convert to Europe/Berlin time zone
    #now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
    # print now_berlin.strftime(fmt)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
