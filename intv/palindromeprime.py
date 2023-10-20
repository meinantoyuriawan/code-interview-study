# get the prime of certain range, flip the number to create the palindrome, check if its prime

def SieveOfEratosthenes(n): 
  
    # Create a boolean array 
    # "prime[0..n]" and initialize 
    #  all entries it as true. 
    # A value in prime[i] will 
    # finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
  
        # If prime[p] is not 
        # changed, then it is a prime 
        if (prime[p] == True): 
  
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1

    return prime

def flipNumber(n):
    res = 0
    while n!= 0:
        digit = n%10
        res = res *10 + digit
        n //= 10

    return res
    
def startStopPrime(start, stop):
    lenStop = len(str(stop))
    endNumber = 10 ** lenStop
    arr = SieveOfEratosthenes(endNumber)

    res = []
    for i in range(start, stop):
        if i<17:
            if arr[i]:
                res.append(i)
        else:
            numCheck = flipNumber(i)
            if arr[i] and arr[numCheck]:
                res.append(i)

    return res

print(startStopPrime(1, 200))