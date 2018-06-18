age = input("How old are ya'?")
old = None
if int(age) > 18:
    old = True
else:
    old = False

print(old)

name = input("What's your name?")
second_half = None
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print(alphabet)

num = 0
for letter in alphabet:
    if (name.lower().startswith(letter)):
        if num > 13:
            print("Your name is in the second half of the alphabet!")
        if num <= 13:
            print("Your name is in the first half of the alphabet!")
    else:
        num += 1

names = ['John', 'Alex', 'Casey']
if names:
    print("The class has enrollments.")
else:
    print("The class is empty!")

car = None

if not car:
    print('You have a Taxi!')
else:
    print('You have a car')
    


