def reverseBits(n):
    res = 0
    for _ in range(32):
        x = n&1
        res = (res << 1) | x

        n = n >> 1

    return res

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)