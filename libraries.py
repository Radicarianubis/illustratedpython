# Libraries are reusable chunks of code, python comes with many "batteries included"
# To use one, you must load the code into the namespace (which holds functions classes and variables)
# Say for instance you want to calculate the sine of an angle, you'll need a function to do that
# or load a pre-existing function. The built-in math library has  a sin function that calculates
# the sine of an angle expressed in radians, and has a variable that defines a value for pi
from math import sin, pi
print(sin(pi/2))

# This doesn't put math into your namespace, but creates a variable that points to the pi variable found
# within the math module itself. You can inspect your current namespace in REPL to confirm this:
# 'sin' in dir()    (will return True)

# You can load in singular functions from a library, but you can alos load the entire library into your
# namespace to reference it all.
import math
# You can dir(math) in REPL to see the attributes
# the above actually makes a variable 'math' that points to the math module
# Most of these are functions. If you wanted to call the tan function, you can't invoke it
# because tan isn't in your namespace, only math is. But you can do a lookup on the math
# variable with a period (.) operator, which will look up attributes on an object
# Because everything in python is an object, you can use the period to lookup the tan attribute
# on the math object
math.tan(0)
# If you wanted to lookup info about tan, you could do help(math.tan)

# If you only need a few attributes from a library, use the from method
# If you need to access most of the library, it requires less typing 

# CONFLICTING IMPORT NAMES
# What if you already had a function names sin, but need to use the sin function from the math library,
# you could import math, then math.sin would reference the library and sin would reference your function
# Python ALSO allows you to redefine the name of what you want to import as a new keyword:
# from math import sin as other_sin
# other_sin(0) will use the sin function from math
# The same thing works with import statements:
# import math as other_math
# other_math.sin(0)

# STAR IMPORTS
# You can CLOBBER your namespace with a star import:
# from math import *
# asin(0) >>> 0.0
# When you * import, it tells Python to throw everything from the math library into the local namespace
# This can be handy but is also pretty dangerous, and makes debugging harder beause it is not EXPLICIT 
# where the code comes from. Even worse are star imports from multiple libraries, as libraries could overwrite 
# each other. These are discgouraged and frowned upon, unless you're writing your own test code or messing around
# within REPL. Remember the Zen of Python: EXPLICIT IS BETTER THAN IMPLICIT

# NESTED LIBRARIES
# Some Python packages have a nested namespace. Ex: the XML library that comes with Python has support for 'minidom'
# and 'etree' Both libraries live under the xml parent package:
from xml.dom.minidom import parseString
dom = parseString('<xml><foo/></xml>')

from xml.etree.ElementTree import XML
elem = XML('<xml><foo/></xml>')

# Notice that the FROM construct allows importing only the functions and classes needed. Using the import construct
# (without from) would require more typing (but also allow access to everyting from the package:)
import xml.dom.minidom
dom = xml.dom.minidom.parseString('<xml><foo/></xml>')

import xml.etree.ElementTree
elem = xml.etree.ElementTree.XML('<xml><foo/></xml>')

# IMPORT ORGANIZATION
# According to PEP 8, import statements should be located at the top of the file following the module docstring, and
# there should be one import per line, grouped by:
# Standard library imports
# 3rd party imports
# Local package imports

# An example module might look like this at the start:
#!/usr/bin/evn Python3
"""
This module converts records into JSON
and shoves them into a database
"""
import json
import sys             # python standard libs

import psycopg2        #3rd party

import recordconverter #local

# it's also useful to sort them alphabetically, and you should avoid circular imports where modules import one another
# If you can't refactor to remove a circular import , it is possible to place the import statement within the function or 
# method containing the code that invokes it
# Avoid importing modules that are not available on some systems
# avoid importing large modules that you aren't going to use
