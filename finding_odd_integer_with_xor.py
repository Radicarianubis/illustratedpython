def find_it(seq):
    length = len(seq)
    for i in range(0, length):
        count = 0
        for j in range(0, length):
            if seq[i] == seq[j]:
                count += 1
        if (count % 2 != 0):
            oddint = seq[i]
            print(f"Found, the number is {oddint}")
            return oddint
    return




find_it([20,1,-1,2,2,3,3,5,5,1,2,4,20,4,-1,2,2])

