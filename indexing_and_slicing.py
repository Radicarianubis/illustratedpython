# INDEXING
my_pets = ["dog", "cat", "bird"]
my_pets[0]
# 'dog'

my_pets[-1]
# 'bird'

# You can also perform an index operation on a tuple or a string:
('Fred', 23, 'Senior')[1]
#23
'Fred'[0]
#'F'

# Some types like sets, don't support index operations. 
# Implement the .__getitem__ method if you want to add
# index operations to your own class

# SLICING
# A slice may contatin the start index, an optional end index, 
# and an optional STRIDE, all separated by a colon

my_pets = ["dog", "cat", "bird"]  # a list
print(my_pets[0:2])
# dog and cat will print out
# python uses HALF-OPEN INTERVAL convention
# The list goes up but DOES NOT include the end index
# The RANGE function also behaves the same with the 2nd param

print(my_pets[:2])
# If you slice with a colon, the first index is optional
# If you leave it blank, it'll start on the 0th item

# You can also use negative indicides when slicing
# -1 is the last item. If you slice up to the last item
# you will get everything but that item
my_pets[0:-1]
my_pets[:-1]
# Both react the same

# The final index is also optional, if it's missing, it'll slice to the end
my_pets[1:]

# You can default both the start and the end of the indices. If they're 
# Both missing, the slice returned will run from the start to the end
# You can use this construct to quickly copy lists:

print(my_pets[:])

# STRIDING SLICES

# Slices also take a stride, following the statring and ending indicies. 
# Default stride is 1

my_pets = ["dog", "cat", "bird"]
dog_and_bird = my_pets[0:3:2]
print(dog_and_bird)

zero_three_six = [0, 1, 2, 3, 4, 5, 6][::3]
print(zero_three_six)

# range has a similar third parameters that defines stride:
list(range(0, 7, 3))
# [0, 3, 6]

# Strides can be negative. A stride of -1 means you move backward
# Right to left. You should make the start slice greater than the
# end slice. The exception is if you leave out the start and the end
# a stride of -1 will reverse the sequence:
my_pets[0:2:-1]
# []
my_pets[2:0:-1]
# ['bird', 'cat']

print([1, 2, 3, 4][::-1])
# [4, 3, 2, 1]

'emerih'[::-1]
# 'hireme'

