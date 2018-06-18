#endswith
xl = 'Oct2000.xls'
print(xl.endswith('.xls')) #True
print(xl.endswith('.exe')) #False
print(xl.endswith('Oct', 0, 3)) #True
print(xl.endswith('ct2', 1, 4)) #True

#startswith
print(xl.startswith('Oct')) #True

#find
mood = 'grateful'


# 0 is g, 1 is r, 2 is a
print(mood.find('ate')) #2
print(mood.find('great')) #-1

#format
print('name: {}, age {}'.\
        format('Matt', 10))

print('{} {} {} {} {}'.format(
    'hello',
    'to',
    'you',
    'and',
    'you',
))

#join
print(', '.join(['1', '2', '3'])) #This is more common than repeatedly using + for strings

#lower
fname = 'readme.txt'
print(fname.endswith('txt') or fname.endswith('TXT')) #True

print(fname.lower().endswith('txt')) #True (This is more PYTHONICC)

#strip
print('      hello   there '.strip()) #Strips out whitespace  
#lstrip and rstrip can remove only leading or rightmost whitespace

#upper
print('yell'.upper()) #YELL

#lower
print('QUIET'.lower()) #quiet

# the STRINGMETHODS entry in the help setion of the REPL contains documentation on all string methods and examples

