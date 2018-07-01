def is_odd(x):
    if(x%2 == 0):
        return False
    else:
        return True

#print(is_odd(1))
#print(is_odd(2))

def is_prime(x):
    return all(x % i for i in range(2, x))

#print(is_prime(52))
#print(is_prime(53))

def snake_case(x):
    separator = '_'
    output = ''
    lowerflag = False
    for char in x:
        if char.islower():
            output += char
            lowerflag = True
        elif (char.isupper() & (lowerflag)):
            output += (separator + char.lower())
        elif char.isupper():
            output += char.lower()
    return output

def kebab_case(x):
    separator = '-'
    output = ''
    lowerflag = False
    for char in x:
        if char.islower():
            output += char
            lowerflag = True
        elif (char.isupper() & (lowerflag)):
            output += (separator + char.lower())
        elif char.isupper():
            output += char.lower()
    return output

print(snake_case('thisIsCamelCase'))
print(kebab_case('thisIsCamelCase'))

