# Looping over the indices, pulling out the items that live at those specific indecies
animals = ["cat", "dog", "bird"]
for index in range(len(animals)):
	print(index, animals[index])

# This is called a 'code smell', because you're not using Python as you should
# Python has a built-in enumerate function that makes this unnecessary
# The ENUMERATE function returns a tuple of (index,item) for every item in the sequence
for index, value in enumerate(animals):
	print(index, value)
# The tuple will return a pair of index and value when using enumerate, so you can use
# 'Tuple unpacking', by creating the two variables, making sure to use a comma
# The tuple must be the same length as the number of variables included in the for loop

# BREAKing out of a loop
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
	if item < 0:
		break
	result += item
print(result)

# It continues to add numbers until it finds an item less than 0 and breaks out

# SKIP over items in a loop
# Using CONTINUE comes in handy
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
	if item < 0:
		continue
	result = result + item
print(result)

# ^^ So this continues to add numbers, but when it finds a negative number
# CONTINUE goes right back to the top of the loop, continuing on to the
# next item, skipping over the item that fails the test

# Using the IN statement for membership
animals = ["cat", "dog", "bird"]
'bird' in animals # Will return True

animals.index('bird') # Will give you the index location, 2 in this case

# Lists are mutable, and are sequences so you can loop over them
# One option is to collect the items to be removed during a pass through the list
# In another loop after that, iterate only over those items and delete them from the original list
names = ['John', 'Paul', 'George', 'Ringo']
names_to_remove = []
for name in names:
	if name not in ['John', 'Paul']:
		names_to_remove.append(name) # Adds any names that aren't in that qualifying list

for name in names_to_remove:
	names.remove(name) # Removes any name name added above from the original list

# Another option is to iterate over a COPY of the list
# Using the [:] slice copy construct
names = ['John', 'Paul', 'George', 'Ringo']
for name in names[:]: # copy of names
	if name not in ['John', 'Paul']:
		names.remove(name)

# ELSE
# Any code in an else block will execute if the for loop didn't break
items = [1, 3, 5, -7, 1]
positive = False
for num in items:
	if num < 0:
		break
else:
	positive = True
print(positive)
# Note that continue statements do not have any effect on else


# WHILE loops
# Loops over a block of code while a condition is held
# An expression evaluates to True or False, followed by:
# The indented code will continue to repeate as long as the
# Original expression is True

# If you have an object that supports ITERATION, you use a for loop
# You use WHILE loops when you don't have easy access to an iterable object
# Counting down is a good example:
n = 3
while n > 0:
	print(n)
	n = n - 1

# You can also use the BREAK statement to exit a WHILE loop:
n = 3
while True:
	print(n)
	n = n - 1
	if n == 0:
		break


