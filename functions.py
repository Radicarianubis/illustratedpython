# Do not use list, dictionaries for default parameters unless you're paying attention
# Default parameters are created only once at function definition time, NOT whenever
# they are called.

# You can workaround this by pushing the creation of the default values from the function def
# time to the actual function runtime. Change the mutable default parameters so that they default
# to None. Then, creat an instance of the desired mutable type within the body of the function
# if the default is none:

def to_list2(value, default=None):
    if default is None:
        default = []
    default.append(value)
    return default

to_list2(4)
# [4]
to_list2('hello')
#['hello']

# if default is None:
#       default = []
# ^^^ this could be written as:
# default = default if default is not None else []
# but who the hell wants to do that?


