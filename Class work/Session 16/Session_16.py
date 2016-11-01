class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

tt1 = Time()
tt1.hour = 5
tt1.minute = 59
tt1.second = 30

tt2 = Time()
tt2.hour = 9
tt2.minute = 23
tt2.second = 30



def print_time(time):
    print("%.2d:%.2d:%.2d" %(time.hour, time.minute, time.second))

# print_time(time) 

def is_after(t1, t2):
    t1_total_seconds = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_total_seconds = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_total_seconds > t2_total_seconds

# print(is_after(tt1,tt2))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second > 60:
        sum.minute += 1
        sum.second -= 60
    if sum.minute > 60:
        sum.hour += 1
        sum.minute -= 60
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  30

duration = Time()
duration.hour = 1
duration.minute = 55
duration.second = 0

done = add_time(start, duration)
# print_time(done)

def subtract_time(t1, t2):
    diff = Time()
    diff.hour = t1.hour - t2.hour
    diff.minute = t1.minute - t2.minute
    diff.second = t1.second - t2.second
    if diff.second < 0:
        diff.minute -= 1
        diff.second += 60
    if diff.minute < 0:
        diff.hour -= 1
        diff.minute += 60
    return diff

diff_time = subtract_time(start,duration)
# print_time(diff_time)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time_2(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

#----------------- Exercise 5

from datetime import date
import time
import datetime

days_of_week = ["Sunday" ,"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

today = date.today()
day_number_of_week = date.weekday(today)
day_of_week = days_of_week[day_number_of_week]

print("Today is %s, which is a %s." %(today, day_of_week))

#Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.

def time_until_birthday():
    year = input("Please enter your birth year: ")
    month = input("Please enter your birth month in numbers (1-12): ")
    day = input("Please enter your birth day in numbers (1-31): ")
    today = date.today()
    birthday = datetime.date(year,month,day)
    years_old = today - birthday

    print("You are currently %s years old." %(years_old))


time_until_birthday()