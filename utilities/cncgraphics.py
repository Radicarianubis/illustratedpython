# Graph out G code path

with open('gcode.txt','r') as f:
    x = f.readlines()

linecount = 0
command = ""
codes = ['X','x','Y','y','G','g','M','m',]
asskeynum = [48,49,50,51,52,53,54,55,56,57]
for line in x:
    if any('X' in s for s in line)\
    or any('x' in s for s in line)\
    or any('Y' in s for s in line)\
    or any('y' in s for s in line)\
    or any('G' in s for s in line)\
    or any('g' in s for s in line)\
    or any('M' in s for s in line)\
    or any('m' in s for s in line):
        for char in line:
            if char in codes:
                command = command + char
                continue
            if ord(char) in asskeynum:
                command = command + char
                continue
            if ord(char) == 46:
                command = command + char
                continue
            if ord(char) == 32:
                continue
            if ord(char) == 10:
                print(command)
                command = ""
                break

