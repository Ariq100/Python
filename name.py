'''
Task 1: sleep_in
A function sleep_in takes is two parameters, weekday and vacation. The parameter weekday is True if it is a weekday, and the parameter vacation is 
True if we are on vacation. We sleep in if it is not a weekday or we’re on vacation. Return True if we sleep in.

    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True
# ''' 
# weekday = 1
# vacation = 0

# def sleep_in(a, b):
#     return True if not a or b else False

# print(sleep_in(weekday, vacation))
# 
'''
Task 2: monkey_trouble
Define a function monkey_trouble which has two parameters. We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

    monkey_trouble(True, True) → True
    monkey_trouble(False, False) → True
    monkey_trouble(True, False) → False
'''

# a_smile = 1
# b_smile = 1

# def monkey_trouble(x, y):
#     return True if x and y or not x and not y else False

# print(monkey_trouble(a_smile, b_smile))

''' 
Task 3: sum_double
Given two integer values, return their sum. If the two values are the same, then return double their sum.
    sum_double(1, 2) → 3
    sum_double(3, 2) → 5
    sum_double(2, 2) → 8
'''

# a = float(input("Enter a value = "))
# b = float(input("Enter anothre vlaue = "))

# def sum_double(a, b):
#     return (a + b) * 2 if a == b else (a + b)
        
# print(sum_double(a, b))

'''
Task 4: diff21
Given an integer n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
'''

# n = int(input('Enter a number : '))

# def diff21(n):
#     return (n - 21) * 2 if n > 21 else (21 - n)

# print(diff21(n))

'''
Task 5:
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is
talking and the hour is before 7 or after 20. Return True if we are in trouble.

    parrot_trouble(True, 6) → True
    parrot_trouble(True, 7) → False
    parrot_trouble(False, 6) → False
'''

# hour = int(input('Enter a hour : '))
# talking = bool(input('Is the parrot talking?? (1/0) = '))

# def trouble(y, x):
#     return True if (y and x < 7 ) or (y and x > 20) and (x <= 23 and x >= 0) else False

# print(trouble(talking, hour))

'''
Task 6:
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
'''

# a = int(input('Enter a number : '))
# b = int(input('Enter a number : '))

# def sum(a, b):
#     return True if a == 10 or b == 10 or (a+b) == 10 else False

# print(sum(a, b))



'''
Task 7: near_hundred
Given an integer n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

    near_hundred(93) → True
    near_hundred(90) → True
    near_hundred(89) → False
'''

# n = int(input('Enter a number : '))

# def near_hundred(n):
#     return True if (90 <= n <= 110) or (190 <= n <= 210) else False

# print(near_hundred(n))

'''
Task 8: pos_neg
A function pos_neg takes two integer values, return True if one is negative and one is positive. Except if 
the parameter "negative" is True, then return True only if both are negative.

    pos_neg(1, -1, False) → True
    pos_neg(-1, 1, False) → True
    pos_neg(-4, -5, True) → True
'''

# x = int(input('Enter a value : '))
# y = int(input('Enter a value : '))
# negative = bool(input(' '))

# def pos_neg(x, y, negative):
#     return True if (x > 0 and y < 0) or (x < 0 and y > 0) or (negative and x < 0 and y < 0) else False

# print(pos_neg(x, y, negative))

'''
Task 9: not_string
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", 
return the string unchanged.

    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
'''

# x = input('Enter a string = ')

# def not_string(x):
#     return ('not ' + x) if 'not' not in x else x

# print(not_string(x))

'''
Task 10: missing_char
Given a non-empty string and an integer n, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in 
the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

    missing_char('kitten', 1) → 'ktten'
    missing_char('kitten', 0) → 'itten'
    missing_char('kitten', 4) → 'kittn'
'''

# y = 'Kitten'
# n = 4

# def missing_char(y, n):
#     return y.replace(y[n], '') if n == int(len(y)) else False

# print(missing_char(y, n))

'''
Task 11: front_back
Given a string, return a new string where the first and last characters have been exchanged.

    front_back('code') → 'eodc'
    front_back('a') → 'a'
    front_back('ab') → 'ba'
'''

# y = input('Enter a word = ')

# def front_back(y):
#     return (y[-1] + y[1:-1] + y[0])

# print(front_back(y))

'''
Task 12: front3
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

    front3('Java') → 'JavJavJav'
    front3('Chocolate') → 'ChoChoCho'
    front3('abc') → 'abcabcabc'
'''

# y = input('Enter a word>>> ')

# def front3(y):
#     return y if len(y) < 3 else y[0 : 3] * 3

# print(front3(y))
