#-------------------------------------------------------------------------------
# Name:        Problem 019.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

# Add an extra index to make indexing more efficent. e.g. Monday is the 1st day
# not the 0th
WeekDayName = ["None", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday", "Sunday"]

MonthName = ["None", "January", "Febuary", "March", "April", "May",
             "June", "July", "August", "September", "October",
             "November", "December"]

DaysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def IsLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True

    return False

def NextDayGenerator():
    while True:
        for i in range(1, 7+1):
            yield i

def NextMonthGenerator():
    while True:
        for i in range(1, 12+1):
            yield i

def main():
    answer = 0

    ndg = NextDayGenerator()
    nmg = NextMonthGenerator()

    # 1st January 1901 was a Tuesday
    day = next(ndg) # Monday
    day = next(ndg) # Tuesday
    month = next(nmg) # January
    monthDay = 1
    year = 1901

    while year <= 2000:
        # 1st of the month is a sunday
        if monthDay == 1 and day == 7:
            print(WeekDayName[day], monthDay, MonthName[month])
            answer += 1

        # New years day
        if monthDay == 1 and month == 1:
            print("")
            print(year)

        day = next(ndg)
        monthDay += 1

        if monthDay >= DaysInMonth[month]:
            month = next(nmg)
            monthDay = 0
            if month == 1:
                year += 1
                # Leap years only effect the second month, Febuary
                if IsLeapYear(year):
                    DaysInMonth[2] = 29
                else:
                    DaysInMonth[2] = 28

    print(answer)

if __name__ == '__main__':
    main()

# A alternate way from the Project Euler solution thread
# import datetime
# count = 0
# for y in range(1901, 2000+1):
#     for m in range(1, 12+1):
#         if datetime.datetime(y, m, 1).weekday() == 6:
#             print "Sunday", 1, Months.String[m], y
#             count += 1
# print count







