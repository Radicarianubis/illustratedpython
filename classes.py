class Chair:                         #1
    ''' A Chair on a chairlift '''   #2
    max_occupants = 4                #3 

    def __init__(self, id):          #4
        self.id = id                 #5
        self.count = 0

    def load(self, number):          #6
        self.count += number        

    def unload(self, number):        #7
        self.count -= number

#1: Name, followed by colon. Names are CamelCased
#2: After you define a class, you can do a docstring to document the class
#3: Class attributes. This will be a state that is true for all instances of the class
#4: def statement, creating a function inside of a class is called a METHOD
#        __init__ is called a constructor, and has two params, self and id
#5: inside the body of the constructor you attach two attributes that are unique
#        to the instance, id and count. Constructor returns nothing, just updates values unique
#        to the created instance
#6: This represents an action that the class can preform. This method tells the instance what to
#        do when loading passeners onto it. 
#7: This method should be called when passangers unload at the top of the hill.
# You've already seen methods such as the .capitalize method. You need  to call it on  an instance
# of the class, rather than calling it by itself:
'matt'.capitalize()
#'Matt' is what is returned
# Within REPL you can inspect the class with dir(Chair)
# That will show you all the default class attributes + the ones you created
# You can inspect attributes as well
Chair.max_occupants
# Will return 4. You can inspect everything since everything is an object within Python:
# Chair.__class__
# <class 'type'>
# Chair.max_occupants.__class__
# <class 'int'>
# Chair.__init__.__class__
# <class 'function'>
# Chair.load.__class__
# <class 'function'>
# Chair.unload.__class__
# <class 'function'>
chair = Chair(21)
# This creates an instance of the Chair class called chair, passing the argument 21 as the id
# This calls the method LOAD from the class:
print(chair.count)
chair.load(3)
print(chair.count)

# PRIVATE AND PROTECTED
# You can access anything within python, but there is syntax to tell you that you shouldn't:
# Prefix the their name with an underscore _
class CorrectChair:
    ''' A Chair on a chairlift '''
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_vale

    def _check(self, number):
        if number < 0 or number > self.max_occupants:
            raise valueError('Invalid count:{}'.format(number))
        return number

# the ._check method is considered private, only the instance should access it inside the class
# In the class, the .load and .unload moethods call the privat method. If wanted, you could call it 
# from outside the class, but you shouldn't, as anything with an underscore should be considered
# an implementation detail that might not exist in future versions of the class.



