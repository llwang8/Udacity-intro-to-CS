# Udacity - Intro to Computer Science
#
# Lesson 2:

#########################################################################
# Days Old
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
# (first try)
def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    daysByYear = (year2 - year1) * 365

    daysToDate1 = daysToDate(year1, month1, day1)
    daysToDate2 = daysToDate(year2, month2, day2)

   #  print leapYearNumbers(year1, year2)
    result = daysByYear + leapYearNumbers(year1, year2) + daysToDate2 - daysToDate1

    print result
    return result

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

#########################################################################
# (another approach following instructor)
# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def nextDay(year, month, day):
    if isLeapYear(year):
        daysOfMonths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < daysOfMonths[month-1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 != 0:
            return True
        else:
            if y % 400 == 0:
                return True
    return False

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

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


#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#

def print_abacus(m):
    factorStr = str(m)
    if len(factorStr) < 10:
        while len(factorStr) < 10:
            factorStr = '0' + factorStr
    i = 0
    while i < 10:
        print_line(int(factorStr[i]))
        i = i + 1

def print_line(n):
    line = '|00000*****   |'
    line = line[0] + line[1:10-n+1] + line[11:14] + line[10-n+1:11] + line[14]
    print line


# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.

def jungle_animal(animal, my_speed):
    if animal == 'zebra':
        print "Try to ride a zebra!"
    if animal == 'cheetah':
        if my_speed > 115:
            print "Run!"
        else:
            print "Stay calm and wait!"
    else:
        print "Introduce yourself!"

jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"


# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
def find_element1(list, val):
    i = 0
    while i < len(list):
        if list[i] == val:
            return i
        i = i + 1
    return -1

def find_element2(list, val):
    i = 0
    for e in list;
        if e == val:
            return i
        i = i + 1
    return -1

def find_element3(list, val):
    if val in list:
        return list.index(val)
    else:
        return -1

def find_element4(list, val):
    if val not in list:
        return -1
    return list.index(val)

def find_element5(list, val):
    try:
        return list.index(val)
    except ValueError:
        return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

