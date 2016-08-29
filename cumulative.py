# Udacity - Intro to Computer Science
#
# Cumulative Practice:


######################################

# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean
# and two other values. If the first input is True, it should return
# the second input. If the first input is False, it should return the
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(val, choiceT, choiceF):
    if val:
        return choiceT
    else:
        return choiceF


print pick_one(True, 37, 'hello')
#>>> 37

print pick_one(False, 37, 'hello')
#>>> hello

print pick_one(True, 'red pill', 'blue pill')
#>>> red pill

print pick_one(False, 'sunny', 'rainy')
#>>> rainy

######################################
# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive
# integer n and returns the nth triangular number.

def triangular(n):
    i = 1
    output = 0
    while i < n + 1:
        output = output + i
        i = i + 1
    return output


print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55

######################################
Quiz 3: Linear Time
Linear Time
For the procedures below, check the procedures whose running time scales linearly with the length of the input in the worst case. You may assume the elements in input_list are fairly small numbers.

def proc1(input_list):
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum

def proc2(input_list):
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

def proc3(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True


######################################
# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.

def remove_tags(str):
    output = ''
    tag_start = str.find('<')
    if tag_start < 0:
        output = str
    else:
        if tag_start != 0:
            output = str[0:tag_start]
        while tag_start >= 0:
            tag_end = str.find('>')
            str = str[tag_end + 1:]
            tag_start = str.find('<')
            if tag_start > 0:
                output = output + " " + str[0:tag_start]

        if len(str) > 0:
            output = output + " " + str
    return output.split()

#print remove_tags('''<h1>Title</h1>''')
print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                    <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags('This is in <i>italics</i>')

print remove_tags('<br />This line starts with a tag')


######################################
# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is
# a dictionary and the second a string. The string is a valid date in
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
6:"June", 7:"July", 8:"August", 9:"September",10:"October",
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012".
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(lib, date_str):
    index = date_str.find('/')
    date_list = []

    while index > 0:
        date_list.append(date_str[0:index])
        date_str = date_str[index+1:]
        index = date_str.find('/')

    return str(date_list[1]) + " " +lib[int(date_list[0])] + " " + date_str


print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791


######################################
#Quiz 6: Termination
#Termination
#For each of the procedures defined below, check the box if the procedure always terminates for all inputs that are natural numbers (1,2,3...).

def proc1(n):
   while True:
      n = n - 1
      if n == 0:
         break
   return 3

def proc2(n):
   if n == 0:
      return n
   return 1 + proc2(n - 2)

def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)

######################################
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and
#     a string, and returns the result of applying the converter to the
#     input string. This replaces all occurrences of the match used to
#     build the converter, with the replacement.  It keeps doing
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return match, replacement

def apply_converter(converter, string):
    match, replacement = converter
    index = string.find(match)

    while index >= 0:
        string = string[0:index] + replacement + string[index + len(match):]
        index = string.find(match)

    return string


# For example,
#print 'aaaa'.find('a')
c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab
#print apply_converter(c, 'aaaba')

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would
# run forever).


######################################
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(list):
    if not list:
        return None
    if len(list) == 1:
        return list
    tally = {}
    last = list[0]
    count = 0
    for e in list:
        if e ==  last:
            count = count + 1
        else:
            if str(last) not in tally:
                tally[str(last)] = count
            else:
                if tally[str(last)] > count:
                    tally[str(last)] = count
            count = 1
        last = e

    max = tally[tally.keys()[0]]
    maxcount = 1
    for entry in tally:
        if tally[entry] > maxcount:
            maxcount = tally[entry]
            max = entry
    return max


#For example,

#print [2, 2] == [2, 2]

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3


print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# None

print longest_repetition([2])

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
#[2,2]


######################################
# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(list):
    new_list = []
    i = -1
    while i >= -len(list):
        if is_list(list[i]):
            item = deep_reverse(list[i])
        else:
            item = list[i]
        #print item
        new_list.append(item)
        i = i - 1
    return new_list



#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
######################################

######################################