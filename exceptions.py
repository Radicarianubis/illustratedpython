# Look Before You Leap (LBYL)
# Checks for exceptional cases before performing an action to mitigate it
numerator = 10
divisor = 0
if divisor != 0:
    result = numerator / divisor
else:
    result = None

# This method is not always a guarantee. For example, if you check that a
# file exists before you open it, that doesn't mean the file will still be
# around later. In multi-threaded environments, this is known as a race condition

# None is ues to represent the undefined state. This is a common idiom throuhgout 
# "Pythondom." Try not to invoke methods on a variable that is assigned None
# as it will raise an exception

# Easier To Ask For Forgiveness Than Permission (EAFP)
# The idea is to perform the operation inside of a TRY block
# If the operation fails, the exception will be caught by the 
# exception block. Try ... except construct provides a mechanism
# for Python to catch exceptional cases:
numerator = 10
divisor = 0
try:
    result = numerator / divisor
except ZeroDivisionError as e:
    result = None

# The TRY construct creates a block, inside of which are statements that
# may throw exceptions. If they do, Python looks for the except block
# that catches that exception (or a parent class of it)
# the e on the end is optional, which gives you access to the instance
# of the exception when it's thrown
# Try to include only lines that will potentially throw an error, 
# as opposed to entire functions

# LBYL is not guaranteed to prevent errors, so many devs favor EAFP
# Some rules of thumb for exception handling:
# * Gracefully handle errors you know how to handle and can reasonably expect
# * Do not silence exceptions that you cannot handle or do not reasonably expect
# * Use a global exception handler to gracefully handle unexpected errors

# MUTLIPLE EXCEPTION CASES
# If there are mutliple exceptions you can chain a list
try:
    some_function()
except ZeroDivisionError as e:
    pass
    # handle specific
except Exception as e:
    pass
    # handle others

# When some_function throws an error, it first checks if it's a ZeroDivisionError
# (or a subclass of it.) If that's not the case, it checks if the exception is a 
# subclass of Exception. Once ONE except block is entered, Python no longer checks 
# the blocks after

# FINALLY clause
# Another clause for error handling is the FINALLY clause
# This statement is used to place code that will always execute regardless of
# whether an exception happens or not. If the try block succeeds, then the finally
# block will be executed
# FINALLY always executes. If the exception is not handled, finally will execute
# and THEN the exception will be re-raised
try:
    some_function()
except Exception as e:
    pass
    # handle errors
finally:
    pass
    # cleanup

# The purpose is usuallyh to cleanup external resources, such as files, network connections
# or databases. These resources should be freed whether the operation was succesful or not

# ELSE CLAUSE
# Optional clause that is executed when no exception is raised
# It must follow any except statements and execute BEFORE the FINALLY block:
try:
    print('hi')
except Exception as e:
    print('Error')
else:
    print('Success')
finally:
    print('at last')

# RAISING EXCEPTIONS
# You can also raise or throw exceptions. Zen of Python wants you to be explicit and refuse
# the temptation of guessing.

# WRAPPING EXCEPTIONS: Page 170 of Illustrated Guide to Python 3

# Writing your own exceptions:
# You should subclass from Exception or anything below Exception
class DataError(Exception):
    def __init__(self, missing):
        self.missing = missing

# example of using it
config = 'important_data' # change to something else to raise DataError
if 'important_data' not in config:
    raise DataError('important_data missing')

