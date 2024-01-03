# Input: n = 00000000000000000000000000001011
# Output: 3

def hammingWeight(n):
    c = 0
    binary = bin(n)[2:]
    for i in range(len(binary)):
        if binary[i] == '1':
            c +=1
    
    return c

n = 11
print(hammingWeight(n))