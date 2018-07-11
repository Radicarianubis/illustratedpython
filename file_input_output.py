#OPENING A FILE
# open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Windows uses \ as a separator, put an r in front of the string to make it raw so Python doesn't treat it as an escape character:
# r"C:\test"
# Mode | Meaning
# 'r'  | Read text file (default)
# 'w'  | Write text file (overwrites if exists)
# 'x'  | Write text file, throw FilesExistsError if already exists
# 'a'  | Append to text file (write to end)
# 'rb' | Read binary file
# 'wb' | Write binary (overwrite)
#'w+b' | Open binary file for reading AND writing
# 'xb' | Write binary file, throw FileExistsError if already exists
# 'ab' | Append to binary file (write to end)
#
# passwd_file = open('/etc/passwd')
# passwd_file.readline()
#
# .readline method will read a single line, and default to reading if no mode is specified
# If you oepn a file that doesn't exist, you'll get an error
# You can call .readline repeatedly to read, or use .readlines to return a list containing all the lines
# To read ALL the contents of a file into one string, use the .read method:
# 
# passwd_file = open('/etc/passwd')
# print(passwd_file.read())
# passwd_file.close()
#
# Always close your files after you're done
#
# BINARY FILES
#
# To read binary file, pass rb as the mode, and you'll get byte strings
#
# bfin = open('img/dict.png', 'rb')
# bfin.read(8)
# That'll give you the first 8 bytes of the PNG file
# You'll see a b in front of the string to tell you it's a byte string
# You can use .readlines on binary files but it'll only read until it gets to a b'\n'
# 
# ITERATION WITH FILES
#
# fin = open('/etc/passwd')
# for line in fin.readlines():
#   print(line)
#
# The problem with that is that .readlines returns a list, meaning Python will have to read the entire
# file first, and if it's big, it could eat up memory like mad
# However, if you iterate over the file instance ITSELF, it'll read each line as needed:
#
# fin = open('/etc/passwd')
# for line in fin:
#   print(line)
#
# .readlines method should only be used if you're sure you can hold the entire file in memory and you needto access
# the lines multiple times
#
# WRITING FILES
#
# You must open the file in write mode to do this:
# fout = open('tmp/names.txt', 'w')
# fout.write('George')
#
# .write takes a string as a param and writes it to the file
# /writelines takes a sequence containing string data and writes it to the file
#
# NOTE: to use newlines, you need to pass \n to end a sring line in unix
#                                         \r\n to end a string in windows
# To have cross platform, the linesep string found in the os module defines the correct newline string for the platform:
# import os
# os.linesep
# '\n'
#
# You must close or .flush the file to have it actually write the text, as the computer will buffer that information  until
# it exceeds a certain limit (4k on unix)
#
# WITH STATEMENT
#
# with open('/tmp/names3.txt', 'w') as fout3:
#   fout3.write('Ringo\n')
#
# This will open and close the statement automatically
#
# It's a good idea to write functions dealing with files separately from the actual function that accepts the filename itself 
# For example, if you wanted to format strings in a file, but want to (a) be able to test it without a file, or (b) use the same
# function but passing arguments from a place other than a file, you need to make sure they are separate:
#
# def add_numbers(filename):
#   with open(filename) as fin:
#       return add_nums_to_seq(fin)
#
# def add_nums_to_seq(seq):
#   results = []
#   for num, line in enumerate(seq):
#       results.append('{0}-{1}'.format(num, line))
#   return results
#
# There are other types that also implement read and write, and anytime you're coding with a filename, ask yourself
# if you may want to apply the logic to other sequence-like things besides a file. If so, use this example of refactoring
# the functions to obtain code that is easier to reuse and test.
