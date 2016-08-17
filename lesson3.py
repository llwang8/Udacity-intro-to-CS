# Udacity - Intro to Computer Science
#
# Lesson 3:


######################################


# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(list):
    n = len(list)
    number_list = []
    column_list = []
    j = 0
    while j < n:
        column_list.append([])  # make a empty column list of lists
        j = j + 1
        number_list.append(j)  # make a valid number list

    for row in list:
        if len(row) != n:
            return False
        for i, e in enumerate(row):
            try:
                int(e)
            except ValueError:
                return False    # make sure element is number
            if e != int(e):     # make sure element is interger
                return False
            if e not in number_list:    # make sure element is valid number
                return False
            column_list[i].append(e)    # make column list
        if contain_once(row) == False:  # make sure each row contains valid number once
            return False

    for column in column_list:
        if contain_once(column) == False: # make sure each column contains valid number once
            return False

    return True

def contain_once(list):
    while list:
        if list.pop() in list:
            return False
    return True


print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False



