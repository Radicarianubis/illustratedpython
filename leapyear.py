
yearstr = input("What year would you like to check to see if it's a leap year?: ")
yearint = int(yearstr)
year4 = yearint % 4
year100 = yearint % 100
year400 = yearint % 400
import pdb; pdb.set_trace()
if year4 == 0:
    if year100 == 0:
        if year400 == 0:
            print(yearstr + " is a leap year!")
        else:
            print(yearstr + " is NOT a leap year!")
    else:
        print(yearstr + " is a leap year!")
else:
    print(yearstr + " is NOT a leap year!")

    
