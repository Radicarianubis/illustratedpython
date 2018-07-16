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
  
