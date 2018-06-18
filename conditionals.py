# There are 'rich comparison' magic methods that are tedious to define
# But there's ' functools.total_ordering ' which is a class decorator and gives you all of the
# comparison functionality as long as you define __eq__ and __le__

import functools
@functools.total_ordering
class Abs(object):
    def __init__(self, num):
        self.num = abs(num)
    def __eq__(self, other):
        return self.num == abs(other)
    def __lt__(self, other):
        return self.num < abs(other)

five = Abs(-5)
four = Abs(-4)

# print(five > four) this doesn't work for some reason, check it out <<<<<<

score = 91
if score > 90 and score <= 100:
    grade = 'A'
    print(grade)

# Python also allows you to do RANGE COMPARISONS but they are not common in other languages:
if 90 < score <= 100:
    grade = 'A'
    print(grade)

# Checking if a given name is a member of a band:
name = 'Paul'
beatle = False
if (name == 'George' or
    name == 'Ringo' or
    name == 'John' or
    name == 'Paul'):
    beatle = True
    print(beatle)
else:
    beatle = False
    print(beatle)
    
# Idiomatic Python method of checking membership:

beatles = {'George', 'Ringo', 'John', 'Paul'}
beatle = name in beatles
print(beatle)

# Examples of using the NOT keyword in a condition statement:

last_name = 'unknown'
if name == 'Paul' and not beatle: # so if beatle is false, it'll go through
    last_name = 'Revere'



# Check for implicit coercion to "truthy' or 'falsey' values:
debug = True
if debug: #checking a boolean
    print("Debugging")

# ELIF for multiple choices
score = 87
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'


