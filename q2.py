"""
Question2
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same.
"""

def unique(l):
    l = str_list(l)
    s = set(l)
    if len(s) != 2:
        return "Test cases will always have exactly one unique number while all others are the same."
    c = []
    for i in s:
        if l.count(i) == 1:
            return i

def str_list(s):
    s = s.split(',')
    return s

l = input("Enter comma seperated list of numbers\neg. 1,2,3 : ")
u = unique(l)
print("unique(",l,") ➞",u)