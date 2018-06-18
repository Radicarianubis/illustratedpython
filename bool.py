# Checking to make sure there's an input
# Empty string is 'falsey' and will act as a negative
# A string with content is 'truthy' and will act as a positive

name = 'Joe'
if name:
	print("The name is {}".format(name))
else:
	print("There is no name")
# Empty containers (lists and dictionaries) are 'falsey' when empty
# They are 'truthy' when populated

# You don't need to explicitly check boolean values
# Don't do stuff like ' if done == True: do something '

done = True
if done:
    print("Done!")

# To test lists for examples, this is sufficient:

members = []
if members:
    print("There are members")
else:
    print("There are NO MEMBERS!")


# If you want to define specific truthiness for a user defined object, use the .__bool__ magic method
# If that isn't defined, the .__len__ method is checked for a non-zero value
# If neither of those things are defined, an ojbect defaults to True

class Nope:
    def __bool__(self):
        return False

n = Nope()
bool(n)
print(bool(n))


# Variables containing None is the same object as any other variable containing None
# so in this instance you use 'is' to check for identiy rather than using ==

a = None
b = None

a is b 
#True
a is not b
#false

# You can put the 'is' expression in an if statement:
if a is None:
    print("A is not set!")

# Since None evaluates to False in a boolean context, you can also:

if not a:
    print("A is not set!")

# But be careful as other values also evaluate to False, such as 0, [] or ' ' (empty string)




