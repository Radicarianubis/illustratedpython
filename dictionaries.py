# Creating / assigning a dictionary
info = {'first': 'Pete', 'last': 'Best'}

# An alternative way is with the built-in DICT class. 
# Pass a list of tuple pairs into the class and it returns a dictionary.
info = dict([('first', 'Pete'),('last', 'Best')])

# You can also used named parameters, they must be vaid python var ames, and will convert to strings
info = dict(first='Pete', last='Best')

# You can use index ops to insert values into the dictionary:
info['age'] = 20
info['occupation'] = 'Drummer'

# Looking up values from keys is quick, the other way around is not
print(info['age'])

# If you try to get a key that isn't real it'll error out
# info['Band']

# The IN operator
# Allows you to quickly check if a key is in a dictionary:
'Band' in info
#False
'first' in info
#True

# This also works in sequences
5 in [1, 3, 6]
#False
't' in {'a', 'e', 'i'}
#False
'P' in 'Paul'
#True

# The IN operator will work with most containers
# You can define your own classes to also respond to the statement
# Your object needs to define the .__contains__ or be iterable

# Dictionary Shortcuts
# The .get method of a dictionary will get you the key
# It also accepts an optional parameters to give back a default value if they key isn't found
genre = info.get('Genre', 'Rock')
genre
#'Rock'

# The .get method is one way to get around the key error above

# SETDEFAULT
# .setdefault behaves like .get, but also sets the value of the key to the default value
# if the key is not found. Because .setdefault returns a value, if you initialize it to
# a mutable type, such as a dict or a list, you can mutate the result in place.
# It can als be used to provide an accumulator or counter for a key
names = ['Ringo', 'Paul', 'John', 'Ringo']

count = {}
for name in names:
	count.setdefault(name, 0)
	count[name] += 1

# If you don't use the .setdefault method, you have to add more code:
names = ['Ringo', 'Paul', 'John', 'Ringo']

count = {}
for name in names:
	if name not in count:
		count[name] = 1
	else:
		count[name] += 1

print(count['Ringo'])

# Performing these counting types of operations was so common they added 
# collections.Counter as a standard library. This class can do it better:
import collections
count = collections.Counter(['Ringo', 'Paul', 'John', 'Ringo'])
print(count)
print(count['Ringo'])
print(count['Fred'])

# Example of .setdefault for dictionary mapping of a person to bands they played in
# You'd want someone who is in two bands to map to both bands
band1_names = ['John', 'George', 'Paul', 'Ringo']
band2_names = ['Paul']
names_to_bands = {}
for name in band1_names:
	names_to_bands.setdefault(name, []).append('Beatles')

for name in band2_names:
	names_to_bands.setdefault(name, []).append('Wings')
print(names_to_bands['Paul'])

# The COLLECTIONS module includes a handy class: defaultdict
# This class behaves like a dictionary but also allows for setting the
# Default value of a key to an arbitrary factory. If the default factory is not None
# it is initlaized and inserted as a value any time a key is missing
from collections import defaultdict
names_to_bands = defaultdict(list)
for name in band1_names:
	names_to_bands[name].append('Beatles')
for name in band2_names:
	names_to_bands[name].append('Wings')

print(names_to_bands['Paul'])
# ^^^^ using defaultdict is easier to understand / read than setdefault


# Deleting Keys
del names_to_bands['Ringo']
# You can't add or remove from a dictionary while you're looping over it

# Dictionary Iteration
# By default when you iterate, you get back the keys
data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
for name in data:
	print(name)

# Dictionary also has the .keys method that will return a view of the keys
# It is NOT a copy of the keys though, if you later remove a key, the view will show this

# To iterate over the VALUES of the dictionary, use .values
for value in data.values():
	print(value)

# To get both the key and the vvalue, use the .items method, which returns a view
for key, value in data.items():
	print(key, value)

# If you materialize the view into a list, you will see that the list is a sequence of (key, value)
# Tuples, the same thing that dict acccepts to create a dictionary in the first place
print(list(data.items()))

# Dictionary is ordered on insertion order, SORTED will return a new sorted list, given a sequence
for name in sorted(data.keys(), reverse=True):
	print(name)


