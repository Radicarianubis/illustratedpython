# Lists are denoted with brackets []
names = list()  # one way of creating it
other_names = [] # another way

names.append('Matt')
names.append('Fred')

#pre-populated list
other_names = ['Fred', 'Charles']

# You can use the list() method to split up other sequence types into a list
mattlist = list('Matt')
print(mattlist)

# Understanding sequence indicies, index starts at 0
print(names[0]) # Matt
print(names[1]) # Fred

# LIST INSERTION
names.insert(0, 'George') # Will insert George into the first and move everything else to the right
print(names)

# REPLACEMENT
names[1] = 'Henry'
print(names)

# LIST APPEND (ADD TO END)
names.append('Paul')
print(names)

# REMOVING AN ITEM
names.remove('Paul')
print(names)

del names[1] # DELETE BY INDEX
print(names) 

# LIST SORTING
names.sort()
print(names)

# SORTED function is more general, and work with any sequence
old = [5, 3, -2, 1]
nums_sorted = sorted(old)
print(nums_sorted)
print(old)

# Be careful about what you sort, Python wants you to be explicit, you can't sort different types!
things = [2, 'abc', 'Zebra', '1']

# By passing in str as the key parameter, every item in the list is sorted as if it were a string:
things.sort(key=str)
print(things)

# RANGE is a built- in fucntion that cosnstructs integer sequences
nums = range(5)
nums # rannge(5)
# Python 3 is lazy, RANGE doesn't make the list, but gives you an interable that will return those numbers WHEN ITERATED
# Pass the result into LIST so you can see the numbers it would generate
list(nums) # [0, 1, 2, 3, 4]
# If you need to start at a non-zero number, RANGE will accept two parameters
# First number is the starting number (including itself), second number is the, up to BUT NOT INCLUDING number

#numbers from 2 to 5
nums2 = range(2, 6)
print(nums2)

# There's a third optional argument, STRIDE. A stride of 2 will return every other number)

even = range(0, 11, 2)
even
print(list(even))


# HALF OPEN INTERVAL is what it means for "up to but not including" 
# It's useful because the DIFFERENCE between the end and sthe start is the length when dealing with a sequence
# Two subsequences can be spliced together cleanly without overlap

a = range(0, 5)
b = range(5, 10)
both = list(a) + list(b)
len(both)  # 10 - 0 
print(both)

# If you are dealing with numeric sequences you might want to follow this samt method, especially when defining APIs



# TUPLES use ()
# IMMUTABLE, ordered records. Once created, they cannot be changed.
row = ('George', 'Guitar')

row2 = ('Paul', 'Bass')

# Not super common to create empty tuples
empty = tuple()

empty = ()

# One item tuples:
one = tuple([1])

one = (1,)
 
one = 1,

# it is the use of a comma that makes it a tuple, this is just an integer:
d = (3)
type(d) # <class 'int'>


# Pythonic way to create a tuple:
p = ('Steph', 'Curry','Guard')
print(p)

# You CANNOT .append them



# SETS use {}
# Unordered collection that CANNOT HAVE DUPLICATES
# Useful for removing duplicates and checking membership, takes little time even on large sets

digits = [0, 1, 1, 3, 4, 5, 6, 7, 8, 9]
digit_set = set(digits)  # this will put the list into a set and remove the extra 1

digit_set = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# To check for membership, us IN
9 in digit_set

42 in digit_set

# If a class (set or list, or user-defined calss) implements the __contains__ method (or the iteration protocl)
# you can use IN with to check membership. Sets are quicker than tests against a list

odd = {1, 3, 5, 7, 9}

# SET OPERATIONS: UNION (|)  INTERSECTION (&)  DIFFFERENCE (-)  XOR (^)

# The difference operator removes items in one set from another

even = digit_set - odd
print(even) # {0, 8, 2, 4, 6}

# INTERSECTION & (two roads intersect) returns ONLY THOSE FOUND IN BOTH SETS

prime = set([2, 3, 5, 7])
prime_even = prime & even
print(prime_even) #{2}

# UNION | returns a set composed of ALL ITEMS FROM BOTH SETS, DUPLICATES REMOVED

numbers = odd | even
print(numbers) # 0 - 9 prints out

# XOR ^ returns a set of items that are only found in one set or the other BUT NOT BOTH

first_five = set([0, 1, 2, 3, 4])
two_to_six = set([2, 3, 4, 5, 6])
in_one = first_five ^ two_to_six
print(in_one) #{0, 1, 5, 6}


