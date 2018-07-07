name = 'Ron'
print(name[0])
print(name[2])
print(name[-1]) #this will grab the last char regardless of length

filename = "README.txt"
print(filename[7:10])
print(filename[-3:]) #this will grab the last 3 chars regardless of length
 
def is_palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print('Palindrome confirmed!')
    else:
        print('Palindrome DENIED')




is_palindrome('racecar')
