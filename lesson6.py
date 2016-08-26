# Udacity - Intro to Computer Science
#
# Lesson 6:


######################################

# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610

#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci_v1(n):
    result = []
    result.append(0)
    result.append(1)
    i = 2
    while i < n + 1:
        result.append(result[i-1] + result[i-2])
        i = i + 1
    return result[n]

def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print fibonacci(1)
print fibonacci(36)
#>>> 14930352


# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
    all_ancestors = []
    if person in genealogy:
        for p in genealogy[person]:
            all_ancestors = add_more(all_ancestors, p)
            more_ancestors = ancestors(genealogy, p)

            for a in more_ancestors:
                all_ancestors = add_more(all_ancestors, a)
    return all_ancestors

def add_more(result, entry):
    if entry not in result:
        result.append(entry)
    return result

# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#>>> []

