# Udacity - Intro to Computer Science
#
# Challenging Practice:


######################################
# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group
# of people Dave, Sarah, Peter and Andy could be split into two groups in
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling
# takes as its inputs two positive integers of which the first is the
# number of items and the second is the number of sets into which those
# items will be split. The second procedure, bell, takes as input a
# positive integer n and returns the Bell number B(n).

def stirling(n, k):
    output = 0
    if n < k:
        return 0
    else:
        if k == 1 or k == n:
            return 1
        output = k * stirling(n-1, k) + stirling(n-1, k-1)
    return output

def bell(n):
    sum = 1
    for i in range(1, n):
        sum = sum + stirling(n, i)
    return sum


#print stirling(1,1)
#>>> 1
#print stirling(2,1)
#>>> 1
#print stirling(2,2)
#>>> 1
#print stirling(2,3)
#>>>0

#print stirling(3,1)
#>>> 1
#print stirling(3,2)
#>>> 3
#print stirling(3,3)
#>>> 1

#print stirling(4,1)
#>>> 1
#print stirling(4,2)
#>>> 7
#print stirling(4,3)
#>>> 6
#print stirling(4,4)
#>>> 1

#print stirling(5,1)
#>>> 1
#print stirling(5,2)
#>>> 15
#print stirling(5,3)
#>>> 25
#print stirling(5,4)
#>>> 10
#print stirling(5,5)
#>>> 1

print stirling(20,15)
#>>> 452329200

print bell(1)
#>>> 1
print bell(2)
#>>> 2
print bell(3)
#>>> 5
print bell(4)
#>>> 15
print bell(5)
#>>> 52
print bell(15)
#>>> 1382958545

#===================================================
# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can
# collude with each other to improve their page ranks.  We consider
# A->B a reciprocal link if there is a link path from B to A of length
# equal to or below the collusion level, k.  The length of a link path
# is the number of links which are taken to travel from one page to the
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A,
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link
# A->B, which includes one link and so is of length 1. (it requires
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to
#   - take an extra input k, which is a non-negative integer, and
#   - exclude reciprocal links of length up to and including k from
#     helping the page rank.


def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}

    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal(graph, node, page, k):
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

def is_reciprocal(graph, target, url, k):
    if k == 0:
        if url == target:
            return True
        return False
    if k == 1:
        if target in graph[url]:
            return True
    for u in graph[url]:
        if is_reciprocal(graph, target, u, k-1):
            return True
    return False

# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

list = ['a', 'b', 'c']
#for x in list:
#    print x
#print is_reciprocal(g, 'c', 'a', 2)

print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}


#==========================================

# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our
# case, consists of the characters '.' and 'x', and changes it according
# to some predetermined rules. The rules consider three characters, which
# are a character at position k and its two neighbours, and determine
# what the character at the corresponding position k will be in the new
# string.

# For example, if the character at position k in the string  is '.' and
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up
# '..x' in the table below. In the table, '..x' corresponds to 'x' which
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs:
#     a non-empty string,
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and
#     a positive integer, n, which is the number of generations.
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

def cellular_automaton(str, num, g):
    generations = [str]
    pattern = pattern_update(num_convert(num))
    i = 1
    while i <= g:
        generations.append(str_generator(pattern, generations[i-1]))
        i = i + 1
    return generations[-1]

def str_generator(pattern, laststr):
    group = ''
    str = ''

    for i in range(0, len(laststr)):
        #print i
        index_l = i - 1
        if index_l < 0:
            index_l = -1

        index_r = i + 1
        if index_r > len(laststr) -1:
            index_r = 0

        group = laststr[index_l] + laststr[i] + laststr[index_r]

        str = str + pattern[group]['replacement']
    return str

def num_convert(num):
    value = [128, 64, 32, 16, 8, 4, 2, 1]
    list = []
    i = 0
    while i < 8:
        if num >= value[i]:
            factor = num / value[i]
            num = num - factor * value[i]
            list.append(value[i])
        i = i + 1
    return list

def pattern_update(list):
    pattern = {}
    pattern['...'] = {'value': 1, 'replacement': '.'}
    pattern['..x'] = {'value': 2, 'replacement': '.'}
    pattern['.x.'] = {'value': 4, 'replacement': '.'}
    pattern['.xx'] = {'value': 8, 'replacement': '.'}
    pattern['x..'] = {'value': 16, 'replacement': '.'}
    pattern['x.x'] = {'value': 32, 'replacement': '.'}
    pattern['xx.'] = {'value': 64, 'replacement': '.'}
    pattern['xxx'] = {'value': 128, 'replacement': '.'}
    for e in list:
        for p in pattern:
            if pattern[p]['value'] == e:
                pattern[p]['replacement'] = 'x'
    return pattern


print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
print cellular_automaton('.', 21, 1)
#>> x



