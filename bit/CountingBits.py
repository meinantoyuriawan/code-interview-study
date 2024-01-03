def countBits(n):
    res = []

    def countN(x):
        c = 0
        binary = bin(x)[2:]
        for i in range(len(binary)):
            if binary[i] == '1':
                c +=1
        
        return c
        
    for i in range(n+1):
        res.append(countN(i))

    return res

# Input: n = 2
# Output: [0,1,1]

n = 2
print(countBits(n))