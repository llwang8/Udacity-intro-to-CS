# Udacity - Intro to Computer Science
#
# Lesson 2:

# Days Old
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def leapYearNumbers(y1, y2):
    y = y1 + 1
    num = 0
    while y < y2:
        if isLeapYear(y) == True:
            num = num + 1
        y = y + 1

    return num

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 != 0:
            return True
        else:
            if y % 400 == 0:
                return True
    return False

def daysToDate(y, m, d):
    days = d - 1
    i = 1
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while i < m:
        days = days + daysOfMonths[i-1]
        i = i + 1

    if isLeapYear(y) == True:
        febAdj = 1
    else:
        febAdj = 0
    if m > 2:
        days = days + febAdj

    return days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()




